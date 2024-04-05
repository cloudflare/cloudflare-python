# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["GsuiteGroupRule", "Gsuite"]


class Gsuite(BaseModel):
    connection_id: str
    """The ID of your Google Workspace identity provider."""

    email: str
    """The email of the Google Workspace group."""


class GsuiteGroupRule(BaseModel):
    gsuite: Gsuite
