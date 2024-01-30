# Solving using bottom up approach
def get_longest_subsequences(x, y, xlen, ylen):
    max_val = 0
    look_up = {}
    for xind in range(xlen):
        for yind in range(ylen):
            key = f'{xind}{yind}'
            x_pre_ind = xind - 1
            y_pre_ind = yind - 1
            if x[xind] == y[yind]:
                look_up[key] = look_up.get(f'{x_pre_ind}{y_pre_ind}', 0) + 1
                max_val = max(max_val, look_up[key])
            else:
                look_up[key] = max(look_up.get(
                    f'{xind}{y_pre_ind}', 0), look_up.get(f'{x_pre_ind}{yind}', 0))
                max_val = max(max_val, look_up[key])
    return max_val
