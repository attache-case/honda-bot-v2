import textwrap
from app.models.rps_stat import RpsStat, update_rps_stat
import discord
import logging

from app.models.enum_rps import Hand, Result
from app.models.game_rps import GameRPS
from app.models.rps_history import RpsHistory
from app.models.user import User, update_user

import constants

logger = logging.getLogger(__name__)


RESULT_HAND_FILEPATHS_MAP = {
    Result.WIN: {
        Hand.ROCK: constants.FILEPATHS_WIN,
        Hand.PAPER: constants.FILEPATHS_WIN,
        Hand.SCISSORS: constants.FILEPATHS_WIN
    },
    Result.LOSE: {
        Hand.ROCK: constants.FILEPATHS_LOSE_R,
        Hand.PAPER: constants.FILEPATHS_LOSE_P,
        Hand.SCISSORS: constants.FILEPATHS_LOSE_S
    }
}

RESULT_HAND_MSG_MAP = {
    Result.WIN: {
        Hand.ROCK: constants.MSG_WIN,
        Hand.PAPER: constants.MSG_WIN,
        Hand.SCISSORS: constants.MSG_WIN
    },
    Result.LOSE: {
        Hand.ROCK: constants.MSG_LOSE_R,
        Hand.PAPER: constants.MSG_LOSE_P,
        Hand.SCISSORS: constants.MSG_LOSE_S
    }
}


class Honda(object):

    ch = None

    async def send_message(self, msg):
        await self.ch.send(msg)

    async def send_message_with_files(self, msg, filepaths):
        files = [discord.File(filepath) for filepath in filepaths]
        await self.ch.send(msg, files=files)

    async def process_message(self, message):
        self.ch = None
        self.ch = message.channel
        if self.ch is None:
            logger.error(
                f'action=process_message Channel of message was None.')
            return
        await self.process_command(message)
        await self.process_greeting(message)
        await self.process_rps(message)

    async def process_command(self, message):
        if message.content.startswith('!stats'):
            await self.respond_stats(message.author)
        elif message.content.startswith('!allstats'):
            await self.respond_allstats()

    async def process_greeting(self, message):
        if message.content.startswith("おはよう"):
            await self.respond_greeting_morning(message)
        elif message.content.startswith("こんにちは"):
            await self.respond_greeting_noon(message)
        elif message.content.startswith("こんばんは"):
            await self.respond_greeting_evening(message)

    async def process_rps(self, message):
        player = message.author
        uid = player.id
        uname = player.name
        hands = GameRPS.parse_hands(message.content)
        if hands == Hand(0):
            return
        if GameRPS.has_played_today(uid):
            await self.send_message(constants.MSG_DAILY_LIMIT_EXCEEDED)
            return
        if not GameRPS.is_valid_hand(hands):
            await self.send_message(constants.MSG_TOO_MANY_HANDS)
            return
        hand = hands
        result = GameRPS.decide_result()

        # TODO: make this part atomic
        update_user(uid, uname)
        rps_history = RpsHistory.create(uid, hand, result)
        update_rps_stat(uid, hand, result, rps_history.created_at)

        await self.respond_rps(hand, result)

    async def respond_stats(self, player):
        uid = player.id
        rps_stat = RpsStat.get_by_uid(uid)
        if rps_stat is None:
            msg = textwrap.dedent(f"""\
                {player.name}さんのデータは存在しないみたいやで！
                一回じゃんけんしてみようや！
            """)
            await self.send_message(msg)
        else:
            wins = rps_stat.result_win_cnt
            loses = rps_stat.result_lose_cnt
            draws = rps_stat.result_draw_cnt
            total = wins + loses + draws
            cont_wins = rps_stat.continuous_win_cnt
            cont_loses = rps_stat.continuous_lose_cnt
            cont_logins = rps_stat.continuous_login_cnt
            msg = textwrap.dedent(f"""\
                {player.name}さんの戦績：
                {wins}勝{loses}敗 => 勝率 {(wins/total):.2%}
            """)
            if cont_wins >= 2:
                msg += '\n'
                msg += f'{cont_wins}連勝中'
            elif cont_loses >= 2:
                msg += '\n'
                msg += f'{cont_loses}連敗中'
            if cont_logins >= 2:
                msg += '\n'
                msg += f'{cont_logins}日連続ログイン中'
            await self.send_message(msg)

    async def respond_allstats(self):
        rps_stats = RpsStat.get_all_rps_stats()
        users = User.get_all_users()
        uid_uname_map = {user.dc_uid: user.dc_uname for user in users}
        if not rps_stats:
            msg = textwrap.dedent(f"""\
                誰のデータも存在しないみたいやで！
                みんなじゃんけんしてみようや！
            """)
            await self.send_message(msg)
        else:
            rps_stats.sort(key=lambda x: x.result_win_cnt /
                           (x.result_win_cnt+x.result_lose_cnt+x.result_draw_cnt), reverse=True)
            msg_list = []
            for rps_stat in rps_stats:
                uid = rps_stat.dc_uid
                wins = rps_stat.result_win_cnt
                loses = rps_stat.result_lose_cnt
                draws = rps_stat.result_draw_cnt
                total = wins + loses + draws
                msg_list.append(
                    f'{uid_uname_map[uid]}さん：{wins}勝{loses}敗 => 勝率 {(wins/total):.2%}')
            await self.send_message('\n'.join(msg_list))

    async def respond_greeting_morning(self, message):
        msg = 'おはようございます、' + message.author.name + 'さん！'
        await self.send_message(msg)

    async def respond_greeting_noon(self, message):
        msg = 'ちーっす、' + message.author.name + 'さん！'
        await self.send_message(msg)

    async def respond_greeting_evening(self, message):
        msg = 'こんばんは、' + message.author.name + 'さん！'
        await self.send_message(msg)

    async def respond_rps(self, hand, result):
        msg = GameRPS.create_rps_battle_string(
            hand, result, opponent_name='HONDA')
        msg += '\n'
        msg += RESULT_HAND_MSG_MAP[result][hand]
        filepaths = RESULT_HAND_FILEPATHS_MAP[result][hand]
        await self.send_message_with_files(msg, filepaths)


# Singleton
honda = Honda()
