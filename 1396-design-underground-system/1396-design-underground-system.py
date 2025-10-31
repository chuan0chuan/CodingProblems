class UndergroundSystem:
    def __init__(self):
        self.checkin = {} # id -> (stattionName, t)
        self.travel_times = defaultdict(lambda: [0,0]) # (start,end) -> [totalTime, count]
    
    def  checkIn(self, id:int, stationName: str, t: int) -> None:
        self.checkin[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkinStation, checkinT = self.checkin.pop(id)
        duration = t - checkinT
        key = (checkinStation, stationName)
        self.travel_times[key][0] += duration
        self.travel_times[key][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime , count = self.travel_times[(startStation, endStation)]
        return totalTime/count


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)