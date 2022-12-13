class Solution:
    # TC: O(nlogn)
    # MC: O(n)
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        mergedIntervals = []

        for interval in intervals:
            if mergedIntervals:
                prevIntervalEnd = mergedIntervals[-1][1]
            currIntervalStart = interval[0]
            currIntervalEnd = interval[1]

            if not mergedIntervals or prevIntervalEnd < currIntervalStart:
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1][1] = max(prevIntervalEnd, currIntervalEnd)

        return mergedIntervals
