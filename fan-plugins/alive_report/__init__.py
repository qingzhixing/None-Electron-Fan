from nonebot import get_plugin_config, on_command
from nonebot.rule import to_me
from nonebot.plugin import PluginMetadata

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="Alive Report",
    description="检测机器人存活状态",
    usage="指令为 /alive 或 /活着吗 或 /alive-check, 需要 @机器人 或者 私聊 才可使用",
    config=Config,
)

config = get_plugin_config(Config)

alive_check = on_command(
    "alive", rule=to_me(), aliases={"活着吗", "alive-check"}, priority=10, block=False
)


@alive_check.handle()
async def handle_alive_check():
    await alive_check.send("💮存活! I'm Alive!")
