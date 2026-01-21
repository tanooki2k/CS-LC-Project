def float_range(start: float, stop: float, step: float):
    cond = False
    if start > stop:
        if step >= 0:
            raise ValueError("Step must be less than 0")
        cond = lambda: start > stop
    elif start < stop:
        if step <= 0:
            raise ValueError("Step must be greater than 0")
        cond = lambda: start < stop

    while cond():
        yield start
        start += step
