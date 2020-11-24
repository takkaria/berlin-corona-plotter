all: fetch process plot open

fetch:
	curl https://www.berlin.de/lageso/gesundheit/infektionsepidemiologie-infektionsschutz/corona/tabelle-bezirke-gesamtuebersicht/index.php/index/all.json > data.json

process:
	bash -c 'jq "`cat script.jq`" data.json > processed.json'

plot:
	mkdir -p plots
	./plot.py

open:
	xdg-open plots/ALL.png
