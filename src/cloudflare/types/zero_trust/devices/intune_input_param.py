# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["IntuneInputParam"]


class IntuneInputParam(TypedDict, total=False):
    compliance_status: Required[
        Literal["compliant", "noncompliant", "unknown", "notapplicable", "ingraceperiod", "error"]
    ]
    """Compliance Status"""

    connection_id: Required[str]
    """Posture Integration ID."""
