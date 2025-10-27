def h(index, arguments):
    return arguments[index] - arguments[index - 1]

def _lambda(index, arguments):
    if index == 0:
        return 0
    return h(index, arguments) / (h(index, arguments) + h(index + 1, arguments))

def difference_quotient(xs, ys):
    if len(xs) == 1:
        return ys[0]
    return (difference_quotient(xs[1:], ys[1:]) - difference_quotient(xs[:-1], ys[:-1])) / (xs[-1] - xs[0])

def df(index, arguments, values):
    if index == 0:
        return 0
    return 6 * difference_quotient(arguments[(index - 1):(index + 2)],
                                   values[(index - 1):(index + 2)])

def second_derivative_values_at_nodes(xs, ys):
    n = len(xs) - 1

    q = [0 for _ in range(n)]                          
    u = [0 for _ in range(n)]
    l = [_lambda(k, xs) for k in range(n)]
    d = [df(k, xs, ys) for k in range(n)]

    for i in range(1, n):
        p = l[i] * q[i - 1] + 2
        q[i] = (l[i] - 1) / p
        u[i] = (d[i] - l[i] * u[i - 1]) / p

    m = [0 for _ in range(n + 1)]
    m[n - 1] = u[n - 1]

    for i in range(n - 2, 0, -1):
        m[i] = u[i] + q[i] * m[i + 1]

    return m

def kfunction(arguments, values, ms, index):
    return lambda x: \
        ((ms[index - 1] * (arguments[index] - x) ** 3) / 6 + (ms[index] * (x - arguments[index - 1]) ** 3) / 6 + \
        (values[index - 1] - (ms[index - 1] * h(index, arguments) ** 2) / 6) * (arguments[index] - x) + \
        (values[index] - (ms[index] * h(index, arguments) ** 2) / 6) * (x - arguments[index - 1])) / h(index, arguments)

def get_s(arguments, values):
    '''Cale Sm'''
    ms = second_derivative_values_at_nodes(arguments, values)
    def res(x):
        for index in range(1, len(arguments)):
            if arguments[index - 1] <= x < arguments[index]:
                return kfunction(arguments, values, ms, index)(x)
    return res