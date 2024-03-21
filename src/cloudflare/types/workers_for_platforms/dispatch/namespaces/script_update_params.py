# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypedDict

from ....._types import FileTypes
from ....._utils import PropertyInfo

__all__ = [
    "ScriptUpdateParams",
    "Variant0",
    "Variant0Metadata",
    "Variant0MetadataMigrations",
    "Variant0MetadataMigrationsWorkersSingleStepMigrations",
    "Variant0MetadataMigrationsWorkersSingleStepMigrationsRenamedClass",
    "Variant0MetadataMigrationsWorkersSingleStepMigrationsTransferredClass",
    "Variant0MetadataMigrationsWorkersSteppedMigrations",
    "Variant0MetadataMigrationsWorkersSteppedMigrationsStep",
    "Variant0MetadataMigrationsWorkersSteppedMigrationsStepRenamedClass",
    "Variant0MetadataMigrationsWorkersSteppedMigrationsStepTransferredClass",
    "Variant0MetadataPlacement",
    "Variant0MetadataTailConsumer",
    "Variant1",
]


class Variant0(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    any_part_name: Annotated[List[FileTypes], PropertyInfo(alias="<any part name>")]
    """A module comprising a Worker script, often a javascript file.

    Multiple modules may be provided as separate named parts, but at least one
    module must be present and referenced in the metadata as `main_module` or
    `body_part` by part name.
    """

    metadata: Variant0Metadata
    """JSON encoded metadata about the uploaded parts and Worker configuration."""


_Variant0MetadataMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords = TypedDict(
    "_Variant0MetadataMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Variant0MetadataMigrationsWorkersSingleStepMigrationsRenamedClass(
    _Variant0MetadataMigrationsWorkersSingleStepMigrationsRenamedClassReservedKeywords, total=False
):
    to: str


_Variant0MetadataMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords = TypedDict(
    "_Variant0MetadataMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Variant0MetadataMigrationsWorkersSingleStepMigrationsTransferredClass(
    _Variant0MetadataMigrationsWorkersSingleStepMigrationsTransferredClassReservedKeywords, total=False
):
    from_script: str

    to: str


class Variant0MetadataMigrationsWorkersSingleStepMigrations(TypedDict, total=False):
    deleted_classes: List[str]
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: List[str]
    """A list of classes to create Durable Object namespaces from."""

    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    renamed_classes: Iterable[Variant0MetadataMigrationsWorkersSingleStepMigrationsRenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[Variant0MetadataMigrationsWorkersSingleStepMigrationsTransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


_Variant0MetadataMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords = TypedDict(
    "_Variant0MetadataMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Variant0MetadataMigrationsWorkersSteppedMigrationsStepRenamedClass(
    _Variant0MetadataMigrationsWorkersSteppedMigrationsStepRenamedClassReservedKeywords, total=False
):
    to: str


_Variant0MetadataMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords = TypedDict(
    "_Variant0MetadataMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords",
    {
        "from": str,
    },
    total=False,
)


class Variant0MetadataMigrationsWorkersSteppedMigrationsStepTransferredClass(
    _Variant0MetadataMigrationsWorkersSteppedMigrationsStepTransferredClassReservedKeywords, total=False
):
    from_script: str

    to: str


class Variant0MetadataMigrationsWorkersSteppedMigrationsStep(TypedDict, total=False):
    deleted_classes: List[str]
    """A list of classes to delete Durable Object namespaces from."""

    new_classes: List[str]
    """A list of classes to create Durable Object namespaces from."""

    renamed_classes: Iterable[Variant0MetadataMigrationsWorkersSteppedMigrationsStepRenamedClass]
    """A list of classes with Durable Object namespaces that were renamed."""

    transferred_classes: Iterable[Variant0MetadataMigrationsWorkersSteppedMigrationsStepTransferredClass]
    """
    A list of transfers for Durable Object namespaces from a different Worker and
    class to a class defined in this Worker.
    """


class Variant0MetadataMigrationsWorkersSteppedMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[Variant0MetadataMigrationsWorkersSteppedMigrationsStep]
    """Migrations to apply in order."""


Variant0MetadataMigrations = Union[
    Variant0MetadataMigrationsWorkersSingleStepMigrations, Variant0MetadataMigrationsWorkersSteppedMigrations
]


class Variant0MetadataPlacement(TypedDict, total=False):
    mode: Literal["smart"]
    """
    Enables
    [Smart Placement](https://developers.cloudflare.com/workers/configuration/smart-placement).
    Only `"smart"` is currently supported
    """


class Variant0MetadataTailConsumer(TypedDict, total=False):
    service: Required[str]
    """Name of Worker that is to be the consumer."""

    environment: str
    """Optional environment if the Worker utilizes one."""

    namespace: str
    """Optional dispatch namespace the script belongs to."""


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

    placement: Variant0MetadataPlacement

    tags: List[str]
    """List of strings to use as tags for this Worker"""

    tail_consumers: Iterable[Variant0MetadataTailConsumer]
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


ScriptUpdateParams = Union[Variant0, Variant1]
