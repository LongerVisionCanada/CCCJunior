def toHourStr(h: int) -> str:
    if h <= 9:
        res = "0" + str(h)
        return res
    else:
        return str(h)


def toMinuteStr(m: int) -> str:
    if m <= 9:
        res = "0" + str(m)
        return res
    else:
        return str(m)


if __name__ == "__main__":
    hh, mm = input().split(":")

    # hard coding
    h = int(hh)
    m = int(mm)

    # 0,1,2,3,4,10,11,12,19,20,21
    if (h >= 19 and h < 22) or h < 5 or (h >= 10 and h < 13):
        res = toHourStr(h + 2) + ":" + mm
    # 22
    elif h == 22:
        res = toHourStr(0) + ":" + mm
    # 23
    elif h == 23:
        res = toHourStr(1) + ":" + mm
    # 5
    elif h == 5:
        if m == 0:
            res = toHourStr(h + 2) + ":" + mm
        elif m == 20:  # 5:20~7:00
            res = toHourStr(h + 2) + ":" + toMinuteStr(40)
        elif m == 40:  # 5:40~7:00
            res = toHourStr(8) + ":" + toMinuteStr(20)
    # 6
    elif h == 6:
        if m == 0:  # 6:00~7:00
            res = toHourStr(9) + ":" + toMinuteStr(0)
        elif m == 20:  # 6:20~7:00
            res = toHourStr(9) + ":" + toMinuteStr(40)
        elif m == 40:  # 6:40~7:00
            res = toHourStr(10) + ":" + toMinuteStr(10)
    # 7
    elif h == 7:
        if m == 0:
            res = toHourStr(10) + ":" + toMinuteStr(30)
        elif m == 20:  # 7:20
            res = toHourStr(10) + ":" + toMinuteStr(40)
        elif m == 40:  # 7:40
            res = toHourStr(10) + ":" + toMinuteStr(50)
    # 8
    elif h == 8:
        if m == 0:  # 8:00
            res = toHourStr(11) + ":" + toMinuteStr(0)
        elif m == 20:  # 8:20
            res = toHourStr(11) + ":" + toMinuteStr(10)
        elif m == 40:  # 8:40
            res = toHourStr(11) + ":" + toMinuteStr(20)
    # 9
    elif h == 9:
        if m == 0:  # 9:00
            res = toHourStr(11) + ":" + toMinuteStr(30)
        elif m == 20:  # 9:20
            res = toHourStr(11) + ":" + toMinuteStr(40)
        elif m == 40:  # 9:40
            res = toHourStr(11) + ":" + toMinuteStr(50)
    # 13
    elif h == 13:
        if m == 0:  # 13:00~15:00
            res = toHourStr(15) + ":" + toMinuteStr(0)
        elif m == 20:  # 13:20~15:00
            res = toHourStr(15) + ":" + toMinuteStr(40)
        elif m == 40:  # 13:40~15:00
            res = toHourStr(16) + ":" + toMinuteStr(20)
    elif h == 14:
        if m == 0:  # 14:00~15:00
            res = toHourStr(17) + ":" + toMinuteStr(0)
        elif m == 20:  # 14:20~15:00
            res = toHourStr(17) + ":" + toMinuteStr(40)
        elif m == 40:  # 14:40~15:00
            res = toHourStr(18) + ":" + toMinuteStr(20)
    elif h == 15:
        if m == 0:  # 15:00
            res = toHourStr(19) + ":" + toMinuteStr(0)
        elif m == 20:  # 15:20~19:00
            res = toHourStr(19) + ":" + toMinuteStr(10)
        elif m == 40:  # 15:40~19:00
            res = toHourStr(19) + ":" + toMinuteStr(20)
    elif h == 16:
        if m == 0:  # 16:00~19:00
            res = toHourStr(19) + ":" + toMinuteStr(30)
        elif m == 20:  # 16:20~19:00
            res = toHourStr(19) + ":" + toMinuteStr(40)
        elif m == 40:  # 16:40~19:00
            res = toHourStr(19) + ":" + toMinuteStr(50)
    elif h == 17:
        if m == 0:  # 17:00~19:00
            res = toHourStr(20) + ":" + toMinuteStr(0)
        elif m == 20:  # 17:20~19:00
            res = toHourStr(20) + ":" + toMinuteStr(10)
        elif m == 40:  # 17:40~19:00
            res = toHourStr(20) + ":" + toMinuteStr(20)
    elif h == 18:
        if m == 0:  # 18:00~19:00
            res = toHourStr(20) + ":" + toMinuteStr(30)
        elif m == 20:  # 18:20~19:00
            res = toHourStr(20) + ":" + toMinuteStr(40)
        elif m == 40:  # 18:40~19:00
            res = toHourStr(20) + ":" + toMinuteStr(50)

    print(res)
