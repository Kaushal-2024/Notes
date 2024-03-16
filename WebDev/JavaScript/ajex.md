### AJAX in JavaScript

AJAX (Asynchronous JavaScript And XML) is a technique for creating fast and dynamic web pages. It allows you to update parts of a web page without reloading the whole page. Here's how you can make GET and POST requests using AJAX with vanilla JavaScript:

### Key Points:

1. **GET Request:**
    - Used for retrieving data from a server.
    - The `XMLHttpRequest` object is used.
    - Here's a sample code snippet for a GET request:

    ```js
    let fetchBtn = document.getElementById('fetchBtn');
    fetchBtn.addEventListener('click', buttonClickHandler);

    function buttonClickHandler() {
        console.log('You have clicked the fetchBtn');
        
        // Create a new XMLHttpRequest object
        const xhr = new XMLHttpRequest();
        
        // Specify the type of request and the URL
        xhr.open('GET', '/endPoint-OR-File', true);
        
        // Optional: What to do on progress
        xhr.onprogress = function() {
            console.log('On progress');
        };
        
        // What to do when the response is ready
        xhr.onload = function() {
            if (this.status === 200) {
                console.log(this.responseText);
            } else {
                console.log("Some error occurred");
            }
        };
        
        // Send the request
        xhr.send();
    }
    ```

2. **POST Request:**
    - Used for sending data to a server to create/update a resource.
    - Here's a sample code snippet for a POST request:

    ```js
    let fetchBtn = document.getElementById('fetchBtn');
    fetchBtn.addEventListener('click', buttonClickHandler);

    function buttonClickHandler() {
        console.log('You have clicked the fetchBtn');
        
        // Create a new XMLHttpRequest object
        const xhr = new XMLHttpRequest();
        
        // Specify the type of request, the URL, and set request headers
        xhr.open('POST', 'http://dummy-restapiexample.com/api/v1/create', true);
        xhr.setRequestHeader('Content-type', 'application/json');
        
        // Optional: What to do on progress
        xhr.onprogress = function() {
            console.log('On progress');
        };
        
        // What to do when the response is ready
        xhr.onload = function() {
            if (this.status === 200) {
                console.log(this.responseText);
            } else {
                console.log("Some error occurred");
            }
        };
        
        // Create the data to send as JSON
        let params = JSON.stringify({
            name: "test34sad545",
            salary: "123",
            age: "23"
        });
        
        // Send the request with the data
        xhr.send(params);
    }
    ```

3. **Key Points to Note:**
    - Use `XMLHttpRequest` object to make AJAX requests.
    - For POST requests, set the `Content-type` header to `'application/json'`.
    - Use `xhr.open()` to specify the type of request (`GET` or `POST`) and the URL.
    - Set up event listeners for `xhr.onload` to handle the response.
    - `xhr.send()` is used to send the request to the server.
    - Always check the `status` property of `xhr` to ensure the request was successful.

By following these steps, you can implement AJAX requests in your JavaScript code to create dynamic and responsive web applications.