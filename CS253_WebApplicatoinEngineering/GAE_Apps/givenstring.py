# User Instructions
# # 
# # Write a function 'sub1' that, given a 
# # string, embeds that string in 
# # the string: 
# # "I think X is a perfectly normal thing to do in public."
# # where X is replaced by the given 
# # string.
# #
#
given_string = "I think %s is a perfectly normal thing to do in public."
def sub1(s):
  print given_string %s

given_string2 = "I think %s and %s are perfectly normal things to do in public."
def sub2(s1, s2):
      return given_string2 % (s1,s2)
#
#
sub1("running") 
# => "I think running is a perfectly normal thing to do in public."    
sub1("sleeping") 
# => "I think sleeping is a perfectly normal thing to do in public."
#
sub2("running", "sleeping")
