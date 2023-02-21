apple = [100, 200, 150, 100, 120, 80, 90, 160, 110, 170]

total_weight = 0

for i in range(len(apple)):
  total_weight = total_weight + apple[i]

avg_apple = total_weight / len(apple)
print(avg_apple)