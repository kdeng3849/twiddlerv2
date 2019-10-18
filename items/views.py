import json
import uuid

from django.core import serializers
from django.http.response import HttpResponse, JsonResponse

from .models import Item, ItemProperty
# from .serializers import ItemSerializer

# Create your views here.
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
    response = {
        'status': 'OK',
        'item': {}
    }
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
    item = {}
    item['id'] = query.id
    item['username'] = query.username
    item['property'] = {}
    item['property']['likes'] = query.property.likes
    item['retweeted'] = query.retweeted
    item['content'] = query.content
    item['timestamp'] = query.timestamp

    context = {
        'status': 'OK',
        'item': item,
    }

    # return HttpResponse(context, content_type='application/json')
    return JsonResponse(context)
