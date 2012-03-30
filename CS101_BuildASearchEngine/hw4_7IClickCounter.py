def record_user_click(index,keyword,url):
    urls = lookup(index, keyword)
    for aurl in urls:
        if(aurl[0] == url):
            aurl[1] = aurl[1] + 1
    

def add_to_index(index, keyword, url):
    for entry in index:
        if entry[0] == keyword:
            for aurl in entry[1]:
                if aurl == url: # I found the keyword and the url. I don't have to add anything
                    return
            entry[1].append([url, 0]) # found the keyword but no the url. Add it.
            return
    # not found, add new keyword to index
    index.append([keyword, [[url, 0]]])


def get_page(url):
    try:
        if url == "http://www.udacity.com/cs101x/index.html":
            return  '<html> <body> This is a test page for learning to crawl! <p> It is a good idea to  <a href="http://www.udacity.com/cs101x/crawling.html">learn to crawl</a> before you try to  <a href="http://www.udacity.com/cs101x/walking.html">walk</a> or  <a href="http://www.udacity.com/cs101x/flying.html">fly</a>. </p> </body> </html> '
        elif url == "http://www.udacity.com/cs101x/crawling.html":
            return  '<html> <body> I have not learned to crawl yet, but I am quite good at  <a href="http://www.udacity.com/cs101x/kicking.html">kicking</a>. </body> </html>'
        elif url == "http://www.udacity.com/cs101x/walking.html":
            return '<html> <body> I cant get enough  <a href="http://www.udacity.com/cs101x/index.html">crawling</a>! </body> </html>'
        elif url == "http://www.udacity.com/cs101x/flying.html":
            return '<html> <body> The magic words are Squeamish Ossifrage! </body> </html>'
    except:
        return ""
    return ""

def union(a, b):
    for e in b:
        if e not in a:
            a.append(e)

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def get_all_links(page):
    links = []
    while True:
        url, endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links

def crawl_web(seed):
    tocrawl = [seed]
    crawled = []
    index = []
    while tocrawl: 
        page = tocrawl.pop()
        if page not in crawled:
            content = get_page(page)
            add_page_to_index(index, page, content)
            union(tocrawl, get_all_links(content))
            crawled.append(page)
    return index

def add_page_to_index(index, url, content):
    words = content.split()
    for word in words:
        add_to_index(index, word, url)

def lookup(index, keyword):
    for entry in index:
        if entry[0] == keyword:
            return entry[1]
    return None

index = crawl_web("http://www.udacity.com/cs101x/index.html")
print lookup(index, 'good') # => [['http://www.udacity.com/cs101x/index.html', 0], ['http://www.udacity.com/cs101x/crawling.html', 0]]
record_user_click(index, 'good', 'http://www.udacity.com/cs101x/crawling.html')
record_user_click(index, 'is', 'http://www.udacity.com/cs101x/index.html')
print lookup(index, 'good')
print lookup(index, 'is')
