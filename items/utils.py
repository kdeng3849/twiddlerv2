def to_dict(item):
    obj = {}
    obj['id'] = item.id
    obj['username'] = item.username
    obj['property'] = {}
    obj['property']['likes'] = item.property.likes
    obj['retweeted'] = item.retweeted
    obj['content'] = item.content
    obj['timestamp'] = item.timestamp

    return obj