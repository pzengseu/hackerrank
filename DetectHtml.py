from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print tag
        if attrs:
            for a in attrs:
                print '->',' > '.join(map(str, a))

    def handle_startendtag(self, tag, attrs):
        print tag
        if attrs:
            for a in attrs:
                print '->',' > '.join(map(str, a))

html = ""
for i in  xrange(input()):
    html += raw_input()

parser = MyHTMLParser()
parser.feed(html)
parser.close()