# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from ...._models import BaseModel

__all__ = ["PermissionGroupGetResponse", "PermissionGroupGetResponseItem"]


class PermissionGroupGetResponseItem(BaseModel):
    id: Optional[str] = None
    """Public ID."""

    category: Optional[
        Literal[
            "developer_platform",
            "ai_and_machine_learning",
            "dns_and_zones",
            "app_security",
            "rules_and_configuration",
            "cloudflare_one_and_zero_trust",
            "analytics_and_logs",
            "network_services",
            "media",
            "email_and_messaging",
            "cache_and_performance",
            "account_and_billing",
            "other",
        ]
    ] = None
    """Product category that this permission group belongs to."""

    name: Optional[str] = None
    """Permission Group Name"""

    scopes: Optional[
        List[
            Literal[
                "com.cloudflare.api.account",
                "com.cloudflare.api.account.zone",
                "com.cloudflare.api.user",
                "com.cloudflare.edge.r2.bucket",
            ]
        ]
    ] = None
    """Resources to which the Permission Group is scoped"""


PermissionGroupGetResponse: TypeAlias = List[PermissionGroupGetResponseItem]
