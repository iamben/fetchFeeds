#!/usr/bin/env python
# -*- coding: utf-8 -*-

import feedparser   # textproc/py-feedparser
import html2text    # textproc/py-html2text
import sys, time, os
import argparse
from hashlib import md5

# helper functions
def msgPrint(msg, quiet=False):
    if quiet is not True:
        print msg


def getFeedContent(feed, prefix='', quiet=True):
    # retrive feeds
    for entry in feed['entries']:
        # use timestamp + title md5 as file name
        fileName = str(int(time.mktime(entry['date_parsed'])))
        fileName += '.' + md5(entry['title'].encode('utf-8')).hexdigest()[0:5]
        fileName = os.path.join(prefix, fileName)

        if os.path.exists(fileName):
            msgPrint("Skipping existing feed: %s" % entry['title'].encode('utf-8'),
                    quiet)
            continue

        with open(fileName, 'wb') as entFile:
            # markdown-like header
            entFile.write('---\nTitle: %s\n---\n' % entry['title'].encode('utf-8'))

            # stripe html tags
            entFile.write(html2text.html2text(entry['summary'], '').encode('utf-8'))

            msgPrint('Fetched feed: %s' % entry['title'].encode('utf-8'), quiet)


def getFeedInfo(feed, quiet=False):
    print "Title: %s" % feed['channel']['title']
    print "Url: %s" % feed['url']


# options parsing
argParser = argparse.ArgumentParser(description='simple RSS feed fetcher')
argParser.add_argument('-f', '--feedurl', help='URL of source feed to subscribe', required=True)
argParser.add_argument('-i', '--info', help='Fetch feed info only', action='store_true')
argParser.add_argument('-p', '--prefix', help='Path prefix of file storing')
argParser.add_argument('-q', '--quiet', help='Suppress message output',
        action='store_true')
args = argParser.parse_args()

# info from options
feed = feedparser.parse(args.feedurl)

if args.quiet is not None:
    quiet = args.quiet
else:
    quiet = False

if args.info is not None:
    getFeedInfo(feed, quiet=False)
    sys.exit(0)

if args.prefix is not None:
    prefix = args.prefix
    try:
        os.makedirs(prefix, 0755)
    except:
        msgPrint("Using existing directory: %s" % prefix, quiet)

if args.info is None:
    getFeedContent(feed, prefix=prefix, quiet=quiet)
