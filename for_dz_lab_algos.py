def next_smaller_element(sp):
    n = len(sp)
    result = [-1] * n
    stak = []

    for i in range(n - 1, -1, -1):
        while stak and sp[i] <= stak[-1]:
            stak.pop()

        if stak:
            result[i] = stak[-1]

        stak.append(sp[i])

    return result


print(next_smaller_element([52, 1, 7, 5, 51]))
