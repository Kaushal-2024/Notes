# Mocking and patching

**Mocking and patching** are common techniques used in unit testing to isolate the code under test and replace dependencies with controlled, testable versions. These are especially useful when dealing with code that interacts with external systems, databases, or APIs.

Here’s a detailed explanation of **mocking** and **patching** with examples:

---

### **Mocking**
Mocking involves creating fake objects or methods to simulate the behavior of real objects or methods. You can control their behavior to test specific scenarios.

#### Example with ` .mock` in Python:
```python
from unittest.mock import Mock

# Assume we have a function that sends an email
def send_email(to, subject, body):
    # Actual implementation here
    return "Email sent"

# Test function that uses a mock object
def test_send_email():
    # Create a mock object
    mock_send_email = Mock(return_value="Mocked Email sent")

    # Call the mock object
    result = mock_send_email("user@example.com", "Hello", "Test Body")

    # Assertions
    assert result == "Mocked Email sent"
    mock_send_email.assert_called_once_with("user@example.com", "Hello", "Test Body")
```

---

### **Patching**
Patching temporarily replaces a real object with a mock object during a test. The `@patch` decorator or `patch()` context manager is commonly used.

#### Example with `patch` decorator:
```python
from unittest.mock import patch

# Function that sends an email using an external service
def send_email(to, subject, body):
    # Simulates a call to an external service
    return external_email_service.send(to, subject, body)

@patch('path.to.external_email_service')
def test_send_email(mock_service):
    # Mock the behavior of the external service
    mock_service.send.return_value = "Mocked Email sent"

    # Call the function under test
    result = send_email("user@example.com", "Hello", "Test Body")

    # Assertions
    assert result == "Mocked Email sent"
    mock_service.send.assert_called_once_with("user@example.com", "Hello", "Test Body")
```

#### Example with `patch()` context manager:
```python
from unittest.mock import patch

def test_send_email_with_context_manager():
    with patch('path.to.external_email_service') as mock_service:
        # Mock the behavior of the external service
        mock_service.send.return_value = "Mocked Email sent"

        # Call the function under test
        result = send_email("user@example.com", "Hello", "Test Body")

        # Assertions
        assert result == "Mocked Email sent"
        mock_service.send.assert_called_once_with("user@example.com", "Hello", "Test Body")
```

---

### **Key Points**
1. **When to Mock or Patch:**
   - Use mocking for dependencies that are irrelevant to the logic being tested.
   - Use patching when you need to replace specific external methods, modules, or classes.

2. **Behavior Control:**
   - You can specify return values, side effects (e.g., raising exceptions), and more for mock objects.

3. **Assertion:**
   - Assert that mock methods were called with expected arguments using methods like `assert_called_once_with()`.

4. **Best Practices:**
   - Patch objects at their usage point (where they’re imported).
   - Avoid over-mocking, which can make tests fragile and harder to maintain.

5. **Common Libraries for Mocking:**
   - `unittest.mock` (built-in for Python 3.3+)
   - `pytest-mock` for integration with pytest

----

## if you done get it than read below explanation

---

### What is Mocking?

Imagine you’re building a **robot** that tells jokes, but the jokes come from a website. To test your robot, you don’t want it to depend on the real website (what if the website is slow, or your internet goes down?). 

Instead, you create a **fake website** that always sends back the same jokes. This fake website is what we call a **mock**.

---

### What is Patching?

Now, let’s say your robot has a piece of code that connects to the real website. When you’re testing, you want to **replace that code with your fake website** only during the test. That’s what **patching** does! It’s like temporarily swapping out the real website for your fake one.

---

### Example in Python: Robots and Jokes

Let’s say you have this robot:

```python
import requests

def get_joke():
    # This connects to a real joke website
    response = requests.get("https://jokeapi.dev/random")
    return response.json()["joke"]
```

When you call `get_joke()`, it connects to the internet and fetches a joke. But during a test, we don’t want it to go online.

---

### Mocking the Joke Website

We create a fake version of the website that always gives the same joke.

```python
from unittest.mock import Mock

def test_robot_tells_joke():
    # Create a fake version of the website
    fake_website = Mock()
    fake_website.get.return_value.json.return_value = {"joke": "Why did the robot go on a diet? Because it had too many bytes!"}

    # Use the fake website instead of the real one
    joke = fake_website.get().json()["joke"]

    # Check if the joke works
    assert joke == "Why did the robot go on a diet? Because it had too many bytes!"
```

Here:
- `Mock()` is your fake website.
- You tell it what to return when `json()` is called.
- You test the joke without touching the real website.

---

### Patching the Joke Website

Now let’s replace the **real website code** in `get_joke()` with our fake website during the test:

```python
from unittest.mock import patch

@patch("requests.get")  # Replace requests.get with a fake one
def test_robot_tells_joke(mock_get):
    # Set up the fake response
    mock_get.return_value.json.return_value = {"joke": "Why did the robot go on a diet? Because it had too many bytes!"}

    # Call the function under test
    joke = get_joke()

    # Check if the joke works
    assert joke == "Why did the robot go on a diet? Because it had too many bytes!"
```

Here:
- `@patch("requests.get")` temporarily replaces `requests.get` with a fake version.
- You tell the fake version to return your joke.
- When you call `get_joke()`, it uses the fake website instead of the real one.

---

### Why Do This?

1. **Faster Tests:** No need to wait for real websites or servers.
2. **Reliable Tests:** Your test works even if the real website is down.
3. **Controlled Tests:** You can create predictable situations, like testing what happens if the website returns an error.

---

Does that help? Think of mocking and patching as building **fake tools** to test your code without relying on the real world! 🚀

