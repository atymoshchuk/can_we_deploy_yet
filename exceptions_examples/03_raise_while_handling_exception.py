# This code snippet explains why we should not raise a new exception
# while trying to handle already one exception
try:
    raise Exception("Something custom happened!!!")
except Exception as e:
    print("Printing exception", repr(e))

    # if we raise a new exception here, we will get a message that
    # while handling our exception another exception occurred
    raise Exception("I want my custom message!!!")
