def set_years_seconds(d):
    d[0][0] = d[4][0] // (365 * 24 * 60 * 60)
    d[4][0] = d[4][0] % (365 * 24 * 60 * 60)


def set_days_seconds(d):
    d[1][0] = d[4][0] // (24 * 60 * 60)
    d[4][0] = d[4][0] % (24 * 60 * 60)


def set_hours_seconds(d):
    d[2][0] = d[4][0] // (60 * 60)
    d[4][0] = d[4][0] % (60 * 60)


def set_minutes_seconds(d):
    d[3][0] = d[4][0] // 60
    d[4][0] = d[4][0] % 60


def set_values(d):
    set_years_seconds(d)
    set_days_seconds(d)
    set_hours_seconds(d)
    set_minutes_seconds(d)


def format_duration(seconds):
    if seconds == 0:
        return "now"
    d = [[0, "year"], [0, "day"], [0, "hour"], [0, "minute"], [seconds, "second"]]
    set_values(d)
    for element in d[::-1]:
        if element[0] == 0:
            del d[d.index(element)]
        elif element[0] > 1:
            element[1] += "s"
    ret_values = [f"{element[0]} {element[1]}" for element in d]
    if len(ret_values) == 1:
        return ret_values[0]
    ret_values = [", ".join(ret_values[:len(ret_values) - 1]), ret_values[len(ret_values) - 1]]
    return " and ".join(ret_values)