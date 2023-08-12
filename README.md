# Project Title

This is a simple guide on how to deploy this repository.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You need to have Docker and Docker Compose installed on your machine. 

### Installing

A step by step series of examples that tell you how to get a development environment running.

1. Clone the repository
```
git clone <repository_url>
```
2. Navigate to the project directory
```
cd <project_directory>
```
3. Install the required Python dependencies
```
pip install -r requirements.txt
```
4. Build the Docker image
```
docker build -t <image_name> .
```
5. Run the Docker container
```
docker run -d -p 5000:5000 <image_name>
```
6. Alternatively, you can use Docker Compose to build and run the container
```
docker-compose up
```

## Running the tests

To run the tests, navigate to the tests directory and run the test files.
```
python -m unittest test_main.py
python -m unittest test_utils.py
```

## Deployment

This application can be deployed on any system that supports Docker.

## Built With

* [Python](https://www.python.org/)
* [Docker](https://www.docker.com/)

## Authors

* **Your Name** - *Initial work* - [YourGithubUsername](https://github.com/YourGithubUsername)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc