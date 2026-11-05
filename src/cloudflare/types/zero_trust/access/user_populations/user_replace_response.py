# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["UserReplaceResponse", "Email", "Meta", "Name"]


class Email(BaseModel):
    primary: Optional[bool] = None

    type: Optional[str] = None

    value: Optional[str] = None


class Meta(BaseModel):
    created: Optional[datetime] = None

    last_modified: Optional[datetime] = FieldInfo(alias="lastModified", default=None)

    location: Optional[str] = None

    resource_type: Optional[str] = FieldInfo(alias="resourceType", default=None)

    version: Optional[str] = None


class Name(BaseModel):
    family_name: Optional[str] = FieldInfo(alias="familyName", default=None)

    formatted: Optional[str] = None

    given_name: Optional[str] = FieldInfo(alias="givenName", default=None)

    honorific_prefix: Optional[str] = FieldInfo(alias="honorificPrefix", default=None)

    honorific_suffix: Optional[str] = FieldInfo(alias="honorificSuffix", default=None)

    middle_name: Optional[str] = FieldInfo(alias="middleName", default=None)


class UserReplaceResponse(BaseModel):
    """A SCIM User resource. Additional SCIM extension attributes are supported."""

    id: Optional[str] = None

    active: Optional[bool] = None

    display_name: Optional[str] = FieldInfo(alias="displayName", default=None)

    emails: Optional[List[Email]] = None

    external_id: Optional[str] = FieldInfo(alias="externalId", default=None)

    meta: Optional[Meta] = None

    name: Optional[Name] = None

    schemas: Optional[List[str]] = None
    """The SCIM schemas that apply to this resource."""

    user_name: Optional[str] = FieldInfo(alias="userName", default=None)

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
