import re

from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

pattern = r"(\+7|8)\s?\(?(\d{0,3})\)?(\s+|-?)(\d{0,3})-?(\d{0,2})-?(\d{0,2})(\s*(\(?(доб.\s\d+)\)?)?)?"
substitution = r"+7(\2)\4-\5-\6 \9"

for tel in contacts_list:
  if tel[-2] != 'phone':
    phone_number = tel[-2]
    phone_number_res = re.sub(pattern, substitution, phone_number)
    tel[-2] = phone_number_res

pattern_name = r"(\w+)\s(\w+)\s?(\w+)?"

for patronymic in contacts_list:
  if patronymic[2] != 'surname':
    if patronymic[2] == '' and patronymic[1] == '':
      patronymicname = patronymic[0]
      patronymicname_res = re.sub(pattern_name, r"\3", patronymicname)
      patronymic[2] = patronymicname_res
    elif patronymic[2] == '' and patronymic[1] != '':
      patronymicname = patronymic[1]
      patronymicname_res = re.sub(pattern_name, r"\2", patronymicname)
      patronymic[2] = patronymicname_res

for name in contacts_list:
  if name[1] != 'firstname':
    if name[1] == '':
      firstname = name[0]
      firstname_res = re.sub(pattern_name, r"\2", firstname)
      name[1] = firstname_res
    else:
      firstname = name[1]
      firstname_res = re.sub(pattern_name, r"\1", firstname)
      name[1] = firstname_res

for surname in contacts_list:
  if surname[0] != 'lastname':
    lastname = surname[0]
    lastname_res = re.sub(pattern_name, r"\1", lastname)
    surname[0] = lastname_res

# pprint(contacts_list)

sort_contacts_dict = {}

for contact in contacts_list:



  if contact[0] + ' ' + contact[1] in sort_contacts_dict:
    if contact[6] != '':
      sort_contacts_dict[contact[0] + ' ' + contact[1]][4] = contact[6]
    if contact[5] != '':
      sort_contacts_dict[contact[0] + ' ' + contact[1]][3] = contact[5]
    if contact[4] != '':
      sort_contacts_dict[contact[0] + ' ' + contact[1]][2] = contact[4]
    if contact[3] != '':
      sort_contacts_dict[contact[0] + ' ' + contact[1]][1] = contact[3]
    if contact[2] != '':
      sort_contacts_dict[contact[0] + ' ' + contact[1]][0] = contact[2]
  else:
    sort_contacts_dict[contact[0] + ' ' + contact[1]] = [contact[2], contact[3], contact[4], contact[5], contact[6]]



contacts_list = []

for key, value in sort_contacts_dict.items():
  contacts_list.append(key.split()+value)

pprint(contacts_list)


# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')

  datawriter.writerows(contacts_list)