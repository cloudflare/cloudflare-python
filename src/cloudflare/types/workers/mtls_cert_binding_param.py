# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["MTLSCERTBindingParam"]


class MTLSCERTBindingParam(TypedDict, total=False):
    certificate_id: Required[str]
    """ID of the certificate to bind to"""

    type: Required[Literal["mtls_certificate"]]
    """The class of resource that the binding provides."""
