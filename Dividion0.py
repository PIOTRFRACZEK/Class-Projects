'''I define a function of two integer variables div0'''
def div0(a,b):
#I set a condition if the given denominator is zero
    if b == 0:
    #if it meets the conditions, display sentence: Error-...
        print('Error – You cannot divide by 0. Please choose an appropriate denominator.')
    #conditions if the denominator is not zero
    else:
        #do the division operation
        result = a/ b
        #display sentence: {0} divided by...
        print("The number {0} divided by {1} is equal to {2}".format(a,b,result))
        #display operation
        print(a,'/',b,"=", result)