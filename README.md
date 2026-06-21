# Ness Technologies - QA Automation Home Assignment

## Project Overview

This project implements an automated end-to-end shopping flow for an e-commerce website using Playwright and Python.

The implementation follows the assignment requirements:

* Page Object Model (POM)
* Data-Driven testing using JSON
* Product search and filtering
* Add products to cart
* Cart total validation
* Allure reporting support

## Project Structure

```text
pages/
├── home_page.py
├── product_page.py
└── cart_page.py

tests/
└── test_home_page.py

utils/
├── data_reader.py
└── price_parser.py

data/
└── test_data.json

config/
└── settings.py
```

## Technologies

* Python 3.14.3
* Playwright
* Pytest
* Allure

## Test Data

Test data is stored externally in:

```text
data/test_data.json
```

Example:

```json
{
  "query": "Digital Cameras",
  "max_price": 140,
  "limit": 5
}
```

## Running the Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

Run tests:

```bash
pytest
```

Generate Allure results:

```bash
pytest --alluredir=allure-results
```

Generate JUnit XML report:

```bash
pytest --junitxml=report.xml
```

To generate an HTML Allure report, Allure Commandline must be installed separately.

## Assumptions and Limitations

### Authentication

The assignment mentions an authentication function, but no credentials or authentication requirements were provided.

Therefore, the scenario is executed as a Guest User and no login flow is implemented.

### Query Implementation

The assignment requires product search by query.

For this implementation, the query is mapped to the eBay "Digital Cameras" category.

### Currency

The implementation assumes USD pricing because the selected eBay category and price filters are based on USD values.

Regional eBay sites may display prices in other currencies depending on location and localization settings.

### Captcha / Bot Protection

According to the assignment instructions, captcha handling is out of scope.

eBay may occasionally display bot-protection or challenge pages during automated execution. The framework does not attempt to bypass such mechanisms.

### Product Availability

eBay is a live production website. Product availability, pricing, filters, and page structure may change over time.

Products that cannot be added to the cart are skipped during execution.

## Reporting

The project includes Allure reporting integration.

Generated Allure results are stored in:

```text
allure-results/
```

JUnit XML reports can also be generated using the command shown above.

## AI Usage

AI tools were used to assist with:

* Code structure planning
* Page Object Model design
* Documentation preparation

All generated code was reviewed, adapted, and validated manually.
