.PHONY: all

all: analysis.html analysis.tex

analysis.tex: analysis.png analysis.rst
	@echo "Building analysis.tex"
	rst2latex.py analysis.rst analysis.tex

analysis.html: analysis.png analysis.rst
	@echo "Building analysis.html"
	rst2s5.py analysis.rst analysis.html

analysis.png: analyze_websites.py websites.txt
	@echo "Building analysis.png"
	python analyze_websites.py websites.txt ${SEARCH_TERM}
