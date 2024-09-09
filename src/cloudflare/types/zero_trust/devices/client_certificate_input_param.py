# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ClientCertificateInputParam"]


class ClientCertificateInputParam(TypedDict, total=False):
    certificate_id: Required[str]
    """UUID of Cloudflare managed certificate."""

    cn: Required[str]
    """Common Name that is protected by the certificate"""
