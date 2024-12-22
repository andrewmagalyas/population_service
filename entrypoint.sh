#!/bin/bash

# Check if a command is passed (either get_data or print_data)
if [ "$1" == "get_data" ]; then
    # Execute the code for fetching data
    python -m app.get_data
elif [ "$1" == "print_data" ]; then
    # Execute the code for printing data
    python -m app.print_data
else
    # Default to running the FastAPI app
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
fi
