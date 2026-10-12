def file():
    weight=int(input("Enter your weight",))
    height=float(input("Enter your height",))
    BMI=weight/(height**2)
    if BMI < 18.5 :
        print("You are underweight")
    elif 18.5 <= BMI <= 24.9 :
        print(" You are normal weight")
    elif 25.0 <= BMI <= 29.9 :
        print("You are overweight")
    else:
        print("You are obese")