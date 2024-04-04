# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .unnamed_schema_ref_3248f24329456e19dfa042fff9986f72 import UnnamedSchemaRef3248f24329456e19dfa042fff9986f72
from .unnamed_schema_ref_ec4d85c3d1bcc6b3b7e99c199ae99846 import UnnamedSchemaRefEc4d85c3d1bcc6b3b7e99c199ae99846

__all__ = [
    "UnnamedSchemaRefE7c61ebe06ebfc3861ae8b9db4ba152b",
    "UnionMember0",
    "UnionMember0Result",
    "UnionMember0ResultAction",
    "UnionMember0ResultActor",
    "UnionMember0ResultOwner",
    "UnionMember0ResultResource",
    "AaaAPIResponseCommon",
]


class UnionMember0ResultAction(BaseModel):
    result: Optional[bool] = None
    """A boolean that indicates if the action attempted was successful."""

    type: Optional[str] = None
    """A short string that describes the action that was performed."""


class UnionMember0ResultActor(BaseModel):
    id: Optional[str] = None
    """The ID of the actor that performed the action.

    If a user performed the action, this will be their User ID.
    """

    email: Optional[str] = None
    """The email of the user that performed the action."""

    ip: Optional[str] = None
    """The IP address of the request that performed the action."""

    type: Optional[Literal["user", "admin", "Cloudflare"]] = None
    """The type of actor, whether a User, Cloudflare Admin, or an Automated System."""


class UnionMember0ResultOwner(BaseModel):
    id: Optional[str] = None
    """Identifier"""


class UnionMember0ResultResource(BaseModel):
    id: Optional[str] = None
    """An identifier for the resource that was affected by the action."""

    type: Optional[str] = None
    """A short string that describes the resource that was affected by the action."""


class UnionMember0Result(BaseModel):
    id: Optional[str] = None
    """A string that uniquely identifies the audit log."""

    action: Optional[UnionMember0ResultAction] = None

    actor: Optional[UnionMember0ResultActor] = None

    interface: Optional[str] = None
    """The source of the event."""

    metadata: Optional[object] = None
    """An object which can lend more context to the action being logged.

    This is a flexible value and varies between different actions.
    """

    new_value: Optional[str] = FieldInfo(alias="newValue", default=None)
    """The new value of the resource that was modified."""

    old_value: Optional[str] = FieldInfo(alias="oldValue", default=None)
    """The value of the resource before it was modified."""

    owner: Optional[UnionMember0ResultOwner] = None

    resource: Optional[UnionMember0ResultResource] = None

    when: Optional[datetime] = None
    """A UTC RFC3339 timestamp that specifies when the action being logged occured."""


class UnionMember0(BaseModel):
    errors: Optional[object] = None

    messages: Optional[List[object]] = None

    result: Optional[List[UnionMember0Result]] = None

    success: Optional[bool] = None


class AaaAPIResponseCommon(BaseModel):
    errors: List[UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]

    messages: List[UnnamedSchemaRef3248f24329456e19dfa042fff9986f72]

    result: UnnamedSchemaRefEc4d85c3d1bcc6b3b7e99c199ae99846

    success: Literal[True]
    """Whether the API call was successful"""


UnnamedSchemaRefE7c61ebe06ebfc3861ae8b9db4ba152b = Union[UnionMember0, AaaAPIResponseCommon]
