
def toJson(data, length):
    json = []
    for row in data:
        res ={}
        res['value'] = row[0]
        json.append(res)

    return json