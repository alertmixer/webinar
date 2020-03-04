while True:
    for i in range(0, 100000000):
        Gig = 1024 * 1024 * 1024 * 2
        a = 787878788888888888888888888888 * (i * Gig)
        a = a * i
        print(str(a) * 2)
