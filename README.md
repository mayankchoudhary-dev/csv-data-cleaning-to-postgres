# CSV → Python Cleaning → PostgreSQL

## Project Overview

This project implements a data engineering pipeline that reads raw sales data from a CSV file, cleans and validates records using Python and Pandas, separates invalid records, and loads valid records into PostgreSQL.

## Pipeline Architecture

Raw CSV → Python Data Cleaning → Data Validation → PostgreSQL

Invalid records are saved separately with rejection reasons.

## Technologies Used

- Python
- Pandas
- PostgreSQL
- Psycopg
- SQL
- pytest
- Linux and Bash
- Git and GitHub

## Data Quality Checks

- Missing required values
- Invalid dates and numeric values
- Duplicate order IDs
- Zero or negative quantities
- Invalid unit prices
- Calculated sales totals

## Project Structure

- `data/raw/`: Original sales dataset
- `data/cleaned/`: Cleaned sales data
- `data/rejected/`: Rejected records and reasons
- `src/`: Python pipeline modules
- `sql/`: Database schema and quality checks
- `config/`: Database configuration
- `tests/`: Automated validation tests
- `logs/`: Pipeline logs

## How to Run

1. Create and activate a Python virtual environment.
2. Install dependencies from `requirements.txt`.
3. Configure the PostgreSQL connection in `.env`.
4. Create the database table using `sql/create_tables.sql`.
5. Run `python -m src.pipeline`.

## Testing

Run automated tests using:

```bash
pytest -v
```

## Security

Database credentials are stored in `.env`. The `.env` file must not be committed to version control.

## Learning Outcomes

- Cleaning and validating CSV data
- Handling rejected records
- Loading data into PostgreSQL
- Writing SQL quality checks
- Testing Python code
- Logging and running pipeline jobs