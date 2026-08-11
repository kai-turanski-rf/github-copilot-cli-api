"""Module to run github copilot cli commands.

Should generally run things in format:
```
gh copilot --available-tools --disable-builtin-mcps --disallow-temp-dir --no-experimental
    --model "<model>" -s --session-id "<current_session_id>" -p "<input_prompt>"
```

Good default settings are:
 - model = "claude-sonnet-5"
"""
import subprocess
from uuid import UUID

DEFAULT_MODEL = "claude-sonnet-5"


def build_copilot_command(
    prompt: str,
    session_id: UUID | str,
    model: str = DEFAULT_MODEL,
) -> list[str]:
    """Build the argv list for a `gh copilot` invocation (no shell involved)."""
    args = [
        "gh",
        "copilot",
        "--available-tools",
        "--disable-builtin-mcps",
        "--disallow-temp-dir",
        "--no-experimental",
        "--model",
        model,
        "-s",
    ]

    if session_id:
        args.extend(["--session-id", str(session_id)])

    args.extend(["-p", prompt])
    return args


def get_copilot_completion(
    prompt: str,
    session_id: UUID | str | None,
    model: str = DEFAULT_MODEL,
    timeout: float | None = 100.0,
)-> str:
    """Run `gh copilot` with the given prompt/session and return its stdout."""
    command = build_copilot_command(prompt, session_id, model)
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        timeout=timeout,
        check=True,
    )
    return result.stdout.strip() if result.stdout else result.stderr.strip() if result.stderr else ""
