def h(index, arguments):
    return arguments[index] - arguments[index - 1]

def difference_quotient(arguments, values):
    if len(arguments) == 1:
        return values[0]
    return (difference_quotient(arguments[1:], values[1:]) - difference_quotient(arguments[:-1], values[:-1])) / (arguments[-1] - arguments[0])

def dk(index, arguments, values):
    if index == 0:
        return 0
    return 6 * difference_quotient(arguments[(index - 1):(index + 2)],
                                   values[(index - 1):(index + 2)])
def _lambda(index, arguments):
    if index == 0:
        return 0
    result = h(index, arguments) / (h(index, arguments) + h(index + 1, arguments))
    return result
def second_derivative_values_at_nodes(xs, ys):
    n = len(xs) - 1

    pom1 = [0] * n
    pom2 = [0] * n
    l = [_lambda(k, xs) for k in range(n)]
    d = [dk(k, xs, ys) for k in range(n)]

    for i in range(1, n):
        p = l[i] * pom1[i - 1] + 2
        pom1[i] = (l[i] - 1) / p
        pom2[i] = (d[i] - l[i] * pom2[i - 1]) / p

    m = [0] * (n + 1)
    m[n - 1] = pom2[n - 1]

    for i in range(n - 2, 0, -1):
        m[i] = pom2[i] + pom1[i] * m[i + 1]

    return m

def kfunction(arguments, values, ms, index):
    def calculate_x(x):
        term1 = (ms[index - 1] * (arguments[index] - x) ** 3) / 6
        term2 = (ms[index] * (x - arguments[index - 1]) ** 3) / 6
        term3 = (values[index - 1] - (ms[index - 1] * h(index, arguments) ** 2) / 6) * (arguments[index] - x)
        term4 = (values[index] - (ms[index] * h(index, arguments) ** 2) / 6) * (x - arguments[index - 1])
        result = (term1 + term2 + term3 + term4) / h(index, arguments)
        return result

    return calculate_x


def s(arguments, values):
    ms = second_derivative_values_at_nodes(arguments, values)
    def result(x):
        for index, arg in enumerate(arguments[1:], start=1):
            if arguments[index - 1] <= x < arg:
                return kfunction(arguments, values, ms, index)(x)
    return result