#!/bin/bash
/home/tanush/bin/pdflatex -output-directory=$2 -interaction=nonstopmode $1
rm -f $2/*.aux $2/*.out $2/*.log