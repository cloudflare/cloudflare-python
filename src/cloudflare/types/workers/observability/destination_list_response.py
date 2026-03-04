# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DestinationListResponse", "Configuration", "ConfigurationJobStatus"]


class ConfigurationJobStatus(BaseModel):
    error_message: str

    last_complete: str

    last_error: str


class Configuration(BaseModel):
    destination_conf: str

    headers: Dict[str, str]

    job_status: ConfigurationJobStatus = FieldInfo(alias="jobStatus")

    logpush_dataset: Literal["opentelemetry-traces", "opentelemetry-logs"] = FieldInfo(alias="logpushDataset")

    type: Literal["logpush"]

    url: str


class DestinationListResponse(BaseModel):
    configuration: Configuration

    enabled: bool

    name: str

    scripts: List[str]

    slug: str
