
def get_key(d, key):
    '''
    >>> get_key({'a': {'b': {'c': 1}}}, 'a.b.c')
    1
    '''

    result = d
    for k in key.split('.'):
        if isinstance(result, dict):
            result = result.get(k, None)
        else:
            result = None
    return result
