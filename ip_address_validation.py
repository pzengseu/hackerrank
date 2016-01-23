import re

ipv4 = r'^([0-1]?[0-9]{1,2}|2[0-5]{2})(\.[0-1]?[0-9]{1,2}|\.2[0-5]{2}){3}$'
ipv6 = r'^[a-f0-9]{1,4}(:[a-f0-9]{1,4}){7}$'

for _ in xrange(input()):
    s = raw_input().strip()
    if re.match(ipv4, s):
        print "IPv4"
    elif re.match(ipv6, s):
        print "IPv6"
    else:
        print "Neither"