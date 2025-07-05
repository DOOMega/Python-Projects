import re
phoneNumRegex = re.compile(r'[5,0]')
mo = phoneNumRegex.findall("Cell: 537-458-6670 Work: 212-555-0000")
print(mo)