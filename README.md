# FastAPI Learning Exercises

This repository contains exercises and examples created while learning [FastAPI](https://fastapi.tiangolo.com/), a modern, fast (high-performance) web framework for building APIs with Python 3.7+.

## Purpose

The purpose of this repository is to practice and solidify concepts related to FastAPI, including but not limited to:
- Building RESTful APIs
- Request and response handling
- Dependency injection
- Authentication and authorization
- Database integration
- Testing FastAPI applications

## Prerequisites

To run the examples in this repository, ensure you have the following installed:
- Python 3.7 or higher
- `pip` (Python package manager)

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/fastapi-learning-exercises.git
    cd fastapi-learning-exercises
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Exercises

1. Start the FastAPI development server:
    ```bash
    uvicorn main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000` to interact with the API.

3. Access the automatically generated API documentation:
    - Swagger UI: `http://127.0.0.1:8000/docs`
    - ReDoc: `http://127.0.0.1:8000/redoc`

## Folder Structure

```
fastapi-learning-exercises/
├── app/                # Application code
├── tests/              # Test cases
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
```

## Contributing

Feel free to fork this repository and submit pull requests with improvements or additional exercises.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.