import xml.etree.ElementTree as ET

# Завантаження XML-файлу
tree = ET.parse('data.xml')
root = tree.getroot()

# # Пошук елементу bbo у timingExbytes для кожної групи
# for group in root.findall('group'):
#     timing_exbytes = group.find('timingExbytes')
#     if timing_exbytes is not None:
#         bbo = timing_exbytes.find('bbo')
#         if bbo is not None:
#             print(f"Group: {group.find('name').text}, bbo: {bbo.text}")
#         else:
#             print(f"Group: {group.find('name').text}, bbo: Не знайдено")
#


for group in root.findall('group'):
    for el_2 in group:
        print(el_2.tag, '--> ', el_2.text)
