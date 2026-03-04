# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["DestinationDeleteResponse", "Configuration"]


class Configuration(BaseModel):
    destination_conf: str

    logpush_dataset: Literal["opentelemetry-traces", "opentelemetry-logs"] = FieldInfo(alias="logpushDataset")

    logpush_job: float = FieldInfo(alias="logpushJob")

    type: Literal["logpush"]

    url: str


class DestinationDeleteResponse(BaseModel):
    configuration: Configuration

    enabled: bool

    name: str

    scripts: List[str]

    slug: str
