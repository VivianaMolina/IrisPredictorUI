import pytest
import os
import sys

# Add the project root to the path to import server.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from server import app 

# --- Fixture for Flask Test Client ---

@pytest.fixture
def client():
    """Configures the Flask test client for use in tests."""
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

# --- Integration Tests ---

def test_homepage_loads(client):
    """Tests that the root page (/) loads correctly (HTTP 200)."""
    response = client.get('/')
    assert response.status_code == 200
    # Check for an expected title or heading text
    assert b"Iris Flower Classifier" in response.data or b"Clasificador de Flores Iris" in response.data

def test_prediction_endpoint_success(client):
    """
    Tests the prediction endpoint with valid data.
    (Use data known to produce a specific, expected classification)
    """
    # Example data for a known species (e.g., Versicolor)
    test_data = {
        'sepal_length': 6.0,
        'sepal_width': 2.2,
        'petal_length': 4.0,
        'petal_width': 1.0
    }

    # Simulate a POST request to the prediction route
    # NOTE: Ensure '/predict' is the correct route in your server.py
    response = client.post('/predict', data=test_data, follow_redirects=True)
    
    # Status code should be 200 if the app successfully renders the result page
    assert response.status_code == 200 
    
    # Verify that the expected result (e.g., 'Versicolor') is in the response HTML
    assert b"Versicolor" in response.data 
    
def test_prediction_endpoint_invalid_input(client):
    """Tests the prediction endpoint with missing data to verify error handling."""
    
    # Incomplete data (missing 'petal_width')
    invalid_data = {
        'sepal_length': 5.1,
        'sepal_width': 3.5,
        'petal_length': 1.4,
    }

    response = client.post('/predict', data=invalid_data, follow_redirects=True)
    
    assert response.status_code == 200 
    # If your app shows an error message for missing data, check for it here.
    # For example: assert b"Missing input data" in response.data