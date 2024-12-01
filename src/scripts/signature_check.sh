#!/bin/bash

EXIT=0

for i in *.asc
do
   echo -e "Checking $i\n"
   if ! gpg --verify $i 2>&1 | grep -q "Good signature"; then
       echo "Signature check failed for $i"
       EXIT=1
   fi
done

if [ $EXIT -eq 1 ]; then
    echo "One or more signature checks did not match."
    exit 1
else
    echo "All signature checks match."
fi