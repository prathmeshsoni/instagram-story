import datetime

from django.shortcuts import render, redirect
from pytz import timezone

from User.insta_story_request import main_file_1
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
        'categorized_data': categorized_data
    }
    return datas


def particular_data(request, hid):
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

    return render(request, 'insta.html', datas)


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
    main_file_1()
    return redirect('/')
