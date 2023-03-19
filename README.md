
![image](https://user-images.githubusercontent.com/108644811/226151915-9dd521ef-3064-4559-b077-1682ab04e983.png)
> This repository contains code for a Flask-based RESTful API that ranks the columns of Excel files and returns the top 5 columns.

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

To verify whether `pandas`, `flask` were installed properly, run the following.

```
$ python
>>> import pandas
>>> import flask
```

If there are no error messages upon importing the above dependencies, it would indicate that the they are correctly installed.

# 🔎 Usage

### Step 1: Enter the keyword on the [Naver Trends site](https://datalab.naver.com/keyword/trendSearch.naver) and download the Excel file.

![image](https://user-images.githubusercontent.com/108644811/225911951-855bde8f-d57f-4405-8f97-921c198ba6ad.png)

### Step 2: Create subfolders for each topic within the top-level folder.

![image](https://user-images.githubusercontent.com/108644811/226096802-b48a3776-2aef-478e-be56-f6607d443573.png)

### Step 3: Place the Excel files corresponding to each topic in their respective subfolders.
![image](https://user-images.githubusercontent.com/108644811/225910798-360fc707-2bcc-46b0-89f7-1f5925814ae4.png) ![image](https://user-images.githubusercontent.com/108644811/226150633-304f5b07-be74-4d76-b606-89c059d66293.png)

### Step 4: Modify the masterpath, extension, and folders parameters in the Ranker class to specify the location of your Excel files.
```py
  self.masterpath = masterpath
  self.extension = extension
  self.folders = folders
```
### Step 5 : Run the script by typing python `main.py` in the terminal.
```
$ python
>>> import pandas
>>> import flask
```

### Step 6 : Access the data by visiting `http://localhost:5000/home` in your web browser.

After running the script, you can access keywords representing the search trend by visiting [http://localhost:5000/home](http://localhost:5000/home) in your web browser. You can also see their search volume, normalized. The data will be presented in the form of  json and sorted in descending order.


# ⚡Results
The API returns a JSON object containing the top 5 columns of each Excel file in the specified folders, ranked by the sum of the values in each column.

![image](https://user-images.githubusercontent.com/108644811/225906918-e77f10a5-99cc-4525-9c9e-608ced58d515.png)


# 🔥Execution
`info/excel_files_ranker_api.ipynb` describes the execution steps of this program pipeline in detail.


# 📝Notes
- This code assumes that the first 5 rows of each Excel file are header information and skips them.

- This code only works with .xlsx file extensions.

- The API can be accessed at localhost:5000/home.

- The code has only been tested on Windows machines.


# 👤 Authors

- sbeen1840

# 🏷 License

- This project is licensed under the `MIT License` - see the [LICENSE](notion://www.notion.so/LICENSE) file for details

# 🙏 Acknowledgments

# ✍ References
