from django.http import JsonResponse

from User.models import StoryModel


def particular_data(request, hid):
    obj = StoryModel.objects.filter(username=hid)
    data = []
    for i in obj:
        items = {
            'Time': i.story_time,
            'Link': i.story_link,
            'Tag': i.tag_list
        }
        data.append(items)

    response = JsonResponse(data, safe=False)

    return response


def all_data(request):
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

    response = JsonResponse(categorized_data, safe=False)

    return response
