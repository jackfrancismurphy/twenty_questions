import json


People = json.load(open("people_data.json", "r"))

def get_people(People, user_input):
	for person_data in People:
		if user_input == "name":
			return person_data

print(People)

print(get_people(People, "Harry Potter"))





