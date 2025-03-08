# -*- coding: utf-8 -*-

import datetime
import dblp
import operator
import pickle
import time

# Open up the author and publication information previously stored in
# pickled files.
authors_file = open("authors.data", 'rb')
sosp_file = open("sosp.data", 'rb')
osdi_file = open("osdi.data", 'rb')
total_file = open("total.data", 'rb')
total_5_file = open("total5.data", 'rb')

sosp = pickle.load(sosp_file)
osdi = pickle.load(osdi_file)
total = pickle.load(total_file)
total5 = pickle.load(total_5_file)
authors = pickle.load(authors_file)

sosp_file.close()
osdi_file.close()
total_file.close()
total_5_file.close()
authors_file.close()

last5 = datetime.datetime.now().year - 5

# choose here whether sosp or osdi or both
# sorted_x then contains the data that we care about

#sorted_x = sorted(sosp.items(), key=operator.itemgetter(1), reverse=True)
#sorted_x = sorted(osdi.items(), key=operator.itemgetter(1), reverse=True)
sorted_x = sorted(list(total.items()), key=lambda x: (-x[1], x[0].split()[-1]))

mypadding = "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"

# Google analytics code for my website. You should change this to your
# analytics information.
print("<!-- Google Analytics Code -->\
<script type='text/javascript'>\
  (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){\
  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new\
  Date();a=s.createElement(o),\
  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\
  })(window,document,'script','//www.google-analytics.com/analytics.js','ga');\
  ga('create', 'UA-20520573-2', 'auto');\
  ga('send', 'pageview');\
</script>\
<!-- End of Google Analytics Code -->")

# Header for the hall of fame. Change this to suit whatever conference
# you are targetting.  Please retain a link to this repo, to DBLP, and
# to CSRankings.

print("<title>Systems Research: SOSP/OSDI Hall of Fame</title>")
print("##Systems Research: SOSP/OSDI Hall of Fame")

print("Authors are ranked by total number of SOSP and OSDI papers (the top conferences for systems research). Authors with same number of papers have the same rank.")
print()
print("For display purposes, within each rank, authors are sorted by last name. Top 100 (approximately) authors are shown.")
print()
print("Disclaimers: ")
print("A real Hall of Fame should be determined by impact, not paper count.")
print("Data pulled from [DBLP](http://dblp.uni-trier.de) using a variation of [dblp-python](https://github.com/scholrly/dblp-python). Typos and name changes can cause miscounts. Please direct all queries about data to DBLP.")
print()
print("Author information obtained with permission from Prof. Emery Berger's [CSRankings](https://github.com/emeryberger/CSrankings/blob/gh-pages/faculty-affiliations.csv). Please direct queries about affiliation to CSRankings.")
print()
print("*Inspired by [ISCA Hall of Fame](http://pages.cs.wisc.edu/~arch/www/iscabibhall.html)")
print("and [MICRO Hall of Fame](http://newsletter.sigmicro.org/micro-hof.txt/view).*")
print()
print("&#128293; indicates five papers in the last five years")
print()
print("*Updated: " + time.strftime("%d/%m/%Y") + "*.")
print()
print("*Reflects data up-to SOSP 21.*")

print("Author \#&nbsp;&nbsp;&nbsp;&nbsp;|Rank&nbsp;&nbsp;|Name|Num. of Papers|&nbsp;&nbsp;Num. of Papers Since " + str(last5) + "|" + mypadding + "Last-Known Affiliation")
print("|:----:|:----|:--------| ----:|----:|:----")

# The function that prints each author
def mprint(i, rank, x, c, c5):
    flame_bar = "&nbsp;"
    for f in range(0, c5//5):
        flame_bar += "&#128293;";
    flame_bar +="|"

    content = ''.join((x, flame_bar, str(c), "|", str(c5)))
    ans = f"|{i}|{rank}|" + content.encode('ascii', 'xmlcharrefreplace').strip().decode('ascii')

    '''
    if c5 >= 10:
        ans = "|" + str(i) + "|" + str(rank) + "|" + u''.join((x, "&nbsp;&#128293;&#128293;|", str(c) ,"|", str(c5))).encode('ascii', 'xmlcharrefreplace').strip()
    elif c5 >= 5:
        ans = "|" + str(i) + "|" + str(rank) + "|" + u''.join((x, "&nbsp;&#128293;|", str(c) ,"|", str(c5))).encode('ascii', 'xmlcharrefreplace').strip()
    else:
        ans = "|" + str(i) + "|" + str(rank) + "|" + u''.join((x, "|", str(c) ,"|", str(c5))).encode('ascii', 'xmlcharrefreplace').strip()
    '''
 
    if x in authors:
        ans += "|" + mypadding + authors[x]
    print(ans)
    
i = 1
count = 0
prev_c = -1
rank = 1

# Go through the sorted publication counts for each author and print
# the information into HTML
for x,c in sorted_x:
    if c == prev_c:
        count += 1
    else:
        rank = i
        count = 0
        print("|||||")
        print("|||||")
        print("|||||")
        
    if rank <= 101:
        mprint(i, rank, x, c, total5.get(x, 0))

    i += 1
    prev_c = c

print() 
