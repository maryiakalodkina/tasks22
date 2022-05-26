# LeetCode task 56

def merge(intervals):
        intervals.sort()
        allMerged = False
        skip = False
        while allMerged != True:
            mergedIntervals = []
            for i in range(0, len(intervals)):
                if skip:
                    skip = False
                    pass
                elif i+1 < len(intervals) and intervals[i+1][0] <= intervals[i][1]:
                    temp = []
                    temp.append(intervals[i][0])
                    if intervals[i+1][1] <= intervals[i][1]:
                        temp.append(intervals[i][1])
                        skip = True
                    else:
                        temp.append(intervals[i+1][1])
                    mergedIntervals.append(temp) 
                else:
                    mergedIntervals.append(intervals[i])
            if intervals == mergedIntervals:
                allMerged = True
            else:
                intervals.clear()
                intervals+=mergedIntervals
        return intervals     

intervals1 = [[1,3],[2,6],[8,10],[15,18]] #[[1,6],[8,10],[15,18]]
intervals2 = [[1,4],[4,5]] #[[1,5]]
intervals3 = [[1,4],[0,4]] #[[0,4]]
intervals4 = [[1,4],[2,3]] #[[1,4]]
intervals5 = [[2,3],[4,5],[6,7],[8,9],[1,10]] #[[1,10]]
intervals6 = [[2,3],[5,5],[2,2],[3,4],[3,4]] #[[2,4],[5,5]]

answer = merge(intervals6)
print(answer)