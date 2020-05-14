#!/bin/sh


for i in {1..170}
do
  i=`printf %03d $i`
  echo ${i}
	mkdir -p abc${i}
	cp -r  a.py abc${i}/a.py
	cp -r  b.py abc${i}/b.py
	cp -r  c.py abc${i}/c.py
	cp -r  d.py abc${i}/d.py
done

