# Excel-Files-Ranker-API
This repository contains code for a Flask-based RESTful API that ranks the columns of Excel files and returns the top 5 columns.

# 📥 Installation Guide

### Step 1 : Clone the Repository

Clone the repository using the following command.

```
$ git clone https://github.com/sbeen1840/Excel-Files-Ranker-API.git
```

### Step 2 : Install Dependencies

**Note** : It is recommended to use a `conda environment` with `Python 3.6` with this code. Before running the commands in this guide, make sure you activate the environment using `$ source activate <name of the env>`

The use the `requirements.txt` file given in the repository to install the dependencies via `pip`.

```
$ pip install -r requirements.txt
```

### Step 3 : Verify the installation of dependencies

To verify whether `pandas`, `pytrends` and `trend` were installed properly, run the following.

```
$ python
>>> import pandas
>>> import flask
```

If there are no error messages upon importing the above dependencies, it would indicate that the they are correctly installed.

# 🔎 Usage

### Step 1 : Update the keywords in the three CSV files.

|1|2|3|4|5|
|---|---|---|---|---|
|JAVA| java|
|C++| c++|
|PYTHON| python| py| PY|
|javaScript| javascript| JAVASCRITP|

Suppose you have a CSV file containing keywords up to five in one row.

The first index of each row becomes the representative keyword.

Keywords similar to the representative keywords may be entered in each row.

### Step 2 : Change the route of csv file and set the themes of the files in main.py

```
csv1 = "C:/Users/user/Desktop/swa-java-2023/팀프로젝트/keyword_language.csv"
csv2 = "C:/Users/user/Desktop/swa-java-2023/팀프로젝트/keyword_jobgroup.csv"
csv3 = "C:/Users/user/Desktop/swa-java-2023/팀프로젝트/keyword_academy.csv"

theme1 = "프로그래밍언어"
theme2 = "개발직군"
theme3 = "개발교육"
```

### Step 3 : Change the variables for data collection in trend.py file.
```
self.numb = 2 # 상위부터 추출 개수 
self.lang = 'ko' # pytrend 기준 언어 설정
self.time = 540 # pytrend 기준 시간대 설정
self.geo = 'KR' # pytrend 기준 위치 설정
self.month = 1 # 현재부터 n개월간의 기록 (정수만 입력)
self.update = 1 # 업데이트할 주기(단위 sec)  # 86400 하루
self.address = csv_address # main.py에서 지
self.dicts = 7 # json파일의 초기
```


### Step 4 : Run the script by typing python `main.py` in the terminal.
![image](https://user-images.githubusercontent.com/108644811/218135256-a527b011-0b86-4f49-98ee-83b8b41698b1.png)

### Step 5 : Access the data by visiting `http://localhost:5000/home` in your web browser.

After running the script, you can access keywords representing the search trend by visiting [http://localhost:5000/home](http://localhost:5000/home) in your web browser. You can also see their search volume, normalized. The data will be presented in the form of  json and sorted in descending order.
# ⚙️Usage
Modify the masterpath, extension, and folders parameters in the Ranker class to specify the location of your Excel files.

Run the code using python main.py.

Access the API at localhost:5000/home.


# ⚡Results
The API returns a JSON object containing the top 5 columns of each Excel file in the specified folders, ranked by the sum of the values in each column.

![image](https://user-images.githubusercontent.com/108644811/225906918-e77f10a5-99cc-4525-9c9e-608ced58d515.png)


# 🔥Execution
`docs/excel_files_ranker_api.ipynb` describes the execution steps of this program pipeline in detail.


# 📝Notes
- This code assumes that the first 5 rows of each Excel file are header information and skips them.

- This code only works with .xlsx file extensions.

- The API can be accessed at localhost:5000/home.

- The code has only been tested on Windows machines.


# ✋Authors
[sbeen1840] - Initial work
