import re
import email.utils

for _ in xrange(input()):
    t = email.utils.parseaddr(raw_input())
    if re.match(r'^([a-zA-Z][\w\.-]*)@([a-zA-Z]+)\.([a-zA-Z]{1,3})$', t[1]):
        print email.utils.formataddr(t)