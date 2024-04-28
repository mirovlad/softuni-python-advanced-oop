import datetime
from collections import deque

until_products_finished = False  # Already satisfies the requirements
# until_products_finished = True  # Additional explorative requirements

line = input()

robots = list()
for robot_line in line.split(";"):
    robot_parts = robot_line.split("-")
    robots.append({
        'name': robot_parts[0],
        'process_time_sec': int(robot_parts[1]),
        'product': None,
        'start_time': None,
    })
# print("OK robots", robots)

start_time = datetime.datetime.strptime(input(), '%H:%M:%S')
# print("OK start_time", start_time, "type(start_time)", type(start_time))

products_queue = deque()
while True:
    line = input()
    if line == 'End':
        break
    products_queue.append(line)
initial_product_cnt = len(products_queue)

finished_products_cnt = 0
finished_products = deque()
time = start_time  # It's actually copy
robots_busy = False
while products_queue or (until_products_finished and finished_products_cnt < initial_product_cnt):
    time += datetime.timedelta(seconds=1)

    product = None
    if products_queue:
        product = products_queue.popleft()

    # Checking if any busy robots are ready
    for robot in robots:
        if robot["start_time"]:  # Robot is busy with a product
            time_passed = (time - robot["start_time"]).total_seconds()
            if time_passed >= robot["process_time_sec"]:
                if until_products_finished:
                    # Not originally required
                    print(f"{robot['name']} - {robot['product']} finished {time.strftime('%H:%M:%S')}")
                finished_products.append(robot["product"])
                finished_products_cnt += 1
                robot["product"] = None
                robot["start_time"] = None

    if product:
        for robot in robots:
            if robot["start_time"] is None:
                robot["product"] = product
                robot["start_time"] = time
                product = None
                print(f"{robot['name']} - {robot['product']} [{robot['start_time'].strftime('%H:%M:%S')}]")
                break

    if product:
        products_queue.append(product)

