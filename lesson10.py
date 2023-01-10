# # # # file = open('input.txt', 'r', encoding='utf-8')
# # # # text = [line.strip() for line in file if line.strip()]
# # # # file.seek(0)
# # # # print(file.readline())
# # # # file.close()
# # # with open('input.txt', 'r', encoding='utf-8') as file:
# # #     lines: list[str] = file.readlines()
# # #
# # # lines[3] = '3. Encoding\n'
# # # with open('input.txt', 'w', encoding='utf-8') as file:
# # #     file.writelines(lines)
# #
# # from json import load, loads, dump, dumps
# #
# # # with open('user.json', 'r', encoding='utf-8') as file:
# # #     data = load(file)
# # # print(data)
# # # text = '{"name": "Alex", "age": 32}'
# # # data2 = loads(text)
# # # print(data2)
# #
# # data = {
# #     'name': 'Доминик',
# #     'city': 'LA',
# #     'is_human': True,
# #     'car': None
# # }
# # # text = dumps(data, indent=2, ensure_ascii=False)
# # # print(text)
# # with open('dominik.json', 'w', encoding='utf-8') as file:
# #     dump(data, file, indent=2, ensure_ascii=False)
#
# from csv import reader, DictReader, writer, DictWriter
#
# with open('users.csv', 'r', encoding='utf-8') as file:
#     data = list(DictReader(file))
# #     fieldnames = file.readline().strip().split(',')
# #     data = [
# #         dict(zip(fieldnames, line.strip().split(',')))
# #         for line in file
# #     ]
# #     # data = list(reader(file))
# #     # data = [line.strip().split(',') for line in file]
# #
# # print(data)
# # data = [
# #     ['name', 'age'],
# #     ['alex', '34'],
# #     ['pavel', '43']
# # ]
# data = [
#     {'name': 'alex', 'age': '34'},
#     {'name': 'pavel', 'age': '43'}
# ]
# with open('new_user.csv', 'w', encoding='utf-8') as file:
#     keys = list(data[0].keys())
#     wrt = DictWriter(file, keys)
#     wrt.writeheader()
#     wrt.writerows(data)
#     # wrt = writer(file)
#     # wrt.writerows(data)
#     # text = ''
#     # for line in data:
#     #     line = ','.join(line)
#     #     line += '\n'
#     #     text += line
#     # file.write(text)
from datetime import datetime

from pydantic import BaseModel, Field, validator, EmailStr, root_validator

categories = ["Category2", "Category3"]


user = {
    "name": "Alex",
    "age": 34,
    "languages": ["ru"],
    "city": "Minsk",
    "category": {"name": "Category1", "description": "description"},
}


class CategorySchema(BaseModel):
    name: str
    description: str
    date_created: datetime = None

    @validator("name")
    def validate_name(cls, value):
        if value not in categories:
            return value
        raise ValueError("name is not unique")

    @validator("date_created", pre=True)
    def validate_date_created(cls, value):
        return datetime.fromtimestamp(value)


class UserSchema(BaseModel):
    name: str = Field(min_length=4)
    age: int = Field(ge=18, lt=100)
    languages: list[str] = Field(min_items=1)
    city: str = Field(default=None, min_length=5)
    category: CategorySchema
    email: EmailStr

    @root_validator(pre=True)
    def validate_email(cls, values):
        if values.get("email"):
            if values.get("name") in values.get("email"):
                return values
        else:
            values["email"] = values.get("name") + "@gmail.com"
            return values
        raise ValueError("почта не содержит имя")


# try:
data = UserSchema(**user)
# except Exception as e:
#     print(e)
print(data.category.name)
print(data.city)
print(data.languages[0])
