# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RobotGetResponse", "UserAgents", "UserAgentsContentSignals"]


class UserAgentsContentSignals(BaseModel):
    """Content signal directives from robots.txt."""

    ai_input: Optional[Literal["yes", "no"]] = FieldInfo(alias="ai-input", default=None)
    """Whether AI input usage is permitted."""

    ai_train: Optional[Literal["yes", "no"]] = FieldInfo(alias="ai-train", default=None)
    """Whether AI training is permitted."""

    search: Optional[Literal["yes", "no"]] = None
    """Whether search indexing is permitted."""


class UserAgents(BaseModel):
    """Parsed rules for a specific user-agent."""

    allow: List[str]
    """List of allowed path patterns."""

    disallow: List[str]
    """List of disallowed path patterns."""

    content_signals: Optional[UserAgentsContentSignals] = FieldInfo(alias="contentSignals", default=None)
    """Content signal directives from robots.txt."""

    crawl_delay: Optional[float] = FieldInfo(alias="crawlDelay", default=None)
    """Crawl delay in seconds."""


class RobotGetResponse(BaseModel):
    """Parsed robots.txt rules for a single domain."""

    user_agents: Dict[str, UserAgents] = FieldInfo(alias="userAgents")
    """Map of user-agent string to its parsed rules."""

    sitemaps: Optional[List[str]] = None
    """List of sitemap URLs found in robots.txt."""

    status: Optional[int] = None
    """HTTP status code from fetching the robots.txt file."""
