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
$ fetchFeeds.py [-h] --feed FEEDURL [--info] [--prefix PREFIX] [--quiet] [--raw]
```
*   _-h_
    Show help message

*   _-f, --feed_
    Feed URL, required

*   _-i, --info_
    Only show feed info (title, URL)

*   _-p, --prefix_
    Prefix of feed storage path

*   _-q, --quiet_
    Quiet mode, no progress message is printed

*   _-r, --raw_
    Raw mode, HTML tags is preserved.

Output
-------------

The feeds would be stored in \[directory-to-store-feeds\] (cwd if no sepcified)
with the file name to be the timestamp of the feed.

The html tag in original feed would be striped using [html2text][1].

[1]: http://www.aaronsw.com/2002/html2text/
[2]: http://code.google.com/p/feedparser
