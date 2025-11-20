wordcounts = {}
with open('tempest.txt') as f:
   for line in f:
      if line == '\n':
         continue
      line = line[:-1]
      words_list = line.split(' ')
      print(f"({words_list})")
      for word in words_list:
         if word == '':
            continue
         if word in wordcounts:
            wordcounts[word]=wordcounts[word] + 1
         else:
            wordcounts[word] = 1

max = 0

for word in wordcounts:
   if wordcounts[word] > max:
      max = wordcounts[word]
      maxword = word

print(wordcounts[maxword],maxword)

