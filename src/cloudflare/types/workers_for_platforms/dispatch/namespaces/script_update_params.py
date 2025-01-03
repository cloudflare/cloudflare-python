# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from ....workers.migration_step_param import MigrationStepParam
from ....workers.single_step_migration_param import SingleStepMigrationParam
from ....zones.origin_max_http_version_param import OriginMaxHTTPVersionParam
from ....workers.placement_configuration_param import PlacementConfigurationParam
from ....workers.scripts.consumer_script_param import ConsumerScriptParam

__all__ = [
    "ScriptUpdateParams",
    "Variant0",
    "Variant0Metadata",
    "Variant0MetadataAssets",
    "Variant0MetadataAssetsConfig",
    "Variant0MetadataBinding",
    "Variant0MetadataMigrations",
    "Variant0MetadataMigrationsWorkersMultipleStepMigrations",
    "Variant0MetadataObservability",
    "Variant1",
]


class Variant0(TypedDict, total=False):
    account_id: Required[str]
    """Identifier"""

    dispatch_namespace: Required[str]
    """Name of the Workers for Platforms dispatch namespace."""

    metadata: Required[Variant0Metadata]
    """JSON encoded metadata about the uploaded parts and Worker configuration."""


class Variant0MetadataAssetsConfig(TypedDict, total=False):
    html_handling: Literal["auto-trailing-slash", "force-trailing-slash", "drop-trailing-slash", "none"]
    """Determines the redirects and rewrites of requests for HTML content."""

    not_found_handling: Literal["none", "404-page", "single-page-application"]
    """
    Determines the response when a request does not match a static asset, and there
    is no Worker script.
    """

    serve_directly: bool
    """
    When true and the incoming request matches an asset, that will be served instead
    of invoking the Worker script. When false, requests will always invoke the
    Worker script.
    """


class Variant0MetadataAssets(TypedDict, total=False):
    config: Variant0MetadataAssetsConfig
    """Configuration for assets within a Worker."""

    jwt: str
    """Token provided upon successful upload of all files from a registered manifest."""


class Variant0MetadataBindingTyped(TypedDict, total=False):
    name: str
    """Name of the binding variable."""

    type: str
    """Type of binding.

    You can find more about bindings on our docs:
    https://developers.cloudflare.com/workers/configuration/multipart-upload-metadata/#bindings.
    """


Variant0MetadataBinding: TypeAlias = Union[Variant0MetadataBindingTyped, Dict[str, OriginMaxHTTPVersionParam]]


class Variant0MetadataMigrationsWorkersMultipleStepMigrations(TypedDict, total=False):
    new_tag: str
    """Tag to set as the latest migration tag."""

    old_tag: str
    """Tag used to verify against the latest migration tag for this Worker.

    If they don't match, the upload is rejected.
    """

    steps: Iterable[MigrationStepParam]
    """Migrations to apply in order."""


Variant0MetadataMigrations: TypeAlias = Union[
    SingleStepMigrationParam, Variant0MetadataMigrationsWorkersMultipleStepMigrations
]


class Variant0MetadataObservability(TypedDict, total=False):
    enabled: Required[bool]
    """Whether observability is enabled for the Worker."""

    head_sampling_rate: Optional[float]
    """The sampling rate for incoming requests.

    From 0 to 1 (1 = 100%, 0.1 = 10%). Default is 1.
    """


class Variant0Metadata(TypedDict, total=False):
    assets: Variant0MetadataAssets
    """Configuration for assets within a Worker"""

    bindings: Iterable[Variant0MetadataBinding]
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

    keep_assets: bool
    """
    Retain assets which exist for a previously uploaded Worker version; used in lieu
    of providing a completion token.
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

    observability: Variant0MetadataObservability
    """Observability settings for the Worker."""

    placement: PlacementConfigurationParam

    tags: List[str]
    """List of strings to use as tags for this Worker."""

    tail_consumers: Iterable[ConsumerScriptParam]
    """List of Workers that will consume logs from the attached Worker."""

    usage_model: Literal["bundled", "unbound"]
    """Usage model for the Worker invocations."""

    version_tags: Dict[str, str]
    """Key-value pairs to use as tags for this version of this Worker."""


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
