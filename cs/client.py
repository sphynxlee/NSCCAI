import requests

class Client:
    def __init__(self, url, page, param):
        self.url = url
        self.page = page
        self.param = param

    def get(self):
        url = self.url + self.page + self.param
        response = requests.get(url)
        if response.status_code != 200:
            print(f'error: {response.status_code}')
            exit(1)
        print(f'response.headers content-type: {response.headers["content-type"]}')
        print(f'response: {response.text}')

my_client = Client('http://127.0.0.1:5000/', '/inputValue/', 'hello')
my_client.get()

my_client2 = Client('http://127.0.0.1:5000/', '/calc/', '5,6')
my_client2.get()