# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RedirectParam"]


class RedirectParam(TypedDict, total=False):
    source_url: Required[str]

    target_url: Required[str]

    include_subdomains: bool

    preserve_path_suffix: bool

    preserve_query_string: bool

    status_code: Literal[301, 302, 307, 308]

    subpath_matching: bool
