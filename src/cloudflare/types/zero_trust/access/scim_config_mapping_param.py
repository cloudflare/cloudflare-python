# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["SCIMConfigMappingParam", "Operations"]


class Operations(TypedDict, total=False):
    create: bool
    """Whether or not this mapping applies to create (POST) operations."""

    delete: bool
    """Whether or not this mapping applies to DELETE operations."""

    update: bool
    """Whether or not this mapping applies to update (PATCH/PUT) operations."""


class SCIMConfigMappingParam(TypedDict, total=False):
    schema: Required[str]
    """Which SCIM resource type this mapping applies to."""

    enabled: bool
    """Whether or not this mapping is enabled."""

    filter: str
    """
    A
    [SCIM filter expression](https://datatracker.ietf.org/doc/html/rfc7644#section-3.4.2.2)
    that matches resources that should be provisioned to this application.
    """

    operations: Operations
    """Whether or not this mapping applies to creates, updates, or deletes."""

    strictness: Literal["strict", "passthrough"]
    """
    The level of adherence to outbound resource schemas when provisioning to this
    mapping. ‘Strict’ removes unknown values, while ‘passthrough’ passes unknown
    values to the target.
    """

    transform_jsonata: str
    """
    A [JSONata](https://jsonata.org/) expression that transforms the resource before
    provisioning it in the application.
    """
