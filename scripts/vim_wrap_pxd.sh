#!/bin/sh

#wrapp vim for openning two files

pxd=$1
cpptrajsrc="$CPPTRAJHOME/src/"

if [ ! -f ${pxd}.pxd  ]; then
    cat PXD_template.dat > ${pxd}.pxd
fi

vim -O ${pxd}.pxd  $cpptrajsrc${pxd}.h
