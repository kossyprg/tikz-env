FNAME   = main
OUTDIR  = out
RES_PPI = 300

.PHONY: build clean view

build: $(OUTDIR)
	platex -output-directory=$(OUTDIR) $(FNAME).tex
	dvipdfmx -o $(OUTDIR)/$(FNAME).pdf $(OUTDIR)/$(FNAME).dvi

$(OUTDIR):
	mkdir -p $(OUTDIR)

png: $(OUTDIR)/$(FNAME).pdf
	pdftocairo -png -r $(RES_PPI) -singlefile $(OUTDIR)/$(FNAME).pdf

gif: $(OUTDIR)/$(FNAME).pdf
	python pdf2gif.py --input ./out/$(FNAME).pdf --output animation.gif --dpi $(RES_PPI)

clean:
	rm -f $(OUTDIR)/*.aux \
	      $(OUTDIR)/*.log \
	      $(OUTDIR)/*.dvi \
	      $(OUTDIR)/*.pdf
