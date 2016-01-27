```
格式化输出json数据
比如：
cat json.txt | python filein.py
```
import fileinput
import json

f_input=fileinput.input()
rest = f_input.readline()
rest=json.loads(rest)
print(json.dumps(rest, sort_keys=True, indent=4))
