#!/bin/bash

ZIPFILE=$1
ROOT=`dirname $0`/../

if [ ! -z $ZIPFILE ];
	then
		echo "Cooking icomoon soup"
		unzip $ZIPFILE -d /tmp

		echo "Firstly add some fonts..."
		cp -f /tmp/icomoon*/fonts/* $ROOT/static/fonts/
		echo "Then throw in stylesheet with codes..."
		cp -f /tmp/icomoon*/style.css $ROOT/_src/less/icomoon.less
		echo "Spring with regexp..."
		sed -i -e "s#url('fonts#url('@{static}/fonts#g" $ROOT/_src/less/icomoon.less
		echo "Cleanup the kitchen"
		rm -Rf /tmp/icomoon*
		echo "And we're done!"
	else
		echo "Usage: $0 icomoonPACKAGE.zip"
	fi
