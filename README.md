# AI Email Client

## Project Description

AI Email Client is a modern web application that combines traditional email functionality with artificial intelligence to enhance email management and productivity. Built with Flask and powered by state-of-the-art AI models, this application provides an intuitive interface for managing emails while offering smart features like email summarization and categorization.

## Key Features

- **AI-Powered Email Summarization**: Automatically generate concise summaries of long emails using advanced NLP models
- **Smart Email Categorization**: Emails are automatically categorized into General, Work, Personal, and Important
- **Modern User Interface**: Clean, responsive design with smooth animations and intuitive navigation
- **Advanced Search**: Quickly find emails using the powerful search functionality
- **Email Statistics**: Track your email usage patterns with detailed statistics
- **Secure Authentication**: Robust user authentication with password hashing and reset functionality
- **Profile Management**: Customize your profile with a personal image and account settings

## Tech Stack

### Frontend
- HTML5, CSS3, JavaScript
- Bootstrap 4.5 for responsive design
- Custom animations and transitions
- Modern UI components with glassmorphism effects

### Backend
- Python 3.10
- Flask web framework
- SQLAlchemy ORM
- Flask-Login for authentication
- Flask-Bcrypt for password hashing
- Flask-Migrate for database migrations

### AI/ML
- Transformers library by Hugging Face
- BERT-based models for text summarization
- Custom NLP pipelines for email categorization

### Database
- SQLite (with plans to migrate to PostgreSQL)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-email-client.git
   cd ai-email-client
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database:
   ```bash
   set FLASK_APP=run.py
   flask db init
   flask db migrate
   flask db upgrade
   ```

5. Run the application:
   ```bash
   python run.py
   ```

## Project Structure

```
AI-Email-Client/
├── Project/
│   ├── static/
│   │   ├── css/
│   │   └── profile_pics/
│   ├── templates/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── forms.py
├── migrations/
├── requirements.txt
├── run.py
└── README.md
```

## Features in Detail

### Email Management
- Compose, send, and receive emails
- View inbox and sent items
- Delete emails
- Categorize emails
- Search functionality

### AI Features
- Automatic email summarization
- Smart categorization
- Email statistics and insights
- Top recipients tracking

### User Features
- Secure registration and login
- Profile customization
- Password reset functionality
- Account management

## Future Enhancements

- [ ] Migrate to PostgreSQL for better scalability
- [ ] Implement real-time email notifications
- [ ] Add email templates and scheduling
- [ ] Enhance AI features with sentiment analysis
- [ ] Add support for multiple email accounts
- [ ] Implement advanced search filters
- [ ] Add dark mode support
- [ ] Improve mobile responsiveness

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
