LATEX=pdflatex
LATEXOPT=--shell-escape #--output-directory=tmp
# NONSTOP=--interaction=nonstopmode
NONSTOP=--interaction=batchmode

LATEXMK=latexmk
LATEXMKOPT=-pdf -auxdir=tmp -outdir=tmp
CONTINUOUS=-pvc

MAIN=main
SOURCES=$(MAIN).tex Makefile 
FIGURES := $(shell find pictures/* -type f)

all:    $(MAIN).pdf

.refresh: 
	touch .refresh

$(MAIN).pdf: $(MAIN).tex .refresh $(SOURCES) $(FIGURES)
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
	-pdflatex="$(LATEX) $(LATEXOPT) $(NONSTOP) %O %S" $(MAIN)

force:
	touch .refresh
	rm $(MAIN).pdf
	$(LATEXMK) $(LATEXMKOPT) $(CONTINUOUS) \
	-pdflatex="$(LATEX) $(LATEXOPT) %O %S" $(MAIN)

clean:
	$(LATEXMK) -C $(MAIN)
	rm -f $(MAIN).pdfsync
	rm -rf *~ *.tmp
	rm -f *.bbl *.blg *.aux *.end *.fls *.log *.out *.fdb_latexmk
	rm -rf tmp/*

once:
	$(LATEXMK) $(LATEXMKOPT) -pdflatex="$(LATEX) $(LATEXOPT) %O %S" $(MAIN)

debug:
	$(LATEX) $(LATEXOPT) $(MAIN)

.PHONY: clean force once all
