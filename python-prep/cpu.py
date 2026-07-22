import heapq

job_queue = []

current_job = None
remaining_time = 0

job_order = 0 

num_slices = int(input("Enter number of time slices: "))

for time_slice in range(1, num_slices + 1):
    print(f"\nTime Slice {time_slice}")

    command = input("Enter command: ")
    if command.lower().startswith("add"):
        name = input("Job Name: ")
        length = int(input("Job Length (1-100): "))