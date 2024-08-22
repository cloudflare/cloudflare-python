# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .settings.settings import SettingsResource, AsyncSettingsResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .settings import SettingsResource, AsyncSettingsResource, SettingsResourceWithRawResponse, AsyncSettingsResourceWithRawResponse, SettingsResourceWithStreamingResponse, AsyncSettingsResourceWithStreamingResponse

__all__ = ["HostnamesResource", "AsyncHostnamesResource"]

class HostnamesResource(SyncAPIResource):
    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> HostnamesResourceWithRawResponse:
        return HostnamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnamesResourceWithStreamingResponse:
        return HostnamesResourceWithStreamingResponse(self)

class AsyncHostnamesResource(AsyncAPIResource):
    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHostnamesResourceWithRawResponse:
        return AsyncHostnamesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnamesResourceWithStreamingResponse:
        return AsyncHostnamesResourceWithStreamingResponse(self)

class HostnamesResourceWithRawResponse:
    def __init__(self, hostnames: HostnamesResource) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._hostnames.settings)

class AsyncHostnamesResourceWithRawResponse:
    def __init__(self, hostnames: AsyncHostnamesResource) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._hostnames.settings)

class HostnamesResourceWithStreamingResponse:
    def __init__(self, hostnames: HostnamesResource) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._hostnames.settings)

class AsyncHostnamesResourceWithStreamingResponse:
    def __init__(self, hostnames: AsyncHostnamesResource) -> None:
        self._hostnames = hostnames

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._hostnames.settings)