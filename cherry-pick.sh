for file in $@
do
    pipenv run python $file
done
