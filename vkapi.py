import requests
from tokenlist import tokenapp
from db import get_user_db, store_matches


class VkRequest:
    url = 'https://api.vk.com/method/'

    def __init__(self):
        self.token = tokenapp
        self.version = 5.126
        self.params = {
            'access_token': self.token,
            'v': self.version
        }

    def search_cities(self, city):
        cities_url = self.url + 'database.getCities'
        cities_params = {
            'country_id': 1,
            'q': city,
            'need_all': 0,
            'count': 1
        }
        res = requests.get(cities_url, params={**self.params, **cities_params})
        data = res.json()
        if data['response']['items']:
            return data['response']['items'][0]
        else:
            return None

    def get_userinfo(self, userid):
        get_userinfo_url = self.url + 'users.get'
        get_userinfo_params = {
            'user_id': userid,
            'fields': 'city,sex,bdate,relation'
        }
        get = requests.get(get_userinfo_url, params={**self.params, **get_userinfo_params})
        data = get.json()
        return data

    def search_matches(self, user_id):
        search_url = self.url + 'users.search'
        user = get_user_db(user_id)
        age = int(user['age'])
        city = int(user['city'])
        sex = 1
        if int(user['sex']) == 1:
            sex = 2
        if int(user['sex']) == 2:
            sex = 1
        search_params = {
            'sort': 0,
            'city': city,
            'sex': sex,
            'age_from': age - 2,
            'age_to': age + 2,
            'has_photo': 1,
            'fields': 'is_closed'
        }
        get = requests.get(search_url, params={**self.params, **search_params})
        data = get.json()
        store_matches(data, user_id)
        return data

    def get_photos(self, match_id=None):
        if match_id is None:
            match_id = 1
        photos_url = self.url + 'photos.get'
        photos_params = {
            'owner_id': match_id,
            'album_id': 'profile',
            'extended': 1,
            'count': 3,
            'rev': 1
        }
        res = requests.get(photos_url, params={**self.params, **photos_params})
        photos = []
        if len(res.json()['response']['items']) > 2:
            for i in range(0, 3):
                photos.append(res.json()['response']['items'][i]['id'])
        else:
            photos.append(res.json()['response']['items'][0]['id'])
        return photos
