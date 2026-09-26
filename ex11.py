import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Ví dụ kiểm tra với điểm (0, 0) và (3, 4):
print(distance((0, 0), (3, 4)))