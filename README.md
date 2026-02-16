# BraveAI-Scraper API

**BraveAI-Scraper** is a Python tool that scrapes data from Brave AI and exposes it as a RESTful API, allowing users to access model responses without needing an API key. This project offers a free solution for developers and researchers to integrate Brave AI's capabilities into their applications.

## Features

- Scrapes search summaries from Brave AI.
- **Asynchronous FastAPI backend** for high concurrency and responsiveness.
- **Production-ready deployment** via Gunicorn and Uvicorn workers.
- **Containerized** with Docker/Podman for easy, consistent, and portable deployment.
- **Configurable** via environment variables for flexible setup.
- Provides a **RESTful API** to access model responses.

## Running the Application

The simplest and recommended way to run this application is by using a container runtime like Docker or Podman.

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/saransridatha/BraveAI-API.git
    cd BraveAI-API
    ```

2.  **Build the container image:**
    ```bash
    docker build -t brave-search-api .
    # Or for Podman:
    # podman build -t brave-search-api .
    ```

3.  **Run the container:**
    ```bash
    docker run -p 8000:8000 --rm brave-search-api
    # Or for Podman:
    # podman run -p 8000:8000 --rm brave-search-api
    ```
    The API will then be available at `http://localhost:8000`.

### Running for Development (Local)

If you wish to run the application locally for development or testing without containers:

1.  **Install Python dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2.  **Install Playwright browsers:**
    ```sh
    playwright install --with-deps chromium
    ```

3.  **Start the development server:**
    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000 --reload
    ```
    The API will be available at `http://0.0.0.0:8000`.

## Configuration

The application can be configured using the following environment variables when running the container or locally:

| Variable        | Description                                                              | Default |
| --------------- | ------------------------------------------------------------------------ | ------- |
| `HEADLESS_MODE` | Set to `true` or `false` to run the browser in headless mode.            | `true`  |
| `PORT`          | The port on which the application will listen.                           | `8000`  |

## API Endpoint

The API has a single endpoint:

-   `GET /search`

    This endpoint accepts a single query parameter `q` and returns the scraped Brave AI summary as a JSON response.

### Example Usage

You can use `curl` to make a request to the API:

```sh
curl "http://localhost:8000/search?q=What+is+the+capital+of+France"
```

The API will return a JSON response like this:

```json
{
  "query": "What is the capital of France",
  "result": "The capital of France is Paris."
}
```

## CAPTCHA Handling

Brave Search may occasionally present a CAPTCHA to verify that the request is not from a bot. In the containerized (headless) environment, manual interaction to solve CAPTCHAs is not possible. If a CAPTCHA is encountered, the API will likely time out and return an error message indicating that the search summary could not be retrieved. A screenshot (`error_screenshot.png`) may be saved inside the container for debugging such issues.

To minimize CAPTCHA occurrences, the application uses a common browser user-agent. For persistent issues, more advanced techniques such as integrating a proxy rotation service or a CAPTCHA-solving service would be necessary.

## Disclaimer

This project is intended for educational purposes only. The developers are not responsible for any misuse of this tool. Please use it responsibly and in accordance with all applicable laws and regulations.

## License

This project is licensed under the MIT License.