import threading

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


# def main():
#     db = CityDatabase('city_locations_test.xlsx')
#     city_overhead_time_queue = CityOverheadTimeQueue()
#     for city in db.city_db:
#         overhead_pass_event = ISSDataRequest.get_overhead_pass(city)
#         print(overhead_pass_event)
#         city_overhead_time_queue.put(overhead_pass_event)
#
#     print(len(city_overhead_time_queue.data_queue))
#     city_overhead_time_queue.get()
#     print(len(city_overhead_time_queue.data_queue))
#
#
# if __name__ == '__main__':
#     main()
