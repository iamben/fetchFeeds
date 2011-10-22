#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser   # textproc/py-feedparser
import html2text    # textproc/py-html2text
import sys, time, os
from hashlib import md5

if len(sys.argv) not in range(2, 4):
    sys.stderr.write('Usage: fetchFeeds.py <feed url> [directory-to-store-feeds]\n')
    sys.exit(1)

feed = feedparser.parse(sys.argv[1])
if len(sys.argv) is 2:
    prefix = ''
else:
    prefix = sys.argv[2]
    try:
        os.makedirs(prefix, 0755)
    except:
        print "Using existing directory: %s" % prefix

# retrive feeds
for entry in feed['entries']:
    # use timestamp + title md5 as file name
    fileName = str(int(time.mktime(entry['date_parsed'])))
    fileName += '.' + md5(entry['title'].encode('utf-8')).hexdigest()[0:5]

    with open(os.path.join(prefix, fileName), 'wb') as entFile:
        # markdown-like header
        entFile.write('---\nTitle: %s\n---\n' % entry['title'].encode('utf-8'))

        # stripe html tags
        entFile.write(html2text.html2text(entry['summary'], '').encode('utf-8'))

        print '%s fetched.' % entry['title'].encode('utf-8')
