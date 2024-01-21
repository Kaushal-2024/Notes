# [3. Prarambh](https://www.youtube.com/live/v5UM825ah08?si=FA13OIg-oH4b-VI6)

## 1. Snapping native
make child divs center with scorlling 

## 2. JS Quetion
ek object hai and usmein kuchh properties ho sakti hai aur we object blank bhi ho sakta hai, aapke us
object ki name property ko touch karna hai jo ki again ek object ho sakti hai aur uske andar aapko first
naam ki property ko access karna hai, aisa code likhive ki type error naa gave kisi bhi case mein

> es11 2020 optinal chaining

```js
    var obj = {}
    console.log(obj.name.first) // give type error

    console.log(obj?.name?.first) // optinal chaining don't give error
```    
## 3. nullish coalescing operator - ?? (es11)

this operaator check it's first oprand if it's null or undefinde then it return second oprand otherwise it's return first oprand

```js
    var ab = null ?? 123 // ab = 123
    var cd = 12 ?? 1555 // cd = 12
```

Usecase : ek object hai uski name property nikaalo aur agar name naa ho to name ko de

```js
    var obj = {};
    vat username = obj?.name?.first ?? defaultName
```