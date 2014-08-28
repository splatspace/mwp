import datetime

from jinja2 import Template
from wordpress_xmlrpc import (
    Client,
    WordPressPost,
    )
from wordpress_xmlrpc.methods.posts import NewPost


TEMPLATE = Template('''
Here's this week's schedule:

<ul>
{% for event in events %}
<li>
    <p><strong>{{ event.date }}</strong> {{ event.name }}:</p>
    <p>{{ event.description }}</p>
</li>
{% endfor %}
</ul>

We hope to see you out!
''')


def get_wp(site, username, password):
    site = site + '/xmlrpc.php'
    return Client(site, username, password)


def make_post(content, wp):
    start = datetime.datetime.utcnow()
    end = start + datetime.timedelta(7)
    dates = (start.strftime('%b %d'), end.strftime('%b %d'))
    post = WordPressPost()
    post.title = "This week's schedule (%s - %s)" % dates
    post.content = content
    post.post_status = 'draft'
    wp.call(NewPost(post))


def get_post_body(events):
    return TEMPLATE.render(events=events)
