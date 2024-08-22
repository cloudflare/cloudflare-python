# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional, List

from typing_extensions import Literal

from datetime import datetime

from .gateway_filter import GatewayFilter

from .rule_setting import RuleSetting

from .schedule import Schedule

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["GatewayRule"]

class GatewayRule(BaseModel):
    id: Optional[str] = None
    """The API resource UUID."""

    action: Optional[Literal["on", "off", "allow", "block", "scan", "noscan", "safesearch", "ytrestricted", "isolate", "noisolate", "override", "l4_override", "egress", "audit_ssh", "resolve"]] = None
    """
    The action to preform when the associated traffic, identity, and device posture
    expressions are either absent or evaluate to `true`.
    """

    created_at: Optional[datetime] = None

    deleted_at: Optional[datetime] = None
    """Date of deletion, if any."""

    description: Optional[str] = None
    """The description of the rule."""

    device_posture: Optional[str] = None
    """The wirefilter expression used for device posture check matching."""

    enabled: Optional[bool] = None
    """True if the rule is enabled."""

    filters: Optional[List[GatewayFilter]] = None
    """
    The protocol or layer to evaluate the traffic, identity, and device posture
    expressions.
    """

    identity: Optional[str] = None
    """The wirefilter expression used for identity matching."""

    name: Optional[str] = None
    """The name of the rule."""

    precedence: Optional[int] = None
    """Precedence sets the order of your rules.

    Lower values indicate higher precedence. At each processing phase, applicable
    rules are evaluated in ascending order of this value.
    """

    rule_settings: Optional[RuleSetting] = None
    """Additional settings that modify the rule's action."""

    schedule: Optional[Schedule] = None
    """The schedule for activating DNS policies.

    This does not apply to HTTP or network policies.
    """

    traffic: Optional[str] = None
    """The wirefilter expression used for traffic matching."""

    updated_at: Optional[datetime] = None