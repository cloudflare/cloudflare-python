# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .subscription_configuration import SubscriptionConfiguration
from .bot_fight_mode_configuration import BotFightModeConfiguration
from .super_bot_fight_mode_likely_configuration import SuperBotFightModeLikelyConfiguration
from .super_bot_fight_mode_definitely_configuration import SuperBotFightModeDefinitelyConfiguration

__all__ = ["BotManagementUpdateResponse"]

BotManagementUpdateResponse: TypeAlias = Union[
    BotFightModeConfiguration,
    SuperBotFightModeDefinitelyConfiguration,
    SuperBotFightModeLikelyConfiguration,
    SubscriptionConfiguration,
]
