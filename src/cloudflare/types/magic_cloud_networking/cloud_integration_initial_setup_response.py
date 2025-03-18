# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = ["CloudIntegrationInitialSetupResponse", "McnAwsTrustPolicy", "McnAzureSetup", "McnGcpSetup"]


class McnAwsTrustPolicy(BaseModel):
    aws_trust_policy: str

    item_type: str


class McnAzureSetup(BaseModel):
    azure_consent_url: str

    integration_identity_tag: str

    item_type: str

    tag_cli_command: str


class McnGcpSetup(BaseModel):
    integration_identity_tag: str

    item_type: str

    tag_cli_command: str


CloudIntegrationInitialSetupResponse: TypeAlias = Annotated[
    Union[McnAwsTrustPolicy, McnAzureSetup, McnGcpSetup], PropertyInfo(discriminator="item_type")
]
