# This code snippet shows basic idea how to catch exceptions
# For more information check: https://docs.python.org/3.8/library/exceptions.html
try:
    ...  # some code here might raise an exception
except Exception as e:  # catching exceptions
    print("Exception occurred:", repr(e))
