def trim_whitespace(s):
    """ 
    Returns a string that has at most one whitespace
    character between non-whitespace characters.

    >>> trim_whitespace(' hi   there')
    'hi there'
    """
    buffer  = ''
    for i, letter in enumerate(s):
         if letter.isspace():
             try:
                 if s[i+1].isspace(): continue
             except IndexError: 
                 pass
         buffer = buffer + letter
    
    return buffer.strip()
