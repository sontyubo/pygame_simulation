import random
import math

def get_sample_data():
    sample_data = [
    [10, 10],
    [0, 10]]

    init_arm = 5
    init_num = 45

    x = 0
    y = 0
    r1 = math.radians(init_num)
    dist1 = 10 * math.sqrt(2)

    x += dist1 * math.cos(r1)
    y += dist1 * math.sin(r1)

    num = random.randint(15, 180)
    r2 = math.radians(num)
    x += init_arm * math.cos(r2)
    y += init_arm * math.sin(r2)


    sample_data[0].append(x)
    sample_data[1].append(y)

    return x, y