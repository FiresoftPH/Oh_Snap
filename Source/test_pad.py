from camera import ShowFrame
import threading

def test_function():
    while True:
        msg = str(input("Type: "))
        print(msg)

def run_cam():
    app = ShowFrame()
    app.detect_hand()

thread_1 = threading.Thread(target = test_function)
thread_2 = threading.Thread(target = run_cam)

thread_1.start()
thread_2.start()