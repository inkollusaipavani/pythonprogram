# function which return reverse of a string 
def reverse(z): 
    return z[::-1] 
  
def isPalindrome(z): 
    # Calling reverse function 
    rev = reverse(z) 
  
    # Checking if both string are equal or not 
    if (z == rev): 
        return True
    return False
  
  
# Driver code 
z = raw_input()
ans = isPalindrome(z) 
  
if ans == 1: 
    print("yes") 
else: 
    print("no")
