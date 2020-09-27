import re

from blog.constants import EMAIL_REGEX
from blog.utils.exceptions import InvalidInput


def validate_email(function):
    def wrapper(*args, **kwargs):
        email_data = kwargs.get('user_data').get('email')
        email = email_data.get('email')
        if email and not re.search(EMAIL_REGEX, email):
            raise InvalidInput(f"Invalid email {email}")
        function(*args, **kwargs)
    return wrapper
