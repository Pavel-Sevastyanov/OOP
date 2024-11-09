from contextlib import contextmanager

@contextmanager
def safe_open(filename, mode='r'):
    try:
        file_1 = open(filename, mode=mode)
        yield file_1, None
        file_1.close()
    except Exception as error:
        yield None, error
    