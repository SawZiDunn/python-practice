students = [
    {"name": "Naruto", "clan": "Uzumaki"},
    {"name": "Nagato", "clan": "Uzumaki"},
    {"name": "Sasuke", "clan": "Uchiha"},
    {"name": "Karin", "clan": "Uzumaki"}
]


# def is_uzumaki(student_dict):
#     return s["clan"] == "Uzumaki"


# - iterate through students list,
# - takes each dict as student_dict,
# - check condition, 
# if true -> appends to uzumaki_list
uzumaki_list = filter(lambda student_dict: student_dict["clan"] == "Uzumaki", students)

for each in sorted(uzumaki_list, key=lambda student_dic: student_dic["name"]):
    print(each["name"])
