# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
     def minMeetingRooms(self, intervals):
            starts = []
            ends = []
            for i in intervals:
                starts.append(i.start)
                ends.append(i.end)

            starts.sort()
            ends.sort()
            s = e = 0
            numRooms = available = 0
            while s < len(starts):
                if starts[s] < ends[e]:
                    if available == 0:
                        numRooms += 1
                    else:
                        available -= 1

                    s += 1
                else:
                    available += 1
                    e += 1

            return numRooms
            
  class Solution(object):
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """

        # If there is no meeting to schedule then no room needs to be allocated.
        if not intervals:
            return 0

        # The heap initialization
        free_rooms = []

        # Sort the meetings in increasing order of their start time.
        intervals.sort(key= lambda x: x.start)

        # Add the first meeting. We have to give a new room to the first meeting.
        heapq.heappush(free_rooms, intervals[0].end)

        # For all the remaining meeting rooms
        for i in intervals[1:]:

            # If the room due to free up the earliest is free, assign that room to this meeting.
            if free_rooms[0] <= i.start:
                heapq.heappop(free_rooms)

            # If a new room is to be assigned, then also we add to the heap,
            # If an old room is allocated, then also we have to add to the heap with updated end time.
            heapq.heappush(free_rooms, i.end)

        # The size of the heap tells us the minimum rooms required for all the meetings.
        return len(free_rooms)

   
