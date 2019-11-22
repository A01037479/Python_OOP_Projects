"""
This module contains a Queue class that manages CityOverheadTimes objects,
two thread classes and main method.
"""

import datetime
import threading
import time

from city_processor import CityOverheadTimes, CityDatabase, ISSDataRequest


class CityOverheadTimeQueue:
    """
    A Queue structure that makes a list of CityOverheadTimes objects with
    methods populate and pop from the list.
    """
    def __init__(self):
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        """
        Append a CityOverheadTimes object to the queue.
        :param overhead_time: CityOverheadTimes
        """
        with self.access_queue_lock:
            self.data_queue.append(overhead_time)

    def get(self) -> CityOverheadTimes:
        """
        Pop the first CityOverheadTimes object from the queue.
        :return: CityOverheadTimes
        """
        with self.access_queue_lock:
            element = self.data_queue[0]
            del self.data_queue[0: 1]
            return element

    def __len__(self) -> int:
        with self.access_queue_lock:
            return len(self.data_queue)


class ProducerThread(threading.Thread):
    """
    ProducerThread extends from Thread class. It contains a
    CityOverheadTimeQueue object and a list of City objects.
    """
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self.queue = queue
        self.cities = cities

    def run(self) -> None:
        """
        When thread is started, the queue is populated with OverheadPassEvent
        object based on the list of City objects.
        Sleeps for 1s for every cities appended.
        """
        for city in self.cities:
            overhead_pass_event = ISSDataRequest.get_overhead_pass(city)
            self.queue.put(overhead_pass_event)
            if (self.cities.index(city) + 1) % 5 == 0:
                print('sleep for 1s.')
                time.sleep(1)


class ConsumerThread(threading.Thread):
    """
    ConsumerThread extends from Thread class. It contains a reference to the
    CityOverheadTimeQueue object that ProducerThread holds.
    """
    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self.data_incoming = True
        self.queue = queue

    def run(self) -> None:
        """
        When thread is started, and when data is incoming, the queue is
        checked and sleep for certain time.
        """
        while self.data_incoming is True or len(self.queue) > 0:
            if len(self.queue) == 0:
                print('sleep for 0.75s.')
                time.sleep(0.75)
            else:
                print(self.queue.get())
                print('sleep for 0.5s.')
                time.sleep(0.5)

    def set_data_incoming_false(self):
        self.data_incoming = False


def main():
    """
    The main method drives the main program.
    It instantiates three ProducerThread objects and one ConsumerThread object
    to create multi-threading for the program.
    """
    db = CityDatabase('city_locations_test.xlsx')
    cities = db.city_db
    num_cities = len(cities)
    cities1 = cities[0: int(num_cities / 3)]
    cities2 = cities[int(num_cities / 3): int(num_cities * 2 / 3)]
    cities3 = cities[int(num_cities * 2 / 3): num_cities + 1]

    city_overhead_time_queue = CityOverheadTimeQueue()

    producer_thread1 = ProducerThread(cities1, city_overhead_time_queue)
    producer_thread2 = ProducerThread(cities2, city_overhead_time_queue)
    producer_thread3 = ProducerThread(cities3, city_overhead_time_queue)
    consumer_thread = ConsumerThread(city_overhead_time_queue)
    start_time = datetime.datetime.now()
    producer_thread1.start()
    producer_thread2.start()
    producer_thread3.start()
    consumer_thread.start()
    producer_thread1.join()
    producer_thread2.join()
    producer_thread3.join()
    consumer_thread.set_data_incoming_false()
    consumer_thread.join()
    stop_time = datetime.datetime.now()
    duration = stop_time - start_time
    print(duration)


if __name__ == '__main__':
    main()
