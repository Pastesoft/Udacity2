#Define a procedure, add_to_index,
#that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

#If the keyword is already
#in the index, add the url
#to the list of urls associated
#with that keyword.

#If the keyword is not in the index,
#add an entry to the index: [keyword,[url]]

index = []

def find_index(index, keyword):
    res = -1
    ln = len(index)
    i = 0
    while i < ln :
        if(index[i][0] == keyword) :
            res = i
        i = i + 1
    return res

def add_to_index(index,keyword,url):
    ind = find_index(index, keyword)
    if(ind > -1):
        urls = index[ind][1]
        if(len(urls) > 0):
            # index[ind][1] = urls + ", " + url
            index[ind][1].append(url)
    else:
        index.append([keyword,[url]])

def add_to_index2(index,keyword,url):
    for entry in index:
        if entry[0] == keyword:
            entry[1].append(url)
            return  # better than break
    # we endend the for without finding anything
    index.append([keyword,[url]])

        

add_to_index2(index,'udacity','http://udacity.com')
print "index=", index
add_to_index2(index,'computing','http://acm.org')
print "index=", index
add_to_index2(index,'udacity','http://npr.org')
print "index=", index
add_to_index2(index,'udacity','http://npr.org')
print "index=", index
