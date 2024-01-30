# Solve using dynamic programming with bottom up approach

def get_len_of_longest_subseq(x, y):
    xlen = len(x)
    ylen = len(y)
    max_val = 0
    look_up = {}
    for xind in range(xlen):
        for yind in range(ylen):
            key = f'{xind}{yind}'
            key1 = xind - 1
            key2 = yind - 1
            if x[xind] == y[yind]:
                look_up[key] = look_up.get(f'{key1}{key2}', 0) + 1
                max_val = max(max_val, look_up[key])
            else:
                look_up[key] = max(look_up.get(
                    f'{xind}{key2}', 0), look_up.get(f'{key1}{yind}', 0))
                max_val = max(max_val, look_up[key])

    return max_val


# Solve using dynamic programming top bottom approach
store = {}


def get_len_of_longest_subseq_top_bottom_approach(x, y, len_x, len_y):
    updated_lenx = len_x - 1
    updated_leny = len_y - 1
    key = f'{len_x}-{len_y}'
    val = store.get(key)

    if val is not None:
        return val
    if len_x == 0 or len_y == 0:
        return 0

    if x[updated_lenx] == y[updated_leny]:
        val = get_len_of_longest_subseq_top_bottom_approach(
            x[:-1], y[:-1], updated_lenx, updated_leny) + 1
        store[key] = val
    else:
        top_side = get_len_of_longest_subseq_top_bottom_approach(
            x[:-1], y, updated_lenx, len_y)
        bottom_side = get_len_of_longest_subseq_top_bottom_approach(
            x, y[:-1], len_x, updated_leny)
        val = max(top_side, bottom_side)
        store[key] = val

    return val
