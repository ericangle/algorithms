def remove_spaces(myStr):
  # want to make recursive, otherwise use return myStr.replace(" ", "")
  if myStr == None:
    return None
  elif not isinstance(myStr, basestring):
    raise TypeError
  else:
    if len(myStr) == 0:
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
  else:
    if len(myStr) <= 1:
      return True
    elif myStr[0] == myStr[-1]:
      return palindrome(myStr[1:len(myStr)-1])
    else:
      return False 
