import requests


def download_file_from_colab(params, filename):
    url = 'http://1315-35-188-177-132.ngrok.io'
    with open(filename, 'wb') as f:
        f.write(requests.post(url, json=params).content)
    return True
