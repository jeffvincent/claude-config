Copy the content of your most recent response (the assistant message immediately preceding this /pbcopy invocation) to the macOS clipboard using pbcopy.

Steps:
1. Identify the full text of your last response — everything you wrote, exactly as it appeared to the user.
2. Run a Bash command that pipes that exact text into `pbcopy`. Use a heredoc or printf to preserve newlines and special characters faithfully.
3. Confirm to the user with a single short line: "Copied to clipboard."

Do not summarize, truncate, or modify the content. Copy it verbatim.
