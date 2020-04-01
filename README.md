# TU Covid

## For Developer

### Design

We designed this system by AdobeXD ([link](https://xd.adobe.com/view/71bbb0c4-bda8-41e7-506b-df5e41971bab-078a/)).

### Feature

    - [x] TU Login
    - [x] Profile and Profile flow
    - [x] Create Relationship
    - [x] Profile link in suggestion
    - [x] Create Joined Event
    - [x] Support Responsive
    - [x] Data API

### Data API

- List of users

```sh
    GET /api/v1/users/
```

```json
[
  {
    "id": 1,
    "full_name": "อาจารย์วสิศ ลิ้มประเสริฐ",
    "phone_no": "0x-xxx-xxxx",
    "extra_attribute": {
      "nickname": "มด"
    }
  },
  {
    "id": 2,
    "full_name": "อาจารย์ศรัณย์ กุลยานนท์",
    "phone_no": "0x-xxx-xxxx",
    "extra_attribute": {
      "nickname": "โย"
    }
  }
]
```

- List of relationships

```sh
    GET /api/v1/relationships/
```

```json
[
  {
    "persons": [
      {
        "id": 1,
        "full_name": "อาจารย์วสิศ ลิ้มประเสริฐ",
        "phone_no": "0x-xxx-xxxx",
        "extra_attribute": {
          "nickname": "มด"
        }
      },
      {
        "id": 2,
        "full_name": "อาจารย์ศรัณย์ กุลยานนท์",
        "phone_no": "0x-xxx-xxxx",
        "extra_attribute": {
          "nickname": "โย"
        }
      }
    ],
    "level": "เพื่อนร่วมงาน/เพื่อนร่วมชั้น",
    "created_date": "2020-03-30T15:08:48.238602", // UTC + 07:00
    "created_by": {
      "id": 1,
      "full_name": "อาจารย์วสิศ ลิ้มประเสริฐ",
      "phone_no": "0x-xxx-xxxx",
      "extra_attribute": {
        "nickname": "มด"
      }
    }
  }
]
```

- List of events

```sh
    GET /api/v1/events/
```

```json
[
  {
    "title": "ประชุมงาน TU Covid",
    "start": "2020-03-27T14:00:00", // UTC + 07:00
    "finish": "2020-03-27T17:00:00", // UTC + 07:00
    "location": "video conference from ........", // Free text
    "reporter": {
      "id": 1,
      "full_name": "อาจารย์วสิศ ลิ้มประเสริฐ",
      "phone_no": "0x-xxx-xxxx",
      "extra_attribute": {
        "nickname": "มด"
      }
    },
    "participants": [
      {
        "id": 2,
        "full_name": "อาจารย์ศรัณย์ กุลยานนท์",
        "phone_no": "0x-xxx-xxxx",
        "extra_attribute": {
          "nickname": "โย"
        }
      }
    ],
    "created_date": "2020-03-27T20:00:00", // UTC + 07:00
    "created_by": {
      "id": 1,
      "full_name": "อาจารย์วสิศ ลิ้มประเสริฐ",
      "phone_no": "0x-xxx-xxxx",
      "extra_attribute": {
        "nickname": "มด"
      }
    }
  }
]
```
