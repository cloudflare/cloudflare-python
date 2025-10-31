# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Organization", "Meta", "MetaFlags", "Parent", "Profile"]


class MetaFlags(BaseModel):
    account_creation: str

    account_deletion: str

    account_migration: str

    account_mobility: str

    sub_org_creation: str


class Meta(BaseModel):
    flags: Optional[MetaFlags] = None
    """Organization flags for feature enablement"""

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


class Profile(BaseModel):
    business_address: str

    business_email: str

    business_name: str

    business_phone: str

    external_metadata: str


class Organization(BaseModel):
    id: str

    create_time: datetime

    meta: Meta

    name: str

    parent: Optional[Parent] = None

    profile: Optional[Profile] = None
