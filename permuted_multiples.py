# Problem 52
x = 1
while True:
    one = { a for a in str(x)}
    two = { b for b in str(2*x)}
    thr = { c for c in str(3*x)}
    fou = { d for d in str(4*x)}
    fiv = { e for e in str(5*x)}
    six = { f for f in str(6*x)}

    if one == two and one == thr and one == fou and one == fiv and one == six:
        print(x)
        break
    x += 1