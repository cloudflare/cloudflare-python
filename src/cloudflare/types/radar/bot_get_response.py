# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BotGetResponse", "Bot"]


class Bot(BaseModel):
    category: str
    """The category of the bot."""

    description: str
    """A summary for the bot (e.g., purpose)."""

    kind: str
    """The kind of the bot."""

    name: str
    """The name of the bot."""

    operator: str
    """The organization that owns and operates the bot."""

    operator_url: str = FieldInfo(alias="operatorUrl")
    """The link to the bot documentation."""

    slug: str
    """A kebab-case identifier derived from the bot name."""

    user_agent_patterns: List[str] = FieldInfo(alias="userAgentPatterns")

    user_agents: List[str] = FieldInfo(alias="userAgents")

    signature_agent_url: Optional[str] = FieldInfo(alias="signatureAgentUrl", default=None)
    """
    The URL of the agent's [Web Bot Auth](https://blog.cloudflare.com/web-bot-auth/)
    resource. Null for bots not verified via request signature.
    """


class BotGetResponse(BaseModel):
    bot: Bot
