import time

start_time = time.time()


# 1
num_of_iterations = 0

while time.time() - start_time < 1:
    num_of_iterations += 1  # num = num + 1

print(num_of_iterations)


# 2

start_time = time.time()

for _ in range(num_of_iterations):
    pass

time_left = time.time() - start_time
print(time_left)

# 3

if 1 < time_left:
    print("While loops is faster")
else:
    print(f"For is faster -> {time_left}")
