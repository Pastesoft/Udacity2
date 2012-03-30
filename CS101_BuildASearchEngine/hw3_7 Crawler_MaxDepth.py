#crawl_web("http://www.udacity.com/cs101x/index.html",1) => ['http://www.udacity.com/cs101x/index.html']
#crawl_web("http://www.udacity.com/cs101x/index.html",3) => ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html']
#crawl_web("http://www.udacity.com/cs101x/index.html",500) => ['http://www.udacity.com/cs101x/index.html', 'http://www.udacity.com/cs101x/flying.html', 'http://www.udacity.com/cs101x/walking.html', 'http://www.udacity.com/cs101x/crawling.html', 'http://www.udacity.com/cs101x/kicking.html']

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

def get_next_target(page):
    start_link = page.find('<a href=')
    if start_link == -1: 
        return None, 0
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1:end_quote]
    return url, end_quote

def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)


def get_all_links(page):
    links = []
    while True:
        url,endpos = get_next_target(page)
        if url:
            links.append(url)
            page = page[endpos:]
        else:
            break
    return links


def crawl_web(seed,max_depth):
    tocrawl = [seed]
    alllinks = []
    levels = []
    crawled = []
    actualLev = 0
    levels.append(1)  # we have only one page al level 0 (the seed)
    while tocrawl:
        page = tocrawl.pop()
        if(levels[actualLev] > 0):  # are there more page to crawl at this level
            levels[actualLev] = levels[actualLev] - 1
        else:
            if(actualLev > 0):
                actualLev = actualLev - 1 # step back
            else:
                break
        if page not in crawled:
            if(actualLev < max_depth):
                alllinks = get_all_links(get_page(page))
                aln = len(alllinks)
                # new level check how many pages to add
                if(aln > 0):
                    union(tocrawl, alllinks)
                    actualLev = actualLev + 1
                    levels.append(aln)
            crawled.append(page)
    return crawled
    
print "with 0: ", crawl_web("http://www.udacity.com/cs101x/index.html",0)
print "with 1: ", crawl_web("http://www.udacity.com/cs101x/index.html",1)
print "with 500: ", crawl_web("http://www.udacity.com/cs101x/index.html",500)
