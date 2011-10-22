fetchFeeds.py: simple script to fetch RSS feeds into file
====================================

Requirements
----------------

- Python 2.7+
- [html2text][1]: textproc/py-html2text in FreeBSD ports.
- [feedparser][2]: textproc/py-feedparser in FreeBSD ports.

Usage
--------------

```bash
$fetchFeeds.py [-h] --feed FEEDURL [--info] [--prefix PREFIX] [--quiet]
```

Output
-------------

The feeds would be stored in \[directory-to-store-feeds\] (cwd if no sepcified)
with the file name to be the timestamp of the feed.

The html tag in original feed would be striped using [html2text][1].

[1]: http://www.aaronsw.com/2002/html2text/
[2]: http://code.google.com/p/feedparser
