# Discord メッセージ保存Bot『かしわ』

![kashiwa_screenshot1](https://github.com/ShunsukeYamamoto0425/discord_scrapbox_bot/assets/93860634/fe25eaca-bee9-4870-9445-03b91f729f5b)
![kashiwa_screenshot2](https://github.com/ShunsukeYamamoto0425/discord_scrapbox_bot/assets/93860634/f4d3395f-bf94-47db-b657-8178776a3911)

特定のリアクションがついたメッセージの内容を保存します。<br>
（正確には、Scrapboxにページを作成するためのURLを生成します）

## 必要なもの

Python 3.8 以降で動作します。<br>
`discord.py`と`python-dotenv`の2つのライブラリをインストールしておいてください。

    $ -m pip install -U discord.py
    $ -m pip install python-dotenv

また、環境変数を定義する`.env`ファイルが必要です。<br>
新しく作成する場合は、`env_template.txt`のファイル名を変更してお使いください。

### 環境変数

`TOKEN`……DiscordBotのアクセストークン<br>
`PROJECT_NAME`……Scrapboxのプロジェクト名

## 起動手順

1. `.env`ファイルにDiscordBotのトークンとScrapboxのプロジェクト名を書き込む<br>
1. `main.py` `settings.py` `.env`を同じディレクトリに配置<br>
1. `main.py`を実行

## 使い方

1. 誰かが良いこと言ったら、そのメッセージにリアクションをつける（デフォルトでは🗒️）<br>
1. かしわが生成したURLをクリックして、ページを作成

※Scrapboxのプロジェクト設定がPrivateの場合、Memberである必要があります。