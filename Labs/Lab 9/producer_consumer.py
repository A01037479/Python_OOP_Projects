import datetime
import threading
import time

from city_processor import CityOverheadTimes, CityDatabase, ISSDataRequest


class CityOverheadTimeQueue:
    def __init__(self):
        self.data_queue = []
        self.access_queue_lock = threading.Lock()

    def put(self, overhead_time: CityOverheadTimes) -> None:
        with self.access_queue_lock:
            self.data_queue.append(overhead_time)

    def get(self) -> CityOverheadTimes:
        with self.access_queue_lock:
            element = self.data_queue[0]
            del self.data_queue[0: 1]
            return element

    def __len__(self) -> int:
        return len(self.data_queue)


class ProducerThread(threading.Thread):
    def __init__(self, cities: list, queue: CityOverheadTimeQueue):
        super().__init__()
        self.queue = queue
        self.cities = cities

    def run(self) -> None:
        for city in self.cities:
            overhead_pass_event = ISSDataRequest.get_overhead_pass(city)
            self.queue.put(overhead_pass_event)
            if (self.cities.index(city) + 1) % 5 == 0:
                print('sleep for 1s.')
                time.sleep(1)


class ConsumerThread(threading.Thread):
    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self.data_incoming = True
        self.queue = queue

    def run(self) -> None:
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
    db = CityDatabase('city_locations_test.xlsx')
    cities = db.city_db
    num_cities = len(cities)
    cities1 = cities[0: int(num_cities / 3)]
    cities2 = cities[int(num_cities / 3): int(num_cities * 2 / 3)]
    cities3 = cities[int(num_cities * 2 / 3): num_cities + 1]

    city_overhead_time_queue = CityOverheadTimeQueue()

    # pt = ProducerThread(cities, city_overhead_time_queue)
    pt1 = ProducerThread(cities1, city_overhead_time_queue)
    pt2 = ProducerThread(cities2, city_overhead_time_queue)
    pt3 = ProducerThread(cities3, city_overhead_time_queue)
    ct = ConsumerThread(city_overhead_time_queue)
    start_time = datetime.datetime.now()
    # pt.start()
    pt1.start()
    pt2.start()
    pt3.start()
    ct.start()
    # pt.join()
    pt1.join()
    pt2.join()
    pt3.join()
    ct.set_data_incoming_false()
    ct.join()
    stop_time = datetime.datetime.now()
    duration = stop_time - start_time
    print(duration)


if __name__ == '__main__':
    main()
