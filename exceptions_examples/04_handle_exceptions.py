# This code snippet explains why we should not raise a new exception
# while trying to handle already one exception
try:
    raise Exception("Something custom happened!!!")
except Exception as e:
    print("Printing exception", repr(e))

    # if we need to rise a new exception, we can use this trick,
    # as a result we will get a message: "The above exception was the direct cause of the following exception"
    raise Exception("I want my custom message!!!") from e
