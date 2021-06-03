'''CODING EXERCISE 1 - BRING IT IN NEXT WEDNESDAY:
Write a simple kg to lb (pounds) conversion program. The user must be able to input the
number of kg they want. Then your program should convert that into lb. Use comments to
show your steps. Data given (conversion rate): 1 kg = 2.205 lb.'''

# defining number of kg
numkg=input('Enter a number of kilograms: ')

# assignment kg to 'x'
x=float(numkg)

# kg to lb converter
y=x*2.205

# presentation of conversion results
print('{0} kg is equal to {1} lb'.format(x, y))