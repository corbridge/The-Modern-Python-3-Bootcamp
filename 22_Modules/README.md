# 22 - Modules

Why modules? They help keep Python files small, reuse code across multiple files.

## How we import modules?

``` python
import random ## here we import all the random module
import random as rd ## here we import random with a shorter name

```

We can use methods inside modules

```python
rd.randint()
```
We can import individual methods from a module

```python
from random import choice, randint

```
We can import every method inside modules

```python
from random import *
```

## Custom Modules

I have two files 

File: hello.py
```python
def fn():
  return 'do something cool'

def other_fn():
  return 'do something boring'
 
 ```
 
 We can use hello.py on another file
 
 ```python
 import hello
 
 print(hello.fn())
 ```
 
 ## External Modules
 
 To install external modules we can use pip, it can be many variants
 
 ```
 pip instal <external_module>
 ```

 ## The `__name__` variable

 Every module, has its own `__name__` variable, if the file is the main file being run, its value is `__main__`

 if we are running a script, ``__name__`` will be equal to ``__main__``, but if we run in an extern file, it will be equal to the name file.

