##https://py3.codeskulptor.org/#isp_dates_template.py
import datetime

def is_leap_year(year):
    """Returns True if year is a leap year."""
    if (year % 400 == 0): return True
    if (year % 100 == 0): return False
    if (year % 4 == 0): return True
    return False

def days_in_month(year, month):
    """Returns the number of days in a given month and year."""
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month in {4, 6, 9, 11}:
        return 30
    if month == 2:
        return 29 if is_leap_year(year) else 28
    return 0

def is_valid_date(year, month, day):
    """Checks if a date is valid."""
    if year < 1 or month < 1 or month > 12 or day < 1:
        return False
    return day <= days_in_month(year, month)

def date_to_absolute_days(year, month, day):
    """Helper to convert a date to the total number of days since Year 1."""
    # Days in years before current year
    y = year - 1
    total_days = y * 365 + (y // 4) - (y // 100) + (y // 400)

    # Days in months of current year
    for m in range(1, month):
        total_days += days_in_month(year, m)

    return total_days + day

def days_between(year1, month1, day1, year2, month2, day2):
    """Returns number of days between two dates."""
    if not (is_valid_date(year1, month1, day1) and is_valid_date(year2, month2, day2)):
        return 0

    days1 = date_to_absolute_days(year1, month1, day1)
    days2 = date_to_absolute_days(year2, month2, day2)

    if days2 < days1:
        return 0
    return days2 - days1

def age_in_days(year, month, day):
    """Calculates age in days based on today's date (2025-12-22)."""
    if not is_valid_date(year, month, day):
        return 0

    # Using your specified server date: 2025, 12, 22
    return days_between(year, month, day, 2025, 12, 22)

# --- Verification ---
print(f"1. age_in_days(2017, 1, 1): {age_in_days(2017, 1, 1)}")
print(f"2. days_between(2014, 5, 5, 2014, 5, 6): {days_between(2014, 5, 5, 2014, 5, 6)}")
print(f"3. days_in_month(1, 1): {days_in_month(1, 1)}")
print(f"4. is_valid_date(2014, 5, 5): {is_valid_date(2014, 5, 5)}")
