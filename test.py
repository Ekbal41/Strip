

import re
line = 'math 2-1/4567*54'

newline = line.strip("'")

keyword = newline.split(' ')[0]


if keyword == "math":
    line_list = newline.split(' ')
    del line_list[0]
    exp = str(line_list).strip("]").strip("[").strip("'")
    res = sum(map(int, re.findall(r'[+-]?\d+', exp)))
    print(res)
   
    

