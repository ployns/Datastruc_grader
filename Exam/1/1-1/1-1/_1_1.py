print(" *** BMI ***")
w,h = (input("Enter your weight(kg) and height(m) : ").split())
w,h = float(w),float(h)
bmi = w/(h*h)
if(bmi<18.5):
    print("Your status is : Below normal weight.")
elif(bmi<25):
    print("Your status is : Normal weight.")
elif(bmi<30):
    print("Your status is : Overweight.")
elif(bmi<35):
    print("Your status is : Case I Obesity.")
elif(bmi<40):
    print("Your status is : Case II Obesity.")
elif(bmi>=40):
    print("Your status is : Case III Obesity.")


