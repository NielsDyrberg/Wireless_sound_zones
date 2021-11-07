import time

randomarray = [0] * 100000


def test_timing():
    for x in range(1000):
        timestart = time.perf_counter()
        for y in range(100):
            fillarray()
        timeend = time.perf_counter()
        howlong = (timeend - timestart)*1000000
        print(f"{howlong:0.0f}")

def fillarray():

    arraysize = len(randomarray)

    for x in range(arraysize):
        randomarray[x] = int((12345 * (0.1 * x) + (23 * x)))
    #print(randomarray)

if __name__ == "__main__":
    test_timing()

"""
Tid i sekunder uden top prioritet
Tid 1.1355853
Tid 1.1381109
Tid 1.1378448
Tid 1.1373751
Tid 1.1379302
Tid 1.1375248
Tid 1.1370060
Tid 1.1377264
Tid 1.1384708
Tid 1.1377597
"""