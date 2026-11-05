# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "DeploymentCreateParams",
    "Version",
    "Annotations",
    "CodeUpdateStrategy",
    "CodeUpdateStrategyMode",
    "CodeUpdateStrategyUnionMember1",
]


class DeploymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    strategy: Required[Literal["percentage"]]
    """Strategy for routing traffic across the listed versions.

    `percentage` splits traffic according to each version's `percentage`.
    """

    versions: Required[Iterable[Version]]
    """Worker versions included in this deployment.

    Each object must contain a `version_id` UUID and a `percentage`; percentages
    across all objects must total 100. In the `cf` CLI, pass the entire array as one
    JSON value to `--versions`, either inline, for example
    `--versions '[{"version_id":"023e105f-2a42-4f8b-a1c1-73f6a2a30c0f","percentage":100}]'`,
    or from a JSON file with `--versions @versions.json`.
    """

    force: bool
    """
    If set to true, the deployment will be created even if normally blocked by
    something such rolling back to an older version when a secret has changed.
    """

    annotations: Annotations
    """Metadata attached to the deployment."""

    code_update_strategy: CodeUpdateStrategy
    """Choose whether to apply Durable Object code updates immediately or defer them.

    When omitted, the default strategy applies.
    """


class Version(TypedDict, total=False):
    percentage: Required[float]
    """Percentage of traffic served by this version."""

    version_id: Required[str]
    """Identifier of the Worker Version."""


class Annotations(TypedDict, total=False):
    """Metadata attached to the deployment."""

    workers_message: Annotated[str, PropertyInfo(alias="workers/message")]
    """Human-readable message about the deployment. Truncated to 1000 bytes if longer."""


class CodeUpdateStrategyMode(TypedDict, total=False):
    mode: Required[Literal["immediate"]]
    """Apply Durable Object code updates immediately."""


class CodeUpdateStrategyUnionMember1(TypedDict, total=False):
    mode: Required[Literal["deferred"]]
    """Allow active Durable Objects to hibernate before updating their code."""

    max_delay: Optional[float]
    """Set the maximum number of seconds to wait before forcing the update.

    When omitted, the default maximum delay applies.
    """


CodeUpdateStrategy: TypeAlias = Union[CodeUpdateStrategyMode, CodeUpdateStrategyUnionMember1, Optional[object]]
