def findMinArrowShots(points):
    n = 0
    while points:
        x = points[0][0]
        j = 0
        count = 0 
        max_count = 0
        while x <= points[0][1]:
            for point in points:
                if x>= point[0] and x<= point[1]:
                    count += 1
            if max_count < count:
                j = x
                max_count = count
            x += 1
        i = 0
        while i <len(points):
            if j>= points[i][0] and j<= points[i][1]:
                del points[i]
                i -= 1
            i += 1
        n += 1
    return n
findMinArrowShots([[10,16],[2,8],[1,6],[7,12]])