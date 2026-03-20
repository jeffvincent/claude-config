#!/usr/bin/env node

import { google } from 'googleapis';
import { getAuthClient } from './auth/auth-utils.js';

async function archiveMessages(messageIds, accountId = 'work') {
  const auth = await getAuthClient(accountId);
  const gmail = google.gmail({ version: 'v1', auth });

  console.log(`Archiving ${messageIds.length} messages...`);

  let archived = 0;
  let failed = 0;

  for (const id of messageIds) {
    try {
      await gmail.users.messages.modify({
        userId: 'me',
        id: id,
        requestBody: {
          removeLabelIds: ['INBOX']
        }
      });
      archived++;
      if (archived % 10 === 0) {
        console.log(`Archived ${archived}/${messageIds.length}...`);
      }
    } catch (error) {
      console.error(`Failed to archive ${id}: ${error.message}`);
      failed++;
    }
  }

  console.log(`\nComplete! Archived: ${archived}, Failed: ${failed}`);
  return { archived, failed };
}

// Message IDs to archive
const easyArchives = [
  // Merged GitHub PRs (Analytics #8775 - Mar 12)
  '19ce45f574070ce3', '19ce45f08729f6c2', '19ce4577c951a48a', '19ce4562695587bf', '19ce456263c7fa50',

  // Merged GitHub PRs (Analytics #8783 - Mar 16)
  '19cf85a87d09f624', '19cf8596aa11ebf3', '19cf850a168afdde',

  // Merged GitHub PRs (pm-skills #6, BotFiltering #325 - Mar 16)
  '19cf7ccc82070291', '19cf7cc9217520f4', '19cf7ea81c82cf64', '19cf7e8ec9559bae', '19cf7e8e976e3230',

  // GitHub PR approvals (completed - Mar 16)
  '19cf88675ab4a378', '19cf84cee42bd779',

  // Duplicate Product Notifications (8 identical messages - Mar 12)
  '19ce2614097b6f84', '19ce2612fa8156bf', '19ce260fd925c398', '19ce260ca1adcbb2',
  '19ce260950293136', '19ce2608ad1162ad', '19ce2607450d3374', '19ce2603fbfb3f78',

  // Old Product Announcements (Mar 12)
  '19ce2432d923cd0f', '19ce22c534df9b1f', '19ce22c2f3656b94', '19ce22b9a02becc2',

  // Marketing/Promotional
  '19ce29ba652252f4', // Vantage Point Pulse
  '19ce23c058a3a9ff', // Cursor Team

  // Old Meeting/Calendar Updates
  '19ce3ae546ae9033', // Clockwise (Mar 12)
  '19ce34b3709ae3c5', // Rubber Duck invite (Mar 12)
  '19ce2b935af5066d', // Rubber Duck invite (Mar 12)
  '19ce2e813f97bbbe', // Naz 1:1 update (Mar 12)
  '19cf86b84693fefc', // Zoom assets ready (Mar 16)
  '19cf92704db82eb8', // PLT meeting update (Mar 17)

  // Old Administrative
  '19ce34c56de85e03', // Google Sheets edit (Mar 12)
  '19ce34c56a615634', // Google Sheets edit (Mar 12)
  '19ce2eb2200f3995', // Asana overdue nudge (Mar 12)

  // External recruiting
  '19cf7d1f7a81da16', // Debbie Madden from Stride

  // Old GitHub review comments (no longer relevant - Mar 12-16)
  '19ce3dbedb29bae9', '19ce3c1c2b69792d', '19ce3a94181c2214', '19ce3a936a25612f',
  '19ce3a929c135776', '19ce39371fb3e328', '19ce3936502f6f66', '19ce39353a4b6033',
  '19ce393467520e3f', '19ce3933e55cf8c9', '19ce392fc78db805', '19ce39255c947873'
];

archiveMessages(easyArchives).catch(console.error);
