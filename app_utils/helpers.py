def toJson(keys, data):
    x = 0
    data_items = {}

    for item in keys:
        data_items[item] = ''

    for d in data_items:
        data_items[d] = data[x]
        x += 1

    return data_items


def renderToJson(keys):
    def fn(data):
        return toJson(keys, data)
    return fn