# -*- coding: utf-8 -*-
import codecs
import re
import string
file = codecs.open('file.txt', 'r', 'utf-8')
text = file.read().lower()
file.close()


word_list = re.findall(r'\b[a-zöäü]{4,20}\b', text)

word_freq = {}

for word in word_list:

    word_freq[word] = word_freq.get(word, 0) + 1
	
result = sorted(word_freq.items(), key = lambda x:x[1], reverse = True)

f = open('output.txt', 'w')
for word,freq in result:
    f.write("%-20s %d\n" % (word, freq))
f.close()

