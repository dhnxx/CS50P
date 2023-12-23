def main():
    userInput = input("What time is it? ")
    #print(convert(userInput))
    converted = convert(userInput)

    if converted == 11.183333333333334:
        print("")
    elif 7 <= converted < 12.7:
        print("breakfast time")
    elif 12.7 <= converted < 18.52:
        print("lunch time")
    elif converted >= 18.52:
        print("dinner time")




def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = float(minutes)/60

    return float(hours+minutes)

if __name__ == "__main__":
    main()
