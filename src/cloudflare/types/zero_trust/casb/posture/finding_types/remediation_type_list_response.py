# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ......_models import BaseModel

__all__ = ["RemediationTypeListResponse"]


class RemediationTypeListResponse(BaseModel):
    """Information about a remediation type."""

    id: str
    """The identifier for the remediation type."""

    description: str
    """A description of the action(s) taken by the remediation type."""

    display_name: str
    """The name of the remediation type as displayed in the cloudflare dashboard."""

    finding_type_id: str
    """
    The identifier of the finding_type which this remediation type should remediate.
    """

    remediation_type: str
    """The name of the remediation type."""
