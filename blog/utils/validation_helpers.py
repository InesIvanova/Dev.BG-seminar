import re

from blog.constants import EMAIL_REGEX
from blog.utils.exceptions import InvalidInput


def validate_email(**kwargs):
    email_data = kwargs.get('user_data').get('email')
    email = email_data.get('email')
    if email and not re.search(EMAIL_REGEX, email):
        raise InvalidInput(f"Invalid email {email}")


def validate(*validation_functions):
    def decorator(decorated_function):
        def wrapper(*args, **kwargs):
            for validation_func in validation_functions:
                if not callable(validation_func):
                    raise TypeError("The object in the decorator should be a function reference")
                validation_func(**kwargs)
            decorated_function(*args, **kwargs)
        return wrapper
    return decorator
