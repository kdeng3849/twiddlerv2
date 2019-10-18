def to_dict(model):
    item = {}
    item['id'] = model.id
    item['username'] = model.username
    item['property'] = {}
    item['property']['likes'] = model.property.likes
    item['retweeted'] = model.retweeted
    item['content'] = model.content
    item['timestamp'] = model.timestamp

    return item