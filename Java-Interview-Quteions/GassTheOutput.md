# 1. Integer caching mechanism

```java
class Demo{
    public static void main(String args[]){
        Integer num1 = 100;
        Integer num2 = 100; //  // -128 and 127        
        Integer num3 = 500; 
        Integer num4 = 500;

        if( num1 == num2){
            System.out.println("num1 == num2");
        }else{
            System.out.println("num1 != num2");
        }


        if( num3 == num4){
            System.out.println("num3 == num4");
        }else{
            System.out.println("num3 != num4");
        }
    }
}
/*
Output :
num1 == num2
num3 != num4
*/
```

## Explantion 

* num1 and num2 both have the value 100, and because of Integer caching in Java for values between -128 and 127, the references num1 and num2 will point to the same Integer object. Therefore, the first if statement (num1 == num2) evaluates to true, and "num1 == num2" is printed.

* num3 and num4 both have the value 500. In this case, the Integer caching mechanism does not apply, and separate Integer objects are created for num3 and num4. As a result, the second if statement (num3 == num4) evaluates to false, and "num3 != num4" is printed.


In Java, the Integer caching mechanism is an optimization introduced to reduce memory usage and improve performance for frequently used integers. The Java Integer class caches values in the range of -128 to 127. When you create an Integer object with a value within this range, Java checks if an Integer object with that value already exists in the cache. If it does, the existing object is reused rather than creating a new one.

**Here's a breakdown of how the Integer caching mechanism works:**

1. **Initialization:** When the Java Virtual Machine (JVM) starts, it creates Integer objects for values in the range -128 to 127 and caches them.

2. **Creation of Integer objects:** When you use the Integer.valueOf(int) method or auto-boxing to create an Integer object with a value within the cached range, the JVM checks if an object with that value is already in the cache.

3. **Reuse of cached objects:** If an Integer object with the specified value is found in the cache, the existing object is reused instead of creating a new one. This is possible because Integer objects are immutable.

4. **Outside the cached range:** If the value is outside the cached range, a new Integer object is created without reusing an existing one.

---
---


# 2. 

```java
class Demo{
    public static void main(String args[]){
        System.out.println(2 + 3);
        System.out.println("str" + "ing");
        System.out.println(2 + "string");
        System.out.println("string" + 3);
        System.out.println(2 + 3 + "string");
        System.out.println("string" + 2 + 3);
        
    }
}
/*
Output :
5
string

2string
string3

5string
string23
*/
```
---
---
# 3.

```java
class Demo {
    public static void main(String[] args) {
        char ch = '1';
        System.out.println(ch++ + ++ch);
    }
}
/*
Output :
100
*/
```

