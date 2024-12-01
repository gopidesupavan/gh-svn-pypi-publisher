#!/bin/bash

EXIT=0

for i in *.asc
do
   echo -e "Checking $i\n"; gpg --verify $i
done

if [ $EXIT -eq 1 ]; then
    echo "One or more checksums did not match."
    exit 1
else
    echo "All checksums match."
fi
