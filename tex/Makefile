all: tex pdf

TARGET = proposal.pdf
MKD_FILE = $(addsuffix .md,  $(basename $(TARGET)))

BIBTEX = bibtex
LATEX  = pdflatex

MAIN_FILE = tmp.tex
AUX_FILE  = $(addsuffix .aux, $(basename $(MAIN_FILE)))
DVI_FILE  = $(addsuffix .dvi, $(basename $(MAIN_FILE)))
PDF_FILE  = $(addsuffix .pdf, $(basename $(MAIN_FILE)))
PS_FILE   = $(addsuffix .ps,  $(basename $(MAIN_FILE)))
TEX_FILE  = $(addsuffix .tex, $(basename $(MAIN_FILE)))

CC=pandoc
FLAGS=--filter pandoc-eqnos --filter pandoc-tablenos --from=markdown-smart --to=latex --indented-code-classes=numberLines --highlight-style=zenburn --listings --ascii --number-sections

all:
	@make tex
	@make pdf

tex:
	@echo "MD -> TEX"
	iconv -t utf-8 proposal.md | $(CC) $(FLAGS) --output=$(TEX_FILE)
	cat beg.tex > tmp.tex
	cat proposal.tex >> tmp.tex
	cat end.tex >> tmp.tex

pdf: $(MAIN_FILE) bibliografia.bib
	$(LATEX) -shell-escape $(MAIN_FILE)
	$(BIBTEX) $(AUX_FILE)
	$(LATEX) -shell-escape $(MAIN_FILE)
	$(LATEX) -shell-escape $(MAIN_FILE)
	@mv tmp.pdf $(TARGET)

clean:
	@rm tmp.* -vf *.brf *.lol *.idx *.lof *.lot *.toc *.bbl *.blg *.log *.aux *.dvi
