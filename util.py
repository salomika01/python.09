import json
from dbook import Diary


def read_from_json_into_application(path):
    file = open(path)
    data = json.loads(file.read())
    diaries = []
    for entry in data:
        diaries.append(Diary(entry['memo'], entry['tags']))

    return diaries


def add_into_json(path):
    f = open(path)
    data = json.loads(f.read())
    new_data = []
    for entry in data:
        new_data.append(Diary(entry['memo'], entry['tags']))
    return new_data


def sort_id_memo(path):
    f = open(path)
    data = json.loads(f.read())
    sorted_by_memo = sorted(data, key=lambda item: item['memo'])
    sorted_by_id = sorted(data, key=lambda item: item['id'], reverse=True)
    return sorted_by_memo, sorted_by_id


















