nums = [1,2,4,6]

for num in nums:
	if num == 4 :
		print("now will break loop")
		break
	else :
		print(num)

# continue unlike break will continue to next iteration. statements after continue keyword doesn't get executed though
nums = [1,2,3,4]

for num in nums :
	if num == 3 :
		continue
	else :
		print("Hello")
		print(num)

# 2 for loops example
nums = [1,2,3,4]
for num in nums:
	for letter in 'abc':
		print(num,letter)

print("new iteration")
# iterating 1-10
for i in range(1,11) :
	for j in range (1,3):
		print(i,j)

print("while loop starts")
# while loop
x = 0
while x < 10 :
	if x == 5 :
		x +=1
		continue
	print(x)
	x += 1

print("hello")

courses = ['history','maths','computer']
for index , course in enumerate(courses):
	print(index , course)