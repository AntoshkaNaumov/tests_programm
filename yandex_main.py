from requests import put


def get_yandex_headers():
    token_yandex = input('Ввести токен Яндекса: ')
    return {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': f'OAuth {token_yandex}'
        }


def create_yandex_folder(url_adress, yandex_folder):
    """Создание папки. path: путь к создаваемой папке"""

    response = put(f'{url_adress}?path={yandex_folder}', headers=get_yandex_headers())
    return response.status_code


if __name__ == '__main__':
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    yandex_folder = 'yandex_test_3'
    create_yandex_folder(url, yandex_folder)
