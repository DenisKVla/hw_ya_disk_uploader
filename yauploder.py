import requests
from pprint import pprint

TOKEN = ""

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str,filename):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Content-Type": "application/json", "Authorization": "OAuth {}".format(TOKEN)}
        params = {"path": file_path,"overwrite": "true"}
        href_response = requests.get(upload_url,headers=headers,params=params)
        href=href_response.json().get("href","")
        upload_response = requests.put(href,data=open(filename,"rb"))
        upload_response.raise_for_status()
        if upload_response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    filename = 'upload.txt'
    path_to_file = 'test/'+filename
    token = TOKEN
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, filename)