# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["Status"]

Status: TypeAlias = Literal[
    "initializing",
    "pending_validation",
    "deleted",
    "pending_issuance",
    "pending_deployment",
    "pending_deletion",
    "pending_expiration",
    "expired",
    "active",
    "initializing_timed_out",
    "validation_timed_out",
    "issuance_timed_out",
    "deployment_timed_out",
    "deletion_timed_out",
    "pending_cleanup",
    "staging_deployment",
    "staging_active",
    "deactivating",
    "inactive",
    "backup_issued",
    "holding_deployment",
]
