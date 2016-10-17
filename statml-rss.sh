#! /bin/bash

fn=statml-`date "+%Y%m%d-%H%M%S"`.html
python statml-rss.py > ${fn}
