# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .waiting_room_rule import WaitingRoomRule

__all__ = ["RuleUpdateResponse"]

RuleUpdateResponse: TypeAlias = List[WaitingRoomRule]
