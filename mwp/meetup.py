import datetime

import requests

START = '0'
END = '1w'


def get_url(key, urlname):
    url = ("http://api.meetup.com/2/events?sign=true&key={}&group_urlname={}"
           "&time={},{}").format(
        key, urlname, START, END)
    return url


def get_events(key, urlname):
    url = get_url(key, urlname)
    data = requests.get(url).json()['results']
    events = []
    for d in data:
        e = {
            'name': d.get('name'),
            'url': d.get('event_url'),
            'description': d.get('description', "No description."),
            }
        timestamp = d['time']
        event_date = datetime.datetime.fromtimestamp(timestamp/1000)
        e['date'] = event_date.strftime('%A, from %I:%M%p')
        events.append(e)
    return events
