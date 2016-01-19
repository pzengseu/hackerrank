from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start :", tag
        if attrs:
            for a in attrs:
                print '->',a[0],'>',a[1] if a[1] else None
    def handle_endtag(self, tag):
        print "End   :", tag
    def handle_startendtag(self, tag, attrs):
        print "Empty :", tag
        if attrs:
            for a in attrs:
                print '->',a[0],'>',a[1] if a[1] else None

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
for _ in xrange(input()):
    parser.feed(raw_input())