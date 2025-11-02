
def _load_logs(file_path: str) -> list:
    """
    Reads a log file and returns its contents as a list of lines.

    Args:
        file_path (str): The path to the log file.
    Returns:
        list: A list of lines from the log file.
    Raises 
        File not found.
        Wrong file format.
    """
    if not file_path.endswith('.log') or file_path.endswith('.txt'):
        print("Unsupported file format. Please provide a .log or .txt file.")
        raise Exception("Wrong file format")
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"Log file '{file_path}' not found.")
        raise Exception("File not found")
    else:
        return [line.strip() for line in lines]


def _normalize_level(level: str) -> str:
    """
    Normalizes the log level string to uppercase.

    Args:
        level (str): The log level string.
    Returns:
        str: The normalized log level string in uppercase.
    """
    return ' ' + level.upper().strip() + ' '


def _filter_logs_by_level(logs: list, level: str) -> list:
    """
    Filters log entries that contain a specific level.

    Args:
        logs (list): A list of log entries (strings).
        level (str): The level to filter logs by.
    Returns:
        list: A list of log entries that contain the level.
    """
    return [log for log in logs if _normalize_level(level) in log]


def _count_logs_by_level(logs: list, level: str) -> int:
    """
    Counts the number of log entries that contain a specific level.

    Args:
        logs (list): A list of log entries (strings).
        level (str): The level to count logs by.
    Returns:
        int: The count of log entries that contain the level.
    """
    return sum(1 for log in logs if _normalize_level(level) in log)


def display_log_summary(file_path: str, level = '') -> None:
    """
    Displays a summary of log entries filtered by a specific level.

    Args:
        file_path (str): The path to the log file.
        level (str): The level to filter and count logs by.
    """
    try:
        logs = _load_logs(file_path)
    except Exception as e:
        return
    
    filtered_logs = _filter_logs_by_level(logs, level)
    count = _count_logs_by_level(logs, level)

    print(f"Total entries: {len(logs)}")

    # If level is specified, show summary for that level
    if level:
        print(f"Log Summary for level '{level}':")
        print(f"Entries with level '{level}': {count}")
        print("Filtered Log Entries:")
    else:
        # General log summary if no level is specified
        print("General Log Summary:")

    for log in filtered_logs:
        print(log)
