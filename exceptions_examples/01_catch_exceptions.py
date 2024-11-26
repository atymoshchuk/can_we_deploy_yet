# This code snippet explains how Exception hierarchy works
# For more information check: https://docs.python.org/3.8/library/exceptions.html
try:
    raise Exception("My custom exception")
except (
    Exception
) as e:  # catching Exception is not the best idea, try to be more specific
    print("Exception occurred:", repr(e))
except (
    BaseException
) as e:  # catching BaseException is even worse, as we can catch KeyboardInterrupt here as well
    print("BaseException occurred:", repr(e))
