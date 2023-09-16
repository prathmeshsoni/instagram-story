import json
import time
import requests
import os
import pymysql

db_host = 'instagramstory.mysql.pythonanywhere-services.com'
db_user = 'instagramstory'
db_password = 'Mksoni18091'
db_name = 'instagramstory$instagram_storys'
table_name = 'User_storymodel'

# db_host = 'localhost'
# db_user = 'root'
# db_password = 'password'
# db_name = 'instagram_storys'
# table_name = 'user_storymodel'


def db_connection():
    connection = pymysql.connect(host=db_host, user=db_user, db=db_name, password=db_password, charset='utf8mb4')
    return connection


def insert_data(item):
    con = db_connection()
    cursor = con.cursor()

    insert_stmt = (
        f"INSERT INTO {table_name} (username, story_time, story_id, story_link, tag_list, testing_time, media_path) "
        "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    )
    try:
        cursor.executemany(insert_stmt, item)
        con.commit()
        return cursor.lastrowid
    except Exception as e:
        # print(f"Error while Data INSERT from {table_name}")
        return False


def update_data(s_id, s_path):
    con = db_connection()
    cursor = con.cursor()

    insert_stmt = (
        f"UPDATE {table_name} "
        f"SET `story_link` = %s "
        f"WHERE id = %s"
    )
    update_value = (
        s_path,
        s_id
    )
    try:
        cursor.executemany(insert_stmt, [update_value])
        con.commit()
        print('Insert Data')
    except Exception as e:
        pass
        # print(f"Error while Data INSERT from {e}")


def main_req():
    global temp_session 
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

    response = temp_session.get('https://www.instagram.com/', headers=headers)
    try:
        csrf_token = response.text.split('csrf_token\\":\\"')[1].split('\\')[0]
        # print(f"Csrf Token Found")

    except Exception as e:
        print(f"Csrf Token Not Found :: {e}")
        csrf_token = ''

    return csrf_token


def req_login(csrf_token):
    global temp_session 
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
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1694892688:AeRQAG63HAlFjVlfVh/mF11C6m5mVQ8lw3TXtPgA4hfnE1RQ45+es8rp0liEvymFDd0rUN0bhJdCmEBEgSzRvDY3b4vKixwHjoJEmlI5CS+k5fNtirM+HwoXwQUJ769oe+JGoRHx8KVS/zqmvslaUJU4/A==',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        # 'trustedDeviceRecords': '{"6331088954":{"nonce":"uqeWPhkmbhB55WzWCa0gIFqzorWOGsV8BiBquMx7P6naQRgfidv9uKbvhBseJYR7","machine_id":"ZBcnRgALAAHTWdwhdRB52fxMT1yL"}}',
        'trustedDeviceRecords': '{}',
        'username': 'just.sonii',
    }

    response = temp_session.post(
        'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
        cookies=cookies,
        headers=headers,
        data=data

    )
    if response.status_code == 200:
        print('Login Completed..')
    else:
        print('Login Failed..')
    temp = response.cookies._cookies['.instagram.com']['/']
    cookies = {}
    for i in temp:
        cookies[temp[i].name] = temp[i].value
    return cookies


def req_login_p(csrf_token):
    global temp_session 
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
        'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1694895319:AeRQAEitLaC8jkdIWmYhCA9VZjJ33ribjq1HH0T83TilVhxX+38/Ie0ZFKzykbvCIz6ASaBNlSuMhuhwfNd30V4DP0t9eMQA+vZLxhnE1P+TleZ96H+3BS3pao558iP5blONRVKSemHnSpbuMu7yyAIf',
        'optIntoOneTap': 'false',
        'queryParams': '{}',
        # 'trustedDeviceRecords': '{"6331088954":{"nonce":"uqeWPhkmbhB55WzWCa0gIFqzorWOGsV8BiBquMx7P6naQRgfidv9uKbvhBseJYR7","machine_id":"ZBcnRgALAAHTWdwhdRB52fxMT1yL"}}',
        'trustedDeviceRecords': '{}',
        'username': 'prathmeshsoni25',
    }

    response = temp_session.post(
        'https://www.instagram.com/api/v1/web/accounts/login/ajax/',
        cookies=cookies,
        headers=headers,
        data=data

    )
    if response.status_code == 200:
        print('Login Completed..')
    else:
        print('Login Failed..')

    try:
        json_data = json.loads(response.text)
        token = json_data['two_factor_info']['two_factor_identifier']
    except:
        token = ''

    return cookies, headers, token


def get_story_list(cookies):
    global temp_session 
    global test_username
    final_count = 0
    headers = {
        'authority': 'www.instagram.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'dpr': '1.25',
        'referer': 'https://www.instagram.com/krishh.naaaa_20',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
        'sec-ch-ua-full-version-list': '"Google Chrome";v="117.0.5938.89", "Not;A=Brand";v="8.0.0.0", "Chromium";v="117.0.5938.89"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"10.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
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

    response = requests.get(
        'https://www.instagram.com/api/v1/feed/reels_tray/',
        params=params,
        cookies=cookies,
        headers=headers
    )
    if response.status_code == 200:
        print('Login Completed..')
    else:
        print('Login Failed..')
        return False

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
    final_data = {}
    if tray:
        # print(f'Tray = {len(tray)}')
        for n in tray:
            try:
                pk = n['user']['pk']
                user_names = n['user']['username']
                media_ids = n['media_ids'][0]
                if test_username:
                    if user_names.lower() == test_username:
                        texts = get_story_details(cookies, pk, user_names, media_ids)
                        temp_text = {
                            'categorized_data': {
                                user_names: texts
                            },
                            'count': len(texts),
                            'hid': user_names
                        }
                        return temp_text
                else:
                    texts = get_story_details(cookies, pk, user_names, media_ids)
                    final_count += len(texts)
                    temp_text = {
                        user_names: texts
                    }
                    final_data.update(temp_text)
                # print(f'Finish {user_names}')
            except Exception as e:
                print(f'Function Error At :: {e}')
    final_ = {
        'categorized_data': final_data,
        'count': final_count,
    }
    return final_
    # with open(f"Story.json", "w") as outfile:
    #     json.dump(final_data, outfile)


def get_story_details(cookies, pk, user_names, media_ids):
    global temp_session 
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

    response = temp_session.get(
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
    try:
        media_path = json_text['reels'][f"{params['reel_ids']}"]['user']['profile_pic_url']

        # i_path = os.path.join('C:\\prathmesh\\update_project\\instagram-story\\uploads', pk)
        i_path = os.path.join('/home/instagramstory/instagram-story/uploads', pk)
        try:
            os.mkdir(i_path)
            try:
                media_text = requests.get(media_path)
                if media_text.status_code == 200:
                    with open(f"{i_path}/{user_names}.png", 'wb') as f:
                        f.write(media_text.content)
                    media_path = f"uploads/{pk}/{user_names}.png"
            except:
                media_path = f"uploads/{pk}/{user_names}.png"
        except:
            media_path = f"uploads/{pk}/{user_names}.png"
    except:
        media_path = f"uploads/{pk}/{user_names}.png"
    for k in items:
        try:
            story_id = k['pk']
        except:
            story_id = ''
        try:
            video_url = k['video_versions'][0]['url']
            video = 1
        except:
            try:
                video_url = k['image_versions2']['candidates'][0]['url']
                video = 0
            except:
                video_url = ''
                video = 2
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
        story_time, testing_time = convert_unix_timestamp(int(temp_time))

        temp_item = {
            'story_time': story_time,
            'username': user_names,
            'story_id': story_id,
            'Video Url': video_url,
            'Tag Username': tags,
            'testing_time': testing_time
        }
        tags = ", ".join(tags)
        if video == 1:
            Linkl = f'uploads/{user_names}/{story_id}.mp4'
        else:
            Linkl = f'uploads/{user_names}/{story_id}.png'
        itemss = {
            'Time': story_time,
            'Link': Linkl,
            'Tag': tags,
            'main_time': {
                'media_path': media_path,
                'testing_time': testing_time
            }
        }
        temp_items = (
            user_names,
            story_time,
            story_id,
            video_url,
            tags,
            testing_time,
            media_path
        )
        test_con = insert_data([temp_items])
        if test_con:
            if video_url:
                # path = os.path.join('C:\\prathmesh\\update_project\\instagram-story\\uploads', user_names)
                path = os.path.join('/home/instagramstory/instagram-story/uploads', user_names)
                try:
                    os.mkdir(path)
                except:
                    pass
                try:
                    video_text = requests.get(video_url)
                    if video_text.status_code == 200:
                        if video == 1:
                            with open(f"{path}/{story_id}.mp4", 'wb') as f:
                                f.write(video_text.content)
                            update_data(test_con, f'uploads/{user_names}/{story_id}.mp4')
                        else:
                            with open(f"{path}/{story_id}.png", 'wb') as f:
                                f.write(video_text.content)
                            update_data(test_con, f'uploads/{user_names}/{story_id}.png')
                except:
                    pass

        total_story.append(itemss)
    return total_story


def convert_unix_timestamp(timestamp):
    from datetime import datetime, timedelta
    import pytz

    server_timezone = 'UTC'
    local_timezone = 'Asia/Kolkata'
    server_tz = pytz.timezone(server_timezone)
    dt_server = datetime.fromtimestamp(timestamp, tz=server_tz)

    # Subtract one day from the datetime object
    dt_server -= timedelta(days=1)

    # Convert the datetime object to the local timezone
    local_tz = pytz.timezone(local_timezone)
    dt_local = dt_server.astimezone(local_tz)

    # Format the datetime object as a string
    formatted_time = dt_local.strftime("%d %B %Y %I:%M %p %A")
    formatted_date = dt_local.strftime("%Y-%m-%d")

    return formatted_time, formatted_date


def main_file():
    while True:
        print('Login Start..')
        csrf_token = main_req()
        cookies = req_login(csrf_token)
        count = 2
        while True:
            get_story_list(cookies)
            print('4 Hour Remaining')
            time.sleep(60 * 60)
            print('3 Hour Remaining')
            time.sleep(60 * 60)
            print('2 Hour Remaining')
            time.sleep(60 * 60)
            print('1 Hour Remaining')
            time.sleep((60 * 60) * 0.5)
            print('30 Minutes Remaining')
            time.sleep((60 * 60) * 0.5)
            print('Start Soon....')

            if count == 3:
                break
            count += 1


def main_file_2(request, auth_otp, search_username):
    global temp_session
    global test_username
    test_username = search_username
    temp_session = requests.Session()
    if not auth_otp:
        print('Login Start..')
        csrf_token = main_req()
        cookies, headers, response = req_login_p(csrf_token)

        return cookies, headers, response
    else:
        cookies = final_otp(request, auth_otp)
        check = get_story_list(cookies)
        if check:
            return check
        else:
            return False


def main_file_1(s_username):
    global temp_session 
    global test_username
    test_username = s_username
    temp_session = requests.Session()
    print('Login Start..')
    csrf_token = main_req()
    cookies = req_login(csrf_token)
    check = get_story_list(cookies)
    if check:
        return check
    else:
        return False


def final_otp(request, verificationCode):
    global temp_session
    headers = request.session.get('headers')
    response = request.session.get('response')
    cookies = request.session.get('cookies')
    del request.session['cookies']
    del request.session['headers']
    del request.session['response']

    headers['referer'] = 'https://www.instagram.com/accounts/login/two_factor?next=%2F'
    data = {
        'identifier': response,
        'queryParams': '{"next":"/"}',
        'trust_signal': 'true',
        'username': 'prathmeshsoni25',
        'verification_method': '2',
        'verificationCode': f'{verificationCode}',
    }

    response = temp_session.post(
        'https://www.instagram.com/api/v1/web/accounts/login/ajax/two_factor/',
        cookies=cookies,
        headers=headers,
        data=data,
    )

    temp = response.cookies._cookies['.instagram.com']['/']
    cookies = {}
    for i in temp:
        cookies[temp[i].name] = temp[i].value

    return cookies


if __name__ == '__main__':
    test_username = ''
    temp_session = requests.Session()
    main_file()

