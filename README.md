# FastAPI WebSocket and HTTP Endpoints Project

This project demonstrates the use of FastAPI to create both WebSocket and custom HTTP endpoints.

## Features

- WebSocket endpoint for real-time communication
- Custom HTTP endpoints for various operations
- Asynchronous handling of requests

## Requirements

- Python 3.7+
- FastAPI
- Uvicorn (ASGI server)

## Installation

1. Clone the repository:

   git clone https://github.com/yourusername/your-repo-name.git
   cd your-repo-name

2. Install the required packages:

   pip install -r requirements.txt

## Usage

1. Start the server:

   uvicorn main:app --reload

2. Access the API documentation:
   Open your browser and navigate to `http://localhost:8000/docs` for the Swagger UI.

## API Endpoints

- `/ws`: WebSocket endpoint for real-time communication
- `/`: Root endpoint, returns a welcome message
- `/items/{item_id}`: GET endpoint to retrieve item details

## WebSocket Usage

Connect to the WebSocket endpoint at `ws://localhost:8000/ws` to establish a real-time connection.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.
