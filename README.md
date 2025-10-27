# quantmath
## Setup
1. Setup `.venv` using `python -m venv .venv`
2. Activate: `source .venv/Scripts/activate`
3. Install: `pip install -r requirements.txt`

## Running Things
1. Run test_metrics.py normally
    - In your root directory: `python -m tests.test_metrics`
    - Why it didn't work during the day: 
        - Clicking 'run' in VSCode calls it like `c:/Users/Administrator/Desktop/quantmath/tests/test_metrics.py` 
        - This calls it from the `tests` directory, and it's not able to see the `quantmath` folder
2. Run pytest
    - How pytest works: it looks in your whole project directory for any files with `test_` in the name. Then runs them locally.
    - In your root directory: `pytest`
    - Why it didn't work during the day: 
        - Pytest assumes module files to be tested are stored in the root. However, they were in `src`. So `src` wasn't considered a module!
        - How to fix yourself: add an `__init__.py` file inside `src`. Then create a file called `pytest.ini` and make it identical to this repo's `pytest.ini`. This configuration tells pytest to look inside `src`. 
3. Run driver
    - Go to `driver.py` and click the run button.
        - `C:/Users/Administrator/AppData/Local/Programs/Python/Python313/python.exe c:/Users/Administrator/Desktop/quantmath/src/driver.py`
    - This isn't really needed. (2) should be the default thing you run
        
