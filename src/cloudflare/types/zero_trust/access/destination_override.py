# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["DestinationOverride"]


class DestinationOverride(BaseModel):
    behavior: Literal["public"]
    """The behavior to apply to matching requests."""

    path_pattern: str
    """The request path pattern to match.

    Wildcards (`*`) are supported, but each path segment may have at most one
    wildcard. Unlike the `uri` in public destinations, override path patterns do not
    implicitly cover subpaths; to do that, use a wildcard.
    """
