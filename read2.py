import re
import string
file = open('file.txt', 'r')
text = file.read().lower()
file.close()


word_list = re.findall(r'\b[a-z]{4,20}\b', text)

word_freq = {}

for word in word_list:

    word_freq[word] = word_freq.get(word, 0) + 1
	
lis = sorted(word_freq.items(), key = lambda x:x[1], reverse = True)
for word,freq in lis:
    print ("%-20s %d" % (word, freq))