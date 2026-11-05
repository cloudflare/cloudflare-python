# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NodeUpdateParams"]


class NodeUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Cloudflare account ID (32-character hexadecimal string)"""

    structure_id: Required[str]
    """ID of the parent tenant structure"""

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
