class LargestRectangleHistogram:

    def __init__(self, heights):
        self.heights = heights

    def largest_rectangle_area(self):
        stack = []
        max_area = 0
        n = len(self.heights)

        for i in range(n + 1):
            current_height = 0 if i == n else self.heights[i]

            while stack and current_height < self.heights[stack[-1]]:
                height = self.heights[stack.pop()]

                if stack:
                    width = i - stack[-1] - 1
                else:
                    width = i

                area = height * width
                max_area = max(max_area, area)

            stack.append(i)

        return max_area


# Driver Code
if __name__ == "__main__":

    heights = list(map(int, input("Enter histogram heights: ").split()))

    obj = LargestRectangleHistogram(heights)

    print("Largest Rectangle Area:", obj.largest_rectangle_area())