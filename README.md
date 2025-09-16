# Text Avatar Generator

This is a simple Flask application that generates text-based avatars. You can customize the avatar by providing a first name and a last name, and the application will generate an avatar with the initials. You can also customize the width and height of the avatar.

## Features

-   Generates avatars with the first letter of the first and last name.
-   If only a first name is provided, it uses the first two letters of the first name.
-   Customizable avatar width and height.
-   Random background colors for the avatars.
-   A Dockerfile is included for easy setup and deployment.

## Getting Started

### Prerequisites

-   Python 3.7+
-   Flask
-   Pillow

### Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/roysuzon/image_generation.git
    ```
2.  Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the application:
    ```bash
    python app.py
    ```
    The application will be running at `http://localhost:5000`.

## Usage

To generate an avatar, make a GET request to the `/generate-avatar` endpoint with the following query parameters:

-   `first_name` (required): The first name.
-   `last_name` (optional): The last name.
-   `width` (optional): The width of the avatar in pixels.
-   `height` (optional): The height of the avatar in pixels.

### Examples

-   **With first and last name:**
    ```
    http://localhost:5000/generate-avatar?first_name=John&last_name=Doe
    ```
    This will generate an avatar with the text "JD".

-   **With only first name:**
    ```
    http://localhost:5000/generate-avatar?first_name=John
    ```
    This will generate an avatar with the text "Jo".

-   **With custom width and height:**
    ```
    http://localhost:5000/generate-avatar?first_name=John&last_name=Doe&width=300&height=300
    ```
    This will generate a 300x300 avatar.

## Docker

You can also run the application using Docker.

1.  Build the Docker image:
    ```bash
    docker build -t text-avatar-generator .
    ```
2.  Run the Docker container:
    ```bash
    docker run -p 5000:5000 text-avatar-generator
    ```
    The application will be running at `http://localhost:5000`.
