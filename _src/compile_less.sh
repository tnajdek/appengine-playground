#!/bin/bash
# compile less & compress css;
# requires lessc and clean-css - both available from npm
ROOT=`dirname $0`/../
lessc $ROOT/_src/less/blog.less > $ROOT/static/css/blog.css
cleancss -o $ROOT/static/css/blog.css $ROOT/static/css/blog.css