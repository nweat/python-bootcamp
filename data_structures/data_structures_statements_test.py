# 1 
st = "print only the words that start with s in this sentence"
for i in st.split(" "):
    if(i[0].lower() == "s"):
        print(i)

#2
print(list(range(0, 11, 2)))
for i in range(0, 11, 2):
    print(i)


#3 
arr = [i for i in range(1, 51) if i % 3 == 0]
print(arr)

#4
st2 = "Print every word in this sentence that has an even number of letters"
for s in st2.split(" "):
    if len(s) % 2 == 0:
        print(s)

# OR
st2_solution = [s for s in st2.split(" ") if len(s) % 2 == 0]
print(st2_solution)


#5 
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")

# 6
st3 = "Create a list of the first letters of every word in this string"
str3_result =  [i[0] for i in st3.split(" ")]
print(str3_result)