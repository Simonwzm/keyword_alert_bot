# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex = r"([a-zA-Z0-9-_]+)"

test_str = ("再放几个码吧，祝大家心想事成\n\n"
	"NrD-XThTyOpJQmz\n"
	"AVIeodk9WSglMTz\n"
	"EheYKKhQjPQcI5r\n"
	"fNV8UpLklFFVRO9\n"
	"jsKdjCciv_-gd8U\n\n"
	"本次释放的邀请码不支持增加牛币")

matches = re.finditer(regex, test_str)

for matchNum, match in enumerate(matches, start=1):
    
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    
    for groupNum in range(0, len(match.groups())):
        groupNum = groupNum + 1
        
        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
