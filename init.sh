#!/bin/sh

execute_computorv1(){
    echo "===== test case #$1 =====
`python main.py "$2"`
`echo`"\
    >> my_output.txt
}

cat /dev/null > my_output.txt

count=0
cat test_case.txt | while read line
do
    execute_computorv1 $count "$line"
    ((count++))
done
