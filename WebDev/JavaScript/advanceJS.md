# [Advance Js](https://youtu.be/EgDmCbhmstU?si=A_hV82HSG1WyX6KQ)

## 1. let var const
a. var old js me tha (ES5) and let const new js(ES6) me he
b. var function scope hota he  and let braces scope hota he
c. var add itself to the `windows` object and let does not add

## 2. stack and heap memory
basically heaps use for store variables values

## 3. Execution context  
ec is a container where thr function is executed and it's create when function is called.

Ec contain(3 things)  variable ,function and lexical environment(Function kiya access kar sakte he or kiya nahi)

## 4. How to copy reference values

```js
var a = [3,4,5,6]
var b  = [...a]
```

## 5. truthy and falsy
In js anything divined in to category truthy and falsy

Falsy : 0 false undefined null NaN document.all
trury  : all things (without falsy)


## 6. forEach loop

## 7. for in an for of loop 


## 8. Callback function
 

## 9. First class function
-> Function as value and store in variable call first class function
-> in js all function are first class function
```js
function abcd(a){
    a();
}

abcd(function (){ console.log(" Hello First function")})
```

## 10. Array in JS is object
-> JS convert array in to object
```js
let arr = [3,5,667,7]

// js covert  like this
arr = {
    0 : 3,
    1 : 5,
    2 : 667,
    3 : 7
}

// try this in js and other lang
arr[-1] = 345;

Array.isArray([])  // true
Array.isArray({})  // False

```

## 11. How to delete obj prop

```js
let obj = {
    name : "Developer",
    age : 21
}

delete obj.age
```
