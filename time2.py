from __future__ import print_function
import calendar

month_days, month_abbr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31], ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

def to_seconds(h):
    s, h = h[0], h[1:]
    h = h.lstrip('0')
    h = 0 if h == '' else int(h)
    res = h % 100 + (h//100)*60
    return res*(-1 if s == '+' else 1)*60

def get_seconds_in_year(day, dd, mon, year, t, tz):
    hours, minutes, seconds = map(int, t.split(':'))
    dd, year = map(int, [dd.lstrip('0'), year])
    minutes *= 60
    hours *= 60*60
    tz = to_seconds(tz)
    dd = (dd-1)*24*60*60
    mon = (sum(month_days[:month_abbr.index(mon)]) + (calendar.isleap(year) and not mon in ['Jan', 'Feb']))*24*60*60
    year = sum([(365+calendar.isleap(i))*24*60*60 for i in range(year)])
    return seconds + minutes + hours + tz + dd + mon + year

for _ in range(int(input())):
    print(abs(get_seconds_in_year(*raw_input().split())-get_seconds_in_year(*raw_input().split())))
