import json
from datetime import datetime
from collections import namedtuple


class Job:

    def __init__(self, description: str, started: datetime):
        self.description = description
        self.started = started

    def __repr__(self) -> str:
        return f'Job({self.description}, {self.started})'


def datetime_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    return obj.__dict__


def object_hook(jobj: dict):
    """ JSON decoder

    Parameters
    ----------
    jobj : dict

    Returns
    -------
    object

    """
    if 'description' in jobj:
        return Job(jobj['description'], datetime.fromisoformat(jobj['started']))

    return namedtuple('VO', jobj.keys())(**jobj)


if __name__ == '__main__':
    data = {
        'first_name': 'John',
        'last_name': 'Dow',
        'age': 30,
        'address': {
            'country': 'ARM',
            'city': 'Yerevan',
        },
        'job': Job('Engineer', datetime.now()),
        'created': datetime.now()
    }

    json_encoded_data = json.dumps(data, indent=4, default=datetime_handler)
    print(json_encoded_data)

    decoded_dict = json.loads(json_encoded_data)
    decoded_obj = json.loads(json_encoded_data, object_hook=object_hook)

    print(decoded_obj)
    print(decoded_dict['address']['country'])
    print(decoded_obj.address.country)
