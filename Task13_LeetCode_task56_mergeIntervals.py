# LC task 56

def merge(intervals):
        intervals.sort()
        mergedIntervals = []
        allMerged = False
        skip = False
        while allMerged != True:
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
                mergedIntervals.clear()
        return intervals     

intervals = [[1,3],[2,6],[8,10],[15,18]]
answer = merge(intervals)
print(answer)