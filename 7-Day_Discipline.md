- [Day-1](#day-1)
  - [JS Interview Question](#js-interview-question)
      - [Parent function retrun fucntion which use parent funcrion variable ,this call closure](#parent-function-retrun-fucntion-which-use-parent-funcrion-variable-this-call-closure)
  - [Web-Dev Change Game](#web-dev-change-game)
      - [sarif vs san sarif](#sarif-vs-san-sarif)
  - [Destructuing Website](#destructuing-website)
  - [https://www.rejouice.com](#httpswwwrejouicecom)
- [Day-2](#day-2)
  - [JS Interview Question](#js-interview-question-1)
      - [Null means nothing](#null-means-nothing)
      - [when we dont assign value then bydedefult it's undefined](#when-we-dont-assign-value-then-bydedefult-its-undefined)
  - [Web-Dev Change Game](#web-dev-change-game-1)
  - [Destructuing Website](#destructuing-website-1)
- [Day-3](#day-3)
  - [JS Interview Question](#js-interview-question-2)
  - [Web-Dev Change Game](#web-dev-change-game-2)
  - [Destructuing Website](#destructuing-website-2)
- [Day-4](#day-4)
  - [JS Interview Question](#js-interview-question-3)
    - [Difference](#difference)
  - [Web-Dev Change Game](#web-dev-change-game-3)
    - [Good image sites](#good-image-sites)
  - [Destructuing Website](#destructuing-website-3)
  - [https://simondaufresne.com/](#httpssimondaufresnecom)
- [Day-5](#day-5)
  - [JS Interview Question](#js-interview-question-4)
  - [Web-Dev Change Game](#web-dev-change-game-4)
  - [Destructuing Website](#destructuing-website-4)
  - [https://showcase.refokus.com/](#httpsshowcaserefokuscom)
- [Day-6](#day-6)
  - [JS Interview Question](#js-interview-question-5)
  - [Web-Dev Change Game](#web-dev-change-game-5)
  - [Destructuing Website](#destructuing-website-5)
  - [https://wonderland.studio/](#httpswonderlandstudio)
- [Mind Blowing website design](#mind-blowing-website-design)


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
---
---

# [Day-6](https://youtu.be/K9lVnav2Gec?si=IyddeeqVz12js7Ov)


## JS Interview Question

> What is EventLoop JS?

The event loop is essentially a loop that runs continuously and checks for tasks that are waiting to be executed. These tasks are added to a queue, and the event loop runs through the queue, executing each task in order. 

An event loop is a key mechanism in JavaScript that allows the program to handle multiple events and processes them efficiently. 

It is responsible for managing the call stack, event handling, and garbage collection. While JavaScript is single-threaded, meaning it can only execute one function at a time, **the event loop allows it to handle multiple asynchronous events simultaneously.**

This makes JavaScript able to handle activities such as user input, network requests, and animations without blocking the main thread of execution.

## Web-Dev Change Game 

>Design sence


## Destructuing Website
<https://wonderland.studio/>
---
---



# Mind Blowing website design

<https://www.awwwards.com/>


<https://historical.nissan.slava.digital/>

<https://web3-mugler.hello-jury.com/>

<https://www.jeanpaulgaultier.com/ww/en/fragrances/le-male-elixir>

<https://www.oculus.com/medal-of-honor/>

<https://bruno-simon.com/>

<https://www.puma-campaigns.com/velocity-2-aw/>

