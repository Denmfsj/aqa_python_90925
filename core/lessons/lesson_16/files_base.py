import os

import definitions


# r - read
# w - write
# a - append

# rb - read bytes
# wb - write bytes
# ab - append bytes

# r+ - read+ write
# w+ - read+ write
# a+ - read+ append
# rb+
# wb+
# ab+


# r - read
# w - write
# a - append

with open(definitions.FILE_TO_READ_WRITE_LESSON_16, 'w') as f:
    f.write('first row\nsecond row\n\nlast row')

with open(definitions.FILE_TO_READ_WRITE_LESSON_16, 'a') as f:
    f.write('\nvery last row')

with open(definitions.FILE_TO_READ_WRITE_LESSON_16, 'r') as f:
    data = f.read()

for row in data.split('\n'):
    if row.startswith('last'):
        print('this is last row', row)

# os.remove(definitions.FILE_TO_READ_WRITE_LESSON_16)
print(data)