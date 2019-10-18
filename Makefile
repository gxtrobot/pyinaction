FONT=STHeiti
pdf:
	cd $(file) && pandoc -t beamer --pdf-engine=xelatex -V CJKmainfont=$(FONT) $(file).md -o $(file).pdf
	open $(file)/$(file).pdf