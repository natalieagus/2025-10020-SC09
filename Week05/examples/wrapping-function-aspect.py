from functools import wraps
import time

def log_function(fn):
    """Decorator that logs when the function starts and finishes."""
    @wraps(fn)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling {fn.__name__}()")
        start = time.time()
        result = fn(*args, **kwargs)       # run the real work
        duration = time.time() - start
        print(f"[LOG] {fn.__name__}() returned {result!r} in {duration:.4f}s")
        return result
    return wrapper


# Any function you decorate now gets automatic logging 

@log_function
def add(a, b):
    return a + b

@log_function
def greet(name):
    return f"Hello, {name}!"

@log_function
def slow_task():
    time.sleep(0.3)
    return "done"



add(2, 3)
greet("Alice")
slow_task()
