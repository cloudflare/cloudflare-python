# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .organization_profile import OrganizationProfile

__all__ = ["Organization", "Meta", "MetaFlags", "Parent"]


class MetaFlags(BaseModel):
    """Enable features for Organizations."""

    account_creation: str

    account_deletion: str

    account_migration: str

    account_mobility: str

    sub_org_creation: str


class Meta(BaseModel):
    flags: Optional[MetaFlags] = None
    """Enable features for Organizations."""

    hierarchy_tags: Optional[List[str]] = None
    """
    Ordered chain of organization tags from the root organization down to (and
    including) this organization itself. Root organizations return a single-element
    array containing their own tag; sub-organizations return
    `[rootTag, ...intermediateTags, parentTag, selfTag]`. Useful for constructing
    authorization scopes that need to cover every ancestor in the hierarchy.
    """

    managed_by: Optional[str] = None

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Parent(BaseModel):
    id: str

    name: str


class Organization(BaseModel):
    """References an Organization in the Cloudflare data model."""

    id: str

    create_time: datetime

    meta: Meta

    name: str

    parent: Optional[Parent] = None

    profile: Optional[OrganizationProfile] = None
