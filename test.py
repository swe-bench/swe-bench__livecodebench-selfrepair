import sys
import json

from io import StringIO
from main import solution

def run_test(test):
    # Simulate standard input
    sys.stdin = StringIO(test['input'])
    
    # Capture the output
    captured_output = StringIO()
    sys.stdout = captured_output
    
    # Run the function
    solution()
    
    # Reset standard input and output
    sys.stdin = sys.__stdin__
    sys.stdout = sys.__stdout__
    
    # Check the result
    return captured_output.getvalue().strip() == test['output'].strip()

def main():
    tests = json.loads(
        json.load(open('tests.json'))['tests'])
    
    for i, test in enumerate(tests):
        if run_test(test):
            print(f"Test {i+1} passed")
        else:
            print(f"Test {i+1} failed")

if __name__ == "__main__":
    main()
