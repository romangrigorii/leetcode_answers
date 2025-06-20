# LeetCode C Solutions with Tests

This repository contains C implementations of LeetCode problems with a structured testing framework.

## Project Structure

```
C/
├── main.c                 # Main entry point that runs all tests
├── compile.sh             # Bash compilation script (Unix/Linux)
├── compile.ps1            # PowerShell compilation script (Windows)
├── src/
│   ├── headers.h          # Function declarations for all algorithms
│   ├── 0001_twosum.c      # Two Sum algorithm implementation
│   └── tests/
│       └── test_0001_twosum.c  # Tests for Two Sum algorithm
└── compiled/              # Compiled object files and library
```

## How to Run Tests

### On Windows (PowerShell):
```powershell
./compile.ps1
```

### On Unix/Linux:
```bash
./compile.sh
```

## Adding New Algorithms

1. **Create the algorithm file** in `src/`:
   - Name format: `XXXX_problemname.c` (e.g., `0002_addtwonumbers.c`)
   - Include the algorithm implementation

2. **Add function declaration** to `src/headers.h`:
   ```c
   // Add your function declaration here
   ```

3. **Create test file** in `src/tests/`:
   - Name format: `test_XXXX_problemname.c`
   - Use the template below

4. **Add test function declaration** to `src/headers.h`:
   ```c
   void run_problemname_tests();
   ```

5. **Call the test function** in `main.c`:
   ```c
   run_problemname_tests();
   ```

## Test File Template

```c
#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
#include "../headers.h"

void test_1_problem_name(){
    // Your test implementation here
    printf("Testing: %s test 1: Success\n", __func__);
}

// Function to run all tests for this problem
void run_problem_name_tests() {
    printf("Running Problem Name Tests...\n");
    test_1_problem_name();
    printf("All Problem Name tests completed successfully!\n\n");
}
```

## Current Algorithms

- **0001: Two Sum** - Find two numbers that add up to a target value
  - File: `src/0001_twosum.c`
  - Tests: `src/tests/test_0001_twosum.c`

## Compilation Process

1. All `.c` files in `src/` and `src/tests/` are compiled to object files
2. Object files are combined into a static library (`libleetcode.a`)
3. Main program is compiled and linked with the library
4. Tests are executed automatically

## Notes

- Tests use assertions to verify correctness
- Memory is properly freed in test functions
- Each algorithm has its own test suite
- The compilation process automatically includes all test files 