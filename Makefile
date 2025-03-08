all: authors.data sosp.data osdi.data
	python3 analyze-markdown.py > top.md
	showdown makehtml -i top.md -o top.html 

local: authors.data sosp.data osdi.data
	python3 analyze-markdown.py > top.md
	showdown makehtml -i top.md -o top.html 

active: authors.data
	python3 analyze-latest.py > top-active.md
	showdown makehtml -i top-active.md -o top-active.html 

authors.data:
	python3 getauthors.py

sosp.data:
	python3 getdata.py

osdi.data:
	python3 getdata.py

clean:
	rm *.data *.html *.md
