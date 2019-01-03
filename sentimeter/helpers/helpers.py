from flask import request, jsonify
from functools import wraps


def decorator_function(func):
    """
    Wrapper Function
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # TODO: Implement logging to some source
        return func(*args, **kwargs)
    return wrapper
