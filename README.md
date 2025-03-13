# Final Project

This project is a web application built with Flask that allows users to register, log in, compose emails, and summarize text.

## Features

- User registration and authentication
- Compose and send emails
- View inbox and sent emails
- Summarize text using a summarizer

## Setup

1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd Final Project
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up the database:
    ```bash
    flask db upgrade
    ```

5. Run the application:
    ```bash
    flask run
    ```

## Usage

- Navigate to `http://127.0.0.1:5000/` to access the application.
- Register a new account or log in with an existing account.
- Use the navigation bar to access different features like composing emails, viewing inbox, and summarizing text.

## License

This project is licensed under the MIT License.

## Install the Requirements

- Install Python 3.10

- Install the Required Libraries
    - (Search the Google to see how to install from requirements.txt)

## To Initialize the DataBase

```bash
set FLASK_APP=run.py
flask db init
flask db migrate
flask db upgrade
```

## Next Things to Add

- Clean up the Front End
- Add more QoL features
- Add AI features
