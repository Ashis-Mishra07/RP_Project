@echo off
echo Starting Word Recognition Bot...
echo.

echo Checking Python environment...
python --version
echo.

echo Testing system components...
python test_system.py
echo.

echo Starting Streamlit application...
echo Open your browser and go to: http://localhost:8501
echo.

streamlit run app.py
