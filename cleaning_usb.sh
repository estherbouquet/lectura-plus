#!/bin/bash

if [ -d "/media/pi" ]
then
    echo "Plusieurs dossiers 'AJOUT' présents !"
    find /media/pi -mindepth 1 -maxdepth 1 -type d -empty -delete
    echo "Dossiers supprimés"
else 
    echo "Pas de dossier détecté"
fi