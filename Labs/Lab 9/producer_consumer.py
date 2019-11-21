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
            overhead_pass_event = ISSDataRequest.get_overheadpass(city)
            self.queue.put(overhead_pass_event)
            if (self.cities.index(city) + 1) % 5 == 0:
                time.sleep(1)


class ConsumerThread(threading.Thread):
    def __init__(self, queue: CityOverheadTimeQueue):
        super().__init__()
        self.data_incoming = True
        self.queue = queue

    def run(self) -> None:
        while self.data_incoming is True or len(self.queue) > 0:
            print(self.queue.get())
            time.sleep(0.5)
            if len(self.queue) == 0:
                time.sleep(0.75)

    def set_data_incoming_false(self):
        self.data_incoming = False



def main():
    db = CityDatabase('city_locations_test.xlsx')
    city_overhead_time_queue = CityOverheadTimeQueue()
    for city in db.city_db:
        overhead_pass_event = ISSDataRequest.get_overhead_pass(city)
        print(overhead_pass_event)
        city_overhead_time_queue.put(overhead_pass_event)

    pt = ProducerThread(db.city_db, city_overhead_time_queue)
    ct = ConsumerThread(city_overhead_time_queue)
    pt.start()
    ct.start()
    pt.join()
    ct.set_data_incoming_false()
    ct.join()


if __name__ == '__main__':
    main()
