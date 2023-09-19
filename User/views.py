import datetime

from django.shortcuts import render, redirect
from pytz import timezone

from User.insta_story_request import intsa_story
from User.models import StoryModel


def p_data(hid, times):
    if hid:
        obj = StoryModel.objects.filter(
            username=hid,
            testing_time__day=times.day,
            testing_time__month=times.month,
            testing_time__year=times.year,
        ).order_by('-testing_time')
    else:
        if times:
            obj = StoryModel.objects.filter(
                testing_time__day=times.day,
                testing_time__month=times.month,
                testing_time__year=times.year,
            ).order_by('-testing_time')
        else:
            obj = StoryModel.objects.all().order_by('-testing_time')
    data = []
    for i in obj:
        items = {
            'Time': i.story_time,
            'Link': i.story_link,
            'Tag': i.tag_list,
            'main_time': i
        }
        data.append(items)

    return data


def test(hid):
    current_date = datetime.datetime.now(timezone("Asia/Kolkata"))
    response = p_data(hid, current_date)
    categorized_data = {
        hid: response
    }

    datas = {
        'categorized_data': categorized_data,
        'count': len(response)
    }
    return datas


def particular_data(request, hid):
    datas = dual_fun(hid)

    return render(request, 'insta.html', datas)


def dual_fun(hid):
    unique_usernames = StoryModel.objects.values('username', 'media_path').distinct()

    try:
        try:
            int(hid)
            con = 1
        except:
            try:
                tess = hid.split('-')
                if len(tess) == 3:
                    con = 2
                else:
                    con = 3
            except:
                con = 3

        if con == 3:
            datas = test(hid)
        else:
            datas = test_1(hid)
        datas['unique_usernames'] = unique_usernames
        datas['hid'] = hid
    except:
        datas = {
            'Nodata': "Nodata",
            'count': 0,
            'unique_usernames': unique_usernames,
            'hid': hid
        }
    return datas


def test_1(hid):
    try:
        tests = hid.split('-')
    except:
        tests = ''
    if len(tests) != 3:
        hid = ''
    else:
        hid = datetime.datetime.strptime(hid, '%Y-%m-%d')
    response = a_data('', hid)

    datas = {
        'categorized_data': response[0],
        'count': response[1]
    }
    return datas


def a_data(hid, times):
    categorized_data = {}
    if not hid:
        if times:
            obj = StoryModel.objects.filter(
                testing_time__day=times.day,
                testing_time__month=times.month,
                testing_time__year=times.year,
            ).order_by('-testing_time')
        else:
            obj = StoryModel.objects.all().order_by('-testing_time')
    else:
        if times:
            obj = StoryModel.objects.filter(
                username=hid,
                testing_time__day=times.day,
                testing_time__month=times.month,
                testing_time__year=times.year,
            )
        else:
            obj = StoryModel.objects.filter(
                username=hid,
            ).order_by('-testing_time')

    for i in obj:
        username = i.username
        if username in categorized_data:
            categorized_data[username].append(
                {'Time': i.story_time, 'Link': i.story_link, 'Tag': i.tag_list, 'main_time': i}
            )
        else:
            categorized_data[username] = [{
                'Time': i.story_time,
                'Link': i.story_link,
                'Tag': i.tag_list,
                'main_time': i
            }]

    return categorized_data, len(obj)


def all_data(request):
    unique_usernames = StoryModel.objects.values('username', 'media_path').distinct()
    if request.method == 'POST':
        search_username = "".join(request.POST.get('search_username')).strip().lower()
        verificationCode = request.POST.get('verificationCode')
        if not verificationCode:
            datas = intsa_story().main_file_prathmesh(search_username)
            if datas:
                datas['unique_usernames'] = unique_usernames
                return render(request, 'insta.html', datas)
            else:
                return redirect(f'/{search_username}/')
        else:
            datas = dual_fun(search_username)
            return render(request, 'insta.html', datas)
    else:
        try:
            current_date = datetime.datetime.now(timezone("Asia/Kolkata"))
            categorized_data, count = a_data('', current_date)

            datas = {
                'categorized_data': categorized_data,
                'count': count,
                'unique_usernames': unique_usernames
            }
        except:
            datas = {
                'categorized_data': '',
                'count': 0,
                'unique_usernames': unique_usernames
            }

        return render(request, 'insta.html', datas)


def all_data_1(request, hid, sid):
    unique_usernames = StoryModel.objects.values('username', 'media_path').distinct()
    try:
        try:
            tests = sid.split('-')
        except:
            tests = ''
        if len(tests) != 3:
            sid = ''
        else:
            sid = datetime.datetime.strptime(sid, '%Y-%m-%d')

        categorized_data, count = a_data(hid, sid)

        datas = {
            'categorized_data': categorized_data,
            'count': count,
            'unique_usernames': unique_usernames,
            'hid': hid
        }
    except:
        datas = {
            'categorized_data': '',
            'count': 0,
            'unique_usernames': unique_usernames,
            'hid': hid
        }

    return render(request, 'insta.html', datas)


def run(request):
    unique_usernames = StoryModel.objects.values('username', 'media_path').distinct()

    check = intsa_story().main_file()
    if check:
        check['unique_usernames'] = unique_usernames
        return render(request, 'insta.html', check)
    else:
        return redirect('/')


def otp(request):
    pass
    # cookies, headers, response = main_file_2(request, '', '')
    # request.session['cookies'] = cookies
    # request.session['headers'] = headers
    # request.session['response'] = response
    # return redirect('/')
