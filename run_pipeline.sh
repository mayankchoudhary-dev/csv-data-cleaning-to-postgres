
#!/bin/bash

set -e

cd "$HOME/projects/csv-data-cleaning-to-postgres"

./venv/bin/python -m src.pipeline
