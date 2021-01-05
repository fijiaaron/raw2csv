#raw2csv

This converts an image in RAW or DNG format to a CSV file with the raw data.

usage:

    raw2csv sample1.dng

To run the python version of the app:
    
    pip install -r requirements.txt
    python raw2csv.py sample1.dmg
    
To build a standalone version of the app for Windows, Mac, or Linux with pyinstaller:

    pip install pyinstaller 
    pyinstaller --onefile raw2csv.py

A windows exe is included:

    raw2csv.exe

