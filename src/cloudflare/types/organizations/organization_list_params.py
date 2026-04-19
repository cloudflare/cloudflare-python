# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["OrganizationListParams", "Containing", "Name", "Parent"]


class OrganizationListParams(TypedDict, total=False):
    id: SequenceNotStr[str]
    """Only return organizations with the specified IDs (ex.

    id=foo&id=bar). Send multiple elements by repeating the query value.
    """

    containing: Containing

    name: Name

    page_size: int
    """The amount of items to return. Defaults to 10."""

    page_token: str
    """
    An opaque token returned from the last list response that when provided will
    retrieve the next page.

    Parameters used to filter the retrieved list must remain in subsequent requests
    with a page token.
    """

    parent: Parent


class Containing(TypedDict, total=False):
    account: str
    """
    Filter the list of organizations to the ones that contain this particular
    account.
    """

    organization: str
    """
    Filter the list of organizations to the ones that contain this particular
    organization.
    """

    user: str
    """Filter the list of organizations to the ones that contain this particular user.

    IMPORTANT: Just because an organization "contains" a user is not a
    representation of any authorization or privilege to manage any resources
    therein. An organization "containing" a user simply means the user is managed by
    that organization.
    """


class Name(TypedDict, total=False):
    contains: str
    """
    (case-insensitive) Filter the list of organizations to where the name contains a
    particular string.
    """

    ends_with: Annotated[str, PropertyInfo(alias="endsWith")]
    """
    (case-insensitive) Filter the list of organizations to where the name ends with
    a particular string.
    """

    starts_with: Annotated[str, PropertyInfo(alias="startsWith")]
    """
    (case-insensitive) Filter the list of organizations to where the name starts
    with a particular string.
    """


class Parent(TypedDict, total=False):
    id: Union[str, Literal["null"]]
    """
    Filter the list of organizations to the ones that are a sub-organization of the
    specified organization.

    "null" is a valid value to provide for this parameter. It means "where an
    organization has no parent (i.e. it is a 'root' organization)."
    """
