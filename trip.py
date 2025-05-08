def hotel_cost(night):
    return 140 * night


def plane_ride(city):
    if 'Charlotte' == city:
        return 183
    elif 'Tampa' == city:
        return 220
    elif 'New York' == city:
        return 330
    elif 'Los Angeles' == city:
        return 475
    

def rental_car(days):
    if days >= 7:
        return 40 * days - 50
    elif days >= 3:
        return 40 * days - 20
    else:
        return 40 * days
    

def total(city, days, spend):
    return rental_car(days) + hotel_cost(days) + plane_ride(city) + spend


print(f'Cost of rental car: {rental_car(5)}')
print(f'Cost of plane ride: {plane_ride('Los Angeles')}')
print(f'Cost of hotel room: {hotel_cost(7)}')
print(f'Total cost of trip: {total('Los Angeles', 7, 500)}')