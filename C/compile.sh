# Set the path of your C compiler
PATH="$PATH":'/C:/MinGW/bin'

# Create compiled directory
mkdir -p compiled

# Compile all .c files in src directory (including tests)
for q in src/*.c src/tests/*.c
do
    if [ -f "$q" ]; then
        name=$(basename "$q" .c)
        echo "Compiling file $q to compiled/$name.o"
        gcc.exe -c "$q" -o "compiled/$name.o"
    fi
done

# Create static library
ar -rc compiled/libleetcode.a compiled/*.o

# Compile main with the library, output to compiled/leetcodeTest.exe
gcc.exe ./main.c -L. compiled/libleetcode.a -o compiled/leetcodeTest.exe

# Run the tests
./compiled/leetcodeTest.exe

# Delete all intermediate files except for the .exe
rm -f compiled/*.o
rm -f compiled/libleetcode.a