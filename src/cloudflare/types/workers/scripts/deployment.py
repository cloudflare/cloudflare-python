# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "Deployment",
    "Version",
    "Annotations",
    "CodeUpdateStrategy",
    "CodeUpdateStrategyMode",
    "CodeUpdateStrategyUnionMember1",
]


class Version(BaseModel):
    percentage: float
    """Percentage of traffic served by this version."""

    version_id: str
    """Identifier of the Worker Version."""


class Annotations(BaseModel):
    """Metadata attached to the deployment."""

    workers_message: Optional[str] = FieldInfo(alias="workers/message", default=None)
    """Human-readable message about the deployment. Truncated to 1000 bytes if longer."""

    workers_triggered_by: Optional[str] = FieldInfo(alias="workers/triggered_by", default=None)
    """Operation that triggered the creation of the deployment."""


class CodeUpdateStrategyMode(BaseModel):
    mode: Literal["immediate"]
    """Apply Durable Object code updates immediately."""


class CodeUpdateStrategyUnionMember1(BaseModel):
    mode: Literal["deferred"]
    """Allow active Durable Objects to hibernate before updating their code."""

    max_delay: Optional[float] = None
    """Set the maximum number of seconds to wait before forcing the update.

    When omitted, the default maximum delay applies.
    """


CodeUpdateStrategy: TypeAlias = Union[CodeUpdateStrategyMode, CodeUpdateStrategyUnionMember1, Optional[object]]


class Deployment(BaseModel):
    id: str

    created_on: datetime

    source: str

    strategy: Literal["percentage"]
    """Strategy for routing traffic across the listed versions.

    `percentage` splits traffic according to each version's `percentage`.
    """

    versions: List[Version]
    """Worker versions included in this deployment.

    Each object must contain a `version_id` UUID and a `percentage`; percentages
    across all objects must total 100. In the `cf` CLI, pass the entire array as one
    JSON value to `--versions`, either inline, for example
    `--versions '[{"version_id":"023e105f-2a42-4f8b-a1c1-73f6a2a30c0f","percentage":100}]'`,
    or from a JSON file with `--versions @versions.json`.
    """

    annotations: Optional[Annotations] = None
    """Metadata attached to the deployment."""

    author_email: Optional[str] = None
