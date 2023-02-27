import Truck
import Delivery


def main():
    gas_price = 4.366
    drivers_salary_hr = 29
    GAS_TRUCK_MAX_CAP = 32
    EV_TRUCK_MAX_CAP = 16
    small_pack_size = 2
    med_pack_size = 4
    large_pack_size = 8
    WAREHOUSE_LONGITUDE = 0
    WAREHOUSE_LATITUDE = 0

    print('Welcome to FabuLorry Delivery System!\n' +
          'This system computes the most efficient and cost effective way to deliver our cabinetry!')
    print()
    print('Here are today\'s costs:\n' +
          'Current NJ gas price: $', format(gas_price, '.2f'), 'per gallon.\n' +
          'Drivers Hourly Pay: $', format(drivers_salary_hr, '.2f'), 'per hour')
    print()
    print("Package Sizings Listed Below:")
    print("Small package - 2 units")
    print("Medium package - 4 units")
    print("Large package - 8 units")
    print("Max capacity- 32 units")
    print()
    tot_orders = int(input('How many orders were placed today? '))
    print()
    orders = delivery(tot_orders, GAS_TRUCK_MAX_CAP, small_pack_size, med_pack_size, large_pack_size)

    ev_orders = create_ev_order_list(orders, WAREHOUSE_LONGITUDE, WAREHOUSE_LATITUDE)
    gas_orders = create_gas_order_list(orders, ev_orders)
    gas_trucks = assign_trucks(gas_orders, GAS_TRUCK_MAX_CAP)
    ev_trucks = assign_trucks(ev_orders, EV_TRUCK_MAX_CAP)

    output(gas_orders, gas_trucks, ev_orders, ev_trucks)

    calculation(gas_trucks, ev_trucks, drivers_salary_hr)


# Creates and returns a list of all the orders
def delivery(tot_orders, max_capacity, small_pack_size, med_pack_size, large_pack_size):
    orders = []

    for x in range(tot_orders):
        print('Please enter the required information below of order ', x + 1)
        address = input('What is the address you are delivering to? ')
        small_pack = 0
        med_pack = 0
        large_pack = 0

        small_pack = int(input('How many small packages are you delivering? '))
        validation_small(small_pack)
        med_pack = int(input('How many medium packages are you delivering? '))
        validation_med(med_pack)
        large_pack = int(input('How many large packages are you delivering? '))
        validation_large(large_pack)

        while small_pack * small_pack_size + med_pack * med_pack_size + large_pack * large_pack_size > max_capacity:
            print("The amount of packages you entered is larger than the truck's capacity of 32 units.\n" +
                  "Please input the amount of packages again: ")
            small_pack = int(input('How many small packages are you delivering? '))
            validation_small(small_pack)
            med_pack = int(input('How many medium packages are you delivering? '))
            validation_med(med_pack)
            large_pack = int(input('How many large packages are you delivering? '))
            validation_large(large_pack)

        order = Delivery.Delivery(address)
        order.set_num_small_packages(small_pack)
        order.set_num_medium_packages(med_pack)
        order.set_num_big_packages(large_pack)
        orders.append(order)
    return orders


def create_ev_order_list(all_deliveries, WAREHOUSE_LONGITUDE, WAREHOUSE_LATITUDE):
    ev_deliveries = []
    for x in all_deliveries:
        distance = x.find_distance(WAREHOUSE_LONGITUDE, WAREHOUSE_LATITUDE)
        if distance <= .3 and x.get_total_units() <= 16:
            ev_deliveries.append(x)
    return ev_deliveries


def create_gas_order_list(all_deliveries, ev_deliveries):
    gas_deliveries = []
    for x in all_deliveries:
        if x not in ev_deliveries:
            gas_deliveries.append(x)
    return gas_deliveries


# assigns deliveries to specific trucks
def assign_trucks(deliveries, max_capacity):
    deliveries_left = []  # This list will hold the deliveries which have not been assigned a truck yet
    for x in deliveries:
        deliveries_left.append(x)

    fleet = [Truck.Truck('1')]  # The list of trucks; trucks will be added as needed
    current_truck = fleet[0]
    current_delivery = deliveries_left[0]
    current_truck.add_delivery(current_delivery)
    del deliveries_left[current_delivery.index()]

    for i in range(len(deliveries)):
        while current_truck.get_current_capacity() < max_capacity:
            closest = deliveries_left[0]
            for j in range(len(deliveries_left)):
                dist = closest.find_distance(current_delivery.get_longitude(), current_delivery.get_latitude())
                if dist < closest.find_distance(current_delivery.get_longitude(), current_delivery.get_latitude()) and \
                        deliveries_left[j].get_total_units < (32 - current_truck.get_current_capacity()):
                    deliveries_left[j] = closest
                    closest_index = j  # saves the index of the number of the closest items

            current_truck.add_delivery(closest)
            current_truck.add_capacity(closest.get_total_units)
            del deliveries_left[closest_index]  # removes the closest index
            current_delivery = closest

        fleet.append(Truck.Truck(str(len(fleet) + 1)))
        current_truck = fleet[len(fleet) - 1]
    return fleet


def calculation(gas_trucks, ev_trucks, drivers_salary_hr):
    total_driving_time = 0
    total_gas_distance = 0
    total_ev_distance = 0
    for x in gas_trucks:
        print('How long did the route of gasoline-powered truck', x.get_number(), 'take?', end=' ')
        driving_time = float(input(''))
        while driving_time <= 0:
            print("Invalid timing!")
            print("Please enter length of route again (in hours) ")
            driving_time = float(input('How long did the route take? '))
        total_driving_time += driving_time

        distance = float(input('How many miles was the route? '))
        while distance <= 0:
            print("Invalid distance.")
            print("Please enter distance again (in miles) ")
            distance = float(input('How many miles was the route? '))
        total_gas_distance += distance

    for x in ev_trucks:
        print('How long did the route of electric truck', x.get_number(), 'take?', end='')
        driving_time = float(input(''))
        while driving_time <= 0:
            print("Invalid timing!")
            print("Please enter length of route again (in hours) ")
            driving_time = float(input('How long did the route take? '))
        total_driving_time += driving_time

        distance = float(input('How many miles was the route? '))
        while distance <= 0:
            print("Invalid distance.")
            print("Please enter distance again (in miles) ")
            distance = float(input('How many miles was the route? '))
        total_ev_distance += distance

    tot_cost_all_trucks = 0
    total_pay_per_route = drivers_salary_hr * driving_time

    total_gallons = total_gas_distance / 6.5
    total_gas_expense = 4.366 * total_gallons
    total_ev_expense = .50 * total_ev_distance

    cost_delivery = total_gas_expense + total_ev_expense + total_pay_per_route
    tot_cost_all_trucks += cost_delivery
    print('The total expense of deliveries is $', format(tot_cost_all_trucks, '.2f'))


def validation_small(small_pack):
    while small_pack < 0 or small_pack > 16:
        print("ERROR! The amount of packages you've entered is invalid.")
        print("Please enter amount of small packages again: ")
        small_pack = int(input('How many small packages are you delivering? '))


def validation_med(med_pack):
    while med_pack < 0 or med_pack > 8:
        print("ERROR! The amount of packages you've entered is invalid.")
        print("Please enter amount of medium packages again: ")
        med_pack = int(input('How many medium packages are you delivering? '))


def validation_large(large_pack):
    while large_pack < 0 or large_pack > 4:
        print("ERROR! The amount of packages you've entered is invalid.")
        print("Please enter amount of large packages again: ")
        large_pack = int(input('How many large packages are you delivering? '))


def output(gas_deliveries, gas_trucks, ev_deliveries, ev_trucks):
    print('You will be sending out', len(gas_trucks), 'gasoline-powered trucks.')
    print('Following are the trucks and the addresses to which they are being sent to:')
    for x in gas_trucks:
        print('Truck', x.get_number(), ':', end='\t')
        for y in x.get_deliveries():
            print(y.get_address())

    print('You will be sending out', len(ev_trucks), 'electric trucks.')
    print('Following are the trucks and the addresses to which they are being sent to:')
    for x in ev_trucks:
        print('Truck', x.get_number(), ':', end='\t')
        for y in x.get_deliveries():
            print(y.get_address())


main()
