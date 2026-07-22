class ContainerWithMostWater:

    def __init__(self, height):
        self.height = height

    def max_water(self):
        left = 0
        right = len(self.height) - 1
        max_area = 0

        while left < right:
            width = right - left
            area = min(self.height[left], self.height[right]) * width
            max_area = max(max_area, area)

            if self.height[left] < self.height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# Driver Code
if __name__ == "__main__":

    height = list(map(int, input("Enter heights: ").split()))

    obj = ContainerWithMostWater(height)

    print("Maximum water that can be stored:", obj.max_water())