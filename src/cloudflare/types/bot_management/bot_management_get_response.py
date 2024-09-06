# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .bot_fight_mode_configuration import BotFightModeConfiguration

from .super_bot_fight_mode_definitely_configuration import SuperBotFightModeDefinitelyConfiguration

from .super_bot_fight_mode_likely_configuration import SuperBotFightModeLikelyConfiguration

from .subscription_configuration import SubscriptionConfiguration

from typing_extensions import TypeAlias

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["BotManagementGetResponse"]

BotManagementGetResponse: TypeAlias = Union[
    BotFightModeConfiguration,
    SuperBotFightModeDefinitelyConfiguration,
    SuperBotFightModeLikelyConfiguration,
    SubscriptionConfiguration,
]
