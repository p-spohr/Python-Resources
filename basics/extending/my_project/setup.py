from setuptools import setup, Extension

# Define the extension module
example_module = Extension('example', sources=['example.c'])

# Run the setup
setup(
    name='example',
    version='1.0',
    description='Example package with a C extension',
    ext_modules=[example_module],
)
