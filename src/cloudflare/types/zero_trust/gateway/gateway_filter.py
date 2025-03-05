# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["GatewayFilter"]

GatewayFilter: TypeAlias = Literal["http", "dns", "l4", "egress", "dns_resolver"]
