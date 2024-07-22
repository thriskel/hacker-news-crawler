# hacker-news-crawler
Simple web crawling exercise that uses a django API to allow interactions with it.

## Table of Contents

- Requirements
- Installation
- Usage
- API Endpoints
- Testing
- Technologies

## Requirements

- Docker

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/thriskel/hacker-news-crawler.git
    cd hacker-news-crawler
    ```

2. Start docker compose:
    ```bash
    docker compose up --build
    ```

## Usage

You can interact with the endpoints accesing through the browser or using a tool like postman or insomnia.

After the initialization of the docker compose you should be able to access the endpoints through localhost:8000/endpoints/.

It is important to fill the .env file once you clone the repo to allow the correct execution of the django and postgres container.

Since this is a practical example Im committing the file with valid data, but that should not be done in a real product.

## API Endpoints

- /news/ ['GET']
- /interactions/ ['GET']

## Testing

1. Run tests:
    ```bash
    docker compose run test
    ```

## Technologies

- Django
- Django REST framework
- PostgreSQL
- Docker
- Beautiful Soup 4
- Pydantic
