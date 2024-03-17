import time

def benchmark(iters=1, output='terminal', file_name=None, round_up=None):
    assert type(output) in set([str, list])
    output = set(output) if type(output) is list else set([output])
    assert all([i in (['terminal','file','dict']) for i in output])
    assert True if 'file' not in output else (file_name is not None)
    assert type(iters) is int and iters > 0

    def actual_decorator(func):
        import time
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            result = total/iters if round_up is None else round(total/iters, round_up)
            result_str = 'benchmark: {} sec.'.format(result)
            if 'terminal' in output:
                print(result_str)
            if 'dict' in output:
                return_value = {'benchmark': result, 'output': return_value}
            if 'file' in output:
                with open(file_name, 'a') as f:
                    print(result_str, file=f)
            return return_value
        return wrapper
    return actual_decorator


# example 1
@benchmark()
def f():
    s = sorted([int(777/(i%17+1)) for i in range(1,10_000)])
    return sum(s) / len(s)
f()

# example 2
@benchmark(iters=10)
def f():
    s = sorted([int(777/(i%17+1)) for i in range(1,10_000)])
    return sum(s) / len(s)
f()
