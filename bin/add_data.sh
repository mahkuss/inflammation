DRUG=$(python /home/rob/Desktop/inflammation/src/assign_drug.py $2)
DEST=data/$1/$1-$DRUG.dat
cp $2 $DEST
git add $DEST
MESSAGE="Add file $DEST to data."
git commit -m "'$MESSAGE'"
echo "New file added to th repo: $DEST"