from django.contrib.auth.models import User
from account.models import Profile
import pandas
import os

# additional format (must skip first row)
# Cannot use head row (has merge cell)
additional_files = [
    'รายชื่อนศ.มธส่งประกัน (เพิ่มเติม) (1)'
]

dataframe_list = list()

print('READING FILES')
for additional_file in additional_files:
    df = pandas.read_excel('./data/{}.xls'.format(additional_file), header=None, skiprows=3)
    dataframe_list.append(df)

df = pandas.concat(dataframe_list, axis=0, ignore_index=True)
print('READING FILES: DONE')
del dataframe_list
df = df.drop_duplicates(subset=[ df.columns[3] ])

# creating users

print('CREATING USER')
users = list()

for (index, row) in df.iterrows():
    user = User()
    user.username = str(row[df.columns[3]])
    users.append(user)

User.objects.bulk_create(users, ignore_conflicts=True)
del users
print('CREATING USER: DONE')

# creating profiles
print('CREATING PROFILES')
profiles = list()

for (index, row) in df.iterrows():
    user = User.objects.get(username=row[df.columns[3]])
    profile = Profile()
    profile.user = user
    profile.full_name = '{}{} {}'.format(row[df.columns[4]], row[df.columns[5]], row[df.columns[6]])
    profile.phone_no = '-'
    profile.extra_attribute = {
        'nickname': '-'
    }
    profiles.append(profile)

Profile.objects.bulk_create(profiles, ignore_conflicts=True)
del profiles
print('CREATING PROFILES: DONE')
