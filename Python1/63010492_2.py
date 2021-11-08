print(" *** Wind classification ***")
s = float(input("Enter wind speed (km/h) : "))
if(s<=51.99):
    print("Wind classification is Breeze.")
elif(s<=55.99):
    print("Wind classification is Depression.")
elif(s<=101.99):
    print("Wind classification is Tropical Storm.")
elif(s<=208.99):
    print("Wind classification is Typhoon.")
elif(s>=209):
    print("Wind classification is Super Typhoon.")

