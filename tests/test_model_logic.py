import pytest
import os
import sys
import subprocess
import time

# --- Test for Training and Saving ---

def test_model_training_and_saving():
    """Tests that the iris.py script executes and saves a model file."""
    
    # Path to the training script
    train_script_path = os.path.join(os.path.dirname(__file__), '..', 'iris.py')
    
    # 1. Execute the training script
    try:
        # Use subprocess to execute the script as a user would
        result = subprocess.run([sys.executable, train_script_path], 
                                capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # Fail the test if the training script throws an error
        pytest.fail(f"iris.py failed to execute: {e.stderr}")
    
    # 2. Verify that the model file was created
    model_path = os.path.join(os.path.dirname(__file__), '..', 'models', 'model_iris.pkl')
    
    # Wait briefly to ensure I/O completes
    time.sleep(0.5) 
    
    # Check that the file exists
    assert os.path.exists(model_path)
    
    # Check that the file is not empty
    assert os.path.getsize(model_path) > 0