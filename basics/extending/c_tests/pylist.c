#include <Python.h>
#include <stdio.h>

// Function to create a C array of PyObject* and handle different types
void handle_pyobject_array() {
    // Define the size of the array
    int size = 4;
    
    // Create a C array to hold PyObject* pointers
    PyObject* py_array[size];

    // Populate the array with different Python objects
    py_array[0] = PyLong_FromLong(10);  // Python integer
    py_array[1] = PyUnicode_FromString("Hello");  // Python string
    py_array[2] = PyList_New(0);  // Empty Python list
    py_array[3] = PyDict_New();  // Empty Python dictionary

    // Iterate over the array and print the type and value of each object
    for (int i = 0; i < size; i++) {
        PyObject* obj = py_array[i];

        // Check the type of the object
        if (PyLong_Check(obj)) {
            printf("Element %d is a Python integer: %ld\n", i, PyLong_AsLong(obj));
        } else if (PyUnicode_Check(obj)) {
            printf("Element %d is a Python string: %s\n", i, PyUnicode_AsUTF8(obj));
        } else if (PyList_Check(obj)) {
            printf("Element %d is a Python list.\n", i);
        } else if (PyDict_Check(obj)) {
            printf("Element %d is a Python dictionary.\n", i);
        } else {
            printf("Element %d is an unknown type.\n", i);
        }
    }

    // Decrease the reference count of each object to prevent memory leaks
    for (int i = 0; i < size; i++) {
        Py_DECREF(py_array[i]);
    }
}

int main() {
    // Initialize the Python interpreter
    Py_Initialize();

    // Create and handle the PyObject* array
    handle_pyobject_array();

    // Finalize the Python interpreter
    Py_Finalize();
    return 0;
}
