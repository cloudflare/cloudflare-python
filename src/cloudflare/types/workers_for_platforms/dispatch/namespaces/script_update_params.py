# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ....._types import FileTypes
from ....._utils import PropertyInfo
from ....workers.stepped_migration_param import SteppedMigrationParam
from ....workers.single_step_migration_param import SingleStepMigrationParam
from ....workers.placement_configuration_param import PlacementConfigurationParam
from ....workers.scripts.consumer_script_param import ConsumerScriptParam

__all__ = ["ScriptUpdateParams", "Variant0", "Variant0Metadata", "Variant0MetadataMigrations", "Variant1"]


class Variant0(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    any_part_name: Annotated[List[FileTypes], PropertyInfo(alias="<any part name>")]
    """A module comprising a Worker script, often a javascript file.

    Multiple modules may be provided as separate named parts, but at least one
    module must be present and referenced in the metadata as `main_module` or
    `body_part` by part name. Source maps may also be included using the
    `application/source-map` content type.
    """

    metadata: Variant0Metadata
    """JSON encoded metadata about the uploaded parts and Worker configuration."""


Variant0MetadataMigrations: TypeAlias = Union[SingleStepMigrationParam, SteppedMigrationParam]


class Variant0Metadata(TypedDict, total=False):
    bindings: Iterable[object]
    """List of bindings available to the worker."""

    body_part: str
    """Name of the part in the multipart request that contains the script (e.g.

    the file adding a listener to the `fetch` event). Indicates a
    `service worker syntax` Worker.
    """

    compatibility_date: str
    """Date indicating targeted support in the Workers runtime.

    Backwards incompatible fixes to the runtime following this date will not affect
    this Worker.
    """

    compatibility_flags: List[str]
    """Flags that enable or disable certain features in the Workers runtime.

    Used to enable upcoming features or opt in or out of specific changes not
    included in a `compatibility_date`.
    """

    keep_bindings: List[str]
    """List of binding types to keep from previous_upload."""

    logpush: bool
    """Whether Logpush is turned on for the Worker."""

    main_module: str
    """Name of the part in the multipart request that contains the main module (e.g.

    the file exporting a `fetch` handler). Indicates a `module syntax` Worker.
    """

    migrations: Variant0MetadataMigrations
    """Migrations to apply for Durable Objects associated with this Worker."""

    placement: PlacementConfigurationParam

    tags: List[str]
    """List of strings to use as tags for this Worker"""

    tail_consumers: Iterable[ConsumerScriptParam]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Literal["bundled", "unbound"]
    """Usage model to apply to invocations."""

    version_tags: object
    """Key-value pairs to use as tags for this version of this Worker"""


class Variant1(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    message: str
    """Rollback message to be associated with this deployment.

    Only parsed when query param `"rollback_to"` is present.
    """


ScriptUpdateParams: TypeAlias = Union[Variant0, Variant1]
