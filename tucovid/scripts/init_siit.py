from django.contrib.auth.models import User
from account.models import Profile
import pandas
import os

# siit format (must skip first row)
# | No. | Student ID | Title | Name | Title | Name (TH) |
siit_files = [
    'รายชื่อนักศึกษาSIIT_bachelor_ผู้มีสิทธิเลือกตั้งTUSU2020 (1,861 คน)'
]

dataframe_list = list()

print('READING FILES')
for siit_file in siit_files:
    df = pandas.read_excel('./data/{}.xlsx'.format(siit_file), skiprows=1)
    dataframe_list.append(df)

df = pandas.concat(dataframe_list, axis=0, ignore_index=True)
print('READING FILES: DONE')
del dataframe_list
df = df.drop_duplicates(subset=['Student ID'])

# creating users

print('CREATING USER')
users = list()

for (index, row) in df.iterrows():
    user = User()
    user.username = row['Student ID']
    users.append(user)

User.objects.bulk_create(users, ignore_conflicts=True)
del users
print('CREATING USER: DONE')

# creating profiles
print('CREATING PROFILES')
profiles = list()

for (index, row) in df.iterrows():
    user = User.objects.get(username=row['Student ID'])
    profile = Profile()
    profile.user = user
    profile.full_name = '{}{}'.format(row['Title.1'], row['Name (TH)'])
    profile.phone_no = '-'
    profile.extra_attribute = {
        'nickname': '-'
    }
    profiles.append(profile)

Profile.objects.bulk_create(profiles, ignore_conflicts=True)
del profiles
print('CREATING PROFILES: DONE')
