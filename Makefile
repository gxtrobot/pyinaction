FONT=STHeiti
pdf:
	cd $(file) && pandoc -t beamer --pdf-engine=xelatex --highlight-style pygments  -V CJKmainfont=$(FONT) $(file).md -o $(file).pdf
	open $(file)/$(file).pdf