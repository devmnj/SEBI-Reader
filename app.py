import feedparser

feed = feedparser.parse("https://www.sebi.gov.in/sebirss.xml")

feed_title = feed['feed']['title']
feed_entries = feed.entries

for entry in feed.entries:
    article_title = entry.title
    article_link = entry.link
    article_published_at = entry.published # Unicode string
    article_published_at_parsed = entry.published_parsed # Time object
   # article_author = entry.author
    print "{}[{}]".format(article_title.encode('utf-8'), article_link.encode('utf-8'))
    print "Published at {}" .format(article_published_at)
    #print "Published by {}" .format(article_author)