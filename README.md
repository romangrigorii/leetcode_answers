
In this module we implement a series of leetcode answers with various approaches in diffrent languages.

## Working in Python directory
 
Simply navigate to /Python and run any of the functions:

```
python3 1_twosum.py
```
The test is implicit in the function file. You can also run all tests at once with:
```
python3 testall.py
```
## Working in C directory
run:
```
compile.sh
```
to compile all functions and run tests
## Working in Cpp directory
run:
```
bazel test --cxxopt=-std=c++14 --test_output=all //...
```
To compile and run all of the tests.