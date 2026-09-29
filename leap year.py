year = input("Input a year")
year = int(year)
print(year)

years_since = year-2000
print(years_since)

rem = years_since % 4
print(rem)

if rem == 0:
    print("leap year!")
else:
    print("not a leap year")



rem1 = year % 400
rem2 = year % 100
rem3 = year % 4

if rem1 == 0:
    print("leap year!")
elif rem2 == 0:
    print("not a leap year")
elif rem3 == 0:
    print("leap year!")
else:
    print("not a leap year")
