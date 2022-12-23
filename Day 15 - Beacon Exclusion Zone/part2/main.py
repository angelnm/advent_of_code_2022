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

def add_range(current_ranges, new_range):   
    start = len(current_ranges)
    end = 0
    for i in range(len(current_ranges)):
        c_rng = current_ranges[i]
        
        if new_range[0]<=c_rng[1]+1 and start==len(current_ranges):
            start = i
        if c_rng[0] <= new_range[1]:
            end = i
        else:
            break
        
    new_min = [x[0] for x in current_ranges[start:end+1]+[new_range]]
    new_max = [x[1] for x in current_ranges[start:end+1]+[new_range]]
    
    n_current_ranges = []
    n_current_ranges = current_ranges[:start]
    n_current_ranges.append([min(new_min), max(new_max)])
    n_current_ranges += current_ranges[end+1:]
    return n_current_ranges

def get_only_beacon_position(sensor_information):
    for y in range(0, MAX_Y):
        not_beacon_ranges = []
        for [sensor, beacon, distance] in sensor_information:
            horizontal_dist = (distance - abs(sensor[1]-y))
            if horizontal_dist >= 0:
                min_x = max(0, sensor[0]-horizontal_dist)
                max_x = min(MAX_X, sensor[0]+horizontal_dist)
                not_beacon_ranges = add_range(not_beacon_ranges, [min_x, max_x])
        if(y%100000==0):
            print("{0:.2f}%".format((y/MAX_X)*100))
        if(len(not_beacon_ranges)!=1):
            return not_beacon_ranges[0][1]+1, y
    return 0, 0

ROW_Y=20
MIN_X = MIN_Y=0
MAX_X = MAX_Y=4000000
if __name__ == "__main__":
    day_input = read_file("input.txt")
    
    # Read the information about all the sensors
    readings_info = []
    for reading in day_input:
        sensor_coor, beacon_coor = read_sensor_output(reading)
        distance = get_manhattan_distance(sensor_coor, beacon_coor)
        
        readings_info.append([sensor_coor, beacon_coor, distance])
    
    x, y = get_only_beacon_position(readings_info)
    print("What is its tuning frequency?")
    print(x*MAX_X + y)
            
           
