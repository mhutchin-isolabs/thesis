latexindent -m -l -w main.tex
latexindent -m -l -w raw_papers/*.tex
latexindent -m -l -w chapters/*.tex
# rm *.bak*
# rm indent.log
# rm raw_papers/*.bak*
# rm raw_papers/indent.log
# rm chapters/*.bak*
# rm chapters/indent.log


latexmk -C main.tex
latexmk -C main_raw_papers.tex
latexmk -C MJH_demo.tex
latexmk -C test_doc.tex