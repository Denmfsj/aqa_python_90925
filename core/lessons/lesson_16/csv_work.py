import csv

data = [
    ['Name', 'Age', 'City'],
    ['John', 30, 'New York'],
    ['Alice', 25, 'Los Angeles'],
    ['Bob', 35, 'Chicago']
]


with open('output.csv') as f:
    reader = csv.reader(f)

    for row in reader:
        header_value = row
        break

    for row_number, row in enumerate(reader, start=0):
        row_dict = dict(zip(header_value, row))
        if len(row_dict.get('Name')) > 0:
            print(f'Row {row_number} has no Name')

print(reader)
print('-'*80)
header = reader[0]
body = reader[1:]
print('-'*80)

print(header)
print(body)

rows_updated = [dict(zip(header, row)) for row in body]  # свторити список словників замість списка списків

print('new body')
print(rows_updated)

print('data')


for row in rows_updated:
    print(f'User {row.get("Name")} is from {row.get("City")}')

# for row in body:
#     print(f'User {row[0]} is from {row[1]}')


# # Відкриття CSV-файлу для запису
# with open('output.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerows(data)