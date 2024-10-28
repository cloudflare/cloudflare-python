# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SCIMConfigMapping", "Operations"]


class Operations(BaseModel):
    create: Optional[bool] = None
    """Whether or not this mapping applies to create (POST) operations."""

    delete: Optional[bool] = None
    """Whether or not this mapping applies to DELETE operations."""

    update: Optional[bool] = None
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class SCIMConfigMapping(BaseModel):
    schema_: str = FieldInfo(alias="schema")
    """Which SCIM resource type this mapping applies to."""

    enabled: Optional[bool] = None
    """Whether or not this mapping is enabled."""

    filter: Optional[str] = None
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: Optional[Operations] = None
    """Whether or not this mapping applies to creates, updates, or deletes."""

    strictness: Optional[Literal["strict", "passthrough"]] = None
    """
    The level of adherence to outbound resource schemas when provisioning to this
    mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown
    values to the target.
    """

    transform_jsonata: Optional[str] = None
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """
