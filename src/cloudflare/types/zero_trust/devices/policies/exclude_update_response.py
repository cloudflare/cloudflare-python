# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .split_tunnel_exclude import SplitTunnelExclude

__all__ = ["ExcludeUpdateResponse"]

ExcludeUpdateResponse: TypeAlias = List[SplitTunnelExclude]
