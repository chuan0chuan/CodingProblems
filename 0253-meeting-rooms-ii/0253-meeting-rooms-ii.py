class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x : x[0])
        room = 0
        heap = []
        for i in range(len(intervals)):
            if i == 0:
                room += 1
                heapq.heappush(heap, intervals[i][1])
            else:
                earliesEnd = heapq.heappop(heap)
                if intervals[i][0] < earliesEnd:
                    room += 1
                    heapq.heappush(heap, earliesEnd)
                    heapq.heappush(heap, intervals[i][1])
                else:
                    heapq.heappush(heap, intervals[i][1])
        return room