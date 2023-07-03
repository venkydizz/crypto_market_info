# CRYPTO MARKET INFO
**crypto_market_info** is a simple microservice which provides crypto currency market updates.

**API Documentation** : https://documenter.getpostman.com/view/10449766/2s93zCaMLX

## Setup Prerequisites

Before getting started with project setup, ensure that you have the following done:

- Python: Download the latest version of Python from the official Python website (https://www.python.org/).
- `venv` package: Install it using pip by running the following command:
    ``` shell
    pip install venv
    ```
- Navigate to your working directory.

## Setup  Instructions.

1. Create a virtual environment:
   ``` shell
   python -m venv {env_name}
   ```
2. Activate the virtual environment:
    * On Windows:
        ``` shell
        {env_name}\Scripts\activate

        ```
    * on Linux:
        ``` shell
        source {env_name}/bin/activate
        ```
3. Clone the repository:
    ``` shell
    git clone https://github.com/venkydizz/crypto_market_info.git
    ```
4. Navigate to the project directory:
    ``` shell
    cd crypto_market_info
    ```
5. Checkout `master` branch:
    ```
    git checkout master
    ```
6. Install the project dependencies:
    ``` shell
    pip install -r requirements.txt
    ```
7. Create a .env file in the project directory and add the client token:
    ```
    CLIENT_KEY = 'SAMPLE_KEY'
    ```
    replace with `'SAMPLE_KEY'` with your API key.
8. Start the server:
    ``` shell
    python manage.py runserver
    ```
9. Open your web browser and visit http://127.0.0.1:8000/ping to check the status.

## Other Commands
1. ### Unit Tests:
    To run the entire unit tests of the microservice, use the below command
    ```
    pytest -v
    ```

2. ### Linting score:
    To generate code quality linting score and  suggestions
    ```
    pylint folder_name/
    ```







