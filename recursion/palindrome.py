# not recursive, but ok for now
# return myStr.replace(" ", "") 
def remove_spaces(myStr):
  if myStr == None:
    return None
  elif not isinstance(myStr, basestring):
    raise TypeError
  elif len(myStr) == 0:
    return myStr
  elif myStr[0] == " ":
    return remove_spaces(myStr[1:])
  else:
    return myStr[0] + remove_spaces(myStr[1:])
 
def palindrome(myStr):
  if myStr == None:
    return False
  elif not isinstance(myStr, basestring):
    raise TypeError
  elif len(myStr) <= 1:
    return True
  elif myStr[0] == myStr[-1]:
    return palindrome(myStr[1:len(myStr)-1])
  else:
    return False  
