# BraveAI-Scraper API

**BraveAI-Scraper** is a Python tool that scrapes data from Brave AI and exposes it as a RESTful API, allowing users to access model responses without needing an API key. This project offers a free solution for developers and researchers to integrate Brave AI's capabilities into their applications.

## Features

- Scrape data from Brave AI
- RESTful API to access model responses
- Access model responses without an API key
- Handles CAPTCHA by allowing manual intervention

## Installation

1.  Clone the repository:
    ```sh
    git clone https://github.com/yourusername/BraveAI-Scraper.git
    cd BraveAI-Scraper
    ```

2.  Install the required dependencies from `requirements.txt`:
    ```sh
    pip install -r requirements.txt
    ```

3.  Install the Playwright browsers:
    ```sh
    playwright install
    ```
4. Install Playwright OS dependencies:
    ```sh
    sudo playwright install-deps
    ```
    On Fedora, you may need to run:
    ```sh
    sudo dnf install libicu libjpeg-turbo gstreamer1-libav
    ```


## Usage

To use the BraveAI-Scraper API, you first need to start the server:

```sh
uvicorn main:app --host 0.0.0.0 --port 8000
```

The API will be available at `http://0.0.0.0:8000`.

### API Endpoint

The API has a single endpoint:

-   `GET /search`

    This endpoint accepts a single query parameter `q` and returns the scraped Brave AI summary as a JSON response.

### CAPTCHA Handling

Brave Search may occasionally present a CAPTCHA to verify that you are not a robot. When this happens, a browser window will open, and you will need to solve the CAPTCHA manually. Once the CAPTCHA is solved, the scraper will continue, and the API will return the search results.

## Example

You can use `curl` to make a request to the API:

```sh
curl "http://0.0.0.0:8000/search?q=What+is+the+capital+of+France"
```

The API will return a JSON response like this:

```json
{
  "query": "What is the capital of France",
  "result": "The capital of France is Paris."
}
```

## Disclaimer

This project is intended for educational purposes only. The developers are not responsible for any misuse of this tool. Please use it responsibly and in accordance with all applicable laws and regulations.

## License

This project is licensed under the MIT License.