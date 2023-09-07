import json
import random
import string
import time
import requests

import pymysql

db_host = 'localhost'
db_user = 'root'
db_password = 'password'
db_name = 'instagram_story'
table_name = 'User_StoryModel'


def db_connection():
    connection = pymysql.connect(host=db_host, user=db_user, db=db_name, password=db_password, charset='utf8mb4')
    return connection


def insert_data(item):
    con = db_connection()
    cursor = con.cursor()

    insert_stmt = (
        f"INSERT IGNORE INTO {table_name} (username, story_time, story_id, story_link, tag_list) "
        "VALUES (%s, %s, %s, %s, %s)"
    )
    try:
        cursor.executemany(insert_stmt, [item])
        con.commit()
    except Exception as e:
        print(f"Error while Data INSERT from {table_name}")


def generate_random_name():
    letters = string.ascii_lowercase
    name_length = random.randint(6, 7)
    random_name = ''.join(random.choice(letters) for _ in range(name_length))
    return random_name


def main_req():
    headers = {
        'authority': 'www.instagram.com',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    }

    response = session.get('https://www.instagram.com/', headers=headers)
    try:
        csrf_token = response.text.split('csrf_token\\":\\"')[1].split('\\')[0]
        print(f"Csrf Token Found")

    except Exception as e:
        print(f"Csrf Token Not Found :: {e}")
        csrf_token = ''

    return csrf_token


def req_login(csrf_token):
    cookies = {
        'csrftoken': f'{csrf_token}',
        'mid': 'ZPm_EwALAAEIhlau9qmmZGACHrCP',
        'ig_did': '6423BEBF-0CCD-43B8-A8BE-F26DA969D994',
        'ig_nrcb': '1',
        'dpr': '1.25',
        'datr': 'Eb_5ZHjPfYYqB98UJTJTloDd',
    }

    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/x-www-form-urlencoded',
        'dpr': '1.25',
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.179", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.179"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'viewport-width': '1536',
        'x-asbd-id': '129477',
        'x-csrftoken': f'{csrf_token}',
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-instagram-ajax': '1008494309',
        'x-requested-with': 'XMLHttpRequest',
    }

    data = {
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1694089092:AVNQAF+9M+CZsKhyPYjow7pvh6P5wlTdLgCVvYkPOJRRiIJy2/Itf466D0fZoWkxXNeffzUUq7VXYwYRfKJ/6uNJ9cJc6bR3Gx8GjSEb4IULw6OCQBe0F1DIth3gEnMGbBx4QgI76DJoZzGwfpewkJZvA331',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        'trustedDeviceRecords': '{}',
        'username': 'just.sonii',
    }

    response = session.post(
        'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
        cookies=cookies,
        headers=headers,
        data=data

    )
    temp = response.cookies._cookies['.instagram.com']['/']
    cookies = {}
    for i in temp:
        cookies[temp[i].name] = temp[i].value
    return cookies


def main_file():
    print('Login Start..')
    csrf_token = main_req()
    cookies = req_login(csrf_token)
    print('Login Completed..')
    # while True:
    print('Start Scraping')
    get_story_list(cookies)
    print('Finish Scraping')
    # time.sleep(10)
        # time.sleep((60 * 60) * 23)


def get_story_list(cookies):
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'dpr': '1.25',
        'referer': 'https://www.instagram.com/prathmeshsoni25/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.141", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'viewport-width': '1536',
        'x-asbd-id': '129477',
        'x-csrftoken': f"{cookies['csrftoken']}",
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': '0',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'is_following_feed': 'false',
    }

    response = session.get(
        'https://www.instagram.com/api/v1/feed/reels_tray/',
        params=params,
        cookies=cookies,
        headers=headers
    )
    try:
        json_text = json.loads(response.text)
    except Exception as e:
        print(f'Json Text Not Found :: {e}')
        return

    try:
        tray = json_text['tray']
    except Exception as e:
        tray = None
        print(f'Tray Not Found : {e}')
    final_data = []
    if tray:
        print(f'Tray = {len(tray)}')
        for n in tray:
            try:
                pk = n['user']['pk']
                user_names = n['user']['username']
                media_ids = n['media_ids'][0]
                texts = get_story_details(cookies, pk, user_names, media_ids)
                temp_text = {
                    user_names: texts
                }
                final_data.append(temp_text)
                print(f'Finish {user_names}')
            except Exception as e:
                print(f'Function Error At :: {e}')
    random_name = generate_random_name()
    with open(f"Story_{random_name}.json", "w") as outfile:
        json.dump(final_data, outfile)


def get_story_details(cookies, pk, user_names, media_ids):
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'dpr': '1.25',
        'referer': f'https://www.instagram.com/stories/{user_names}/{media_ids}/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Google Chrome";v="116"',
        'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.141", "Not)A;Brand";v="24.0.0.0", "Google Chrome";v="116.0.5845.141"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'viewport-width': '1536',
        'x-asbd-id': '129477',
        'x-csrftoken': f"{cookies['csrftoken']}",
        'x-ig-app-id': '936619743392459',
        'x-ig-www-claim': 'hmac.AR0YGqCd_GkrpiVrhWlOPni3t-aTwFDNlpKZ0YzIWdndrfXc',
        'x-requested-with': 'XMLHttpRequest',
    }

    params = {
        'reel_ids': f'{pk}',
    }

    response = session.get(
        'https://www.instagram.com/api/v1/feed/reels_media/',
        params=params,
        cookies=cookies,
        headers=headers
    )

    try:
        json_text = json.loads(response.text)
    except Exception as e:
        print(f'Json Text Not Found :: {e}')
        return

    items = json_text['reels'][f"{params['reel_ids']}"]['items']

    total_story = []

    for k in items:
        try:
            story_id = k['pk']
        except:
            story_id = ''
        try:
            video_url = k['video_versions'][0]['url']
        except:
            try:
                video_url = k['image_versions2']['candidates'][0]['url']
            except:
                video_url = ''
        if not video_url:
            print('')
        try:
            tag_list = k['story_bloks_stickers']
        except:
            tag_list = None
        tags = []
        if tag_list:
            for j in tag_list:
                try:
                    t_username = j['bloks_sticker']['sticker_data']['ig_mention']['username']
                    tags.append(t_username)
                except:
                    pass

        temp_time = k['expiring_at']
        story_time = convert_unix_timestamp(int(temp_time))

        temp_item = {
            'story_time': story_time,
            'username': user_names,
            'story_id': story_id,
            'Video Url': video_url,
            'Tag Username': tags
        }
        tags = ", ".join(tags)
        temp_items = (
            user_names,
            story_time,
            story_id,
            video_url,
            tags
        )
        insert_data(temp_items)

        total_story.append(temp_item)
    return total_story


def convert_unix_timestamp(timestamp):
    from datetime import datetime, timedelta

    # Convert the timestamp to a datetime object
    dt_object = datetime.fromtimestamp(timestamp)

    # Subtract the specified number of days
    dt_object -= timedelta(days=1)

    # Format the datetime object as a string
    formatted_time = dt_object.strftime("%A, %B %d, %Y %I:%M:%S %p")

    return formatted_time


if __name__ == '__main__':
    session = requests.Session()
    main_file()
