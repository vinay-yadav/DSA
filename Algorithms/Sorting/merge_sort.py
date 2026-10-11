"""
Merge Sort
"""


class MergeSort:
    def sort(self, nums: list[int]) -> list[int]:
        """Return a new sorted list (stable). The input is not modified."""
        arr = nums[:]  # work on a copy
        if len(arr) < 2:  # handles [] and [x]
            return arr

        buf = [0] * len(arr)  # single reusable scratch buffer
        self._sort(arr, buf, 0, len(arr) - 1)
        return arr

    def _sort(self, arr: list[int], buf: list[int], lo: int, hi: int) -> None:
        if lo >= hi:  # 0 or 1 element: already sorted
            return

        mid = lo + (hi - lo) // 2
        self._sort(arr, buf, lo, mid)  # sort left half in place
        self._sort(arr, buf, mid + 1, hi)  # sort right half in place
        self._merge(arr, buf, lo, mid, hi)

    @staticmethod
    def _merge(arr: list[int], buf: list[int], lo: int, mid: int, hi: int) -> None:
        # Snapshot the range, then merge back into arr from the snapshot.
        buf[lo : hi + 1] = arr[lo : hi + 1]

        i, j, k = lo, mid + 1, lo
        while i <= mid and j <= hi:
            if buf[i] <= buf[j]:  # <= keeps the sort stable
                arr[k] = buf[i]
                i += 1
            else:
                arr[k] = buf[j]
                j += 1
            k += 1

        # Leftover left-half items must be copied over.
        while i <= mid:
            arr[k] = buf[i]
            i += 1
            k += 1
        # Leftover right-half items are already in their final positions in arr.


if __name__ == "__main__":
    for case in ([], [1], [3, 1, 2], [9, 5, 2, 4, 3, 0, 1, 2, 6, 10], [2, 2, 1, 1]):
        assert MergeSort().sort(case) == sorted([case]), case
    print("all good")
