datafun-03-analytics
Week 3 coursework

Brief Project Overview: 
I am building a project that can get a URL and then process the data that it contains. For this project, we had to use CSV, Excel, JSON, and txt files. That means we have to find the URLs where this data can be found and then build a function to process this data in the way that we want. 


Function Breakdown:  
CSV Function: The CSV calculated some key metrics for the obesity data. It shows the max, min, mean, and standard deviation of the data.

Excel Function: The function counts the number of times 314 occurred in the second column of my sheet.

JSON Function: The JSON file lists out the number of players on each team. I also created a mapping so that values that don't correspond to teams (-2, -1, etc.) are mapped to their correct designation (inactive, free agent, etc.).

Text Function: The text file counts the number of times "Plato" is used in The Republic.

## Project Requirements

- VS Code
- Git
- Python 


## Commands to Manage Virtual Environment

For Windows PowerShell (change if using Mac/Linux).
Verify that all required packages are included in requirements.txt (and have NOT been commented out).


```powershell
py -m venv .venv
.\.venv\Scripts\activate
py -m pip install --upgrade pip setuptools wheel
py -m pip install --upgrade -r requirements.txt
```

## Commands to Run Python Scripts

Remember to activate your .venv (and install packages if they haven't been installed yet) before running files.

```shell
py utils_case.py
py dirbot_case.py
```

## Commands to Git add-commit-push

```shell
git add .
git commit -m "custom message"
git push -u origin main
```

## Reference Projects

Custom implementation of the example project at 
[datafun-02-project-setup](https://github.com/denisecase/datafun-02-project-setup)

- [Module 1 Repo](https://github.com/denisecase/datafun-01-utils/)