import re

result = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', raw_input().strip(), re.I)
print '\n'.join(result) or -1