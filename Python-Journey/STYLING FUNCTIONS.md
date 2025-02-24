# 🎨 **Python Function Styling Guide** 🐍✨

Writing **clean and readable functions** is crucial for maintaining code that is **easy to understand, debug, and extend**. Follow these best practices to style your Python functions like a **pro!** 🚀

---

## 1️⃣ **Use Descriptive Function Names**

✅ Function names should be **clear and meaningful** so that anyone can understand their purpose **without reading the implementation.**

❌ **Bad:**

```python
def c(a, b):
    return a + b
```

✅ **Good:**

```python
def add_numbers(a, b):
    return a + b
```

✔ Use **snake_case** (`lowercase_with_underscores`) for function names.

---

## 2️⃣ **Follow the PEP 8 Naming Convention**

🐍 **PEP 8 (Python Enhancement Proposal 8)** is the official style guide for Python. It recommends:

|Naming Type|Convention|Example|
|---|---|---|
|Function Names|`snake_case`|`calculate_total()`|
|Private Functions|`_underscore_prefix`|`_hidden_function()`|
|Constants|`UPPERCASE`|`PI = 3.14`|

📌 **Private functions** (used internally within a module) should have an **underscore prefix** `_`.

```python
def _helper_function():
    """This is a private function used internally."""
    pass
```

---

## 3️⃣ **Keep Functions Short and Focused**

✅ A function should **do one thing and do it well**.

- **Limit function length** to ~20-30 lines.
- **Break down complex functions** into smaller, reusable ones.

❌ **Bad:** (Too much in one function)

```python
def process_data(data):
    # Cleaning data
    cleaned_data = [item.strip() for item in data if item]
    
    # Transforming data
    transformed_data = [int(item) for item in cleaned_data if item.isdigit()]
    
    # Printing results
    for item in transformed_data:
        print(item)
```

✅ **Good:** (Divided into smaller functions)

```python
def clean_data(data):
    return [item.strip() for item in data if item]

def transform_data(data):
    return [int(item) for item in data if item.isdigit()]

def print_results(data):
    for item in data:
        print(item)

data = [" 12 ", "hello", " 34 ", " 56 "]
cleaned = clean_data(data)
transformed = transform_data(cleaned)
print_results(transformed)
```

✔ **Easier to read, debug, and reuse.**

---

## 4️⃣ **Use Type Hints for Clarity**

✅ **Type hints** make function parameters and return values **explicit**, improving readability.

```python
def multiply(x: int, y: int) -> int:
    return x * y
```

✔ Now, anyone reading this function **knows** it expects two integers and returns an integer.

---

## 5️⃣ **Use Docstrings to Explain Functions**

✅ **Docstrings** describe what a function does and should be written **inside triple quotes (`"""`)** at the beginning of the function.

```python
def greet(name: str) -> str:
    """Return a greeting message for the given name."""
    return f"Hello, {name}!"
```

✔ This helps **document the function** for yourself and other developers.

### 📌 **Multi-line Docstring Format (PEP 257)**

```python
def calculate_area(radius: float) -> float:
    """
    Calculate the area of a circle.

    Parameters:
    radius (float): The radius of the circle.

    Returns:
    float: The area of the circle.
    """
    return 3.14159 * radius * radius
```

✔ Useful for functions with **multiple parameters**.

---

## 6️⃣ **Use Default Parameter Values Wisely**

✅ **Default parameters** should be **immutable** (`None`, `int`, `str`, `float`, `tuple`).  
❌ **Avoid mutable defaults** like `lists` and `dicts` (causes unexpected behavior).

❌ **Bad:**

```python
def append_item(item, my_list=[]):
    my_list.append(item)
    return my_list
```

📌 **Why is this bad?** The **same list** is used every time the function is called!

✅ **Good:**

```python
def append_item(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list
```

✔ **Creates a new list every time**, avoiding bugs.

---

## 7️⃣ **Return Early to Reduce Nesting**

✅ **Returning early** makes functions easier to read.

❌ **Bad:** (Nested and hard to follow)

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
```

✅ **Good:** (Simplified)

```python
def is_even(number):
    return number % 2 == 0
```

✔ **Less code, same logic.**

---

## 8️⃣ **Use `*args` and `**kwargs` When Needed**

✅ `*args` for multiple positional arguments.  
✅ `**kwargs` for multiple keyword arguments.

```python
def print_numbers(*args):
    """Prints all numbers given as arguments."""
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4)
```

```python
def print_info(**kwargs):
    """Prints key-value pairs."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)
```

✔ **Flexibility in function arguments!**

---

## 9️⃣ **Use List Comprehensions for Simple Loops**

✅ **List comprehensions** make functions cleaner and more efficient.

❌ **Bad:**

```python
def get_even_numbers(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens
```

✅ **Good:**

```python
def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]
```

✔ **Cleaner, more Pythonic!**

---

## 🔟 **Follow Proper Function Ordering**

✅ **Order functions logically** in a script or module.

### 📌 Recommended Order:

1. **Imports**
2. **Global variables/constants**
3. **Helper (private) functions**
4. **Main functions**
5. **Execution (`if __name__ == "__main__":`)**

Example:

```python
import math  # 1. Imports

PI = 3.14  # 2. Constants

def _helper_function():  # 3. Private helper function
    pass

def calculate_circle_area(radius):  # 4. Main function
    return PI * radius * radius

if __name__ == "__main__":  # 5. Execution
    print(calculate_circle_area(5))
```

---

## 🚀 **Final Summary: Function Styling Checklist ✅**

✔ **Use descriptive, `snake_case` function names**  
✔ **Keep functions short and focused** (1 task per function)  
✔ **Use type hints (`x: int, y: float -> str`)**  
✔ **Write docstrings to explain the function**  
✔ **Avoid mutable default arguments (`None` instead of `[]`)**  
✔ **Use early returns to improve readability**  
✔ **Use `*args` and `**kwargs` when flexibility is needed**  
✔ **Prefer list comprehensions for simple operations**  
✔ **Structure functions logically in the script**

---

Now you're styling Python functions like a **pro!** 🎨🐍  
What’s the next function you’re planning to write? 🚀🔥