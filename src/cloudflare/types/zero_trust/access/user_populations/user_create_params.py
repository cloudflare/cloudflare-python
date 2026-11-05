# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import datetime
from typing_extensions import Required, Annotated, TypedDict

from ....._types import SequenceNotStr
from ....._utils import PropertyInfo

__all__ = ["UserCreateParams", "Email", "Meta", "Name"]


class UserCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    active: bool

    display_name: Annotated[str, PropertyInfo(alias="displayName")]

    emails: Iterable[Email]

    external_id: Annotated[str, PropertyInfo(alias="externalId")]

    meta: Meta

    name: Name

    schemas: SequenceNotStr[str]
    """The SCIM schemas that apply to this resource."""

    user_name: Annotated[str, PropertyInfo(alias="userName")]


class Email(TypedDict, total=False):
    primary: bool

    type: str

    value: str


class Meta(TypedDict, total=False):
    created: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    last_modified: Annotated[Union[str, datetime], PropertyInfo(alias="lastModified", format="iso8601")]

    location: str

    resource_type: Annotated[str, PropertyInfo(alias="resourceType")]

    version: str


class Name(TypedDict, total=False):
    family_name: Annotated[str, PropertyInfo(alias="familyName")]

    formatted: str

    given_name: Annotated[str, PropertyInfo(alias="givenName")]

    honorific_prefix: Annotated[str, PropertyInfo(alias="honorificPrefix")]

    honorific_suffix: Annotated[str, PropertyInfo(alias="honorificSuffix")]

    middle_name: Annotated[str, PropertyInfo(alias="middleName")]
