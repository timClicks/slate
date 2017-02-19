import re

def normalise_whitespace(s):
    """ 
    Returns a string that has at most one whitespace
    character between non-whitespace characters. We
    leave a few extra spaces because most NLP parsers
    don't tend to care.

    >>> normalise_whitespace(' hi   there')
    ' hi there'
    >>> normalise_whitespace('meh\n\n\f')
    'meh '
    """
    return re.sub(r'\s+', ' ', s) 
