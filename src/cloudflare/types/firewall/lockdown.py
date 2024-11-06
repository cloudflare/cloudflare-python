# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from datetime import datetime

from ..._models import BaseModel
from .lockdown_url import LockdownURL
from .configuration import Configuration

__all__ = ["Lockdown"]


class Lockdown(BaseModel):
    id: str
    """The unique identifier of the Zone Lockdown rule."""

    configurations: Configuration
    """
    A list of IP addresses or CIDR ranges that will be allowed to access the URLs
    specified in the Zone Lockdown rule. You can include any number of `ip` or
    `ip_range` configurations.
    """

    created_on: datetime
    """The timestamp of when the rule was created."""

    description: str
    """An informative summary of the rule."""

    modified_on: datetime
    """The timestamp of when the rule was last modified."""

    paused: bool
    """When true, indicates that the rule is currently paused."""

    urls: List[LockdownURL]
    """The URLs to include in the rule definition.

    You can use wildcards. Each entered URL will be escaped before use, which means
    you can only use simple wildcard patterns.
    """
