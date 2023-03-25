import re
my_match=input('Вводи циферку:')
u=re.fullmatch(r'[-+]?\d+(\.\d+)?', my_match)
if u:
   print('Да, это циферка', u.group(0))
else:
    print('Мне сказали послать тебя, обманщика, в лес, так как это не циферка')