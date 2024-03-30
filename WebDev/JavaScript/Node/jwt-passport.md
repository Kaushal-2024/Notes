# Login With JWt Passport with ejs and MySQL


### Step 1: Setting Up Your Project

Follow the same steps as before to set up your project structure and install the necessary packages.

### Step 2: Refactoring into MVC

Create the following directory structure for your project:

```
- node-jwt-auth
  - controllers
    - authController.js
    - dashboardController.js
  - models
    - userModel.js
  - views
    - login.ejs
    - dashboard.ejs
  - routes
    - index.js
  - app.js
```

#### models/userModel.js

Define the `userModel` for interacting with the `users` table:

```javascript
const db = require('../db');

const userModel = {
  findByUsername: function (username, callback) {
    db.query('SELECT * FROM users WHERE username = ?', [username], callback);
  }
};

module.exports = userModel;
```

#### controllers/authController.js

Create the `authController` to handle user authentication:

```javascript
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const userModel = require('../models/userModel');

const authController = {
  login: async function (req, res) {
    const { username, password } = req.body;

    try {
      const [user] = await userModel.findByUsername(username);

      if (!user) {
        return res.status(401).send('Invalid username or password');
      }

      const validPassword = await bcrypt.compare(password, user.password);

      if (!validPassword) {
        return res.status(401).send('Invalid username or password');
      }

      const token = jwt.sign({ id: user.id, username: user.username }, 'your_jwt_secret', { expiresIn: '1h' });
      res.status(200).json({ token });
    } catch (error) {
      console.error(error);
      res.status(500).send('Internal Server Error');
    }
  }
};

module.exports = authController;
```

#### controllers/dashboardController.js

Create the `dashboardController` to handle dashboard related logic:

```javascript
const dashboardController = {
  showDashboard: function (req, res) {
    res.render('dashboard', { user: req.user });
  }
};

module.exports = dashboardController;
```

#### routes/index.js

Set up the routes using Express Router:

```javascript
const express = require('express');
const router = express.Router();
const authController = require('../controllers/authController');
const dashboardController = require('../controllers/dashboardController');
const passport = require('passport');

router.get('/', (req, res) => {
  res.render('login');
});

router.post('/login', authController.login);

router.get('/dashboard', passport.authenticate('local', { session: false }), dashboardController.showDashboard);

module.exports = router;
```

#### app.js

Modify the `app.js` file to use the MVC structure and set up the Express app:

```javascript
const express = require('express');
const session = require('express-session');
const passport = require('passport');
const db = require('./db');
const routes = require('./routes');
const path = require('path');

const app = express();
const port = 3000;

// MySQL connection
db.connect((err) => {
  if (err) throw err;
  console.log('Connected to MySQL database');
});

// Middleware
app.use(express.urlencoded({ extended: false }));
app.use(express.json());
app.use(session({
  secret: 'secret',
  resave: true,
  saveUninitialized: true
}));
app.use(passport.initialize());
app.use(passport.session());
app.use(express.static(path.join(__dirname, 'public')));

// EJS
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Routes
app.use('/', routes);

app.listen(port, () => {
  console.log(`Server running on http://localhost:${port}`);
});
```

### Step 3: Running the Application

Start your application:

```bash
node app.js
```

Visit `http://localhost:3000` in your web browser to see the login form. You can then fill in the credentials, and upon successful login, you'll be redirected to the dashboard.

This refactoring separates concerns into different files:

- **Models**: Responsible for interacting with the database.
- **Controllers**: Handle the application logic.
- **Views**: Display the data and receive user input.

This makes the code more organized, easier to read, and maintainable. Remember to replace `'your_jwt_secret'` with your actual JWT secret key for production use.