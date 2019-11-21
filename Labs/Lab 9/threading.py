import threading
import time
from producer_consumer import CityOverheadTimeQueue
from city_processor import CityOverheadTimes, CityDatabase, ISSDataRequest


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



def main():
    db = CityDatabase('city_locations_test.xlsx')
    city_overhead_time_queue = CityOverheadTimeQueue()
    for city in db.city_db:
        overhead_pass_event = ISSDataRequest.get_overhead_pass(city)
        print(overhead_pass_event)
        city_overhead_time_queue.put(overhead_pass_event)

    print(len(city_overhead_time_queue.data_queue))
    city_overhead_time_queue.get()
    print(len(city_overhead_time_queue.data_queue))


if __name__ == '__main__':
    main()
