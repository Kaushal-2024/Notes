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

