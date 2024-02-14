# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .scripts.scripts import Scripts, AsyncScripts

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .scripts import (
    Scripts,
    AsyncScripts,
    ScriptsWithRawResponse,
    AsyncScriptsWithRawResponse,
    ScriptsWithStreamingResponse,
    AsyncScriptsWithStreamingResponse,
)
from ....._wrappers import ResultWrapper

__all__ = ["Namespaces", "AsyncNamespaces"]


class Namespaces(SyncAPIResource):
    @cached_property
    def scripts(self) -> Scripts:
        return Scripts(self._client)

    @cached_property
    def with_raw_response(self) -> NamespacesWithRawResponse:
        return NamespacesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamespacesWithStreamingResponse:
        return NamespacesWithStreamingResponse(self)


class AsyncNamespaces(AsyncAPIResource):
    @cached_property
    def scripts(self) -> AsyncScripts:
        return AsyncScripts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncNamespacesWithRawResponse:
        return AsyncNamespacesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamespacesWithStreamingResponse:
        return AsyncNamespacesWithStreamingResponse(self)


class NamespacesWithRawResponse:
    def __init__(self, namespaces: Namespaces) -> None:
        self._namespaces = namespaces

    @cached_property
    def scripts(self) -> ScriptsWithRawResponse:
        return ScriptsWithRawResponse(self._namespaces.scripts)


class AsyncNamespacesWithRawResponse:
    def __init__(self, namespaces: AsyncNamespaces) -> None:
        self._namespaces = namespaces

    @cached_property
    def scripts(self) -> AsyncScriptsWithRawResponse:
        return AsyncScriptsWithRawResponse(self._namespaces.scripts)


class NamespacesWithStreamingResponse:
    def __init__(self, namespaces: Namespaces) -> None:
        self._namespaces = namespaces

    @cached_property
    def scripts(self) -> ScriptsWithStreamingResponse:
        return ScriptsWithStreamingResponse(self._namespaces.scripts)


class AsyncNamespacesWithStreamingResponse:
    def __init__(self, namespaces: AsyncNamespaces) -> None:
        self._namespaces = namespaces

    @cached_property
    def scripts(self) -> AsyncScriptsWithStreamingResponse:
        return AsyncScriptsWithStreamingResponse(self._namespaces.scripts)
