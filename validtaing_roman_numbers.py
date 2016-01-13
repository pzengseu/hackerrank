import re

pat = re.compile(r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IV|IX|V?I{0,3})$')
print True if re.search(pat, raw_input()) else False