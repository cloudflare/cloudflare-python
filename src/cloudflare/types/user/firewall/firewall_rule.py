# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel
from ...firewall import (
    ASNConfiguration,
    IPV6Configuration,
    CountryConfiguration,
    AccessRuleIPConfiguration,
    AccessRuleCIDRConfiguration,
)

__all__ = ["FirewallRule", "Configuration"]

Configuration = Union[
    AccessRuleIPConfiguration, IPV6Configuration, AccessRuleCIDRConfiguration, ASNConfiguration, CountryConfiguration
]


class FirewallRule(BaseModel):
    id: str
    """The unique identifier of the IP Access rule."""

    allowed_modes: List[Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]]
    """The available actions that a rule can apply to a matched request."""

    configuration: Configuration
    """The rule configuration."""

    mode: Literal["block", "challenge", "whitelist", "js_challenge", "managed_challenge"]
    """The action to apply to a matched request."""

    created_on: Optional[datetime] = None
    """The timestamp of when the rule was created."""

    modified_on: Optional[datetime] = None
    """The timestamp of when the rule was last modified."""

    notes: Optional[str] = None
    """
    An informative summary of the rule, typically used as a reminder or explanation.
    """
