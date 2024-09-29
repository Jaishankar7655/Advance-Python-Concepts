from threading import Thread
from time import sleep
class Race1(Thread):

    def run(self):
        for i in range(5):
            print("Race one class is running: ")
            sleep(1)

class Race2(Thread):
    def run(self):
        for i in range(5):
            print("Race 2 class is runnig")
            sleep(1)

obj1 = Race1()
obj2 = Race2()

obj1.start()
obj2.start()