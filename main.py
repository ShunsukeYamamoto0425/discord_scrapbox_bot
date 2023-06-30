# -------------------------------------------------------------------------------------------------
# Discord メッセージ保存Bot [main.py]
# Author:ShunsukeYamamoto Date:2023/06/29
# -------------------------------------------------------------------------------------------------

# インストールした discord.py を読み込む
import discord
# 日付を扱う
import datetime
# .envファイルから値を読み込む
import settings

# DiscordBotのアクセストークン
TOKEN = settings.TOKEN
# Scrapboxのプロジェクト名
PROJECT_NAME = settings.PROJECT_NAME

# Botが反応する絵文字
EVENT_EMOJI = '🗒️'
# ページタイトルの文字数上限
TITLE_LENGTH_MAX = 30
# 本文の文字数上限
BODY_LENGTH_MAX = 1000

# インテントを生成
intents = discord.Intents.default()
intents.message_content = True
# 接続に必要なオブジェクトを生成
client = discord.Client(intents=intents)


# -----------------------------------------------
# 起動時に動作する処理
@client.event
async def on_ready():
  # 起動したらターミナルにログイン通知が表示される
  print(f'We have logged in as {client.user}')
# -----------------------------------------------


# -----------------------------------------------
# リアクション追加時に実行される
@client.event
async def on_raw_reaction_add(payload):

  # サーバー
  guild = client.get_guild(payload.guild_id)
  # リアクションされたメッセージがあるチャンネル
  txt_channel = client.get_channel(payload.channel_id)
  # リアクションされたメッセージ
  message = await txt_channel.fetch_message(payload.message_id)
  # リアクションされたユーザー
  message_author = await guild.fetch_member(message.author.id)
  # リアクションしたユーザー
  reaction_author = payload.member
  
  # 自分自身に対するリアクションは通知しない
  #if(message.author == reaction_author):
  #  return
  # ↑
  # 良いこと言ったなって自分で思った場合を考慮してコメントアウトした（2023/06/27）

  # 本Botに対するリアクションは通知しない
  if(message_author == client.user):
    return
  
  # 特定の絵文字以外は通知しない
  if(payload.emoji.name != EVENT_EMOJI):
    return

  # Botの発言内容
  msg = f"{reaction_author.mention}\n\
発言者:{message_author.display_name} さん\n\
クリックでScrapboxにページをつくるよ\n\
↓\n\
https://scrapbox.io/{PROJECT_NAME}/{message.content[:TITLE_LENGTH_MAX]}?body=%23{message_author.display_name}+%23{datetime.date.today()}%0D{message.content[:BODY_LENGTH_MAX]}"

  # メッセージ送信
  await message.channel.send(msg)
# -----------------------------------------------


# Botの起動とDiscordサーバーへの接続
client.run(TOKEN)


# -------------------------------------------------------------------------------------------------