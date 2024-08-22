# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from ...._models import BaseModel

__all__ = ["WorkspaceOneInput"]


class WorkspaceOneInput(BaseModel):
    compliance_status: Literal["compliant", "noncompliant", "unknown"]
    """Compliance Status"""

    connection_id: str
    """Posture Integration ID."""
