import re

m = re.search(r'([a-zA-Z0-9])\1+', raw_input().strip())
print m.group(1) if m else -1