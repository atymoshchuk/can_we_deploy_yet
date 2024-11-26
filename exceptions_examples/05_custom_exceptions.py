# For more examples, visit official documentation: https://docs.python.org/3.8/tutorial/errors.html#tut-userexceptions
class MyCustomException(Exception):
    pass


try:
    raise MyCustomException("Something custom happened!!!")
except (
    MyCustomException
) as e:  # always a good idea to be more specific in catching exceptions
    print("We are handling this exception here!", repr(e))
