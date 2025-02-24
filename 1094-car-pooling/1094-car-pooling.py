class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x : x[1])
        cur_passenger = 0
        heap = []
        for numPassenger, start, end in trips:
            while heap and heap[0][0] <= start:
                drop , people = heapq.heappop(heap)
                cur_passenger -= people
            cur_passenger += numPassenger
            if cur_passenger > capacity:
                return False
            heapq.heappush(heap, (end, numPassenger))
        return True