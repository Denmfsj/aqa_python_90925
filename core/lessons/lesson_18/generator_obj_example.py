

def first_5_sq():
    # return [1, 2, 4, 16, 32]
    print('inside first_5_sq')
    yield 1 #  оператор преривання
    print('inside first_5_sq')
    yield 2
    print('inside first_5_sq')
    yield 4
    print('inside first_5_sq')
    yield 16
    print('inside first_5_sq')
    yield 32


def file_generator_read(path):
    with open(path) as f:
        rows = f.readlines()  # список строк
        for row in rows:
            yield row


for line in file_generator_read('text.txt'):
    print('reading by 1 lne')
    print(line)
    if line == 'asdg\n':
        break


