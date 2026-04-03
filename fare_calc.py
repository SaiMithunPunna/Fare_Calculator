vehicle_price={'economy':10, 'premium': 18,'suv': 25}

print("\n           CityCab Ride Estimate      \n")
#user inputs
try:
    vehicle_type=(input("Enter the type of vehicle (Economy , Premium , SUV ): "))
    distance=float(input("Enter the distance to travel (in km) : "))
    if distance<=0.0:
        raise ValueError
    hour=int(input("Enter the hour of the day(0-23) : "))
    if not (0 <= hour <= 23):
        raise ValueError
except ValueError:
    print("Please provide valid input")
    exit()

#calculate fare function
def calculate_fare(km , vehicle_type , hour ):

    #error handling
    try:
            
        fare=km*vehicle_price[vehicle_type.lower()]

        #surge pricing 
        surge_applied=False
        if(hour>=17 and hour<=20):
            surge_applied=True
            fare=surge_pricing(fare)
            
        #print receipt
        print_receipt(vehicle_type , km ,hour , fare , surge_applied )
            
    except KeyError:
        print("Service Not Available")
            
        
def surge_pricing(fare):
    return fare*1.5

def print_receipt(vehicle_type , km ,hour , fare , surge_applied):
    print("\n\n             Fare receipt")
    print("-------------------------------------")
    print("     Vehicle type :   ", vehicle_type)
    print("     Distance     :   " , km , "km")
    print("     Hour         :   ", hour)
        
    if(surge_applied):
        print("     Surge        :    Applied(1.5x)")
    else:
        print("     Surge        :    Not applied")
    print("-------------------------------------")
    print(f"     Total Fare   :    ₹{fare:.2f}"  )
    print("-------------------------------------\n\n")

calculate_fare(distance , vehicle_type , hour)