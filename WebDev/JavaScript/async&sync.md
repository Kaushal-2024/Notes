# async and sync js
-> sync  = ak ke bad dushra hoga, jub tak ak task complete n ho tab tak 
dusra kam start nahi hoga

-> async =  sare kam ak sath suru kare jisk ans pele aye uska ans de dena

## JavaScript is sync (signal threaded)
-> concept of main stack ans side stack

## Callback ( ek function)
-> callback function tag chalta he jab async code ka completion hota he

`async code likne ke liye`

1. fetch
2. XMLHttpRequest
3. axios
4. promises
5. setTimeout
6. setInterval

`async code ka ans chale ne ke liye`

1. Callbacks
2. fetch then catch
3. async await

## Promises
-> Promise resolve hoga ya reject hoga.
-> ager resolve huva to `then` chalega age reject hoga to `catch` chalega

```js
// user will ask number between 0 to 9 
// if number is below 5 then resolve

var ans = new Promise((res,rej)=>{
    let num = Math.floor(Math.random * 10)

    if( num < 5)
    {
        return res();
    }else{
        return rej();
    }
})

ans.then(function(){
    console.log("Below")
})
.catch(function(){
    console.log("above")
})

```
-> Explore Promise chaining, waterfall and all


## async & await
-> jo code async he useke function ke age async lagdao

-> aur jo task async he uske age await lagado 

-> it help to reduce the code compare to promises 


# mysql pacakge

You can use `async/await` with the `mysql` package in Node.js to write asynchronous code that interacts with your MySQL database. Here's an example of how you can do this:

First, make sure you have the `mysql` package installed in your Node.js project. You can install it using npm:

```bash
npm install mysql
```

Next, create a new JavaScript file (let's call it `db.js` for this example) where you'll write your database operations.

### Example using `async/await` with `mysql`

Here is an example of using `async/await` with the `mysql` package:

```javascript
// Import the mysql package
const mysql = require('mysql');

// Create a connection to the database
const connection = mysql.createConnection({
  host: 'your_database_host',
  user: 'your_database_user',
  password: 'your_database_password',
  database: 'your_database_name',
});

// Connect to the database
connection.connect((error) => {
  if (error) {
    console.error('Error connecting to database: ' + error.stack);
    return;
  }
  console.log('Connected to database as ID ' + connection.threadId);
});

// Example function to get users from the database using async/await
const getUsers = async () => {
  return new Promise((resolve, reject) => {
    const query = 'SELECT * FROM users';
    connection.query(query, (error, results) => {
      if (error) {
        reject(error);
      } else {
        resolve(results);
      }
    });
  });
};

// Example usage of async/await to get users
const fetchUsers = async () => {
  try {
    const users = await getUsers();
    console.log('Users:', users);
  } catch (error) {
    console.error('Error fetching users:', error);
  } finally {
    connection.end(); // Close the database connection
  }
};

// Call the function to fetch users
fetchUsers();
```

In this example:

1. We create a connection to the MySQL database using `mysql.createConnection()`.
2. We define an `async` function `getUsers` that returns a Promise. Inside this function, we run a SQL query to fetch all users from a `users` table.
3. We define another `async` function `fetchUsers` that uses `await` to call `getUsers` and then logs the results.
4. Finally, we call `fetchUsers` to execute the database query and fetch the users.

Remember to replace `'your_database_host'`, `'your_database_user'`, `'your_database_password'`, and `'your_database_name'` with your actual database credentials.

This is a basic example to get you started. You can expand on this pattern to perform various CRUD operations or more complex database interactions using `async/await` with the `mysql` package in Node.js.