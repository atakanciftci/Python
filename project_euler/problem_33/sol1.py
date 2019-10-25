# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

def solution():
  result = 1
  for b in range(11,100):
      if(b%10!=0):
          for k in range(1,10):
              c=b%10*10+k
              if(c%11!=0):
                  if(b/c==int(b/10)/k):
                      result *= c/b
  return(int(result))

if __name__ == "__main__":
    print(solution())
