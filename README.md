# Final Year Project

## Project Description

This project is a comprehensive web application designed to streamline various tasks and improve user experience through a clean and intuitive interface. The backend is powered by Flask, a lightweight WSGI web application framework in Python, which ensures robust and scalable performance. The frontend is designed to be user-friendly and responsive, making it accessible across different devices. The application also integrates AI features to enhance functionality and provide intelligent insights.

The project aims to solve common problems faced by users in managing their tasks efficiently. By leveraging modern web technologies and AI, the application provides a seamless experience that adapts to user needs. Key features include task automation, personalized recommendations, and real-time data analysis.

## Advantages of the Project

- **User-Friendly Interface**: The application features a clean and intuitive interface that enhances user experience.
- **Scalability**: Built with Flask, the application is highly scalable and can handle increasing loads efficiently.
- **AI Integration**: Incorporates AI features to provide intelligent insights and automate tasks.
- **Cross-Device Compatibility**: The responsive design ensures accessibility across various devices.
- **Extensibility**: The modular architecture allows for easy addition of new features and functionalities.

## Major Libraries Used

- **Flask**: A lightweight WSGI web application framework in Python that provides the core functionality for the backend.
- **SQLAlchemy**: An SQL toolkit and Object-Relational Mapping (ORM) library for Python, used for database interactions.
- **Flask-Migrate**: Handles SQLAlchemy database migrations for Flask applications using Alembic.
- **Flask-Login**: Provides user session management for Flask applications.
- **TensorFlow/PyTorch**: Used for implementing AI features and machine learning models.
- **Transformers**: A library by Hugging Face that provides state-of-the-art general-purpose architectures for natural language understanding and generation.

## Transformer Library and Model

The project utilizes the Transformers library by Hugging Face, which provides a wide range of pre-trained models for various natural language processing tasks. The specific model used in this project is the BERT (Bidirectional Encoder Representations from Transformers) model. BERT is designed to understand the context of a word in search queries, making it highly effective for tasks such as text classification, sentiment analysis, and question answering.

## Tech Stack Used

The project utilizes a modern tech stack to ensure high performance, scalability, and maintainability. The key components of the tech stack include:

- **Frontend**:
  - **HTML/CSS**: For structuring and styling the web pages.
  - **JavaScript**: For adding interactivity to the web pages.
  - **React**: A JavaScript library for building user interfaces, ensuring a responsive and dynamic frontend.

- **Backend**:
  - **Python**: The primary programming language used for backend development.
  - **Flask**: A lightweight WSGI web application framework for building the backend services.
  - **SQLAlchemy**: An ORM library for database interactions.
  - **Flask-Migrate**: For handling database migrations.
  - **Flask-Login**: For managing user sessions and authentication.

- **Database**:
  - **SQLite**: A lightweight, disk-based database used for storing and managing data.

- **AI/ML**:
  - **TensorFlow/PyTorch**: Libraries used for implementing AI features and machine learning models.
  - **Transformers**: A library by Hugging Face for natural language processing tasks.

- **Version Control**:
  - **Git**: For version control and collaboration.
  - **GitHub**: For hosting the repository and managing project collaboration.

## Install the Requirements

- Install Python 3.10 from the official [Python website](https://www.python.org/downloads/).
- Clone the repository:
    ```
    git clone <repository-url>
    ```
- Navigate to the project directory:
    ```
    cd <project-directory>
    ```
- Create a virtual environment:
    ```
    python -m venv venv
    ```
- Activate the virtual environment:
    - On Windows:
        ```
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```
        source venv/bin/activate
        ```
- Install the required libraries:
    ```
    pip install -r requirements.txt
    ```

## To Initialize the Database

```
set FLASK_APP=run.py
flask db init
flask db migrate
flask db upgrade
```

## Next Things to Add

- Migerate to PostreSQL
- Clean up the front end
- Add more QoL features
- Add AI features
- Implement user authentication and authorization
- Optimize database queries for better performance
- Add comprehensive unit and integration tests
