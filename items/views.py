import time
import json
import uuid

from django.core import serializers
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Item, ItemProperty
# from .serializers import ItemSerializer
from .utils import to_dict

def home(request):
    context = {
        'items': []
    }
    query = list(Item.objects.filter(timestamp__lte=time.time()).order_by('-timestamp')[:10])
    for item in query:
        context['items'].append(to_dict(item))

    return render(request, 'items/home.html', context)

@csrf_exempt
def add_item(request):
    data = json.loads(request.body, encoding='utf-8')

    try:
        username = request.user.username
        content = data['content']
        # child_type = data['childType']
    except KeyError:
        context = {
            'status': 'ERROR',
            'error': "POST body must include properties 'content', 'parent', and 'media' in the form of JSON",
        }
        return JsonResponse(context)

    item = Item()
    item.id = uuid.uuid4().node
    item.username = username
    item.property = ItemProperty()
    item.content = content
    item.save()

    context = {
        'status': 'OK',
        'id': item.id,
        # 'timestamp': item.timestamp,
    }
    return JsonResponse(context)

def get_item(request, id):
    try:
        query = Item.objects.get(id=id)
        # query = list(Item.objects.filter(id=id).values('id', 'username', 'property', 'retweeted', 'content', 'timestamp'))
    except:
        context = {
            'status': 'ERROR',
            'error': 'Invalid item ID'
        }
        return JsonResponse(context)

    # data = serializers.serialize("json", item)
    # data = ItemSerializer(item)
    # print(data)
    # jsondata = json.dumps(data)
    # item = {}
    # item['id'] = query.id
    # item['username'] = query.username
    # item['property'] = {}
    # item['property']['likes'] = query.property.likes
    # item['retweeted'] = query.retweeted
    # item['content'] = query.content
    # item['timestamp'] = query.timestamp
    item = to_dict(query)
    context = {
        'status': 'OK',
        'item': item,
    }

    # return HttpResponse(context, content_type='application/json')
    return JsonResponse(context)

@csrf_exempt
def search(request):
    data = json.loads(request.body, encoding='utf-8') if request.body else {}
    timestamp = data.get('timestamp') or time.time()
    limit = data.get('limit') or 25

    if limit > 100:
        response = {
            'status': 'ERROR',
            'error': 'limit must not be greater than 100'
        }
        return JsonResponse(response)

    response = {
        'status': 'OK',
        'items': [],
    }

    query = list(Item.objects.filter(timestamp__lte=timestamp).order_by('-timestamp')[:limit])
    for item in query:
        response['items'].append(to_dict(item))

    return JsonResponse(response)

@csrf_exempt
@require_http_methods(["POST"])
def like(request):
    data = json.loads(request.body, encoding='utf-8')
    print(data)
    id = data['id']

    try:
        item = Item.objects.get(id=id)
        item.property.likes += 1
        item.save()
    except:
        return JsonResponse({'status': 'ERROR'})

    response = {
        'status': 'OK',
        'likes': item.property.likes,
    }
    return JsonResponse(response)