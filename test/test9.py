def value_to_str(data):
    if isinstance(data, dict):
        for key in data:
            data[key] = value_to_str(data[key])
    else:
        data = str(data)
    return data


def gap_set(gap):
    if isinstance(gap, dict):
        for key in gap:
            gap[key] = gap_set(gap[key])
    else:
        gap = "<font color='{}' >{:+d}<font>".format(
            '#21f805' if gap['zj'][0] > 0 else '#f40c0c', gap['zj'][0])
    return gap


a = {'zj': {'sg': 42, 'lz': 166}, 'jt': {'sg': 42, 'lz': 166}, 'z_jt': {'sg': 48, 'lz': 191}, 'a': {'sg': 6, 'lz': 25},
     'ty': 46, 'san_one': 52, 'san_two': 58}
b = {'zj': {'sg': 42, 'lz': 166}, 'jt': {'sg': 42, 'lz': 166}, 'z_jt': {'sg': 48, 'lz': 191}, 'a': {'sg': 6, 'lz': 25},
     'ty': 46, 'san_one': 52, 'san_two': 58}
print(value_to_str(a))
