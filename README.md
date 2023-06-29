# Discord メッセージ保存Bot『かしわ』

特定のリアクションがついたメッセージの内容を保存します。<br>
（正確には、Scrapboxにページを作成するためのURLを生成します）

## 必要なもの

Python 3.8 以降で動作します。<br>
また、`discord.py`と`python-dotenv`の2つのライブラリをインストールしておいてください。

    $ -m pip install -U discord.py
    $ -m pip install python-dotenv

## 起動手順

1. `.env`ファイルにDiscordBotのトークンとScrapboxのプロジェクト名を書き込む<br>
1. `main.py`を実行

## 使い方

1. 誰かが良いこと言ったら、そのメッセージにリアクションをつける（デフォルトでは🗒️）<br>
1. かしわが生成したURLをクリックして、ページを作成

※Scrapboxのプロジェクト設定がPrivateの場合、Memberである必要があります。