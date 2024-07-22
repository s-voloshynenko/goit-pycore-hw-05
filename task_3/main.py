import sys
from pathlib import Path
from log_utils import count_logs_by_level, load_logs, filter_logs_by_level

file_to_check = sys.argv[1] if len(sys.argv) > 1 else None
log_level = sys.argv[2] if len(sys.argv) > 2 else None
current_dir = Path(".")

def display_log_counts(counts: dict):
    indent_count = 17

    # headings
    print(f"{"Level":<{indent_count}}{" | "}{"Amount":<{indent_count}}")
    print(f"{"-" * indent_count:<{indent_count}}{" | "}{"-" * indent_count:<{indent_count}}")

    # body
    for key, prop in counts.items():
        print(f"{key:<{indent_count}}{" | "}{prop:<{indent_count}}")

    # margin
    print("\n")

def display_logs_by_level(logs_by_level: list, level: str):
    if not len(logs_by_level):
        print(f"No logs for the specified level - {level}")
        return

    # headings
    print(f"Log details for level '{level}':")

    # body
    for log in logs_by_level:
        print(f"{log["date"]} {log["time"]} - {log["message"]}")

def main(file_path: str, log_level: str | None):
    logs = load_logs(file_path)

    logs_by_level_count = count_logs_by_level(logs)
    display_log_counts(logs_by_level_count)

    if log_level:
        logs_by_specified_level = filter_logs_by_level(logs, log_level)
        display_logs_by_level(logs_by_specified_level, log_level)

if __name__ == "__main__":
    if not file_to_check:
        print("File name was not specified.")
        sys.exit(1)

    file_path = current_dir.joinpath(file_to_check)

    if not file_path.exists():
        print("Specified file doesn't exist.")
        sys.exit(1)

    main(file_path, log_level)
