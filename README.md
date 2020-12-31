﻿# honda-bot

# About
- じゃんけんをしてくれる本田ロイドです
- Discordの`honda-bot`チャンネルで「ぐー」とか発言するとじゃんけんをしてくれます

## Usage
```
python main.py
```

## Installation (TBD)
1. Add bot to your server
1. Set environment variable `DISCORD_TOKEN` to your bot token
1. Add channel named `honda-bot` to your server


## EC2インスタンスへの操作
1. python3のインストール
https://qiita.com/yuta-38/items/12fbb94363dd00b4e299
1. codedeploy-agentのインストール
https://qiita.com/yukofeb/items/e077fc8755416c904032#appspec%E4%BD%9C%E6%88%90

## Requirements
- Python < 3.7(checking)
- discord.py==1.0.1(checking)

## Patch Notes
`v1.1.0`
- 勝率が10%になりました
- ✊✌🖐などの絵文字にも反応するようになりました
- その他，メッセージ内容など微調整を行いました

`v1.0.0`
- 勝率が50%になりました
- じゃんけんできるのは1日1回までになりました
  - 24時間ごとにbotが自動で再起動するタイミングでリセットされます
- bot起動時メッセージを追加しました
- `honda-bot`という名前のチャンネルでのみ反応するようになりました
- その他，メッセージ内容など微調整を行いました
