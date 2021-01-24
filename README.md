# honda-bot

# TODO
- EC2へのデプロイフロー確立（実行・停止・再実行）
- DB処理のアトミック化
- DBのインバウンド・アウトバウンドアクセス制御
- 機能拡張（手の統計・連続ログインボーナス）
- パッケージ構造見直し

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
sudo yum -y install gcc wget curl-devel expat-devel gettext-devel openssl-devel zlib-devel perl-ExtUtils-MakeMaker autoconf bzip2 bzip2-devel libbz2-dev openssl openssl-devel readline readline-devel sqlite-devel
1. python3のインストール(仮想環境)
https://qiita.com/yuta-38/items/12fbb94363dd00b4e299
https://messefor.hatenablog.com/entry/2020/08/22/181519
1. codedeploy-agentのインストール
https://qiita.com/yukofeb/items/e077fc8755416c904032#appspec%E4%BD%9C%E6%88%90
1. jqのインストール
https://qiita.com/toshiro3/items/37821bdcc50c8b6d06dc


## Requirements()
- Python > 3.3 <= 3.6.6(checking)
- discord.py==1.5.1(checking)
- SQLAlchemy==1.3.22
- PyMySQL==0.10.1

## Patch Notes
`v2.0.0`
- じゃんけん結果のGIFを軽量化しました
- 連勝数・連敗数・連続ログイン日数を記録するようになりました
- いつ・どの手を出して・勝ったか負けたかの履歴を保存するようになりました
