# [Exspress JS](https://youtu.be/pKJ4GGyDgJo?si=yFdIRcI9j-Iopu57)

## install express js 

```sh
npm i express
```

## Hellow word in express 

search express starter npm 

```js
const express = require("express");
const app = express();

app.get("/",funciton(res,req){
    res.send("Hello World")
});

app.listen(3000)
```

## Routing 

```js

app.get("/",funciton(res,req){
    res.send("Hello World")
});

app.get("/profile",funciton(res,req){
    res.send("Hello profile")
});
```

## middleware

```js
app.use(funciton(res,req,next){
    next();
});
```

## dynamic routing
```js
app.get("/profile:username",funciton(res,req){
    res.send(`Hello ${req.params.username}`)
});
```


## templet Engine (ejs)

1. ejs install
   ```sh
   npm i ejs
   ```

2. configure ejs
   ```js
        app.set("view engine","ejs")
   ```

3. make folder views

4. make ejs file in views folder (index.ejs)
   
5. send ki jagah rander karo
    ```js
    app.get("/profile:username",funciton(res,req){
        res.render("index")
    });
    ```

    dynemic value

    a. add data in render
     ```js
    app.get("/profile:username",funciton(res,req){
        res.render("index",{name:"kaushal"})
    });
    ```

    b. add value in ejs file
    ```ejs
    <h1><%= name %></h1>
    ```

## static file

1. create folder public
2. create folder inside  public >  images,stylesheets,javascripts
3. configure the express static in script.js file
   ```js
   app.use(express.static('./public'))
   ```
4. undestand the path
   

## error handling (gsearch)
1. throw error
   ```js
        throw Error("Err msg")
    ```
2. make error handler with error page and show error
   ```js
    function errorHandler (err, req, res, next) {
        if (res.headersSent) {
            return next(err)
        }
        res.status(500)
        res.render('error', { error: err })
    }
   ```