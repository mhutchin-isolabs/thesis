latexmk -quiet -bibtex -shell-escape -pvc -f -pdf -pdflatex="pdflatex -synctex=1 -interaction=nonstopmode" main.tex
# latexmk -quiet -bibtex -shell-escape -pvc -f -pdf -pdflatex="lualatex -synctex=1 -interaction=nonstopmode" main.tex

# latexmk -quiet -bibtex -pvc -f -pdf -xelatex main.tex