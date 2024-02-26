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

app.get("/",funciton(req,res){
    res.send("Hello World")
});

app.listen(3000)
```

## Routing

```js

app.get("/",funciton(req,res){
    res.send("Hello World")
});

app.get("/profile",funciton(req,res){
    res.send("Hello profile")
});
```

## middleware

req se pasele middleware run hoga

```js
app.use(funciton(req,res,next){
    console.log("first middleware")
    next();  // go to second miallware
});

app.use(funciton(req,res,next){
    console.log("second middleware")
    next(); // got to request
});
```

## dynamic routing

```js
app.get("/profile:username",funciton(req,res){
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
   app.set("view engine", "ejs");
   ```

3. make folder views

4. make ejs file in views folder (index.ejs)
5. send ki jagah rander karo

   ```js
   app.get("/profile:username",funciton(req,res){
       res.render("index")
   });
   ```

   dynemic value

   a. add data in render

   ```js
   app.get("/profile:username",funciton(req,res){
      res.render("index",{name:"kaushal"})
   });
   ```

   b. add value in ejs file

   ```ejs
   <h1><%= name %></h1>
   ```

## static file

1. create folder public
2. create folder inside public > images,stylesheets,javascripts
3. configure the express static in script.js file
   ```js
   app.use(express.static("./public"));
   ```
4. undestand the path

## error handling (gsearch)

1. throw error
   ```js
   throw Error("Err msg");
   ```
2. make error handler with error page and show error

   ```js
   app.get("/error", (req, res, next) => {
     throw Error("Error ai he error ay hi he");
   });

   app.use(function errorHandler(err, req, res, next) {
     if (res.headersSent) {
       return next(err);
     }
     res.status(500);
     res.render("error", { error: err });
   });
   ```

## Do All above thing using express generator

give project structure

1.  install globally

    ```sh
    npm i express-generator -g
    ```

2.  create new app

    ```sh
    express appname --view=ejs
    ```

3.  Use 2 coomands
    ```sh
    cd appname
    npm i
    ```
4.  Open it on vs code
    ```sh
    code .
    ```
5.  Explore project

## Flase Messages (like alerts)

flash message allow you to user data in route which create in other route

for use coonect-flash must use express sessions

1. install connect-flash pkg and express-session ppkg

   ```sh
    npm i connect-flash
    npm i exrpress-session
   ```

2. setup session
3. put connect-flash in app.use function
   app.use(flash())

4. create flash in route
   ```js
   req.flash("age", 12);
   ```
5. uer flash in other route
   ```js
   req.flash("age");
   ```
