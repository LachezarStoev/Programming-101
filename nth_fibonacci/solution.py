def nth_fibonacci(nth):
    if nth < 1:
        return "Error!" #better description for Exception
    if(nth==1 or nth==2):
        return 1
    fst = 1
    snd = 1
    next_n = fst + snd
    steps = 3 
    while(steps != nth + 1):
        fst = snd
        snd = next_n
        next_n = fst + snd
        steps += 1
    result = snd
    return result