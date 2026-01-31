#include <Python.h>

// Define a simple C function
static PyObject* hello(PyObject* self, PyObject* args) {
    return Py_BuildValue("s", "Hello from C!");
}

// Define methods for the module
static PyMethodDef ExampleMethods[] = {
    {"hello", hello, METH_VARARGS, "Greet from C code"},
    {NULL, NULL, 0, NULL}
};

// Define the module
static struct PyModuleDef examplemodule = {
    PyModuleDef_HEAD_INIT,
    "example",  // Name of the module
    NULL,       // Module documentation, may be NULL
    -1,         // Size of per-interpreter state of the module
    ExampleMethods
};

// Module initialization function
PyMODINIT_FUNC PyInit_example(void) {
    return PyModule_Create(&examplemodule);
}
