# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from ....._models import BaseModel

__all__ = ["TenantStructureNode"]


class TenantStructureNode(BaseModel):
    id: str
    """Server-assigned UUID"""

    created_at: datetime

    native_id: str
    """
    Cloud-native identifier of this node, unique within the structure; the
    parent-reference target. Shape depends on the structure's application. Immutable
    after create.
    """

    node_kind: str
    """Position in the tree.

    Legal values depend on the structure's application (aws: root/ou/account;
    cloudflare: org/account/zone). At most one root per structure. Immutable after
    create.
    """

    updated_at: datetime

    name: Optional[str] = None
    """Display name (e.g. an OU or account name), mutable. Optional; empty by default."""

    parent: Optional[str] = None
    """Native ID of this node's parent.

    Required for non-root nodes and omitted for the root. The parent must be in the
    same structure and able to contain this node kind.
    """
