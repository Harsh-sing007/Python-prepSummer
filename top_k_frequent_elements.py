from collections import Counter
import heapq


class TopKFrequentElements:

    def __init__(self, nums):
        self.nums = nums

    def find_top_k(self, k):
        frequency = Counter(self.nums)

        heap = []

        for num, count in frequency.items():
            heapq.heappush(heap, (-count, num))

        result = []

        for _ in range(k):
            result.append(heapq.heappop(heap)[1])

        return result


# Driver Code
if __name__ == "__main__":

    nums = list(map(int, input("Enter array elements: ").split()))
    k = int(input("Enter k: "))

    obj = TopKFrequentElements(nums)

    print("Top", k, "frequent elements:", obj.find_top_k(k))