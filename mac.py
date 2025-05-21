import re, uuid

# joins elements of getnode() after each 2 digits.
# using regex expression
print("The MAC address in formatted and less complex way is : ", end="")
print('-'.join(re.findall('..', '%012x' % uuid.getnode())))
s='-'.join(re.findall('..', '%012x' % uuid.getnode()))
s1=s.upper()
if str(s1)==str(s1):
    print("test")
else:
    print("normal")
print(s1)