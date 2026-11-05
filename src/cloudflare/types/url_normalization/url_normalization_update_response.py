# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = [
    "URLNormalizationUpdateResponse",
    "UnionMember0",
    "UnionMember1",
    "UnionMember2",
    "UnionMember3",
    "UnionMember4",
]


class UnionMember0(BaseModel):
    scope: Optional[Literal["incoming", "both", "none"]] = None
    """The scope of the URL normalization."""

    type: Optional[Literal["cloudflare", "rfc3986"]] = None
    """The type of URL normalization performed by Cloudflare."""


class UnionMember1(BaseModel):
    scope: Optional[Literal["incoming", "both", "none"]] = None
    """The scope of the URL normalization."""

    type: Optional[Literal["cloudflare", "rfc3986"]] = None
    """The type of URL normalization performed by Cloudflare."""


class UnionMember2(BaseModel):
    scope: Optional[Literal["incoming", "both", "none"]] = None
    """The scope of the URL normalization."""

    type: Optional[Literal["cloudflare", "rfc3986"]] = None
    """The type of URL normalization performed by Cloudflare."""


class UnionMember3(BaseModel):
    scope: Optional[Literal["incoming", "both", "none"]] = None
    """The scope of the URL normalization."""

    type: Optional[Literal["cloudflare", "rfc3986"]] = None
    """The type of URL normalization performed by Cloudflare."""


class UnionMember4(BaseModel):
    scope: Optional[Literal["incoming", "both", "none"]] = None
    """The scope of the URL normalization."""

    type: Optional[Literal["cloudflare", "rfc3986"]] = None
    """The type of URL normalization performed by Cloudflare."""


URLNormalizationUpdateResponse: TypeAlias = Union[
    Optional[UnionMember0], UnionMember1, UnionMember2, UnionMember3, UnionMember4
]
