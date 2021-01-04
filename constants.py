import textwrap

MSG_HELLO = '本田ロイド、再起動したで！'

DISCORD_EMOJI_R = ':fist:'
DISCORD_EMOJI_S = ':v:'
DISCORD_EMOJI_P = ':hand_splayed:'

HAND_R_KEYWORDS = [
    'ぐー',
    'グー',
    'gu',
    'rock',
    'Rock',
    'ROCK',
    DISCORD_EMOJI_R,
    '✊'
]
HAND_S_KEYWORDS = [
    'ちょき',
    'チョキ',
    'choki',
    'cyoki',
    'tyoki',
    'scissors',
    'Scissors',
    'SCISSORS',
    DISCORD_EMOJI_S,
    '✌'
]
HAND_P_KEYWORDS = [
    'ぱー',
    'パー',
    'pa',
    'paper',
    'Paper',
    'PAPER',
    DISCORD_EMOJI_P,
    '🖐'
]

MSG_DAILY_LIMIT_EXCEEDED = textwrap.dedent("""\
    じゃんけんは1日1回まで！
    ほな、また明日！
""")
MSG_TOO_MANY_HANDS = textwrap.dedent("""\
    手を複数同時に出すのは反則やで！
""")
MSG_WIN = textwrap.dedent("""\
    やるやん。
    明日は俺にリベンジさせて。
    では、どうぞ。
""")
MSG_LOSE_R = textwrap.dedent("""\
    俺の勝ち！
    負けは次につながるチャンスです！
    ネバーギブアップ！
    ほな、いただきます！
""")
MSG_LOSE_S = textwrap.dedent("""\
    俺の勝ち！
    たかがじゃんけん、そう思ってないですか？
    それやったら明日も、俺が勝ちますよ
    ほな、いただきます！
""")
MSG_LOSE_P = textwrap.dedent("""\
    俺の勝ち！
    なんで負けたか、明日まで考えといてください。
    そしたら何かが見えてくるはずです
    ほな、いただきます！
""")
FILEPATHS_WIN = [
    'contents/imgs/honda_win.png'
]
FILEPATHS_LOSE_R = [
    'contents/gifs/honda_p.gif'
]
FILEPATHS_LOSE_S = [
    'contents/gifs/honda_r.gif'
]
FILEPATHS_LOSE_P = [
    'contents/gifs/honda_s.gif'
]
YOUTUBE_LOSE_R = 'https://youtu.be/LhPJcvJLNEA'
YOUTUBE_LOSE_S = 'https://youtu.be/SWNCYpeDTfo'
YOUTUBE_LOSE_P = 'https://youtu.be/28d78XP1TJs'
