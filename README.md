# ats
This is a project demonstrating a candidate ATS System that is capable of adding, deleting and updating and searching of candidates

# prerequisities
Make sure you have python version as 'Python 3.13.1'. You can check by using this command:
on mac/linux
```
    python3 --version 
```

OR 

on windows
```
    python --version 
```

# Running The Project

1. **Create a Virtual Environment**

    On mac/linux:
    ```bash
    python3 -m venv <name of your env>
    ```

    OR on Windows:
    ```bash
    py -m venv <name of your env>
    ```

2. **Activate the Virtual Environment**

    On mac/linux:
    ```bash
    source <name of your env>/bin/activate
    ```

    On Windows:
    ```bash
    <name of your env>\Scripts\activate
    ```

3. **Install the requirements from `requirements.txt`**

    ```bash
    pip install -r requirements.txt
    ```

4. **Prepare an `.env` file with the help of `test.env`**

    ```bash
    cp test.env .env
    ```

    (Modify `.env` file with the necessary environment variables as required.)

5. **Run all the migrations**

    ```bash
    python manage.py migrate
    ```

6. **Run the project in development mode**

    ```bash
    python manage.py runserver
    ```

    The application will now be running on `http://127.0.0.1:8000/`.


## Viewing API Endpoints with Swagger

This project uses **Swagger** for API documentation. You can easily view and interact with all the available API endpoints via the Swagger UI.

### How to Access Swagger Documentation:

1. **Make sure the development server is running**
   ```bash
   python manage.py runserver
   ```

2. **Open Your Website Url and Navigate to swagger**
    ```bash
    https://<your-web-address>/swagger/
    ```

### How to Run The Tests:

1. **Make sure You're in Project Root Directory**
   ```bash
   cd <path-to-project-root-directory>
   ```

2. **Run The Tests Using the Following Command**
    ```bash
    pytest
    ```

3. **To View The Test Cases, Go to Tests Directory in the App**
    ```bash
    cd candidate/tests
    ```   
