# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .tls import TLSResource, AsyncTLSResource

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .tls import TLSResource, AsyncTLSResource, TLSResourceWithRawResponse, AsyncTLSResourceWithRawResponse, TLSResourceWithStreamingResponse, AsyncTLSResourceWithStreamingResponse

__all__ = ["SettingsResource", "AsyncSettingsResource"]

class SettingsResource(SyncAPIResource):
    @cached_property
    def tls(self) -> TLSResource:
        return TLSResource(self._client)

    @cached_property
    def with_raw_response(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self)

class AsyncSettingsResource(AsyncAPIResource):
    @cached_property
    def tls(self) -> AsyncTLSResource:
        return AsyncTLSResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self)

class SettingsResourceWithRawResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> TLSResourceWithRawResponse:
        return TLSResourceWithRawResponse(self._settings.tls)

class AsyncSettingsResourceWithRawResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> AsyncTLSResourceWithRawResponse:
        return AsyncTLSResourceWithRawResponse(self._settings.tls)

class SettingsResourceWithStreamingResponse:
    def __init__(self, settings: SettingsResource) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> TLSResourceWithStreamingResponse:
        return TLSResourceWithStreamingResponse(self._settings.tls)

class AsyncSettingsResourceWithStreamingResponse:
    def __init__(self, settings: AsyncSettingsResource) -> None:
        self._settings = settings

    @cached_property
    def tls(self) -> AsyncTLSResourceWithStreamingResponse:
        return AsyncTLSResourceWithStreamingResponse(self._settings.tls)