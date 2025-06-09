# MRO in python

MRO in Python stands for **Method Resolution Order**. It is the order in which Python looks for a method or attribute in a class hierarchy when it is accessed.

When you call a method or access an attribute, Python follows the MRO to determine where to look first. This is especially important in the context of multiple inheritance, where a class is derived from more than one parent class.

### Key Points About MRO:
1. **Linearization of Classes**: 
   - Python computes a linear sequence (called the MRO) that determines the order of method lookups.
   - It ensures a consistent and predictable way of resolving methods in the presence of multiple inheritance.

2. **Algorithm**: 
   - Python uses the **C3 Linearization Algorithm** to compute the MRO.
   - This algorithm ensures that:
     - A class appears before its parent classes in the MRO.
     - The order respects the order in which classes are specified in the inheritance list.

3. **How to View the MRO**:
   - Use the `__mro__` attribute or the `mro()` method of a class to view its MRO:
     ```python
     class A: pass
     class B(A): pass
     class C(B): pass
     
     print(C.__mro__)
     # Output: (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)

     print(C.mro())
     # Output: [<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>]
     ```

4. **Example of Multiple Inheritance**:
   ```python
   class A:
       def show(self):
           print("A")

   class B(A):
       def show(self):
           print("B")

   class C(A):
       def show(self):
           print("C")

   class D(B, C):
       pass

   d = D()
   d.show()
   # Output: B
   # The MRO is: D -> B -> C -> A -> object
   ```

   In this case, Python first looks for the `show` method in `D`, then in `B`, and so on according to the MRO.

5. **Conflict Resolution**:
   The MRO resolves conflicts that arise from multiple inheritance by following the C3 Linearization rules.

MRO ensures a deterministic lookup for methods and attributes, which is crucial for maintaining consistency and avoiding ambiguity in object-oriented programming.


---

### **MRO (Method Resolution Order)** is not only useful for multiple inheritance.
It is applicable and significant even in **single inheritance** scenarios or with the base `object` class. Here's why:

### 1. **Single Inheritance Scenarios**
   Even in single inheritance, MRO ensures the correct resolution of methods and attributes along the class hierarchy.

   Example:
   ```python
   class A:
       def show(self):
           print("A")

   class B(A):
       pass

   b = B()
   b.show()
   # Output: A
   ```

   In this example, the MRO determines that `show` is found in class `A`. Without MRO, Python wouldn't know where to look for the method in complex hierarchies.

---

### 2. **Integration with the `object` Class**
   - In Python, all classes (new-style classes) implicitly inherit from `object`, making MRO relevant for understanding how methods like `__init__`, `__str__`, etc., are resolved.
   - Even with a single class, Python computes the MRO to ensure that the `object` class is accounted for.

   Example:
   ```python
   class A:
       pass

   print(A.__mro__)
   # Output: (<class '__main__.A'>, <class 'object'>)
   ```

---

### 3. **Super() in Single Inheritance**
   - The `super()` function relies on the MRO to delegate calls to parent classes.
   - This is true even in single inheritance.

   Example:
   ```python
   class A:
       def show(self):
           print("A")

   class B(A):
       def show(self):
           print("B")
           super().show()

   b = B()
   b.show()
   # Output:
   # B
   # A
   ```

   Here, `super().show()` follows the MRO to call the `show` method of `A`.

---

### 4. **Diamond Problem Prevention**
   While the importance of MRO is more pronounced in multiple inheritance (e.g., the diamond problem), it provides consistency and predictability across all class hierarchies.

---

### In Summary
MRO is always computed and used by Python, whether for single or multiple inheritance. While its importance is most apparent in resolving ambiguities in multiple inheritance, it also plays a role in single inheritance by ensuring method resolution consistency and proper integration with the base `object` class.