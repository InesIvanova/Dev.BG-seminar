import re

from blog.constants import EMAIL_REGEX


def validate_email(email):
    if re.search(EMAIL_REGEX, email):
        return True
    return False
