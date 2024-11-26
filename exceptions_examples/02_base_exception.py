# This code snippet explains how Exception hierarchy works
try:
    input()  # try to interrupt it and check which exception will be called
except Exception as e:
    print("Exception occurred:", repr(e))
except BaseException as e:
    # KeyboardInterrupt inherits from BaseException so as to not be accidentally caught by code that catches Exception
    # and thus prevent the interpreter from exiting. -> from official Python documentation
    print("BaseException occurred:", repr(e))
