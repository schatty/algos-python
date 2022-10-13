def isReflected(points) -> bool:
    # Edge case
    if len(points) <= 1:
        return True
    if len(points) == 2:
        return points[0][1] == points[1][1] or (points[0][0] == points[1][0]) 
    
    # Remove duplicates O(n)
    points = list(set([(x, y) for (x, y) in points]))
    n = len(points)
    
    # Find symmetry O(n * logn)
    points.sort(key = lambda x: x[0])
    if n % 2 == 0:
        x_sym = (points[n // 2][0] + points[n // 2 - 1][0]) / 2
    else:
        x_sym = points[n // 2][0]

    # Construct hash map O(n)
    hsh = {}
    for (x, y) in points:
        if x not in hsh:
            hsh[x] = [y]
        else:
            hsh[x].append(y)
            
    # Check symmetry O(n)
    for (x, y) in points:
        if x < x_sym:
            x_find = x_sym + (x_sym - x)
        else:
            x_find = x_sym - (x - x_sym)
        
        if x_find not in hsh or y not in hsh[x_find]:
            return False

    return True

print(isReflected([[-16,1],[16,1],[16,1]]))
