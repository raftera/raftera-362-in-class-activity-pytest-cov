
def leapyear(num):

    if int(num) % 4 == 0:
         if int(num) % 100 == 0:
             if int(num) % 400 != 0:
                     return 0
    else:  
      return 0
    return 1
   

