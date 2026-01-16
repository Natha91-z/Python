user = ["user1", "user2", "user3"]
courses = ("Python", "Django", "Flask")
scores = (10, 8, 7)

response = list(zip(user, courses, scores))
print(response) 

response = tuple(zip(user, courses, scores))
print(response)
