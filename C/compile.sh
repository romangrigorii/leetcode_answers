# Set the path of your C compiler
PATH="$PATH":'/C:/MinGW/bin'

mkdir -p compiled
for q in $(find src -name '*.c')
do
    name=$(echo ${q##*/} | sed 's/\.[^.]*$//')
    # echo "compiling file $q to compiled/$name.o"
    if ! [[ $q == *"main"* ]]; then
        gcc.exe -c $q -o "compiled/$name.o"
    fi
done

ar -rc compiled/libleetcode.a $(find -name *.o)

gcc.exe ./main.c -L. compiled/libleetcode.a -o leetcodeTest

./leetcodeTest.exe