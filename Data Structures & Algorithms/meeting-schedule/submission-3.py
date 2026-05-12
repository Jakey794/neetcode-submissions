"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        a=defaultdict(int)
        for i in intervals:
            for j in range(i.start,i.end):
                a[j]+=1
        return 2 not in list(a.values())

