# for file in $(find code/diagrams -name '*.py' -printf "%f\n"); 
# do
#     code/venv/bin/python "code/diagrams/${file}"
# done

# for file in $(find figures/tex -name '*.tex' -printf "%f\n"); 
# do 
#     file="${file%.tex}";
#     echo "${file}";
#     latexmk -quiet -bibtex -f -pdf -pdflatex="pdflatex -synctex=1 -interaction=nonstopmode" "figures/tex/${file}.tex" -output-directory="figures/tex"
#     # latexmk -c "figures/tex/${file}.tex" -output-directory="figures/tex"
# done

latexmk -quiet -bibtex -f -pdf -shell-escape -pdflatex="pdflatex -synctex=1 -interaction=nonstopmode" main.tex