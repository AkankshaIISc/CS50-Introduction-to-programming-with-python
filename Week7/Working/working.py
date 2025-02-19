import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        print("ValueError")
        sys.exit(1)


def convert(s):
    if url := re.search(r"^([0-9]{1,2}.*\:?[0-9]{1,2}*)\ ([A-Z]{1,2}+)\ (\-[a-z]{1,2}*)\ ([0-9]{1,2}.*\:?[0-9]{1,2}*)\ ([A-Z]{1,2}+)$", s):
        h1, t1, ad, h2, t2 = url.groups()
        if ad == "to":
            if ":" in h1 and ":" in h2:
                hour1, minute1 = h1.split(":")
                hour2, minute2 = h2.split(":")
                if int(hour1) <= 12 and int(hour2) <= 12 and int(minute1) < 60 and int(minute2) < 60:
                    if t1 == "AM" and t2 == "PM":
                        hour3 = int(hour2) + 12
                        return f"{int(hour1):02d}:{int(minute1):02d} to {int(hour3):02d}:{int(minute2):02d}"
                    elif t1 == "PM" and t2 == "AM":
                        hour_1 = int(hour1) + 12
                        return f"{int(hour_1):02d}:{int(minute1):02d} to {int(hour2):02d}:{int(minute2):02d}"
                    elif t1 == "PM" and t2 == "PM":
                        hour_1 = int(hour1) + 12
                        hour_2 = int(hour2) + 12
                        return f"{(hour_1):02d}:{minute1:02d} to {int(hour_2):02d}:{int(minute2):02d}"
                    elif t1 == "AM" and t2 == "AM":
                        return f"{(hour1):02d}:{minute1:02d} to {int(hour2):02d}:{int(minute2):02d}"
                    else:
                        raise ValueError
                else:
                    raise ValueError

            elif h1 <= 12 and h2 <= 12:
                if t1 == "AM" and t2 == "PM":
                    h3 = int(h2) + 12
                    return f"{int(h1):02d}:00 to {int(h3):02d}:00"
                elif t1 == "PM" and t2 == "AM":
                    h_1 = int(h1) + 12
                    return f"{int(h_1):02d}:00 to {int(h2):02d}:00"
                elif t1 == "PM" and t2 == "PM":
                    h_1 = int(h1) + 12
                    h_2 = int(h2) + 12
                    return f"{(h_1):02d}:00 to {int(h_2):02d}:00"
                elif t1 == "AM" and t2 == "AM":
                    return f"{(h1):02d}:00 to {int(h2):02d}:00"
                else:
                    raise ValueError

            else:
                raise ValueError
        else:
             raise ValueError




if __name__ == "__main__":
    main()
