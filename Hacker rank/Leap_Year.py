def is_leap(year):
    # Write your logic here
    leap = False
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            leap = False
            return leap
        leap = True
        return leap
    else:
        return leap
year = int(input())
print(is_leap(year))