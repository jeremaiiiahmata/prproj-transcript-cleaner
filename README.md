# Premier Pro Transcript Cleaner

## Transcript Cleaner
A lightweight desktop GUI tool that cleans raw transcript .txt files by removing timestamps and speaker labels — turning messy exports into clean, readable text in seconds.
 
 > Designed for editors and content creators, it supports batch processing to save time and eliminate repetitive manual work.
 

## Features : 
* Process an entire folder of transcripts at once
* Automatically removes:
    * Timecodes (e.g. 00;00;12;15 - 00;00;15;20)
    * Speaker labels (e.g. V1, 123)
* Outputs cleaned files with cleaned_ prefix
* Simple and easy-to-use GUI


## How It Works


1. Select a folder containing .txt transcript files
2. Click Clean Transcripts
3. The app scans all files inside the folder
4. Cleaned versions are generated automatically

## Installation
1. `git clone` this project 
2. `cd` to the directory of the project
3. run `pip install -r requirements.txt`
4. run `python cleaner.py`
---
