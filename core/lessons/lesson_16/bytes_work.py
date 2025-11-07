#
#
# # відправити файл через api
#
# with open('img.png', 'rb') as fb:
#
#     bytes_data = fb.read()
#
# print(str(bytes_data))
#
# # response = request.get(...)
#
# image_bytes = bytes_data # response.context
#
# with open('new_image.png', 'wb') as fb:
#     fb.write(image_bytes)
#
# with open('new_image.png', 'rb') as fb:
#     new_images_bytes = fb.read()
#
# print(bytes_data == new_images_bytes)
