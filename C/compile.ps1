# PowerShell compilation script for LeetCode C tests

# Create compiled directory if it doesn't exist
if (!(Test-Path "compiled")) {
    New-Item -ItemType Directory -Path "compiled"
}

# Clear previous object files
Remove-Item "compiled/*.o" -ErrorAction SilentlyContinue

# Compile all .c files in src directory (including tests)
$srcFiles = Get-ChildItem -Path "src" -Filter "*.c" -Recurse
foreach ($file in $srcFiles) {
    $name = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)
    Write-Host "Compiling file $($file.FullName) to compiled/$name.o"
    & gcc.exe -c $file.FullName -o "compiled/$name.o"
}

# Create static library
& ar -rc compiled/libleetcode.a compiled/*.o

# Compile main with the library, output to compiled/leetcodeTest.exe
Write-Host "Compiling main program..."
& gcc.exe ./main.c -L. compiled/libleetcode.a -o compiled/leetcodeTest.exe

# Run the tests
Write-Host "Running tests..."
& ./compiled/leetcodeTest.exe

# Delete all intermediate files except for the .exe
Remove-Item compiled/*.o -ErrorAction SilentlyContinue
Remove-Item compiled/libleetcode.a -ErrorAction SilentlyContinue 