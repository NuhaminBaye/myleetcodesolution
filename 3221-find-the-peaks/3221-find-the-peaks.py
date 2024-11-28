class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        peaks = []
        if len(mountain) < 3:
            return []
        for i in range(1, len(mountain) - 1):
            if mountain[i] > mountain[i - 1] and mountain[i] > mountain[i + 1]:
                peaks.append(i)
        return peaks