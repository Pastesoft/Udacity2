# program that will convert the single character of a string in another one
# adding 13 to the number value
#

charstr= "abcdefghijklmnopqrstuvwxyz"
chars2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm','n','o','p','q','r','s','t','u','v','w','x','y','z']


def charConverter():
  for a in chars2:
    p = chars.find(a)
    c = (p+13)%26
    c2 = (c+13)%26
    print p,"\t",c,"\t",c2
  print chars.find(" ")
  print chars.find("\n")

def stringCrypto(s):
  uppChars = charstr.upper()
  ret = []
  for a in s:
    p = charstr.find(a)
    if p > -1:
      ret.append(charstr[(p+13)%26])
    else:
      p = uppChars.find(a)
      if (p > -1):
        ret.append(uppChars[(p+13)%26])
      else:
        ret.append(a)
  return "".join(ret)

#charConverter()
print stringCrypto("hello")
print stringCrypto("Hello")
print stringCrypto(stringCrypto("Hello"))

