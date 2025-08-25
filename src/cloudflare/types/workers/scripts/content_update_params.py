# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from ...._types import FileTypes
from ...._utils import PropertyInfo

__all__ = ["ContentUpdateParams", "Metadata"]


class ContentUpdateParams(TypedDict, total=False):
    account_id: Required[str]
    """Identifier."""

    metadata: Required[Metadata]
    """JSON-encoded metadata about the uploaded parts and Worker configuration."""

    files: List[FileTypes]
    """An array of modules (often JavaScript files) comprising a Worker script.

    At least one module must be present and referenced in the metadata as
    `main_module` or `body_part` by filename.<br/>Possible Content-Type(s) are:
    `application/javascript+module`, `text/javascript+module`,
    `application/javascript`, `text/javascript`, `text/x-python`,
    `text/x-python-requirement`, `application/wasm`, `text/plain`,
    `application/octet-stream`, `application/source-map`.
    """

    cf_worker_body_part: Annotated[str, PropertyInfo(alias="CF-WORKER-BODY-PART")]

    cf_worker_main_module_part: Annotated[str, PropertyInfo(alias="CF-WORKER-MAIN-MODULE-PART")]


class Metadata(TypedDict, total=False):
    body_part: str
    """Name of the uploaded file that contains the Worker script (e.g.

    the file adding a listener to the `fetch` event). Indicates a
    `service worker syntax` Worker.
    """

    main_module: str
    """Name of the uploaded file that contains the main module (e.g.

    the file exporting a `fetch` handler). Indicates a `module syntax` Worker.
    """
