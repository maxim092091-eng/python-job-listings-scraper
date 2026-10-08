# python-job-listings-scraper

A web scraper that collects job listings from the Fake Python Jobs website.

## Features

- Scrape job listings from the Fake Python Jobs website and export them to a CSV file.

## Requirements

- Python 3.10+

## Technologies

- Python
- Requests
- Beautiful Soup 4

## Installation

### Clone the repository

```bash
git clone https://github.com/maxim092091-eng/python-job-listings-scraper.git
``` 

### Navigate to the project directory

```bash
cd python-job-listings-scraper
``` 

### Create a virtual environment

#### On Windows

```bash
py -m venv .venv
```

#### On Linux/macOS

```bash
python3 -m venv .venv
```

### Activate the virtual environment

#### On Windows

```bash
.venv\Scripts\activate
```

#### On Linux/macOS

```bash
source .venv/bin/activate
```

### Install the project

```bash
python -m pip install .
```

## Usage

Run the application:

```bash
job-scraper
```

The CSV file `job_listings.csv` with the collected job listings will be created in the project directory.

## Project Structure

```text
python-job-listings-scraper/
├── src/
│   └── python_job_listings_scraper/
│       ├── api.py
│       ├── main.py
│       └── scraper.py
├── tests/
│   └── test_scraper.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Tests

Run the tests with:

```bash
pytest
```

## Project

This project was built following the [Python Job Listings Scraper](https://roadmap.sh/projects/job-listings-scraper) project requirements from Roadmap.sh.

## License

This project is licensed under the MIT License.

## Author

Created by [Maxim](https://github.com/maxim092091-eng)
