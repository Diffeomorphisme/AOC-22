import re


def read_file():
    sensors = tuple()
    beacons = tuple()
    min_x = 0
    max_x = 0
    min_y = 0
    max_y = 0
    with open("app/days/day15/input.txt", "r") as file:
        for line in file:
            coordinates = re.findall(r"(\-*[0-9]+)", line.strip())
            sensor_x = int(coordinates[0])
            sensor_y = int(coordinates[1])
            beacon_x = int(coordinates[2])
            beacon_y = int(coordinates[3])
            if max(sensor_y, beacon_y) > max_y:
               max_y = max(sensor_y, beacon_y)
            if min(sensor_y, beacon_y) < min_y:
               min_y = min(sensor_y, beacon_y)
            if max(sensor_x, beacon_x) > max_x:
               max_x = max(sensor_x, beacon_x)
            if min(sensor_x, beacon_x) < min_x:
               min_x = min(sensor_x, beacon_x)
            sensors = sensors + ((sensor_x, sensor_y),)
            beacons = beacons + ((beacon_x, beacon_y),)
    return sensors, beacons, [min_x, max_x, min_y, max_y]


def calculate_distance(sensor: tuple[int, int], beacon: tuple[int, int]):
    return abs(beacon[0] - sensor[0]) + abs(beacon[1] - sensor[1])


def first_part():
    sensors: tuple[tuple[int, int]]
    beacons: tuple[tuple[int, int]]
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    target_line = 2000000
    # target_line = 10
    (sensors, beacons, [min_x, max_x, min_y, max_y]) = read_file()
    distances = []
    unique_beacons = tuple(beacon for beacon in set(beacons))
    for index, sensor in enumerate(sensors):
        sensor_beacon_distance = calculate_distance(sensor, beacons[index])
        distances.append(sensor_beacon_distance)
    tot = 0
    # j = target_line
    # sensors_beacons = sum([1 for sensor in sensors if sensor[1] == j]) + sum(
    #     [1 for beacon in unique_beacons if beacon[1] == j])
    # for i in range(min_x, max_x + 1):
    #     print(i)
    #     max_distance = -1
    #     for sensor_index, sensor in enumerate(sensors):
    #         distance = distances[sensor_index] - calculate_distance(sensor, (i, j))
    #         if distance > max_distance:
    #             max_distance = distance
    #     if max_distance >= 0:
    #         if i == min_x or i == max_x:
    #             tot += 1 + max_distance
    #         else:
    #             tot += 1
    # tot -= sensors_beacons
    return tot


def second_part():
    sensors: tuple[tuple[int, int]]
    beacons: tuple[tuple[int, int]]
    min_x: int
    max_x: int
    min_y: int
    max_y: int
    allowed_min_x = 0
    # allowed_max_x = 4000000
    allowed_max_x = 20
    allowed_min_y = 0
    # allowed_max_y = 4000000
    allowed_max_y = 20
    (sensors, beacons, [min_x, max_x, min_y, max_y]) = read_file()
    distances = []
    for index, sensor in enumerate(sensors):
        sensor_beacon_distance = calculate_distance(sensor, beacons[index])
        distances.append(sensor_beacon_distance)
    i = 0
    j = 0
    while True:
        min_distance = allowed_max_x + allowed_max_y
        for index, sensor in enumerate(sensors):
            distance = calculate_distance(sensor, (i, j)) - distances[index]
            if distance < min_distance:
                min_distance = distance
        if min_distance < 0:
            i += abs(distance)
        elif min_distance == 0:
            i += 1
        else:
            return i * 4000000 + j
        if i > allowed_max_x:
            j += i // allowed_max_x
            i %= allowed_max_x
            print(i, j)




