#!/bin/sh

execute_computorv1(){
    count=$1
    line=$2
    echo "===== test case #$count =====
`python main.py $line`
`echo`"\
    >> my_output.txt
}

cat /dev/null > my_output.txt

count=1
cat test_case.txt | while read line
do
    execute_computorv1 $count $line
    ((count++))
done
