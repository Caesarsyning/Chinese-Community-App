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
- **Database**: Deployed using Postgres on the Heroku platform.
- **Media Storage**: Utilized AWS S3 buckets for storing images and other types of data.

## Deployment

The web application is deployed on the Heroku platform with data being stored in a Postgres database. AWS S3 is used for media storage.

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Install the necessary dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up the database:

    ```bash
    python manage.py migrate
    ```

4. Run the development server:

    ```bash
    python manage.py runserver
    ```

5. Deploy to Heroku:

    Follow Heroku's deployment guidelines [here](https://devcenter.heroku.com/articles/deploying-python).

## Author

- **Caesar Ning**


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
