#!/usr/bin/env python3
"""Rich Run - A command runner with rich formatting."""

import argparse
import shutil
import subprocess
import sys
import time
from datetime import datetime

from .banner import RICH_RUN_BANNER


def check_rich_cli():
    """Check if rich-cli is installed."""
    if not shutil.which("rich"):
        print("rich could not be found, please install it with 'pipx install rich-cli'")
        sys.exit(1)


def run_rich_command(args):
    """Run a rich command with the given arguments."""
    try:
        result = subprocess.run(["rich"] + args, check=False)
        return result.returncode
    except FileNotFoundError:
        print("Error: rich command not found")
        sys.exit(1)


def format_duration(seconds):
    """Format duration in a human-readable way."""
    if seconds < 1:
        return f"{seconds*1000:.0f}ms"
    elif seconds < 60:
        return f"{seconds:.2f}s"
    else:
        minutes = int(seconds // 60)
        remaining_seconds = seconds % 60
        return f"{minutes}m {remaining_seconds:.2f}s"


def main():
    """Main entry point for rich-run."""
    parser = argparse.ArgumentParser(
        description="Run commands with rich formatting", add_help=False
    )
    parser.add_argument(
        "--help", "-h", action="help", help="Show this help message and exit"
    )
    parser.add_argument("command", nargs=argparse.REMAINDER, help="Command to run")

    args = parser.parse_args()

    if not args.command:
        print(RICH_RUN_BANNER)
        parser.print_help()
        sys.exit(1)

    # Check if rich is installed
    check_rich_cli()

    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the command string for display
    command_str = " ".join(args.command)

    # Display command panel
    panel_args = [
        "--print",
        "--panel",
        "square",
        f"[dim]Command:[/dim] {command_str}",
        "--panel-style",
        "blue",
        "--title",
        f"[{timestamp}]",
    ]
    run_rich_command(panel_args)

    # Display separator rule
    run_rich_command(["--rule", "--rule-style", "dim"])

    # Record start time
    start_time = time.time()

    # Execute the actual command
    try:
        # If there's only one argument and it contains shell operators, run it through shell
        shell_operators = [
            "&&",
            "||",
            "|",
            ";",
            ">",
            ">>",
            "<",
            "2>",
            "2>>",
            "&",
            "$(",
            "`",
        ]
        if len(args.command) == 1 and any(
            op in args.command[0] for op in shell_operators
        ):
            result = subprocess.run(args.command[0], shell=True)
        else:
            result = subprocess.run(args.command)
        exit_code = result.returncode
    except FileNotFoundError:
        print(f"Error: Command '{args.command[0]}' not found")
        exit_code = 127
    except KeyboardInterrupt:
        print("\nCommand interrupted")
        exit_code = 130

    # Record end time and calculate duration
    end_time = time.time()
    duration = end_time - start_time

    # Display separator rule
    run_rich_command(["--rule", "--rule-style", "dim"])

    # Display result with duration
    duration_str = format_duration(duration)
    if exit_code == 0:
        run_rich_command(
            [
                "--print",
                f"[bold green]SUCCESS[/bold green] [dim](exit code: {exit_code}, duration: {duration_str})[/dim]",
            ]
        )
    else:
        run_rich_command(
            [
                "--print",
                f"[bold red]FAILED[/bold red] [dim](exit code: {exit_code}, duration: {duration_str})[/dim]",
            ]
        )

    print()  # Empty line

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
