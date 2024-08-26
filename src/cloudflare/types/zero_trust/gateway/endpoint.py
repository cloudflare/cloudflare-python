# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ...._models import BaseModel

from typing import Optional

from .doh_endpoint import DOHEndpoint

from .dot_endpoint import DOTEndpoint

from .ipv4_endpoint import IPV4Endpoint

from .ipv6_endpoint import IPV6Endpoint

from typing import Optional, Union, List, Dict, Any
from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["Endpoint"]

class Endpoint(BaseModel):
    doh: Optional[DOHEndpoint] = None

    dot: Optional[DOTEndpoint] = None

    ipv4: Optional[IPV4Endpoint] = None

    ipv6: Optional[IPV6Endpoint] = None