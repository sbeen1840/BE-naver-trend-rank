# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 14:15:59 2023

@author: sbeen
"""

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
            print(folder_path)

            if os.path.isdir(folder_path):
                files = [file for file in os.listdir(folder_path) if file.endswith(self.extension)]
                print(files)
                df = pd.DataFrame()

                for file in files:
                    df_temp = pd.read_csv(os.path.join(folder_path, file))
                    # df_temp = pd.read_excel(os.path.join(folder_path, file))
                    # df_temp = df_temp.iloc[5:]
                    df = pd.concat([df, df_temp], axis=0)
                
                df['총조회수'] = df['총조회수'].str.replace(',', '').astype(float)
                sorted_df = df.sort_values(by='총조회수', ascending=False)
                keyword_values = sorted_df.head(5)['키워드'] # 열 이름은 리스트형태로 넣어서 줘야함
                final_dict = keyword_values.reset_index(drop=True)
                final_dict = final_dict.to_dict()
                self.result[folder]=final_dict
                


    def run(self):
        self.app.run()

if __name__ == '__main__':
    ranker = Ranker('C:/Users/sbeen/OneDrive/바탕 화면/키워드파일/', '.csv', ['국비교육', '취업분야', '프로그래밍언어'])
    ranker.run()
