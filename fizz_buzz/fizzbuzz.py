import sys

# while len(sys.argv) == 1:
#   print "Please enter number"
#   else:
#     user_input = sys.argv[1]
#     n = 1

n = 1
user_input = int(raw_input("Lets play Fizz Buzz. What number should we count up to? "))

#if divisible by 3 say fizz, by 5 say buzz, by both say fizz buzz, neither say the number
print "Fizz buzz counting up to %d" % user_input
while n <= user_input:
  if n % 3 == 0:
    if n % 5 == 0:
      print "fizzbuzz"
    else:
      print "fizz"
  elif n % 5 == 0:
    print "buzz"
  else:
    print n
  n +=1
