filename='source.csv'

with open(filename,'r') as file:
   sum = 0
   count = 0
   header = file.readline()
   header = header.split(',')
   columns_count = len(header)

   sum = []
   for i in range(columns_count):
      sum.append(0)
   counter=0
   for line in file.readlines():
      # print(f"line: ({line})")
      nonewline = line[0:-1]
      columns_lst = nonewline.split(',')
      # print(columns_lst)
      if  nonewline == '':
         continue
      for i in range(columns_count):
         element_str = columns_lst[i]
         element_number = float(element_str)
         sum[i] = sum[i] + element_number
      counter = counter+1

print(sum)
