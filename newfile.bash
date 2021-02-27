#!/bin/bash

for i in {1..20}
do
    if [ ! -f "/yourdirectoryforstoringoldlists/ostoslista$i.txt" ]; then
	mv /your/flaskapp/static/ostoslista.txt /yourdirectoryforstoringoldlists/ostoslista$i.txt
	break 
    fi
done
#the file that gets sended to the web page
touch /your/flaskapp/static/ostoslista.txt
