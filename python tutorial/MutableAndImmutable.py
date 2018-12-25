# There is a problem 
# it would print ['Arts', 'maths', 'geography'] for both lists
list_1 = ["science","maths","geography"]
list_2 = list_1

list_1[0] = "Arts"
print(list_1)
print(list_2)

# Thats why tupples come handy
# But tupple is immutable cannot be changed like on line 15
tupple_1 = ("science","maths","geography")
tupple_2 = tupple_1

# we can't do tupple_1[0] = "Arts"
print(tupple_1)
print(tupple_2)

#Creating empty tupples
empty_tuple = ()
empty_tuple = tuple()
print(empty_tuple)
