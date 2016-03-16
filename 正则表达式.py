__author__ = 'Junior'
import os
import time
import random
import re


output = 'www.baidu.comwww.baidu.com'
pattern = re.compile(r'baidu')
result = pattern.findall(output)
print result