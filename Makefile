all: authors.data sosp.data osdi.data
	python analyze-markdown.py > top.md
	showdown makehtml -i top.md -o top.html 

local: authors.data sosp.data osdi.data
	python analyze-markdown.py > top.md
	showdown makehtml -i top.md -o top.html 

active: authors.data
	python analyze-latest.py > top-active.md
	showdown makehtml -i top-active.md -o top-active.html 

authors.data:
	python getauthors.py

sosp.data:
	python getdata.py

osdi.data:
	python getdata.py

clean:
	rm *.data *.html *.md
