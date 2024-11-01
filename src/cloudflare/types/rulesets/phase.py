# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["Phase"]

Phase: TypeAlias = Literal[
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
    "http_request_transform",
    "http_response_compression",
    "http_response_firewall_managed",
    "http_response_headers_transform",
    "magic_transit",
    "magic_transit_ids_managed",
    "magic_transit_managed",
    "magic_transit_ratelimit",
]
