"""
Runs doctests for all specified modules as a unittest suite.

# --- Execution guidelines ---
# To execute main (__main__) & module-level (non-testing/callable) helper code:
# (option 1) run (|>) script in dedicated terminal
# (option 2) execute script in terminal (`python <script_name>.py`) with wd=repo
# To execute selection and share declarations with global namespace: shift+enter
"""

if __name__ == "__main__":
    import doctest
    import unittest

    modules_to_test = (
        'display_dataset', 'nb_utils', 'media_scrape', 
        'datamodel_utils', '_examples', 'models.media_pulse'
    )
    for module in modules_to_test:
        temp_module = __import__(module, fromlist=["*"])
        test_suite = doctest.DocTestSuite(temp_module)
        unittest.TextTestRunner().run(test_suite)