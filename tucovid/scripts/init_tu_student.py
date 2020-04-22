from django.contrib.auth.models import User
from account.models import Profile
import pandas
import os

# normal format
# | FACULTYID | FACULTYNAME | LEVELID | STUDENTCODE | PREFIXNAME | STUDENTNAME | STUDENTSURNAME |
normal_files = [
    'รายชื่อนักศีกษาป.ตรีมีสภาพภาค262-ท่าพระจันทร์',
    'รายชื่อนักศีกษาป.ตรีมีสภาพภาค262-พัทยา',
    'รายชื่อนักศีกษาป.ตรีมีสภาพภาค262-รังสิต',
    'รายชื่อนักศีกษาป.ตรีมีสภาพภาค262-ลำปาง'
]

dataframe_list = list()

print('READING FILES')
for normal_file in normal_files:
    df = pandas.read_excel('./data/{}.xls'.format(normal_file))
    dataframe_list.append(df)

df = pandas.concat(dataframe_list, axis=0, ignore_index=True)
print('READING FILES: DONE')
del dataframe_list
df = df.drop_duplicates(subset=['STUDENTCODE'])

# creating users

print('CREATING USER')
users = list()

for (index, row) in df.iterrows():
    user = User()
    user.username = row['STUDENTCODE']
    users.append(user)

User.objects.bulk_create(users, ignore_conflicts=True)
del users
print('CREATING USER: DONE')

# creating profiles
print('CREATING PROFILES')
profiles = list()

for (index, row) in df.iterrows():
    user = User.objects.get(username=row['STUDENTCODE'])
    profile = Profile()
    profile.user = user
    profile.full_name = '{}{} {}'.format(row['PREFIXNAME'], row['STUDENTNAME'], row['STUDENTSURNAME'])
    profile.phone_no = '-'
    profile.extra_attribute = {
        'nickname': '-'
    }
    profiles.append(profile)

Profile.objects.bulk_create(profiles, ignore_conflicts=True)
del profiles
print('CREATING PROFILES: DONE')
