# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["CloudIntegrationEditParams"]


class CloudIntegrationEditParams(TypedDict, total=False):
    account_id: Required[str]

    aws_arn: str

    azure_subscription_id: str

    azure_tenant_id: str

    description: str

    friendly_name: str

    gcp_project_id: str

    gcp_service_account_email: str
