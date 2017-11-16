import os
from functools import wraps

# Create the directory if it does not exists
def autoCreateDir(dirPath):

    def autoCreateDirDecorator(func):
        # Wraps decorator of "autoCreateDir" so that the decorated function has the right attributes
        # (If not, the decorated function will have the attribute of the "decorated(*args, **kwargs)" function)
        @wraps(func)
        def wrapper(*args, **kwargs):
            if not os.path.isdir(dirPath):
                os.mkdir(dirPath)

            return func(*args, **kwargs)

        return wrapper

    return autoCreateDirDecorator
