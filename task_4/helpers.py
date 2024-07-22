def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return e
        except IndexError as e:
            return e
        except KeyError as e:
            return e

    return inner

def input_validate_args(params: list):
    def decorator(func):
        def inner(*args, **kwargs):
            if len(args[0]) != len(params):
                raise ValueError(
                    f"Enter the argument for the command. Required arguments: {", ".join(params)}."
                )
            return func(*args, **kwargs)
        return inner
    return decorator
