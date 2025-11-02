
def fibonacci_with_caching(number: int) -> int:
    """ 
        Counts the nth Fibonacci number using memoization 
        to cache results of previous computations.
        Args:
            number (int): The position in the Fibonacci sequence to compute.
        Returns:
            int: The nth Fibonacci number.
    """
    cache = {}

    def fib_helper(current_number: int) -> int:
        """ 
           Helper function to compute Fibonacci number with caching.
           Uses a dictionary to store previously computed Fibonacci numbers.
           Counts recursively.
        """
        if current_number in cache:
            return cache[current_number]
        if current_number <= 1:
            return current_number
        result = fib_helper(current_number - 1) + fib_helper(current_number - 2)
        cache[current_number] = result
        return result

    return fib_helper(number)