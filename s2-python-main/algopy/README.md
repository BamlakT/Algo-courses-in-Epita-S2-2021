# `algopy` directory

Contains all "modules" (.py) needed for algo classes

## Utilization

To import the module `xxx.py`

```python
from algopy import xxx
```

- the algopy directory must be in the same directory as the file containing the import
- or the `algopy` directory has to be added to the "PYTHONPATH" variable

### timing.py

To use the `timing` (and `timing_ret`) function, use the following syntax:

```python
from algopy import timing

@timing.timing
def my_function(...):
    ...
```

When calling the function `my_function`, the computing time will be displayed

### matrix.py

To use any function from the `matrix` module, use the following syntax:

```python
from algopy import matrix

Minit = matrix.init(10, 5, 0)

Mload = matrix.load("/home/foo/my_matrix_file.txt")
```
