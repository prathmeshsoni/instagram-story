from django.http import JsonResponse
from django.shortcuts import render

from User.models import StoryModel


def p_data(hid):
    obj = StoryModel.objects.filter(username=hid)
    data = []
    for i in obj:
        items = {
            'Time': i.story_time,
            'Link': i.story_link,
            'Tag': i.tag_list
        }
        data.append(items)

    return data


def particular_data(request, hid):
    response = p_data(hid)

    return response


def particular_data_1(request, hid):
    response = p_data(hid)
    categorized_data = {
        hid: response
    }

    datas = {
        'categorized_data': categorized_data
    }

    return render(request, 'story-information.html', datas)


def a_data():
    categorized_data = {}

    obj = StoryModel.objects.all()
    for i in obj:
        username = i.username
        if username in categorized_data:
            categorized_data[username].append({'Time': i.story_time, 'Link': i.story_link, 'Tag': i.tag_list})
        else:
            categorized_data[username] = [{
                'Time': i.story_time,
                'Link': i.story_link,
                'Tag': i.tag_list
            }]
    return categorized_data


def all_data(request):
    categorized_data = a_data()

    response = JsonResponse(categorized_data, safe=False)

    return response


def all_data_1(request):
    categorized_data = a_data()

    datas = {
        'categorized_data': categorized_data
    }

    return render(request, 'story-information.html', datas)
