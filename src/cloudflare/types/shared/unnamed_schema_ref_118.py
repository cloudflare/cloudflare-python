# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UnnamedSchemaRef118"]


class UnnamedSchemaRef118(BaseModel):
    none: Optional[int] = None
    """The number of requests served over HTTP."""

    tl_sv1: Optional[int] = FieldInfo(alias="TLSv1", default=None)
    """The number of requests served over TLS v1.0."""

    tl_sv1_1: Optional[int] = FieldInfo(alias="TLSv1.1", default=None)
    """The number of requests served over TLS v1.1."""

    tl_sv1_2: Optional[int] = FieldInfo(alias="TLSv1.2", default=None)
    """The number of requests served over TLS v1.2."""

    tl_sv1_3: Optional[int] = FieldInfo(alias="TLSv1.3", default=None)
    """The number of requests served over TLS v1.3."""
