import time

# Create Your Own Python Decorator
# Objective Create your own decorator function to measure
# the amount of seconds that a function takes to execute.

current_time = time.time()
# print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper():
        start_time = time.time()  # Record the start time
        result = function()  # Execute the function
        end_time = time.time()  # Record the end time
        print(f"Function {function.__name__} took {end_time - start_time:.4f} seconds to execute.")
        return result  # Return the original function's result
    return wrapper


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()