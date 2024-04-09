# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["AdditionalRoutesParam"]


class AdditionalRoutesParam(TypedDict, total=False):
    host: str
    """The hostname to which this waiting room will be applied (no wildcards).

    The hostname must be the primary domain, subdomain, or custom hostname (if using
    SSL for SaaS) of this zone. Please do not include the scheme (http:// or
    https://).
    """

    path: str
    """Sets the path within the host to enable the waiting room on.

    The waiting room will be enabled for all subpaths as well. If there are two
    waiting rooms on the same subpath, the waiting room for the most specific path
    will be chosen. Wildcards and query parameters are not supported.
    """
