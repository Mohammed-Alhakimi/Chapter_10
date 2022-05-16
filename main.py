"""
Chapter  10 Think Python

Lists in Python are very essential.  You can think of them as arrays in Java.

"""

# One way of creating lists in Python is by using square brackets []
# You can create a list of numbers
list_numbers = [1, 2, 76, 4, 86, 23]

# Or you can create a list of Strings or objects or etc.

list_names = ["ali", "Roba", "bader", "mohammed"]

list_objects = [12.4, ["ali", 12], "word", False]

# A list within another list is called nested list
# A-List with no items is called an empty list. You can create that by 2 square brackets
empty_list = []

print(list_numbers, list_objects, list_names, empty_list)

# __________________________________________________________
# lists are mutable. You can access the elements of a list by using the square brackets just like a string

print(list_names[0])

# unlike strings, Python lists are mutable. You can use the square operator to change an element of a list

list_names[0] = "Mohammed"
print(list_names[0])
"""
List indices work like string indices: 

1. Any Integer expression can be used as an index 
2. If you try to access an element that doesn't exist you get an index error 
3. If an index has a negative value, it counts backwards from the end of the list
"""
# The in operator also works with lists

print("Mohammed" in list_names)
print("Ali" in list_names)
# __________________________________________________________
# The most common way to traverse through a list in Python is using for loop
for name in list_names:
    print(name)
"""
The above way is very effective if you want to read items from a list.
However, if you want to write items to a list, you can use indices.
"""
# This function is used to multiply all the numbers in a list by 2
for i in range(len(list_numbers)):
    list_numbers[i] = list_numbers[i] * 2

print(list_numbers)

# A for loop for an empty list never runs the body
for x in []:
    print("This will never happen")
"""
Please note that even if a list will contain a nested list that nested list will only be one element of that list
"""
# __________________________________________________________
list1 = [1, 2, 3]
list2 = [4, 5, 6]
# The + operator concatenates two lists
print(list1 + list2)
# The * operator repeats the elements of a list by the number it is multiplied with

print(list1 * 3)
# __________________________________________________________
# The Slice operator can also be used with lists
list1 = ["a", "b", "c", "d", "e"]
print(list1[4:])
print(list1[:2])
print(list1[:])
# The Slice operator helps us in creating copies of a list and then
# performing operations on them. This is a very helpful feature.
list1_copy = list1[1:4]
print(list1_copy)

# A slice operator on the left of an assignment can update multiple elements

list1[:3] = ["z", "y", "x"]
print(list1)
# __________________________________________________________
# Some useful list methods
# Append
list_letters = ["a", "b", "c", "d", "e"]
print(list_letters)
list_letters.append("f")
print(list_letters)
# Extend
list_x = ["1", "2", "3"]
list_y = ["4", "5", "6"]
list_x.extend(list_y)
# Please note that the extend method will leave the list that is passed as an argument unmodified
# __________________________________________________________
list_w = ["bbb", "zzz", "hhh", "lll", "ppp"]
list_w.sort()
print(list_w)
"""
Please note that their turn value of the sort method is void. You can't use t = t.sort()
"""

# __________________________________________________________
# Let's say that you want to add up all the elements in a list.
# You might use this approach :
list_a = [1, 6, 8, 9, 10]


def add_all(l):
    total = 0
    for number in l:
        total += number
    return total


print(add_all(list_a))
print(sum(list_a))

"""
 However, you don't have to do this. There is a built-in function in Python called sum that will take care of this for you.
 If you want to traverse through a list while building another list. You can do that like this example:
"""
list_b = ["ali", "bali", "mali"]


def capitalize_all(l):
    capitalized_list = []
    for s in list_b:
        capitalized_list.append(s.capitalize())
    return capitalized_list


new_list = capitalize_all(list_b)
print(new_list)

# An operation that selects some elements of a list and filters the others is called a filter.

list_c = ["A", "b", "C", "d", "E", "f", "G"]


def only_upper(l):
    res = []
    for s in list_c:
        if s.isupper():
            res.append(s)
    return res


print(only_upper(list_c))

# __________________________________________________________
# Deleting items from a list

# Pop method deletes the last element od a list

print(list_c.pop())  # Returns the popped item
print(list_c)

# del operator is used when you don't need the removed value

del list_c[0]

print(list_c)

# If you know the element you want to remove but not the index you can use the remove function

list_c.remove("C")  # Returns None
print(list_c)

# You can use the del operator with a slice of a list
del list_c[1:3]
print(list_c)
# __________________________________________________________

# You can convert a string into a list

s = "spam"
list_word = list(s)
print(list_word)

# If you want to split a sentence into words u can use the split function

sentence = "I love Pizza!"
list_d = sentence.split()

print(list_d)
# The split function can use a delimiter
sentence = "I-love-Pizza!"
list_f = sentence.split("-")
print(list_f)
# __________________________________________________________

# Join is the inverse of spilt when you use it you invoke the method on a delimiter and join the parts together

list_e = ["I", "Am", "a", "Rabbit"]
delimiter = "#"
word = delimiter.join(list_e)
print(word)

# __________________________________________________________

# Objects and values
"""
a = "banana"
b = "banana"
Above both variables refer to a string in memory. However, we don't know if they refer to the same object or two objects with the same value. 
We can check that by the is operator 
"""
a = "banana"
b = "banana"
print(a is b)

# Here, Python created a string, and both A and B refer to it. However, when you create two lists you create two objects

list_h = [1, 2, 3]
list_g = [1, 2, 3]
print(list_g is list_h)

# In this case, we would say that the two lists are equivalent because they have the same elements.
# However, they are not identical
# __________________________________________________________
# Aliasing
# If a refers to an object, and then you assign a to b then a and b refer to the same object
list_i = [1, 2, 3]
var = list_i
print(var is list_i)
# any changes to an aliase affect the other
list_i[0] = 54
print(var[0])
# This method is error-prone its recommended that you avoid using aliasing
"""
For immutable objects like strings, aliasing is not much of a problem. Since you cannot change immutable objects,
 it almost never makes a difference whether a and b refer to the same string or not
"""

# __________________________________________________________
"""
When you pass a list to a function, the function gets a reference to the list. If the function
modifies the list, the caller sees the change.
"""
list_j = [1, 2, 3, 4]


def delete_head(t):
    del t[0]


delete_head(list_j)
print(list_j)
"""
The parameter t and the variable letters are aliases for the same object.
That's why the function changes the contents of a list.
Because aliases refer to the same object.
It is important to distinguish between operations that modify lists and operations that create new lists. For example, 
the append method modifies a list, but the + operator creates a
new list.
Here’s an example using append:
>>> t1 = [1, 2]
>>> t2 = t1.append(3)
>>> t1
[1, 2, 3]
>>> t2
None

The result of the operator is a new list, and the original list is unchanged.
This difference is important when you write functions that are supposed to modify lists.
For example, this function does not delete the head of a list:
def bad_delete_head(t):
t = t[1:] # WRONG!
The slice operator creates a new list and the assignment makes t refer to it, but that doesn’t
affect the caller.
>>> t4 = [1, 2, 3]
>>> bad_delete_head(t4)
>>> t4
[1, 2, 3]
At the beginning of bad_delete_head, t and t4 refer to the same list. At the end, t refers
to a new list, but t4 still refers to the original, unmodified list.
An alternative is to write a function that creates and returns a new list. For example, tail
returns all but the first element of a list:
def tail(t):
return t[1:]
This function leaves the original list unmodified. Here’s how it is used:
>>> letters = ['a', 'b', 'c']
>>> rest = tail(letters)
>>> rest
['b', 'c']

"""


