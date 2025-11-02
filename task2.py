import re

def generator_numbers_in_text(text: str):
    """
    Generator function that yields numbers found in the input text.
    Uses regular expressions to identify both integer and floating-point numbers.
    
    Args:
        text (str): The input string containing numbers and other characters.
        
    Yields:
        int: The next number found in the text.
    """
    # Regular expression to match integers and floating-point numbers
    number_pattern = re.compile(r'\d+\.\d+|\d+')

    for match in number_pattern.finditer(text):
        # Extract the matched number as a string
        number_str = match.group()
        # Convert to float if it contains a decimal point, else to int
        if '.' in number_str:
            yield float(number_str)
        else:
            yield int(number_str)


def sum_profit(text: str) -> float:
    """
    Sums all the numbers found in the input text.
    
    Args:
        text (str): The input string containing numbers and other characters.
        
    Returns:
        float: The sum of all numbers found in the text.
    """
    total_sum = 0.0
    for number in generator_numbers_in_text(text):
        total_sum += number
    return total_sum

