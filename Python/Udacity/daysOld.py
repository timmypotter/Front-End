#using python3

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    monthDay = [0,31,28,31,30,31,30,31,31,30,31,30,31] #0 for easily count
    monthDayLeap = [0,31,29,31,30,31,30,31,31,30,31,30,31] #0 for easily count
    i = month1
    j = 1 # for the month in year2
    k = year1 + 1 # for count years between y1 and y2
    between = 0
    if year1 == year2:
        if month2 == month1:
            return day2 - day1
        if year1%4 == 0:  #consider leap month
            while i < month2:
                between = between + monthDayLeap[i]
                i = i + 1
            return between - day1 + day2
        while i < month2:
            between = between + monthDay[i]
            i = i + 1
        return between - day1 + day2
    else: #year1 != year2
        if year2 - year1 <= 1:
            if year1%4 == 0 and year1%100 != 0:
                while i <= 12:
                    between = between + monthDayLeap[i]
                    i = i + 1
            while i <= 12:
                between = between + monthDay[i]
                i = i + 1
            if year2%4 == 0 and year2%100 != 0:
                while j < month2:
                    between = between + monthDayLeap[j]
                    j = j + 1
                return between - day1 + day2
            while j < month2:
                between = between + monthDay[j]
                j = j + 1
            return between - day1 + day2
        else: #year2-year1 > 1
            if year1%4 == 0 and year1%100 != 0:
                while i <= 12:
                    between = between + monthDayLeap[i]
                    i = i + 1
            while i <= 12:
                between = between + monthDay[i]
                i = i + 1
            if year2%4 == 0 and year2%100 != 0:
                while j < month2:
                    between = between + monthDayLeap[j]
                    j = j + 1
                return between - day1 + day2
            while j < month2:
                between = between + monthDay[j]
                j = j + 1
            while k < year2:
                if k%4 == 0 and k%100 != 0:
                    between = between + 366
                    k = k + 1
                between = between + 365
                k = k + 1

            return between - day1 + day2


if __name__ == '__name__':
	y1 = int(input("Input year1:\n"))
	m1 = int(input("Input month1:\n"))
	d1 = int(input("Input day1:\n"))
	y2 = int(input("Input year2:\n"))
	m2 = int(input("Input month2:\n"))
	d2 = int(input("Input day2:\n"))

	print(daysBetweenDates(y1, m1, d1, y2, m2, d2))


