import calendar

mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
def get_seconds_in_year(day, dd, mon, year, t, tz):
    hours, minutes, seconds = map(int, t.split(':'))
    hours *= 60*60
    minutes *= 60
    year = sum([(365 + calendar.isleap(y))*24*60*60 for y in xrange(int(year))])
    mon = (sum(mdays[:list(calendar.month_abbr).index(mon)]) + (calendar.isleap(int(year)) and not mon in ['Jan', 'Feb']))*24*60*60
    dd = (int(dd) - 1)*24*60*60
    tz = get_tz_seconds(tz)
    return year + mon + dd + hours + minutes + seconds + tz


def get_tz_seconds(tz):
    s, h = tz[0], int(tz[1:])
    secs = h/100*60 + h%100
    return secs*(1 if s=='-' else -1)*60

for _ in xrange(input()):
    print abs(get_seconds_in_year(*raw_input().split()) - get_seconds_in_year(*raw_input().split()))