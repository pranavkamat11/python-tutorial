# Sets
# order printed changes with each execution
# Sets gets rid of duplicates like Maths
cs_courses = {"History","Maths","Physics","Maths"}
print(cs_courses)


# union intersection difference
cs_courses = {"History","Maths","Physics","Chem"}
art_courses = {"History","Maths","comp","arts"}
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))


#creating empty set
empty_set = set()
print(empty_set)