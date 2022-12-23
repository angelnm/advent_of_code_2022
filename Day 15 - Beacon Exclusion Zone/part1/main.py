def read_file(namefile):
    with open(namefile, 'r') as f:
        lines = f.read().splitlines()
    return lines

def read_sensor_output(reading):
    sensor, beacon = reading.split(':')
    
    sensor_x, sensor_y = sensor[10:].split(',')
    sensor_x = int(sensor_x[2:])
    sensor_y = int(sensor_y[3:])
    
    beacon_x, beacon_y = beacon[22:].split(',')
    beacon_x = int(beacon_x[2:])
    beacon_y = int(beacon_y[3:])
    
    return [sensor_x, sensor_y],[beacon_x, beacon_y]

def get_manhattan_distance(coord1, coord2):
    distance = abs(coord1[0] - coord2[0]) + abs(coord1[1] - coord2[1])
    return distance

def check_add_x(sensor_x, nearest_beacon):
    return  ROW_Y!=nearest_beacon[1] or sensor_x!=nearest_beacon[0]

if __name__ == "__main__":
    day_input = read_file("input.txt")
    
    # Read the information about all the sensors
    readings_info = []
    for reading in day_input:
        sensor_coor, beacon_coor = read_sensor_output(reading)
        readings_info.append([sensor_coor, beacon_coor])
        
    ROW_Y=2000000
    not_beacon = {}
    # Check the sensors
    for  [sensor, beacon] in readings_info:
        distance = get_manhattan_distance(sensor, beacon)
        min_y = sensor[1] - distance
        max_y = sensor[1] + distance
        # Check if the sensor has information about ROW_Y
        if min_y<=ROW_Y<=max_y: 
            horizontal_dist = (distance - abs(sensor[1]-ROW_Y))
           
            # Add the empty x_pos to the dict
            check_x = sensor[0]
            if check_add_x(check_x, beacon):
                not_beacon[check_x] = True
            for i in range(1,horizontal_dist+1):
                for sign in [-1, +1]:
                    check_x = sensor[0]+(i*sign)
                    if check_add_x(check_x, beacon):
                        not_beacon[check_x] = True
    print(len(not_beacon))