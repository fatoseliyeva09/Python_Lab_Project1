import BMI
import zodiac
import birthday_guess

while True:
    print("press 'a1' for BMI ")
    print("press 'a2' for zodiac ")
    print("press 'a3' for birthday_guess ")
    print("press 'a4' for exit ")
    
    ans=input("Choose one:", )
    
    if ans=="a1":
        BMI.file()
    elif ans=="a2":
        zodiac.file()
    elif ans=="a3":
        birthday_guess.file()
    elif ans=="a4":
        break