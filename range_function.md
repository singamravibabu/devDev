# range() iterator function
- Syntax:
    - range([start, ]stop[, step])
    - start and stop parameters are optional
    - By default, start = 0 and step = 1
    - The start = 0 means the range() function starts giving numbers from 0
    - The step = 1, means the range() function adds step value continuously to start value till it teaches stop value. So, the last value is close stop, but not stop.
    - Start value is inclusive and stop value is exclusive

### range(stop)     # start is 0 & step is 1
range(5)        # 0, 1, 2, 3, 4
range(3)        # 0, 1, 2
range(8)        # 0, 1, 2, 3, 4, 5, 6, 7

### range(start, stop)      # step is 1
range(4, 10)            # 4, 5, 6, 7, 8, 9
range(-3, 3)            # -3, -2, -1, 0, 1, 2
range(3, -3)            # wrong

### range(start, stop, step)
range(5, 51, 5)     # 5, 10, 15, 20, 25, 30, 35, 40, 45, 50
range(3, 21, 3)     # 3, 6, 9, 12, 15, 18
range(-50, 50, 20)  # -50, -30, -10, 10, 30

range(100, -100, -30)   # 100, 70, 40, 10, -20, -50, -80