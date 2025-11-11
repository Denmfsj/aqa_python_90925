import xml.etree.ElementTree as ET

# Завантаження XML-файлу
tree = ET.parse('data.xml')
root = tree.getroot()

# # Пошук елементу bbo у timingExbytes для кожної групи
for group in root.findall('group'):
    for element in group:

        if element.tag == 'timingExbytes':
            child1 = ET.SubElement(element, 'child1')
            child1.text = 'True'

        print(f'Name is {element.tag}')
        print(f'Values is {element.text}')
        print('-'*80)

tree = ET.ElementTree(root)
tree.write('output.xml')

    # timing_exbytes = group.find('timingExbytes')
    # if timing_exbytes is not None:
    #     bbo = timing_exbytes.find('bbo')
    #     if bbo is not None:
    #         print(f'BBO tag is {bbo.tag}')
    #         print(f"Group: {group.find('name').text}, bbo: {bbo.text}")
    #     else:
    #         print(f"Group: {group.find('name').text}, bbo: Не знайдено")
#

