import re

# common variables

rawstr = r"""(?P<values>[+-]?[0-9]*[.]?[0-9]*[eE]?[+-]?\d*(?:[^,]+))\w*"""
embedded_rawstr = r"""(?P<values>[+-]?[0-9]*[.]?[0-9]*[eE]?[+-]?\d*(?:[^,]+))\w*"""
matchstr = """-12.354e+10,-34.5e-6,3,-34.,.34,-34,5.67,-1,+10"""

# method 1: using a compile object
compile_obj = re.compile(rawstr)
match_obj = compile_obj.search(matchstr)

# method 2: using search function (w/ external flags)
match_obj = re.search(rawstr, matchstr)

match_all = re.findall(rawstr, matchstr)
# method 3: using search function (w/ embedded flags)
match_obj = re.search(embedded_rawstr, matchstr)

# Retrieve group(s) from match_obj
all_groups = match_obj.groups()

# Retrieve group(s) by index
group_1 = match_obj.group(1)

# Retrieve group(s) by name
values = match_obj.group('values')

