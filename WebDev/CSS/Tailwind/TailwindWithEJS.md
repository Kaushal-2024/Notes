To integrate Tailwind CSS with a Node.js project using EJS (Embedded JavaScript templates), you'll need to follow these steps:

### Step 1: Set Up a Node.js Project

If you haven't already created a Node.js project, you can create a new project directory and initialize it with npm.

```bash
mkdir my-project
cd my-project
npm init -y
```

### Step 2: Install Tailwind CSS

You need to install Tailwind CSS and its dependencies. For this, you'll also need to install `postcss` and `autoprefixer`:

```bash
npm install tailwindcss postcss autoprefixer
```

### Step 3: Create Tailwind CSS Configuration

Create a `tailwind.config.js` file in the root of your project to configure Tailwind. You can generate a basic configuration file by running:

```bash
npx tailwindcss init
```

### Step 4: Create PostCSS Configuration

Create a `postcss.config.js` file in the root of your project:

```javascript
module.exports = {
  plugins: [
    require('tailwindcss'),
    require('autoprefixer'),
  ],
};
```

### Step 5: Create a CSS File

Create a CSS file (for example, `src/styles.css`) where you will include Tailwind CSS:

```css
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';
```

### Step 6: Include CSS in EJS Template

In your EJS templates (for example, `views/index.ejs`), include the CSS file you created:

```html
<!DOCTYPE html>
<html>
<head>
  <title>My Node.js App</title>
  <link href="/styles.css" rel="stylesheet">
</head>
<body>
  <!-- Your HTML content here -->
</body>
</html>
```

### Step 7: Set Up Build Script

In your `package.json` file, add a script to build your CSS file:

```json
"scripts": {
  "build:css": "postcss src/styles.css -o public/styles.css"
}
```

### Step 8: Build Tailwind CSS

Now, you can build your Tailwind CSS file by running the build script:

```bash
npm run build:css
```

This will generate a `public/styles.css` file that includes the compiled Tailwind CSS.

### Step 9: Set Up Express.js

If you're using Express.js for your Node.js server, you'll need to serve static files. Here's a basic example:

```javascript
const express = require('express');
const app = express();

// Serve static files from the 'public' folder
app.use(express.static('public'));

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
  res.render('index');
});

app.listen(3000, () => {
  console.log('Server is running on http://localhost:3000');
});
```

### Step 10: Start Your Node.js App

Start your Node.js app:

```bash
node app.js
```

Now you should be able to visit `http://localhost:3000` in your browser and see your EJS template rendered with Tailwind CSS styles applied.

That's it! You've now integrated Tailwind CSS with your Node.js EJS project. You can now use Tailwind CSS utility classes in your EJS templates to style your HTML elements.