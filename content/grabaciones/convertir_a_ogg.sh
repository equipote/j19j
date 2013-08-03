#!/bin/sh
for f in `ls *.wav`
do
    echo Ejecutando $f ...
    oggenc --utf8 -q 1 --resample 11025 --downmix ${f} -o ${f}.ogg
done

