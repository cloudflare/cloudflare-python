# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ScriptDeleteParams"]


class ScriptDeleteParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    force: bool
    """
    If set to true, delete will not be stopped by associated service binding,
    durable object, or other binding. Any of these associated bindings/durable
    objects will be deleted along with the script.
    """
