vehicle_price={'Economy':10, 'Premium': 18,'SUV': 25}
hour=int(input("Enter the hour of the day(0-23) : "))
vehicle_type=(input("Enter the type of vehicle : "))
distance=int(input("Enter the distance to travel (in km) : "))

#calculate fair function
def calculate_fair(km , type , hour ):
    fair=km*vehicle_price[type]
    return fair 
