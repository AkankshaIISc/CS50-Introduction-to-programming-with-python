def main():
    info = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}
    while True:
        try:
            x = input("Date: ")
            month, day, year = x.split("/")
            try:
                m = int(month)
                d = int(day)
                y = int(year)
                if 1 <= m <= 12 and 1 <= d <= 31:
                    print(f"{y}-{m:02d}-{d:02d}")
                    break
                else:
                    pass
            except KeyError:
                continue
        except ValueError:
            try:
                if ',' in x:
                    m_info, d_info, y_info = x.replace(",", "").split()
                    m_1 = info[m_info]
                    d_1 = int(d_info)
                    y_1 = int(y_info)
                    if 1 <= m_1 <= 12 and 1 <= d_1 <= 31:
                        print(f"{y_1}-{m_1:02d}-{d_1:02d}")
                        break
                    else:
                        pass

            except (EOFError, KeyError, ValueError):
                pass

main()


