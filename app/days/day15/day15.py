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
    sensor_map = []
    distances = []
    # for i in range(min_x, max_x + 1):
    #     line = []
    #     for j in range(min_y, max_y + 1):
    #         if (i, j) in sensors:
    #             line.append("S")
    #         elif (i, j) in beacons:
    #             line.append("B")
    #         else:
    #             line.append(".")
    #     print("".join(line))
    #     sensor_map.append(line)

    for index, sensor in enumerate(sensors):
        sensor_beacon_distance = calculate_distance(sensor, beacons[index])
        distances.append(sensor_beacon_distance)
        print(sensor, beacons[index], sensor_beacon_distance)
    found = False
    tot = 0
    j = target_line
    for i in range(min_x, max_x + 1):
        print(i)
        if (i, j) not in sensors and (i, j) not in beacons:
            max_distance = -1
            for sensor_index, sensor in enumerate(sensors):
                distance = distances[sensor_index] - calculate_distance(sensor, (i, j))
                if distance > max_distance:
                    max_distance = distance
            if max_distance >= 0:
                if i == min_x or i == max_x:
                    # print(max_distance)
                    tot += 1 + max_distance
                else:
                    tot += 1
                # print("found")

    return tot


def second_part():
    pass