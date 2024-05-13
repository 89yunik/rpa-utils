from collections.abc import Iterable
from numbers import Number
from traceback import format_exc
from .log import logger

def error_handler(exit_program=True, on_exception=None, updated_exc_message=None, *exc_args, **exc_kwargs):
    def decorator(target_function):
        def wrapper(*args, **kwargs):
            function_name = target_function.__name__
            try:
                execute_function = f'\nfunc : {function_name}\nkwargs : {kwargs}\n'
                logger.info(execute_function)
                
                returned_value = target_function(*args, **kwargs)
                if isinstance(returned_value, (Number, Iterable, type(None))): 
                    record_returned_value = f'\nreturn : {returned_value}\n'
                    logger.info(record_returned_value)
                return returned_value
            except Exception as exc_message:
                if updated_exc_message: exc_message = updated_exc_message
                record_error_info = f'\nfunc : {function_name}\nexc : {exc_message}\ntraceback : {format_exc()}'
                logger.error(record_error_info)
                
                if on_exception: on_exception(*exc_args, **exc_kwargs)
                if exit_program: exit()
        return wrapper
    return decorator