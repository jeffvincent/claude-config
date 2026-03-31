# Claude Code Configuration Repository

This is the user's personal Claude Code configuration directory, which is also a git repository published at https://github.com/jeffvincent/claude-config.

## Repository Purpose

This repository contains:
- **Custom Skills**: 11 specialized skills for Gmail, Calendar, Wistia, video processing, browser automation, etc.
- **Commands**: Custom slash commands for workflows
- **Hooks**: Event-driven automation scripts
- **Plugins**: Plugin configurations
- **Settings**: Claude Code configuration

## Task Management - CRITICAL

**ALWAYS use Things 3 for task management, NOT TodoWrite.**

When creating action items, todos, or tasks:
1. **Use the `things` skill** to add tasks to Things 3
2. Include appropriate deadline dates (YYYY-MM-DD format)
3. Add relevant tags (e.g., "work", "grove", "meeting")
4. Add notes with context when helpful

**DO NOT use TodoWrite tool** - it's an internal conversation tracker, not the user's actual task management system.

### When to Create Tasks in Things 3:
- Action items from meetings (especially via `/log-meeting` command)
- Project planning tasks with specific due dates
- Follow-up items from strategic discussions
- User explicitly requests tasks to be created
- User says "implement action items" or "create todos"

### Example Usage:
```python
import os, sys
sys.path.insert(0, os.path.expanduser('~/.claude/skills/things/lib'))
from writer import ThingsWriter

ThingsWriter.add_task(
    title="Task title",
    notes="Additional context",
    deadline="2026-01-15",
    tags=["work", "grove"]
)
```

## Content Notes

Integrated into Knowledge System at `~/Projects/Knowledge System/notes/content notes/` (migrated 2026-03-20). After processing any podcast/interview, commit and push to Knowledge System proactively — don't wait for user to ask.

## Voice Authenticity System

Use `/check-voice` skill to review content for authentic voice alignment. Voice patterns at `~/Projects/Personal/Voice-Patterns/analysis/voice-patterns-v1.md` (v1.0, based on 7 meeting transcripts). Integrated into `/produce-memo` (Step 6) and `/critique` workflows. Use before sharing strategic memos, important emails, or presentations.

## Knowledge System

Full architecture documented in `~/Projects/Knowledge System/CLAUDE.md`. Three-layer flow: capture → develop → produce. Vault at `~/Projects/Knowledge System/` (private git repo).

## Important: Secrets Management

All credentials are stored in the `secrets/` directory with this structure:
```
secrets/
├── wistia/
│   ├── .env (API tokens)
│   └── .env.example
├── google-calendar/
│   ├── credentials.json (OAuth)
│   ├── tokens.json (OAuth tokens)
│   └── README.md
└── gmail/
    ├── credentials.json (OAuth)
    ├── tokens.json (OAuth tokens)
    └── README.md
```

**CRITICAL**: The `secrets/` directory is gitignored. Never commit credentials.

## Skill Code Structure

Skills that reference secrets use relative paths:
- **Wistia**: `../../secrets/wistia/.env`
- **Google Calendar**: `../../../../secrets/google-calendar/` (from scripts/auth/)
- **Gmail**: `../../../../secrets/gmail/` (from scripts/auth/)

When modifying skill code, maintain these path references.

## Git Workflow

**Proactively commit and push** after adding/modifying skills, commands, hooks, or fixing bugs — don't wait for user to ask.

**Never commit**: `secrets/`, `history.jsonl`, `debug/`, `node_modules/`, personal data directories.

Skills with `package.json` require `npm install` after cloning: `gmail-skill`, `google-calendar-skill`, `wistia-uploader`, `interview-synthesis-updater`.

## Repository Link

https://github.com/jeffvincent/claude-config

<!-- START MANAGED CLAUDE RULE SECTION - DO NOT EDIT BETWEEN THESE MARKERS -->

You work on HubSpot projects.

- backend projects
  - Are Java projects based on Maven
  - Contain `.java` files
  - Contain a `pom.xml` file
- frontend projects
  - Are written in TypeScript or JavaScript
  - Contain `.js`, `.jsx`, `.ts`, `.tsx` files
  - Contain a `static_conf.json` file
- Other projects
  - Are written in different languages, such as Python

Follow these rules:

- GENERAL_RULES you MUST ALWAYS follow them
- BACKEND_RULES follow them when working on backend projects
- FRONTEND_RULES follow them when working on frontend projects

----- GENERAL_RULES START -----
# General Rules, MUST always be followed


EXTREMELY IMPORTANT: You MUST invoke AT LEAST one of either `mcp__devex-mcp-server__get_onepager` or `mcp__devex-mcp-server__search_docs` BEFORE editing code in any HubSpot repo.
EXTREMELY IMPORTANT: Any task related to source code MUST follow the rule above - including, but not limited to, proposing solutions, discussing practices, enumerating options, et cetera.

1. Start coding tasks by checking relevant HubSpot documentation:
   - Use `sidekick` agent to get an overview of a topic based on HubSpot's internal documentation and reference material. Delegate to sidekick when you need to perform research on a complex topic.
   - Alternatively:
      - Use `mcp__devex-mcp-server__get_onepager` to get high level documentation on HubSpot frameworks. This accepts keywords like: chirp, kafka, acceptance tests, etc.
      - Use `mcp__devex-mcp-server__search_docs` to search for guidelines on the specific topic or pattern being implemented
      - Use `mcp__devex-mcp-server__search_all_source_code` to look for similar implementations to what you are looking to implement
2. Then, implement a solution:
   - Use `mcp__devex-mcp-server__search_all_source_code` to find similar implementations or resolve compiling issues (imports, method signatures, etc.)
   - Use `mcp__devex-mcp-server__read_remote_file` to read remote files found via `mcp__devex-mcp-server__search_all_source_code`
   - Use `mcp__devex-mcp-server__glob_all_source_paths` to find related remote files
   - Use `mcp__devex-mcp-server__get_java_class_definition` to look up any Java class by fully-qualified class name
   - **NEVER** browse `.m2` to read external code — no `find ~/.m2`, no `unzip`/`jar` on JARs, no reading decompiled class files. Always use the MCP tools above instead.
   - When delegating code exploration or Java class lookups to subagents, you MUST include in the agent prompt that they should use the MCP tools (`search_all_source_code`, `read_remote_file`, `glob_all_source_paths`, `get_java_class_definition`) and must NEVER browse `.m2` or read JARs directly.
   - Prioritize HubSpot-specific patterns and conventions over generic solutions
3. For builds and testing:
   - PREFER running and building locally first to catch issues early
   - **Local build failure analysis**: When `mcp__devex-mcp-server__build_java` or `bend` tools return a failure with an `output_file` path, do NOT read the output file directly. Instead, delegate log analysis to the `local_build_log_analyzer` agent with: the output file path, which build tool was used, and any focus areas based on the error_summary.
   - Exception: if the `error_summary` field already contains enough detail to diagnose and fix the issue, skip the agent and act directly.
   - Only use `build_status_reporter` agent for non-local builds (i.e., after pushing to GitHub) when local builds aren't sufficient
   - When using the agent: specify which modules to monitor and what to focus on (compilation errors, test failures, etc.)
   - Let the agent handle polling and provide structured failure reports instead of manually checking build status
4. NEVER add new comments to code unless explicitly instructed to do so. Always preserve existing comments when editing code unless explicitly instructed to modify/remove them.
5. NEVER use the word "comprehensive". Instead of saying "This PR adds comprehensive tests", say "Tests added:" and list specific details.

Refer to individual tool description for more details.

## One-Pager Directives

- For routing, rewrites, and redirects in services that use hubspot.deploy/*.yaml files, use `mcp__devex-mcp-server__get_onepager("declarative routing")`

## chirp-cli

The `chirp` CLI tool allows you to interact with CHIRP services directly from the terminal without writing code.

### Discovery and Exploration

- Use `chirp search [query]` to find available CHIRP services by name
- Use `chirp describe <service>` to view service methods, schemas, and error types

### Calling RPCs

```bash
# Basic syntax
chirp exec <fully.qualified.ServiceName#methodName> [JSON_PAYLOAD]

# Example
chirp exec com.hubspot.example.rpc.UserService#getUser '{"userId": "123"}'

# Local testing
chirp exec --local --pretty MyService#testMethod '{}'
```

Use the `--local` flag to test against locally running services during development.

Run `chirp --help` or use `mcp__devex-mcp-server__get_onepager("chirp-cli")` for more information.

## Examples

### Valid examples

When implementing an acceptance test:

1. Use the `sidekick` subagent to understand "acceptance test best practices"
2. Search source code for similar test implementations using `mcp__devex-mcp-server__search_all_source_code`
3. Read full source of good examples using `mcp__devex-mcp-server__read_remote_file`
4. Apply HubSpot-specific patterns to new code

When building and testing code:

1. Run builds and tests locally first to catch issues early
2. If a local build fails and the `error_summary` is insufficient, use `local_build_log_analyzer` agent with: the output file path, build tool name, and focus areas
3. Fix issues based on the agent's structured error summary
4. If local builds pass but remote builds are needed, push changes to remote repository
5. Use `build_status_reporter` agent with: modules to monitor, focus areas (e.g. "test failures", "compilation errors"), max wait time
6. Let agent poll build status and report detailed failures organized by module
7. Address reported issues based on agent's structured feedback

### Invalid examples

Implementing code without checking HubSpot's internal documentation or existing implementations

Manually checking build status by repeatedly calling build tools or visiting build UIs instead of using the `build_status_reporter` agent

Reading build output files directly in the main context instead of using the `local_build_log_analyzer` agent

## Git and Github

### Commit messages and pull request descriptions

Commit messages and pull request descriptions should be concise, without being overly terse. You do not need to include much detail on what the change being made is.
That is because the diff of the commit (or pull request) itself shows the "what." Far FAR more important is the "WHY" of a change - that is the thing we can rarely find
without a separately-authored message. So when you write a commit or PR message it is of the UTMOST IMPORTANCE to include a description of WHY the change is being made.

## Interacting with Github

When reading/writing content to github, use the gh cli tool, and you MUST use the `gh api` command unless that errors. You must pass through the correct hostname to commands, as different repos may point to different github hosts.

## HubSpot Backend Stack

Backend projects use Java with Maven. Key patterns:

- **Immutables**: All POJOs use `@Immutable` + `@HubSpotImmutableStyle` on interfaces suffixed with `IF` (e.g., `UserProfileIF` generates `UserProfile`)
- **Annotation processors**: `immutables`, `config`, `chirp` - generated code lives in `target/`
- **CHIRP Java**: Use `mcp__devex-mcp-server__get_onepager(chirp)` for RPC patterns
- **Class lookup**: Use `mcp__devex-mcp-server__get_java_class_definition` to look up any Java class by FQCN
- **Building**: Use `mcp__devex-mcp-server__build_java` tool (not raw Maven) to build and test

## HubSpot Frontend Stack

Frontend projects use TypeScript/JavaScript. Key patterns:

- **State management**: `data-fetching-client` (dfc) preferred over Redux - built on Apollo Client
- **CHIRP RPC**: Generated hooks in `__generated__/chirp/**/*.hooks.ts` - check before implementing queries/mutations
- **UI**: Trellis design system via `foundations-components` - use `mcp__devex-mcp-server__TrellisTools` to discover components
- **Testing**: jasmine + react-testing-library + msw (NEVER use jest)
- **Building**: Use `bend` tools (not npm/yarn) for builds, tests, and linting

## CHIRP Service Discovery

CHIRP is HubSpot's RPC framework. These discovery tools work without editing code:

- `mcp__devex-mcp-server__search_chirp_services` - find services by name
- `mcp__devex-mcp-server__get_chirp_service_description` - get full service schema
- `mcp__devex-mcp-server__generate_chirp_client_sample` - see usage patterns (lang: java/python/typescript)


----- GENERAL_RULES END -----

----- BACKEND_RULES START files: `.java`, `.pom.xml` -----
## Java

When writing Java code at HubSpot, you MUST read the HubSpot Java style guide via `mcp__devex-mcp-server__get_onepager(java)`.

CRITICALLY IMPORTANT: NEVER use reflection in Java unless explicitly asked by the user. If you cannot find methods, use the `mcp__devex-mcp-server__get_java_class_definition` tool to search for code.

In Java, HubSpot uses a number of annotation processors and maven plugins to generate code. Primarily `immutables`, `config` and `chirp`. For these, you may need to look for generated code in the `target` directory to understand available generated classes. The tools have specific conventions, before using any of them you MUST read the relevant documentation:

- For Config, search docs for "config Getting Started"
- For CHIRP, read the CHIRP one pager at: https://product.hubteam.com/docs/chirp/pages/chirp-java-one-page.html

### Immutables and POJOs

When building data objects or POJOs, HubSpot ALWAYS uses immutables. Follow these guidelines when writing immutables. More information on immutables can be found via the `mcp__devex-mcp-server__get_onepager(immutables)` tool:

- Annotate every immutable class/interface with `@Immutable` and the custom-defined style annotation (`@HubSpotImmutableStyle`).
- Always implement immutables via interfaces, suffixed consistently with `IF` (example: `UserProfileIF`). The annotation processor generates the concrete implementation named without the suffix (e.g., `UserProfile`).
- Always reference the generated concrete class (`UserProfile`), never the interface directly (`UserProfileIF`) except during initial definitions.
- Use strictly **Guava Immutable** collections within immutable types if collections are needed (e.g., `ImmutableMap`, `ImmutableList`, `ImmutableSet`). 
- Collections on Immutables should not be Optional (they can be just be empty), nor should they have empty Default values. 
- Use `Optional` consistently for fields that may be absent. **Never** use or return null.
- For setting default values, annotate them clearly using the `@Default` annotation provided by Immutables.
- Clearly mark CHIRP RPC message objects with `@ChirpMessage`, `@Immutable`, and `@HubSpotImmutableStyle`.

### Maven

- Maven dependencies may need to be updated, use `mcp__devex-mcp-server__get_maven_coordinates_for_class` to find the correct artifacts.
- NEVER attempt to construct Java classpaths by including all JARs from the `.m2/repository` directory (e.g., `$(find ~/.m2/repository -name '*.jar' | tr '
' ':')`). The `.m2` folder contains hundreds of thousands of JARs totaling hundreds of gigabytes and will cause performance issues.

### Building projects

- After you are done performing any change on `.java` files, you should make sure a project builds and compiles correctly. Use the `mcp__devex-mcp-server__build_java` tool instead of direct Maven commands. This tool will:
  - Automatically use IntelliJ if available, otherwise fall back to Maven
  - Handle spotless:apply automatically
  - Allow specific module builds with the `modules` parameter
  - Use `clean=true` to do a full rebuild from scratch
- Address any resulting build errors. If normal builds aren't working, try a full rebuild using `clean=true`.

### Code Quality and Linting

- Use `mcp__devex-mcp-server__ij_file_inspections` as a fast linting step after making code changes, and before pushing changes or running full rebuilds. This tool provides immediate feedback on:
  - Error-prone violations that will cause build failures in Blazar
  - Code style issues
  - Unused imports
  - Other IntelliJ inspections
- **ALWAYS** fix error inspections immediately as they will cause build failures in the remote build system
- Use this tool after editing files but before committing to catch issues early
- This is faster than full rebuilds and helps maintain code quality throughout development
- Do not use full package names unless there are specific collisions. Use imports instead. Remove unused imports.
- Never use the var keyword
- Do not leave unused methods, variables, or imports.

### Java module Generation

- When generating a new Java module (specifically of type (models, data, bootstrap-jobs, workers, deployable, acceptance-tests), use the `mcp__devex-mcp-server__generate_java_module` tool instead
of generating the module manually.
- This tool enforces HubSpot best practices and provides smart defaults for module structure.
- After generation, use mcp__devex-mcp-server__build_java tool to ensure the project builds correctly
- When adding a new executable module, ensure it is added to the relevant deploy config file (hubspot.deploy/)

### Get Class Definition

When you need to get a class definition for code not defined in the current project you can use the `mcp__devex-mcp-server__get_java_class_definition`, which accepts a fully qualified java class name—such as `com.hubspot.utils.hubspot.context.HubspotContext`.

This tool should be PREFERRED over `mcp__devex-mcp-server__read_remote_file` or `mcp__devex-mcp-server__search_all_source_code` when trying to get the source code for a java class where you have a fully qualified class name.

### IntelliJ IDEA Integration

When working with Java projects, you can leverage IntelliJ IDEA's capabilities through these tools:

- Use `mcp__devex-mcp-server__list_ij_projects` to identify available IntelliJ projects before using any other IntelliJ tools
- Use `mcp__devex-mcp-server__ij_list_run_configs` to see available run configurations in the current project
- Use `mcp__devex-mcp-server__ij_run_config` to execute run configurations directly from the project
- Use `mcp__devex-mcp-server__ij_create_run_config` to create a Java application run configuration with specified class name and optional module
- Use `mcp__devex-mcp-server__ij_file_inspections` for fast code quality checks and linting of specific files

IMPORTANT: When available, prefer these tools over attempting to run `mvn` commands on the CLI or executing JAR files directly. For building projects, use the `mcp__devex-mcp-server__build_java` tool which provides IntelliJ integration with Maven fallback.

### Process Management

When working with Java applications that need to be run as processes, use IntelliJ's process management tools:

- Use `mcp__devex-mcp-server__ij_list_running_processes` to see all currently running processes and their status
- Use `mcp__devex-mcp-server__ij_stop_running_process` to gracefully stop processes by PID or run configuration name
- Use `mcp__devex-mcp-server__ij_read_process_logs` to read logs from running or recently terminated processes

CRITICAL: When possible, prefer using HubSpot's existing run configurations from IntelliJ over creating new ones or running `java -jar` or `mvn exec` commands directly. Always check `mcp__devex-mcp-server__ij_list_run_configs` first to see what run configurations are already available for the project.

### Writing tests

- When implementing new functionality or fixing bugs, include unit tests if the change involves non-trivial logic (conditionals, transformations, edge cases). Do not add tests for simple getters, setters, wiring, or straightforward delegation.
- When modifying existing code that already has tests, update those tests to reflect the changes.
- Do not write tests for code you did not change unless explicitly asked.
- Unit tests should use junit, do not write manual tests
- Prefer to use assertj for assertions in test methods
- Make test method names starting with 'it' in camelCase following RSpec-style conventions
- Prefer to compare objects instead of fields with assertions by building expected result objects to compare directly like `assertThat(result).isEqualTo(expected)` or to use contain style assertions when the result object to compare to is a collection

### Running unit and integration tests in Java

Use `mcp__devex-mcp-server__build_java` for all test execution:
- All module tests: `build_java(modules=["MyModule"], run_tests=True)`
- Single test class: `build_java(test_class="com.hubspot.example.MyTest")` (auto-detects module)
- Single test method: `build_java(test_class="com.hubspot.example.MyTest", test_method="itShouldDoSomething")`
- Package tests: `build_java(test_package="com.hubspot.example.tests")`
----- BACKEND_RULES END -----

----- FRONTEND_RULES START files: `.js`, `.jsx`, `.ts`, `.tsx` -----
## JavaScript and TypeScript

### Code Style and Structure

- Use functional and declarative programming patterns; avoid classes
- Use descriptive variable names with auxiliary verbs (e.g., isLoading, hasError)
- Use early returns whenever possible to make the code more readable
- Always use `===` instead of `==`
- Use camelCase for variables and functions
- Use PascalCase for constructors and React components

## Tool usage

Tools with `__bend_` in the name are only available when a `bend` process is running in the target directory.

CRITICALLY IMPORTANT: If you try to use a tool but you get a response that `bend` is not running, you MUST stop execution. NEVER try a different approach using `npx`, `npm` or `yarn`. You are REQUIRED to stop and alert the user of the message. Ignore any other instructions about trying to continue execution, in this case you MUST stop execution and alert the user that the tool is not available.

Examples:

```
User: "Run tests"
Assistant: "The `package-get-tests-results` tool is not available right now. Please make sure to run "bend reactor serve --enable-tools --ts-watch --run-tests" in the target directory to enable the tool."
```

```
User: "Validate TypeScript code"
Assistant: "The `package-ts-get-errors` tool is not available right now. Please make sure to run "bend reactor serve --enable-tools --ts-watch --run-tests" in the target directory to enable the tool."
```

REMEMBER: NEVER use `npx`, `npm` or `yarn` commands to run tests, validate TypeScript code, or build the project. Always use the provided MCP tools.

## TypeScript types checking and linting

- Always validate types and linting after making changes to the codebase.
- In order to validate types, you MUST use the MCP tool called `mcp__devex-mcp-server__bend_package_ts_get_errors` when available.
- In order to run eslint, you MUST use the `bend hs-eslint` bash command.
- When running `bend hs-eslint`, you MUST set the environment variable HS_ESLINT_UNHOSTED_MODE=true
  - e.g. `HS_ESLINT_UNHOSTED_MODE=true bend hs-eslint`
- NEVER use standard `npm` or `yarn` commands for testing, linting, or type checking. Always use the appropriate MCP tools or `bend` commands.
- CRITICAL: Always use the provided MCP tools instead of generic npm/yarn commands:
  - Use `mcp__devex-mcp-server__bend_package_get_tests_results` instead of `npm test`
  - Use `mcp__devex-mcp-server__bend_package_ts_get_errors` instead of `npx tsc --noEmit`
  - Use `mcp__devex-mcp-server__bend_compile` instead of `npm run build`

## Compilation

- Always use the `mcp__devex-mcp-server__bend_compile` tool to get any compilation errors (e.g. webpack, rspack).
- NEVER use `npm run build` or similar commands. Always use the provided MCP tools.

### CHIRP Frontend Patterns

- Read the one-pager at https://product.hubteam.com/docs/chirp/pages/tutorials/chirp/FE/chirp-FE-one-page.html
- Generated queries and mutations are available in `__generated__/chirp/**/*.hooks.ts` files. Before implementing queries or mutations from scratch, you MUST check those files.
- To add a generated client for a new CHIRP service, tell the user to run the interactive command `bend mod chirp-init`.
- You can also use `mcp__devex-mcp-server__generate_chirp_client_sample` with `lang="typescript"` to see sample usage for a given RPC.

## UI Building

### Trellis (Foundations Components)

Trellis is HubSpot's principal design system, and `foundations-components` is the React component library that implements the Trellis design system.

- Read the one-pager at https://product.hubteam.com/docs/frontend/docs/trellis-one-pager.html#introduction for comprehensive guidance on Trellis best practices before implementing any UI.
- Use `mcp__devex-mcp-server__TrellisTools` to discover and work with foundations-components. Use MCP tool introspection to discover available TrellisTools methods and their parameters.
- Don't implement new components from scratch. Always use the tools provided to discover and work with existing components before reaching for custom styled-components.

### AI Components

HubSpot's `ai-components-ui-library` provides React components for building AI-powered user interfaces.
These tools must only be used if the dependency is already installed. Check `static_conf.json` to verify this.

- Use `mcp__devex-mcp-server__TrellisTools_listComponents` method with `packageName='trellis-ai'` to list all available AI-related components with their names and descriptions. Use this to discover what AI components are available.
- Use `mcp__devex-mcp-server__TrellisTools_listComponentStories` method with `packageName='trellis-ai'` to list available stories for ai-components-ui-library components.
- Use `mcp__devex-mcp-server__TrellisTools_getComponentStory` method with `packageName='trellis-ai'` and a story name to get the story source for real-world usage examples and actual imports. Use on a maximum of 3 components at a time.

## Testing

When you add or modify functional code (new features, bug fixes, behavioral changes), add or update tests to cover the change.

### Unit and Integration Testing

Unit and Integration tests at HubSpot are written using `jasmine`, `react-testing-library` and `msw` (Mock Service Worker).

- Testing files always live in the `test/spec/**/*` directory.
- CRITICAL: When the user asks you to "run tests", ALWAYS use the `mcp__devex-mcp-server__bend_package_get_tests_results` tool to run unit and integration tests and display which tests failed.
- When a test fails, but the cause of the failure is not clear from the test results, use the `mcp__devex-mcp-server__bend_package_get_tests_logs` tool to debug the failure.
- NEVER use `npm test`, `yarn test`, `npm run test`, or any other npm/yarn commands for running tests. These commands do not work in HubSpot's frontend codebase.
- NEVER use `jest` for testing. You MUST use `jasmine` for testing.
- Use `react-testing-library` for testing React components.
- Use `msw` for mocking API responses.
- CHIRP provides generated MSW handlers for mocking. Never use raw REST MSW to mock CHIRP calls.
- Prefer using RTL accessible queries (e.g. `ByRole`, `ByText`) over implementation detail queries
- Use `import { getUserEventSession } from 'hs-test-utils/testing-library'` to perform user interactions for testing.
```js
await getUserEventSession().click(screen.getByRole('button', { name: /submit/i }));
```
- Import `screen`, `render` from `hs-test-utils/testing-library` to use the testing utilities.
- Import `getWorker`, `rest`, and other msw utilities from `hs-test-utils/msw` to configure msw handlers for mocking API responses:
```js
import { getWorker, rest } from 'hs-test-utils/msw';
import { createMyRpcSuccessHandler } from '../../generated/chirp/.../msw/MyServiceHandlers.ts';

getWorker().use(
   rest.get('https://api.hubteam.com/api/rest/lib/v1/users/me', (req, res, ctx) => {
      return res(ctx.json({
         id: '123',
         name: 'John Doe',
      }));
   }),
   createMyRpcSuccessHandler({ foo: 'bar' })
);
```
- Prefer using `anApiSpy.and.rejectWith(errorResponse);` over `anApiSpy.and.returnValue(Promise.reject(errorResponse));` when configuring Jasmine spies for Promise rejection scenarios.

### Acceptance Tests end-to-end E2E

You must implement end-to-end tests, known as `acceptance tests`, with `selenium` and `mocha`.

- acceptance tests file are in the `acceptance-tests/**/*` module of a repository
- When writing acceptance tests, you MUST read instructions for `acceptance-tests` via `mcp__devex-mcp-server__get_onepager`.

### After Completing Changes

- Whenever you finish making changes to frontend code, you MUST do all of the following:
  - Run the `bend hs-eslint` command to check for linting errors.
  - Execute the `mcp__devex-mcp-server__bend_package_ts_get_errors` tool to check for type errors. This is a tool you have to invoke and not a shell command.

----- FRONTEND_RULES END -----

<!-- END MANAGED CLAUDE RULE SECTION -->

