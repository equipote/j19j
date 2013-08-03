#!/bin/sh
for f in `ls *.ogg`
do
    echo Ejecutando $f ...
    ffmpeg -i ${f} ${f}.mp3
done

