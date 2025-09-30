bool([])  # False
bool(dict())  # False
bool(tuple())  # False
bool(set())  # False
bool(False)  # False
bool(None)  # False
bool(0)  # False
bool(0.0)  # False
bool('')  # False

age = 20

if age > 18:  # if bool(age > 18)
    print('You are older 18')


users_from_api = []

# if len(users_from_api) > 0
# if bool(users_from_api) is True
if users_from_api:# is not None:  # if bool(users_from_api)
    print('Processing')
