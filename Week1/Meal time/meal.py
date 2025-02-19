def convert(time):
    times = time.split(":")
    num = int(times[0]) + int(times[1])/60

    return num


def main():
    user = input("What time is it? ")
    meal_time = convert(user)
    if 7.0 <= meal_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= meal_time <= 13.0:
        print("lunch time")
    elif 18.0 <= meal_time <= 19.0:
        print("dinner time")
    else:
        return ""
    
if  __name__ == "__main__":
    main()


