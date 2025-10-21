

if  32 > 15:
    print('32 is more than 15')

if 32 < 15:
    print('32 is less than 15')

print('Done')

# True, False

# True and True   => True
# True and False  => False
# True or True   => True
# True or False  => True
# not True  => False
# not False  => True

user_email_1 = None
user_email_2 = ''
user_email_3 = 'asd@asd.asd'

if user_email_1 == None or user_email_1 == '':  # if None == None or '' == None =>  if True or False
    print('v1 invalid user')

if not(user_email_2 == None and user_email_2 == ''):  # if None == None and '' == None =>  if False and True
    print('v2 invalid user')

if user_email_3 != None and user_email_3 != '': # if  'asd@asd.asd' != None AND  'asd@asd.asd' != '' => True and True
    print('Valid user')

