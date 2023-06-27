import pytest
import requests

def test_website_loading():
    url = "https://www.atg.world"

    response = requests.get(url)

    if response.status_code == 200:
        print("Website loaded successfully.")
    else:
        print("Failed to load the website.")

    assert response.status_code == 200

if __name__ == "__main__":
    pytest.main()

