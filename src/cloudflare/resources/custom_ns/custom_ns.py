# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .availabilities import Availabilities, AsyncAvailabilities

from ..._compat import cached_property

from .verifies import Verifies, AsyncVerifies

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from .availabilities import (
    Availabilities,
    AsyncAvailabilities,
    AvailabilitiesWithRawResponse,
    AsyncAvailabilitiesWithRawResponse,
    AvailabilitiesWithStreamingResponse,
    AsyncAvailabilitiesWithStreamingResponse,
)
from .verifies import (
    Verifies,
    AsyncVerifies,
    VerifiesWithRawResponse,
    AsyncVerifiesWithRawResponse,
    VerifiesWithStreamingResponse,
    AsyncVerifiesWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["CustomNs", "AsyncCustomNs"]


class CustomNs(SyncAPIResource):
    @cached_property
    def availabilities(self) -> Availabilities:
        return Availabilities(self._client)

    @cached_property
    def verifies(self) -> Verifies:
        return Verifies(self._client)

    @cached_property
    def with_raw_response(self) -> CustomNsWithRawResponse:
        return CustomNsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomNsWithStreamingResponse:
        return CustomNsWithStreamingResponse(self)


class AsyncCustomNs(AsyncAPIResource):
    @cached_property
    def availabilities(self) -> AsyncAvailabilities:
        return AsyncAvailabilities(self._client)

    @cached_property
    def verifies(self) -> AsyncVerifies:
        return AsyncVerifies(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomNsWithRawResponse:
        return AsyncCustomNsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomNsWithStreamingResponse:
        return AsyncCustomNsWithStreamingResponse(self)


class CustomNsWithRawResponse:
    def __init__(self, custom_ns: CustomNs) -> None:
        self._custom_ns = custom_ns

    @cached_property
    def availabilities(self) -> AvailabilitiesWithRawResponse:
        return AvailabilitiesWithRawResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> VerifiesWithRawResponse:
        return VerifiesWithRawResponse(self._custom_ns.verifies)


class AsyncCustomNsWithRawResponse:
    def __init__(self, custom_ns: AsyncCustomNs) -> None:
        self._custom_ns = custom_ns

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesWithRawResponse:
        return AsyncAvailabilitiesWithRawResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> AsyncVerifiesWithRawResponse:
        return AsyncVerifiesWithRawResponse(self._custom_ns.verifies)


class CustomNsWithStreamingResponse:
    def __init__(self, custom_ns: CustomNs) -> None:
        self._custom_ns = custom_ns

    @cached_property
    def availabilities(self) -> AvailabilitiesWithStreamingResponse:
        return AvailabilitiesWithStreamingResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> VerifiesWithStreamingResponse:
        return VerifiesWithStreamingResponse(self._custom_ns.verifies)


class AsyncCustomNsWithStreamingResponse:
    def __init__(self, custom_ns: AsyncCustomNs) -> None:
        self._custom_ns = custom_ns

    @cached_property
    def availabilities(self) -> AsyncAvailabilitiesWithStreamingResponse:
        return AsyncAvailabilitiesWithStreamingResponse(self._custom_ns.availabilities)

    @cached_property
    def verifies(self) -> AsyncVerifiesWithStreamingResponse:
        return AsyncVerifiesWithStreamingResponse(self._custom_ns.verifies)
