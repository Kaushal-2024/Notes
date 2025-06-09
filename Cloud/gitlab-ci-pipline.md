### GitLab CI Pipeline Jobs

---


#### **Pipeline Overview**
This pipeline is designed to ensure:
1. **Code Quality**: Static analysis tools check for code style, type correctness, and security issues.
2. **Code Formatting**: Ensures consistent formatting across the codebase.
3. **Security**: Identifies potential security vulnerabilities.

---

#### **1. Stages**
- **test**:
  - Executes all testing, static analysis, and security scanning.
- **format**:
  - Validates the code formatting.

---

#### **2. Jobs**
- **`before_script`**:
  - Sets up the environment, installs dependencies, and starts a Flask server on port `1111`.
  - Ensures the server process is terminated after the CI job ends.

- **`job_test`**:
  - Runs automated tests using `nose2`.

  **Script Details**:
  ```bash
  nose2 -v  # Executes tests with verbose output
  ```

- **`format_code`**:
  - Verifies code formatting with `black`.

  **Script Details**:
  ```bash
  black --check .  # Checks code format without modifying files
  ```

- **`lint`**:
  - Lints the code with `flake8` to ensure compliance with PEP 8 and detect common errors.

  **Script Details**:
  ```bash
  flake8 .  # Recursively lints all Python files
  ```

- **`pylint`**:
  - Runs `pylint` to perform a deeper code quality analysis.

  **Script Details**:
  ```bash
  pylint app.py tests/  # Analyzes both app and tests for coding issues
  ```

- **`type_check`**:
  - Validates type hints using `mypy`.

  **Script Details**:
  ```bash
  mypy app.py tests/  # Ensures type annotations are correct
  ```

- **`security_scanning`**:
  - Analyzes the codebase for security vulnerabilities using `Bandit`.

  **Script Details**:
  ```bash
  bandit -r app.py tests/  # Recursively scans app and tests for security issues
  ```

---

#### **3. Key Points**
- **Tools Used**:
  - **Black**: Enforces consistent code formatting.
  - **Flake8**: Checks for PEP 8 violations and other common errors.
  - **Pylint**: Performs comprehensive static code analysis.
  - **Mypy**: Validates type annotations for correctness.
  - **Bandit**: Identifies potential security issues in Python code.

- **Triggers**:
  - Jobs are triggered on `merge_requests` and `main` branch updates to ensure quality before merging.


---
---



 `.gitlab-ci.yml`
```yaml
image: python:3.9

stages:
  - test
  - format

before_script:
  - python --version ; pip --version  # For debugging
  - pip install virtualenv
  - virtualenv venv
  - source venv/bin/activate
  - pip install -r requirements.txt
  - flask run --port=1111 &
  - SERVER_PID=$!
  - trap "kill $SERVER_PID" EXIT

job_test:
  stage: test
  script:
    - echo "Running tests with nose2..."
    - nose2 -v

format_code:
  stage: format
  script:
    - echo "Installing black..."
    - pip install black
    - echo "Checking code formatting with black..."
    - black --check .
  only:
    - merge_requests
    - main

lint:
  stage: test
  script:
    - echo "Installing flake8..."
    - pip install flake8
    - echo "Linting code with flake8..."
    - flake8 .

pylint:
  stage: test
  script:
    - echo "Installing pylint..."
    - pip install pylint
    - echo "Running pylint on app.py and tests..."
    - pylint app.py tests/

type_check:
  stage: test
  script:
    - echo "Installing mypy..."
    - pip install mypy
    - echo "Running type checking with mypy..."
    - mypy app.py tests/

security_scanning:
  stage: test
  script:
    - echo "Installing Bandit for security scanning..."
    - pip install bandit
    - echo "Running Bandit for security analysis..."
    - bandit -r app.py tests/

```