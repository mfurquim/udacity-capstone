all: tex pdf

TARGET = proposal.pdf
AUX_FILE = $(addsuffix .aux, $(basename $(TARGET)))
DVI_FILE = $(addsuffix .dvi, $(basename $(TARGET)))
PDF_FILE = $(addsuffix .pdf, $(basename $(TARGET)))
PS_FILE  = $(addsuffix .ps,  $(basename $(TARGET)))
TEX_FILE = $(addsuffix .tex, $(basename $(TARGET)))
BIB_FILE = $(addsuffix .bib, $(basename $(TARGET)))

BIBTEX = bibtex
LATEX  = pdflatex

all:
	@make pdf

tex:
	$(MAKE) -C md tex

pdf:
	$(LATEX) -interaction nonstopmode -halt-on-error -file-line-error -shell-escape $(TEX_FILE)
	$(BIBTEX) $(AUX_FILE)
	$(LATEX) -interaction nonstopmode -halt-on-error -file-line-error -shell-escape $(TEX_FILE)
	$(LATEX) -interaction nonstopmode -halt-on-error -file-line-error -shell-escape $(TEX_FILE)
	@cp -v $(TARGET) ../$(TARGET)
	@rm -vf *.brf *.lol *.idx *.lof *.lot *.toc *.bbl *.blg *.log *.aux *.dvi *.out

clean:
	@rm -vf *.brf *.lol *.idx *.lof *.lot *.toc *.bbl *.blg *.log *.aux *.dvi *.tex *.out *.pdf
