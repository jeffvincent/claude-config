#!/usr/bin/env node

import { google } from 'googleapis';
import minimist from 'minimist';
import { getAuthClient, parseAccountArg } from './auth/auth-utils.js';
import { logAction } from './action-logger.js';

async function createEvent(args) {
  // Validate required args
  if (!args.summary && !args.title) {
    throw new Error('Missing required argument: --summary or --title (event title)');
  }

  // Get authenticated client for specified account (or default)
  const accountId = parseAccountArg(args);
  const oauth2Client = await getAuthClient(accountId);

  const calendar = google.calendar({ version: 'v3', auth: oauth2Client });

  // Build event object
  const event = {
    summary: args.summary || args.title
  };

  // Optional description
  if (args.description || args.desc) {
    event.description = args.description || args.desc;
  }

  // Optional location
  if (args.location || args.loc) {
    event.location = args.location || args.loc;
  }

  // Handle start/end times
  const timezone = args.timezone || args.tz || 'America/Los_Angeles';

  if (args.allDay) {
    // All-day event
    if (!args.date) {
      throw new Error('All-day events require --date (YYYY-MM-DD format)');
    }
    event.start = { date: args.date };
    event.end = { date: args.endDate || args.date };
  } else {
    // Timed event
    if (!args.start) {
      throw new Error('Missing required argument: --start (ISO datetime or use --allDay with --date)');
    }
    if (!args.end) {
      throw new Error('Missing required argument: --end (ISO datetime)');
    }

    event.start = {
      dateTime: args.start,
      timeZone: timezone
    };
    event.end = {
      dateTime: args.end,
      timeZone: timezone
    };
  }

  // Optional attendees
  if (args.attendees) {
    event.attendees = args.attendees.split(',').map(email => ({
      email: email.trim()
    }));
  }

  // Optional reminders
  if (args.reminders) {
    const reminderMinutes = args.reminders.split(',').map(m => parseInt(m.trim()));
    event.reminders = {
      useDefault: false,
      overrides: reminderMinutes.map(minutes => ({
        method: 'popup',
        minutes
      }))
    };
  }

  // Optional recurrence - supports raw RRULE or --repeat shorthand
  if (args.recurrence) {
    const rule = args.recurrence.startsWith('RRULE:') ? args.recurrence : `RRULE:${args.recurrence}`;
    event.recurrence = [rule];
  } else if (args.repeat) {
    const repeatRules = {
      daily: 'RRULE:FREQ=DAILY',
      weekdays: 'RRULE:FREQ=DAILY;BYDAY=MO,TU,WE,TH,FR',
      weekly: 'RRULE:FREQ=WEEKLY',
      biweekly: 'RRULE:FREQ=WEEKLY;INTERVAL=2',
      monthly: 'RRULE:FREQ=MONTHLY',
      yearly: 'RRULE:FREQ=YEARLY',
      annually: 'RRULE:FREQ=YEARLY',
    };
    const rule = repeatRules[args.repeat.toLowerCase()];
    if (!rule) {
      throw new Error(`Unknown --repeat value: "${args.repeat}". Valid: daily, weekdays, weekly, biweekly, monthly, yearly`);
    }
    event.recurrence = [rule];
  }

  // Optional recurrence end (used with --repeat or --recurrence)
  if (event.recurrence && (args.until || args.repeatUntil)) {
    const untilDate = (args.until || args.repeatUntil).replace(/-/g, '');
    event.recurrence[0] += `;UNTIL=${untilDate}`;
  }
  if (event.recurrence && args.count) {
    event.recurrence[0] += `;COUNT=${args.count}`;
  }

  // Optional color
  if (args.colorId) {
    event.colorId = args.colorId;
  }

  // Optional visibility
  if (args.visibility) {
    event.visibility = args.visibility; // default, public, private, confidential
  }

  // Optional conference data (Google Meet)
  if (args.addMeet || args.googleMeet) {
    event.conferenceData = {
      createRequest: {
        requestId: `meet-${Date.now()}`,
        conferenceSolutionKey: { type: 'hangoutsMeet' }
      }
    };
  }

  // Create event
  const params = {
    calendarId: args.calendar || 'primary',
    resource: event
  };

  // Add conferenceDataVersion if creating Meet
  if (event.conferenceData) {
    params.conferenceDataVersion = 1;
  }

  const result = await calendar.events.insert(params);

  return {
    success: true,
    eventId: result.data.id,
    htmlLink: result.data.htmlLink,
    summary: result.data.summary,
    start: result.data.start,
    end: result.data.end,
    location: result.data.location,
    attendees: result.data.attendees,
    hangoutLink: result.data.hangoutLink,
    conferenceData: result.data.conferenceData
  };
}

// Main execution
const args = minimist(process.argv.slice(2));
const startTime = Date.now();

createEvent(args)
  .then(result => {
    // Log the action
    logAction('create_event', args, result, {
      account: args.account || 'default',
      duration: Date.now() - startTime
    });

    console.log(JSON.stringify(result, null, 2));
  })
  .catch(error => {
    const errorResult = {
      success: false,
      error: error.message
    };

    // Log the failed action
    logAction('create_event', args, errorResult, {
      account: args.account || 'default',
      duration: Date.now() - startTime,
      failed: true
    });

    console.error(JSON.stringify(errorResult, null, 2));
    process.exit(1);
  });
