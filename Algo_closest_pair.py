import random

def generate_map(n):
    return [(random.randint(-111, 111), random.randint(-11,11)) for _ in range(n)]

def distance(x_0, x_1):
    return ((x_0[0] - x_1[0]) ** 2 + (x_0[1] - x_1[1]) ** 2) ** 0.5

def brute_forces(points):
    n = len(points)
    best_pair = points[0], points[1]
    best_distance = distance(points[0], points[1])
    for i in range(n):
        for j in range(n):
            if i != j:
                dist = distance(points[i], points[j])
                if dist < best_distance:
                    best_distance = dist
                    best_pair = (points[i], points[j])
    return best_pair, best_distance

def closest_intersction(sorted_x, min_dist):
    n = len(sorted_x)
    median = sorted_x[n//2 - 1]
    tmp = [sorted_x[i] for i in range(n) if abs(median[0] - sorted_x[i][0]) < min_dist]
    sorted_y = sorted(tmp, key= lambda y: y[1])
    best_distance = None
    best_pair = None
    for i in range(len(sorted_y)):
        for j in range(len(sorted_y)):
            if j != i:
                dist = distance(sorted_y[i], sorted_y[j])
                if dist < min_dist:
                    min_dist = dist
                    best_distance = min_dist
                    best_pair = (sorted_y[i], sorted_y[j])
    return best_pair, best_distance

    
def closest_pair(sorted_x):
    n = len(sorted_x)
    if n == 2:
        return sorted_x, distance(*sorted_x)
    elif n == 3:
        dist_1_2 = distance(sorted_x[0], sorted_x[1])
        dist_1_3 = distance(sorted_x[0], sorted_x[2])
        dist_2_3 = distance(sorted_x[1], sorted_x[2])
        if dist_1_2 <= dist_1_3 and dist_1_2 <= dist_2_3:
            return sorted_x[:2], dist_1_2
        elif dist_1_3 <= dist_1_2 and dist_1_3 <= dist_2_3:
            return (sorted_x[0], sorted_x[2]), dist_1_3
        elif dist_2_3 <= dist_1_2 and dist_2_3 <= dist_1_3:
            return sorted_x[1:], dist_2_3
    else:
        left_sorted_x = sorted_x[:n//2]
        right_sorted_x = sorted_x[n//2:]
        left_pair, dist_left = closest_pair(left_sorted_x)
        right_pair, dist_right = closest_pair(right_sorted_x)
        delta = min(dist_left, dist_right)
        intersection_pair, dist_intersection = closest_intersction(sorted_x, delta)
        dist_intersection = dist_intersection if dist_intersection != None else max(dist_left, dist_right)
        if dist_left <= dist_right and dist_left <= dist_intersection:
            return left_pair, dist_left
        elif dist_right <= dist_left and dist_right <= dist_intersection:
            return right_pair, dist_right
        elif dist_intersection <= dist_left and dist_intersection <= dist_right:
            return intersection_pair, dist_intersection
    

n = int(input("ENTER N: "))
for i in range(5):
    print(f"{i+1}")
    points = generate_map(n)
    print("POINTS: {}".format(points))
    points_sorted_x = sorted(points, key= lambda x: x[0])
    res = closest_pair(points_sorted_x)
    brute_res = brute_forces(points)
    print(f"THE CLOTHEST PAIRS ARE: {res[0]}, THE DISTANCE = {res[1]}")
    print(f"BRUTE FORCE: THE CLOTHEST PAIRS ARE: {brute_res[0]}, THE DISTANCE = {brute_res[1]}", end="\n\n")
