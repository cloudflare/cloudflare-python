# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["RulesetsRulesetsResponse", "RulesetsRulesetsResponseItem"]


class RulesetsRulesetsResponseItem(BaseModel):
    kind: Literal["managed", "custom", "root", "zone"]
    """The kind of the ruleset."""

    name: str
    """The human-readable name of the ruleset."""

    phase: Literal[
        "ddos_l4",
        "ddos_l7",
        "http_config_settings",
        "http_custom_errors",
        "http_log_custom_fields",
        "http_ratelimit",
        "http_request_cache_settings",
        "http_request_dynamic_redirect",
        "http_request_firewall_custom",
        "http_request_firewall_managed",
        "http_request_late_transform",
        "http_request_origin",
        "http_request_redirect",
        "http_request_sanitize",
        "http_request_sbfm",
        "http_request_select_configuration",
        "http_request_transform",
        "http_response_compression",
        "http_response_firewall_managed",
        "http_response_headers_transform",
        "magic_transit",
        "magic_transit_ids_managed",
        "magic_transit_managed",
    ]
    """The phase of the ruleset."""

    id: Optional[str] = None
    """The unique ID of the ruleset."""

    description: Optional[str] = None
    """An informative description of the ruleset."""

    last_updated: Optional[datetime] = None
    """The timestamp of when the ruleset was last modified."""

    version: Optional[str] = None
    """The version of the ruleset."""


RulesetsRulesetsResponse = List[RulesetsRulesetsResponseItem]
