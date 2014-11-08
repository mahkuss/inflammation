DRUG=$(python /home/rob/Desktop/inflammation/src/assign_drug.py $2)
DEST=data/$1/$1-$DRUG.dat
echo cp $2 $DEST