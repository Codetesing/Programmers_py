import calendar

def solution(a, b):
    days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    return days[calendar.weekday(2016, a, b)]

a = 5
b = 24

print(solution(a, b))