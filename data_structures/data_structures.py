
#lists -- ordered sequence 
#dictionaries - not immutable (CAN CHANGE), does not maintain order, use OrderedDict if want order
#TUPLES - immutable (CANT CHANGE)
#SETS - unordered collection of unique elements

a = 23.45
print(type(a))

a = "abcdefg"
print(a[1:3])
print(a[::2]) #jump over every 2 characters
print(a[::-1]) #reverse a string 
print("tinker"[1:4]) #ink

#String formatting
test = "Hi {} {}".format("Nik", "Tom")
print(test)

#f string interpolation (Python 3.6)
name="Nik"
print(f"Hello {name}")

#float formatting  value:width
result = 0.123455
print("The result was {r:1.5f}".format(r=result))


#lists -- ordered sequence 
ls = [1,1,[1,2]]
print(ls[2][0])

#dictionaries - not immutable, does not maintain order, use OrderedDict if want order

#TUPLES - immutable (cant change)
t=(1,1,2,3)
print(t.count(1))
print(type(t))
#t[0] = "7" #fails

#SETS - unordered collection of unique elements
myset = set()
myset.add(1)
myset.add(1)
myset.add(4)
print(myset)

#Booleans


#Basic I/O
#with open("test.txt") as file:
 #   print(file.readline())


# list comprehension
test = [t.upper() for t in "testing"]
print(test)





