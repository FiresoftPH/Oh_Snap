from time import time

initial = time()
while True:
    current = time()
    if current - initial >= 1:
        print(current - initial)
        initial = time()

    