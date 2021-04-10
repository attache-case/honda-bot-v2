# honda-bot

## About
- じゃんけんをしてくれる本田ロイドです
- Discordの特定のチャンネルで「ぐー」とか発言するとじゃんけんをしてくれます

## Feature
- ログイン時にランダムに本田圭佑の名言を投稿します
- 特定のチャンネルで「ぐー」などじゃんけんの手を含んだ投稿をするとじゃんけんをしてくれます
- 自分の勝率や、同じDiscordサーバーで他にじゃんけんをしている人全員の勝率を見ることが出来ます

## Usage
※botが参加しているDiscordサーバーの、`ACTIVE_CHANNEL_NAME`でしていしたチャンネルに対する投稿にのみ反応します。
- あいさつをする
  - `おはよう`・`こんにちは`・`こんばんは`で始まる投稿をするとあいさつを返してくれます
- じゃんけんをする
  - `ぐー`・`ちょき`・`ぱー`などじゃんけんの手を含む投稿をすると勝率`10%`でじゃんけんをしてくれます
- 統計情報を見る
  - `!stats`コマンド
    - 自分の勝率が確認出来ます
  - `!allstats`コマンド
    - サーバーでじゃんけんしたことがある人の勝率が高い順に表示されます


## Installation (Beta)
1. Add bot to your server
2. Set up to deploy this bot in Heroku
3. Set environment variable `DISCORD_ACCESS_TOKEN` to the access token of your bot
4. Set environment variable `ACTIVE_CHANNEL_NAME` to the channel name you plan the bot to respond
5. (Optional) Add channel named `<ACTIVE_CHANNEL_NAME>` to your server if you don't have it yet

## Requirements
- Python > 3.3 <= 3.6.13
- discord.py==1.5.1
- SQLAlchemy==1.3.22
- psycopg2

## TODO
- DB処理のアトミック化
- 機能拡張（手の統計・連続ログインボーナス）
- パッケージ構造見直し
- 10,000件を超えたときの対応検討(Heroku PostgreSQLの無料上限)

## Patch Notes
`v2.1.0`
- Herokuで動作するように構成を変更しました
- botのログイン（再起動）時に本田圭佑の名言を投稿するようになりました
`v2.0.0`
- じゃんけん結果のGIFを軽量化しました
- `!stats`コマンドで連勝数・連敗数・連続ログイン日数がするようになりました
- いつ・どの手を出して・勝ったか負けたかの履歴をDBに保存するようになりました
