

def get_dict_for_defined_vars(obj: object):
    return {key: value for key, value in vars(obj) if not key.startswith('_') and value is not None}