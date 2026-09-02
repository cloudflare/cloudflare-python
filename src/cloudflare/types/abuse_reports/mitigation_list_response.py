# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["MitigationListResponse", "Mitigation"]


class Mitigation(BaseModel):
    id: str
    """ID of remediation."""

    effective_date: str
    """Date when the mitigation will become active.

    Time in RFC 3339 format (https://www.rfc-editor.org/rfc/rfc3339.html)
    """

    entity_id: str

    entity_type: Literal["url_pattern", "account", "zone", "custom_expression"]
    """The type of entity targeted by a mitigation."""

    status: Literal["pending", "active", "in_review", "cancelled", "removed"]
    """The status of a mitigation"""

    type: str
    """The type of mitigation applied to a reported entity."""


class MitigationListResponse(BaseModel):
    mitigations: List[Mitigation]
