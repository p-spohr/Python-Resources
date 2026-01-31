### PyPA (Python Packaging Authority)
PyPA is a working group that maintains a core set of software projects used in Python packaging. They are responsible for tools like `pip`, `setuptools`, `wheel`, and `build`, which are essential for packaging, distributing, and installing Python projects.

### Using the `build` Module
Instead of `python setup.py sdist bdist_wheel`, you should use the `build` module to create both source distributions and wheels:

1. **Install the `build` module**:
   ```sh
   pip install build
   ```

2. **Create the Distributions**:
   Navigate to your project directory and run:
   ```sh
   python -m build
   ```

This command will create both the source distribution and the wheel file in the `dist` directory.

### Example Workflow

1. **Create `setup.py`**:
   ```python
   from setuptools import setup, Extension

   example_module = Extension('example', sources=['example.c'])

   setup(
       name='example',
       version='1.0',
       description='Example package with a C extension',
       ext_modules=[example_module],
   )
   ```

2. **Create the Distributions**:
   ```sh
   # inside directory with setup.py and source .c files
   python -m build
   ```

3. **Install the Package Using `pip`**:
   ```sh
   pip install dist/example-1.0.tar.gz  # Source distribution
   # or
   pip install dist/example-1.0-py3-none-any.whl  # Wheel
   ```

By using the `build` module, you align with the current best practices for Python packaging. If you have any more questions or need further assistance, feel free to ask!
