# Chinese Community App

## Overview

This project is a Django-based web application developed for the Chinese student community at Charlottesville, VA. The app aims to provide a platform that facilitates community engagement, including features like a resale and housing market, course evaluations, and event notifications.

## Features

- **Resale and Housing Market**: A section for users to buy and sell goods or search for housing.
- **Course Evaluations**: A platform for students to share and access course reviews.
- **Event Notifications**: A feature to notify the community about upcoming events and activities.

## Technologies Used

- **Backend**: Developed using the Django framework with a Model-View-Template (MVT) pattern.
- **Frontend**: Designed using HTML templates, Bootstrap for styling, and JavaScript for interactive elements.
- **Database**: Deployed using MySQL in a Docker container for local development.
- **Media Storage(Developing)**: Utilized AWS S3 buckets for storing images and other types of data.
- **Containerization**: The application is containerized using Docker for easy deployment and development.

## Deployment

The web application can be deployed using Docker for local development and deployed to the Heroku platform. MySQL is used for database management, and AWS S3 is utilized for media storage.

### Docker Setup

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Build and run the Docker containers:

    ```bash
    docker-compose up --build
    ```

   This will start the Django application and the MySQL database inside Docker containers.

3. Run database migrations:

    ```bash
    docker-compose exec web python manage.py migrate
    ```

4. Access the development server:

    Open your browser and navigate to `http://localhost:8000`.

### Manual Setup (Without Docker)

1. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2. Set up the MySQL database:

    Make sure you have MySQL installed and running. Update your `settings.py` to configure the database settings for MySQL.

3. Run database migrations:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

### Deploy to Heroku

Follow Heroku's deployment guidelines [here](https://devcenter.heroku.com/articles/deploying-python). Ensure you configure your Heroku app to use MySQL as the database.

## Author

- **Caesar Ning**

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
