__author__ = 'CQC'
import re

pattern = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world'
# print re.sub(pattern, r'\2 \1', s)
print re.sub(pattern, r'\2 \2', s)

# pattern = re.compile(r'\d+')
# print re.split(pattern, 'one1two222three3four4')
# print re.findall(pattern, 'one1two222three3four4')

# pattern = re.compile(r'world')
# # match = re.search(pattern, 'hello world!')
# match = re.match(pattern, 'hello world!')
# if match:
#     print match.group()
# print 'end'
# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'o w!')
#
# print "m.string: ", m.string
# print "m.re: " , m.re
# print "m.pos: " , m.pos
# print "m.endpos: " , m.endpos
# print "m.lastindex: " , m.lastindex
# print "m.lastgroup: " , m.lastgroup
# print "m.group(1, 2): " , m.group(1, 2)
# print "m.groups(): " , m.groups()
# print "m.groupdict(): " , m.groupdict()
# print "m.start(2): " , m.start(2)
# print "m.end(2): " , m.end(2)
# print "m.span(2): " , m.span(2)
# print "m.expand(r'\g \g\g'): " , m.expand(r'\2 \1\3')

# pattern = re.compile(r'hello')
# result1 = re.match(pattern, 'hello')
# result2 = re.match(pattern, 'helloo cqc')
# result3 = re.match(pattern, 'helo cqc')
# result4 = re.match(pattern, 'hello cqc')
#
# if result1:
#     print result1.group()
# else:
#     print 'error'
#
# if result2:
#     print result2.group()
# else:
#     print 'error'
#
# if result3:
#     print result3.group()
# else:
#     print 'error'
#
# if result4:
#     print result4.group()
# else:
#     print 'error'