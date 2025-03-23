# Set the path of your C compiler
PATH="$PATH":'/C:/MinGW/bin'

mkdir functions/compiled
for q in $(find functions -name '*.c')
do
    name=$(echo ${q##*/} | sed 's/\.[^.]*$//')
    echo "compiling file $q to functions/compiled/$name.o"
    if ! [[ $q == *"main"* ]]; then
        gcc.exe -c $q -o "functions/compiled/$name.o"
    fi
done

ar -rc libleetcode.a $(find -name *.o)

gcc.exe ./main.c -L. -lleetcode -o leetcode

./leetcode.exe