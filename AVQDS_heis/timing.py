import time

def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()
        print(f' {method.__name__} {te - ts:.2f} s')
        return result
    return timed
