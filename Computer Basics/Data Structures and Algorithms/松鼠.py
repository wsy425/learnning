def squirrel(time):
    list_s = [1]
    count = 1
    for t in range(time-1):
        if t < 1:
            new = 0
        else:
            new = count - list_s[-1]
        list_s.append(new)
        if t > 8:
            count = count + new - list_s[-10]
        else:
            count += new
    return count


print(squirrel(13))
