#  [Day-1](https://youtu.be/dVixA26SbnA?si=djPQip4JZrqHwhFU)

## JS Interview Question

> What is closure and How you define closure ?

#### Parent function retrun fucntion which use parent funcrion variable ,this call closure       

```js
function parent(){
    var a="Parent var";
    
    return function(){
        console.log(a);
    }
}

var ans = parent();
ans();
```

## Web-Dev Change Game 

>Font Metters
#### sarif vs san sarif


## Destructuing Website
<https://www.rejouice.com>
---
---



# [Day-2](https://youtu.be/TuBZp0igUcs?si=mT8Jfh5F05TYbf4C)


## JS Interview Question

> What is null and undefined in js and diffiereence between those?

#### Null means nothing       
#### when we dont assign value then bydedefult it's undefined

```js
var a;
console.log(a); //undefined
```

## Web-Dev Change Game 

>Alignment


## Destructuing Website
<https://www.lifeofabusker.dk/en>

---
---



# [Day-3](https://youtu.be/OQev2qCxxHo?si=Z7w6eJhZvnGDrg1d)


## JS Interview Question

> What is difference between **Event Bubbling** and **Event Capturing**?

Any event ocur in child element(div) if any listener not in child element then call parent listener. 

If parent element not have any listener than it call it's parent listenr.this consept know as event bubbling.

When we any event call in parent listener than also caled it child listener.
this consept know as event Capturing

```js
document.querySelector(".parent").addEventListener("click",function(){
    alert("hello");
},true);
// true allow event capturing

document.querySelector(".child").addEventListener("click",function(){
    alert("hello");
});
```

## Web-Dev Change Game 

>Color


## Destructuing Website
<https://meadlight.com/en>


# [Day-4](https://youtu.be/B9ZLDN-G_X0?si=dlCO8LLFHc6dIEr8)


## JS Interview Question

> What is **use strict**?

It's one kind of mode for code writing in js.

### Difference 

1. Variable declaration
```js
//not Strick mode
a = 10; //work

//Strick mode
"use strick"

var a = 10; //work
b = 20;  // Error
```
2. can't delete the variable
```js
//not Strick mode
a = 10; 
delete a; //not error

//Strick mode
"use strick"

var a=12;
delete a; // Error
```

3. can't make same parameters in functions
```js
//not Strick mode
function doSomthing(a,b,b){

}//not error

//Strick mode
"use strick"

function doSomthing(a,b,b){

}//Error
```

## Web-Dev Change Game 

>**Images**

### Good image sites

<https://unsplash.com/>


## Destructuing Website
<https://simondaufresne.com/>
---
---



# [Day-5](https://youtu.be/nPgvmybIVvM?si=tyq-MDKZCbb-SteQ)


## JS Interview Question

> What is sync and async code in JS?

**Synchronous JavaScript:**
every statement of the code gets executed **one by one**. So, basically a statement has to wait for the earlier statement to get executed.

```js
console.log("1");
console.log("2");
console.log("3");
```

**Asynchronous JavaScript**
Code which excuate after **main stack code excuation**

```js
console.log("1");
setTimeout(function(){
console.log("2");
},0)
console.log("3");


//output : 1 3 2
```

**Callback function:** which function run after some time it's call callaback function.

## Web-Dev Change Game 

>Trends


## Destructuing Website
<https://showcase.refokus.com/>

