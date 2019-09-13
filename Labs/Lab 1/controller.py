import random
import time
from asteroid import Asteroid
from datetime import datetime


class Controller:
    """
    A controller that controls asteroids
    """
    def __init__(self):
        """
        Initialization of a controller
        Creates 100 Asteroids.
        """
        self.asteroid_list = []
        i = 0
        while i < 100:
            self.asteroid_list.append(Asteroid(random.randint(1, 4),
                                               [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],
                                               [random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5)],
                                               datetime.now()))
            i += 1

    def simulate(self, seconds):
        """
        Simulates the movements for asteroids.
        Accepts a number of seconds and move all asteroids every second
        Prints resultant information
        :param seconds: an int
        """
        i = 0
        while i < int(seconds):
            print(datetime.now())
            j = 0
            while j < 100:
                self.asteroid_list[j].move()
                print(self.asteroid_list[j])
                j += 1
            time.sleep(1)
            i += 1


def main():
    """
    Main method that drives the program.
    Creates a controller object, accepts a user input seconds and starts simulation of asteroid movements
    """
    seconds_input = input("Enter Seconds: ")
    controller = Controller()
    controller.simulate(seconds_input)


if __name__ == '__main__':
    main()
