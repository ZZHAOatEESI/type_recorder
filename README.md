# Type_recorder
1. Contributors:
	- Joe
	- Lynn
2. Dependencies:
	- Python 3.6.4 :: Anaconda, Inc
	- Dash (https://plot.ly/products/dash/)
3. User Guide:
	1. What's Type_recorder
		- Type_recorder is a web server that record users' speed and accuracy typing sample texts.
	2. How to run
		1. Check Dependencies
		2. Type in `python type_recorder.py` in terminal
		3. The server will be running on local host (for example http://127.0.0.1:8050/)
		4. Copy the http address to your browser to access to the user interface
		5. When done with all sample texts, run post_processing.py to evaluate user typed content
		6. The final records is in a csv file named *records.csv*
	3. How to interpret records
		- *records.csv* has 5 columns, namely, test id (implicit), duration, user input, reference content and mistakes
		- **test id** refers to the index of test, each test asks user to type in a sentence according to the reference
		- **duration** how long did it take for the user to type this sentence
		- **user input** the content that user typed in
		- **reference content** the reference content the user referred to
		- **mistakes** *Levenshtein* distance between user input and the reference
	4. If you want to add more practice sentence, please edit `type_recorder.py` file.
	5. UI Overview
		- ![Screenshot unavailable](ui_1.png)
		- The box under the red text is the reference text
		- The box under the green text is the user input region
		- The timer will start to record the duration of typing when user starts to enter content
		- The timer will stop when user click on **SUBMIT** button

4. Note
	- Feel free to (re)use my code in any way you wish but it is on your own risk and you are solely responsible for whatever happens then.
