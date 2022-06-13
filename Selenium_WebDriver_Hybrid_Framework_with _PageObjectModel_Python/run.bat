pytest -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome

rem pytest -s -v -n=2 testCases/test_login.py --browser firefox

rem pytest -s -v -n=2 testCases/ --browser chrome