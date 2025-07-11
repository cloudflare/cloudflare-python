# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from ..._models import BaseModel

__all__ = ["BotListResponse", "Bot"]


class Bot(BaseModel):
    category: str
    """The category of the bot."""

    description: str
    """A summary for the bot (e.g., purpose)."""

    name: str
    """The name of the bot."""

    operator: str
    """The organization that owns and operates the bot."""

    slug: str
    """A kebab-case identifier derived from the bot name."""


class BotListResponse(BaseModel):
    bots: List[Bot]
