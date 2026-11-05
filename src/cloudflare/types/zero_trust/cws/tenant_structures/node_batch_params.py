# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, TypedDict

__all__ = ["NodeBatchParams", "Create", "Delete", "Update"]


class NodeBatchParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    creates: Required[Iterable[Create]]
    """Nodes to create; parents may be created elsewhere in this request"""

    deletes: Required[Iterable[Delete]]
    """
    Nodes to delete; every descendant that will not be reparented must also be
    deleted
    """

    updates: Required[Iterable[Update]]
    """Nodes whose mutable fields should be fully replaced"""


class Create(TypedDict, total=False):
    native_id: Required[str]
    """
    Cloud-native identifier of this node, unique within the structure; the
    parent-reference target. Shape depends on the structure's application. Immutable
    after create.
    """

    node_kind: Required[str]
    """Position in the tree.

    Legal values depend on the structure's application (aws: root/ou/account;
    cloudflare: org/account/zone). At most one root per structure. Immutable after
    create.
    """

    name: str
    """Display name (e.g. an OU or account name), mutable. Optional; empty by default."""

    parent: str
    """Native ID of this node's parent.

    Required for non-root nodes and omitted for the root. The parent must be in the
    same structure and able to contain this node kind.
    """


class Delete(TypedDict, total=False):
    id: Required[str]
    """ID of the node to delete"""


class Update(TypedDict, total=False):
    id: Required[str]
    """ID of the node to update"""

    name: str
    """Full replacement display name"""

    parent: str
    """Full replacement parent native ID; omit for the root"""
