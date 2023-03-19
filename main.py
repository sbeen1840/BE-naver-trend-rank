from flask import Flask, jsonify
import pandas as pd
import os

class Ranker:
    def __init__(self, masterpath, extension, folders):
        self.masterpath = masterpath
        self.extension = extension
        self.folders = folders
        self.result = {}
        
        self.app = Flask(__name__)
        self.app.config['JSON_AS_ASCII'] = False
        
        @self.app.route('/home', methods=['GET'])
        def getjson():
            return jsonify(self.result)
        
        self.getrank()
        
    def getrank(self):
        for folder in self.folders:
            folder_path = os.path.join(self.masterpath, folder)

            if os.path.isdir(folder_path):
                files = [file for file in os.listdir(folder_path) if file.endswith(self.extension)]
                df = pd.DataFrame()

                for file in files:
                    df_temp = pd.read_excel(os.path.join(folder_path, file))
                    df_temp = df_temp.iloc[5:]
                    df = pd.concat([df, df_temp], axis=1)

                df = df.drop(df.columns[::2], axis=1)
                df.columns = df.iloc[0]
                df = df.drop(df.index[0])
                df = df.astype(float)
                sums = df.sum()
                rank = sums.sort_values(ascending=False)
                head = rank.head(5)
                index = head.index
                series = index.to_series()
                dictionary = {i+1: val for i, val in enumerate(series)}
                self.result[folder] = dictionary

    def run(self):
        self.app.run()

if __name__ == '__main__':
    ranker = Ranker('C:/Users/sbeen/OneDrive/바탕 화면/네이버트렌드파일/', '.xlsx', ['국비교육', '취업분야', '프로그래밍언어'])
    ranker.run()
