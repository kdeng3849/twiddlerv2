import json
import uuid

from django.http.response import JsonResponse

from .models import Item, ItemProperty

# Create your views here.
def additem(request):
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
