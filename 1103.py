h1, m1, h2, m2 = map(int, input().split())

while h1 != 0 or h2 != 0 or m1 != 0 or m2 != 0:
    if h1 == 0:
        h1 = 24
    if h2 == 0:
        h2 = 24
    full_min1 = (h1*60) + m1 
    full_min2 = (h2*60) + m2

    if h1 == 24:
        h1 = 0
    if h2 == 24:
        h2 = 0
    
    if full_min2 < full_min1:
        diff = full_min1 - full_min2
        one_day_to_min = 24*60
        print(one_day_to_min-diff)
    else:
        print(full_min2 - full_min1)

    h1, m1, h2, m2 = map(int, input().split())