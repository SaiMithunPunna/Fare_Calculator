vehicle_price={'economy':10, 'premium': 18,'suv': 25}

print("\n           CityCab Ride Estimate      \n")
#user inputs
try:
    vehicle_type=(input("Enter the type of vehicle (Economy , Premium , SUV ): "))
    distance=float(input("Enter the distance to travel (in km) : "))
    hour=int(input("Enter the hour of the day(0-23) : "))


    #calculate fare function
    def calculate_fare(km , type , hour ):

        #error handling
        try:
            
            fare=km*vehicle_price[type.lower()]

            #surge pricing 
            surge_applied=False
            if(hour>=17 and hour<=20):
                surge_applied=True
                fare=surge_pricing(fare)
            
            #print receipt
            print_receipt(type , km ,hour , fare , surge_applied )
            
        except:
            print("Service Not Available")
            
        
    def surge_pricing(fare):
        return fare*1.5

    def print_receipt(type , km ,hour , fare , surge_applied):
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
except:
    print("Please provide valid inputs")