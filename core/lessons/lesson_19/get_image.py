import requests

url = 'https://lms.ithillel.ua/assets/favicon/apple-touch-icon.png'
response = requests.get(url)

with open('some_image.png', 'wb') as f:
    f.write(response.content)


with open('some_image.png', 'rb') as f:
    files_to_upload = {'file': f.read()}

    requests.post(url=url, files=files_to_upload)