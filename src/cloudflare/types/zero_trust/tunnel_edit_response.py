# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union

from .tunnel import Tunnel
from ..warp_connector import WARPConnector

__all__ = ["TunnelEditResponse"]

TunnelEditResponse = Union[Tunnel, WARPConnector]
