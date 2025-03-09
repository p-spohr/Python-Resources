# Build through Commandline
```sh
gcc .\pylist.c -o pylist -I C:\Users\pat_h\Python\Python313\include -L C:\Users\pat_h\Python\Python313\libs -lPython313
```
-I points to the Python.h and the rest of the necessary headers in the include files
-L points to the static library file
-lPython313 or -l`name` tells which .lib file to use in -L directory

# python313.lib
The `python313.lib` file is a **static library file** for Python 3.13. Static libraries contain a collection of object files that are linked into your program during the build process. When you compile a C program that uses Python's C API, you need to link against the Python library to access Python's functions and features.

### Key Points:
- **Static Library**: `python313.lib` is a static library, meaning it contains compiled code that gets included directly into your executable.
- **Linking**: During compilation, the linker uses `python313.lib` to resolve references to Python functions and objects.
- **Dependency**: It's essential for ensuring that your compiled program can interact with the Python interpreter and use its functionalities.

### Example Usage:
When compiling a C program that uses Python's C API, you might use a command like this:
```sh
gcc example.c -o example -I C:\Users\pat_h\Python\Python313\include -L C:\Users\pat_h\Python\Python313\libs -l python313
```
Here, `-lpython313` tells the linker to use the `python313.lib` file to resolve Python-related dependencies.

You can directly specify the path to the `python313.lib` file when linking your program. This can be particularly useful if your library is in a non-standard location or if you prefer not to modify the `PATH` or use the `-L` flag.

Instead of using `-L` to add the directory and `-l` to specify the library, you can directly provide the full path to the `.lib` file:

```sh
gcc example.c -o example -IC:\Users\pat_h\Python\Python313\include C:\Users\pat_h\Python\Python313\libs\python313.lib
```

### Explanation:
- **`-I`**: Includes the directory for the Python header files.
- **Full Path to Library**: Instead of using `-L` and `-l`, you specify the full path to `python313.lib`.

### Benefits:
- **Simplicity**: Directly specifying the path can simplify your command line and avoid issues with incorrect library search paths.
- **Explicitness**: Ensures that the exact library you want to link against is used, avoiding any potential conflicts or mismatches.

When you provide the full path to a library file (like `python313.lib`), the linker recognizes it directly as a file to be included in the linking process. This method bypasses the need for the `-L` and `-l` flags.

### How It Works:
1. **Direct File Inclusion**:
   - By specifying the full path, you're telling the linker exactly where to find the library file and to use that specific file.
   - This eliminates the need for the linker to search directories for the specified library name.

### Example:
```sh
gcc example.c -o example -IC:\Users\pat_h\Python\Python313\include C:\Users\pat_h\Python\Python313\libs\python313.lib
```

### Benefits:
- **Simplicity**: Directly providing the path avoids potential issues with library search paths and ensures the correct file is used.
- **Clarity**: It makes the command more explicit and easier to understand, especially when dealing with multiple libraries or non-standard locations.

### Why Flags are Typically Used:
- **`-L` Flag**: Adds directories to the library search path.
- **`-l` Flag**: Specifies which library to link against by name.

However, if you already know the exact location of the library file, you can bypass these flags and directly include the file in your command.

This approach ensures that there is no ambiguity about which library file is being linked, making it straightforward and effective for specific use cases.
