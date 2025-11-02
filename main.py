import argparse

from task1 import fibonacci_with_caching as fib_cache
from task2 import sum_profit
from task3 import display_log_summary

def parse_cli_args():
    """Parse command-line arguments for log summary configuration."""
    parser = argparse.ArgumentParser(
        description="Display a filtered summary for a log file."
    )
    parser.add_argument(
        "log_path",
        nargs="?",
        default="log.log",
        help="Path to the log file (default: log.log).",
    )
    parser.add_argument(
        "filter_level",
        nargs="?",
        default="error",
        help="Log level to filter by (default: error).",
    )
    parser.add_argument(
        "fibonacci_number",
        nargs="?",
        type=int,
        default=10,
        help="Fibonacci number to compute (default: 10).",
    )
    return parser.parse_args()


def main():
    """ Main function organizing the execution flow. """
    args = parse_cli_args()
    print("----------------TASK 1--------------")
    print("Calculating Fibonacci numbers with caching:")
    print(f"Fibonacci for {args.fibonacci_number}: ", fib_cache(args.fibonacci_number))  # Example: 10th Fibonacci number
    print("------------------------------------")
    print("----------------TASK 2--------------")
    text = "Загальний дохід працівника складається з декількох частин: \n" \
       "1000.01 як основний дохід, доповнений додатковими \n" \
       "надходженнями 27.45 і 324.00 доларів."
    print("Calculating sum of numbers in text:\n\n" + text + "\n")
    total = sum_profit(text)
    print(f"Total sum of numbers in text: {total}")
    print("------------------------------------")
    print("----------------TASK 3--------------")
    print("Displaying log summary:")
    display_log_summary(args.log_path, level=args.filter_level)
    print("------------------------------------")

if __name__ == "__main__":
    main()
