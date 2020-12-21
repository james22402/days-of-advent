PREFIX="Day_"
NUM_DAYS=25
for(( i = 1; i <= $NUM_DAYS; i++)); do
  mkdir "${PREFIX}${i}"
  cd "${PREFIX}${i}"
  touch README.md
  echo "# ${PREFIX}${i}" >> README.md
  cd ..
done