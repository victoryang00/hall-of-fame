import dblp

auth_count = {}

for y in range(1969, 2017, 2):
    print(y)
    a = dblp.searchvenue("/conf/sosp/" + str(y))
    for x in a:
        #print x.title
        if x.venue != "SOSP":
            continue
        
        if "proceedings" in x.title:
            continue

        if "Proceedings" in x.title:
            continue

        print(x.title)
        print(x.authors)
        for xx in x.authors:
            auth_count[xx] = auth_count.get(xx, 0) + 1


print(auth_count)
