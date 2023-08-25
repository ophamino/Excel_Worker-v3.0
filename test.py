def setup(data, where):
    print(*data)
    print(**where)
    



setup(
    data={
        "username": "pillot",
        "first_name": "dsafd",
    },
    where={
        "id": 1234,
    }
)
