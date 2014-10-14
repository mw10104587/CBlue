import time

def divideTwoOrTimesThreeAddOne(number, counter):
  
  if number == 1:
    #print counter
    #print "end!"
    return counter
  if number % 2 == 0:
    number = number/2
    counter = counter + 1
  else:
    number = number*3 + 1
    counter = counter + 1

  divideTwoOrTimesThreeAddOne(number, counter)

sizeOfArray = 100
check = [-1]*sizeOfArray

def divideTwoOrTimesThreeAddOneWithMemory(number, counter):
  
  if number == 1:
    #print "final"
    #setArray( number, counter)
    return counter
  
  # if arrived at a saved number, we use the result
  if number < sizeOfArray:
    if check[number-1] != -1 and check[number-1] is not None:
      #print "check of number" + str(check[number-1])
      return counter + check[number-1] - 1 

  if number % 2 == 0:
    number = number/2
    counter = counter + 1
  else:
    number = number * 3 + 1
    counter = counter + 1

  return divideTwoOrTimesThreeAddOneWithMemory(number, counter)

t0 = time.time()
for x in xrange(1,100):
  divideTwoOrTimesThreeAddOne(x,1)
print time.time() - t0, "seconds wall time"

t0 = time.time()
for x in xrange(1,100):
  counter = divideTwoOrTimesThreeAddOneWithMemory(x, 1)
  check[x-1] = counter
  #print str(x) + " :" + str(counter)
print time.time() - t0, "seconds wall time with memory"