# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["DeploymentCreateParams"]


class DeploymentCreateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    _headers: FileTypes
    """Headers configuration file for the deployment."""

    _redirects: FileTypes
    """Redirects configuration file for the deployment."""

    _routes_json: Annotated[FileTypes, PropertyInfo(alias="_routes.json")]
    """Routes configuration file defining routing rules."""

    _worker_bundle: Annotated[FileTypes, PropertyInfo(alias="_worker.bundle")]
    """Worker bundle file in multipart/form-data format.

    Mutually exclusive with `_worker.js`. Cannot specify both `_worker.js` and
    `_worker.bundle` in the same request. Maximum size: 25 MiB.
    """

    _worker_js: Annotated[FileTypes, PropertyInfo(alias="_worker.js")]
    """Worker JavaScript file.

    Mutually exclusive with `_worker.bundle`. Cannot specify both `_worker.js` and
    `_worker.bundle` in the same request.
    """

    branch: str
    """Git branch to deploy.

    Uses the branch's `HEAD`; defaults to the project's production branch.
    """

    commit_dirty: Literal["true", "false"]
    """Whether the associated Git working tree has uncommitted changes.

    Provide `true` or `false`.
    """

    commit_hash: str
    """Git commit SHA associated with the deployment."""

    commit_message: str
    """Git commit message associated with the deployment."""

    functions_filepath_routing_config_json: Annotated[
        FileTypes, PropertyInfo(alias="functions-filepath-routing-config.json")
    ]
    """Functions routing configuration file."""

    manifest: str
    """
    JSON-encoded object mapping deployment file paths to their uploaded content
    hashes. Required for Direct Upload deployments. Maximum 20,000 entries.
    """

    pages_build_output_dir: str
    """The build output directory path."""

    wrangler_config_hash: str
    """Hash of the Wrangler configuration file used for this deployment."""
