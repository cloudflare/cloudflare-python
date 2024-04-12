# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .zero_trust import Tunnel
from .warp_connector import WARPConnector

__all__ = ["WARPConnectorDeleteResponse"]

WARPConnectorDeleteResponse = Union[Tunnel, WARPConnector]
