from collections import defaultdict

def parse_log_line(line: str) -> dict:
    date, time, level, *message = line.split(" ")

    parsed_log = {
        "date": date,
        "time": time,
        "level": level,
        "message": " ".join(message)
    }

    return parsed_log

def count_logs_by_level(logs: list) -> dict:
    logs_by_level_count = defaultdict(int)

    for log in logs:
        logs_by_level_count[log["level"]] += 1

    return logs_by_level_count

def filter_logs_by_level(logs: list, level: str) -> list:
    logs_by_level = filter(lambda log: log["level"].lower() == level.lower(), logs)
    return list(logs_by_level)

def load_logs(file_path: str):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            parsed_lines = []

            while True:
                line = file.readline()
                normalized_line = line.strip()
                if not normalized_line:
                    file.close()
                    break
                parsed_lines.append(parse_log_line(normalized_line))
            return parsed_lines
    except FileNotFoundError as e:
        print(f"File was not found. Details: {e}")
