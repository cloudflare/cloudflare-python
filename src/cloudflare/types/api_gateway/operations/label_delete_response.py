# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["LabelDeleteResponse", "Label"]


class Label(BaseModel):
    created_at: datetime

    description: str
    """The description of the label"""

    last_updated: datetime

    metadata: object
    """Metadata for the label"""

    name: str
    """The name of the label"""

    source: Literal["user", "managed"]
    """
    - `user` - label is owned by the user
    - `managed` - label is owned by cloudflare
    """


class LabelDeleteResponse(BaseModel):
    endpoint: str
    """
    The endpoint which can contain path parameter templates in curly braces, each
    will be replaced from left to right with {varN}, starting with {var1}, during
    insertion. This will further be Cloudflare-normalized upon insertion. See:
    https://developers.cloudflare.com/rules/normalization/how-it-works/.
    """

    host: str
    """RFC3986-compliant host."""

    last_updated: datetime

    method: Literal["GET", "POST", "HEAD", "OPTIONS", "PUT", "DELETE", "CONNECT", "PATCH", "TRACE"]
    """The HTTP method used to access the endpoint."""

    operation_id: str
    """UUID."""

    labels: Optional[List[Label]] = None
