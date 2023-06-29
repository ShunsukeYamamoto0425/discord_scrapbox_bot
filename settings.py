# -------------------------------------------------------------------------------------------------
# .envファイルから値を読み込む [settings.py]
# Author:ShunsukeYamamoto Date:2023/06/29
# -------------------------------------------------------------------------------------------------

import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)

# settings.pyの相対パスを取得し、.envファイルを指定
dotenv_path = join(dirname(__file__), '.env')
# ファイルの中身を読み取る
load_dotenv(dotenv_path)

# 環境変数を参照
TOKEN = os.environ.get("TOKEN")
PROJECT_NAME = os.environ.get("PROJECT_NAME")