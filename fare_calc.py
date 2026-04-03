vehicle_price={'Economy':10, 'Premium': 18,'SUV': 25}

vehicle_type=(input("Enter the type of vehicle (Economy , Premium , SUV ): "))
distance=int(input("Enter the distance to travel (in km) : "))
hour=int(input("Enter the hour of the day(0-23) : "))

#calculate fair function
def calculate_fair(km , type , hour ):
    try:
        fair=km*vehicle_price[type]
        #surge pricing 
        if(hour>=17 and hour<=20):
            fair=surge_pricing(fair)
        
    except:
        print("Service Not Available")
        
    
def surge_pricing(fair):
    return fair*1.5


#Error handling