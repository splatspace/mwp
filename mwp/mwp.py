from optparse import OptionParser
from ConfigParser import ConfigParser

from meetup import get_events
from post import (
    get_post_body,
    get_wp,
    make_post,
    )

parser = OptionParser()
parser.add_option(
    '-i', '--ini', dest='ini', help="ini file to use", metavar="INI")


def main():
    options, args = parser.parse_args()
    ini = options.ini
    if ini is None:
        ini = 'development.ini'
    cfg = ConfigParser()
    cfg.readfp(file(ini))
    events = get_events(
        cfg.get('meetup', 'key'), cfg.get('meetup', 'urlname'))
    post_body = get_post_body(events)
    wp = get_wp(
        cfg.get('wordpress', 'url'),
        cfg.get('wordpress', 'user'),
        cfg.get('wordpress', 'pass'))
    make_post(post_body, wp)


if __name__ == '__main__':
    main()
