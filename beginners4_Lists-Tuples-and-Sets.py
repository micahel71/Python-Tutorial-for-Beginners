courses = ['History',  'Math', 'Physics', 'CompSci']

print(courses)
print(len(courses))
print(courses[0])
print(courses[1])
print(courses[3])
print(courses[-1])
print(courses[0:2])
print(courses[:2])
print(courses[2:])

courses.append('Art')
print(courses)

courses.insert(0, 'Sport')
print(courses)

courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print(courses)

courses = ['History',  'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend(courses_2)
print(courses)

courses = ['History',  'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.append(courses_2)
print(courses)

courses = ['History',  'Math', 'Physics', 'CompSci']
popped = courses.pop()
print(popped)
print(courses)

courses = ['History',  'Math', 'Physics', 'CompSci']
courses.reverse()
print(courses)

courses = ['History',  'Math', 'Physics', 'CompSci']
courses.sort()
print(courses)
