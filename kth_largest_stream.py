import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        for num in nums:
            self.add(num)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]
# Driver code'''
if __name__ == "__main__":

    k = int(input("Enter k: "))

    nums = list(map(int, input("Enter initial numbers: ").split()))

    kthLargest = KthLargest(k, nums)

    while True:
        value = input("Enter a number to add (or type 'exit' to quit): ")

        if value.lower() == "exit":
            break

        value = int(value)
        print("Current", k, "th largest element:", kthLargest.add(value))