import requests


def download_file_from_colab(params, filename):
    url = 'https://c7c0-35-240-154-233.ngrok.io'
    with open(filename, 'wb') as f:
        f.write(requests.post(url, json=params).content)
    return True
