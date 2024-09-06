# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .bindings import BindingsResource, AsyncBindingsResource

from ....._compat import cached_property

from .prefixes import PrefixesResource, AsyncPrefixesResource

from .statuses import StatusesResource, AsyncStatusesResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .bindings import (
    BindingsResource,
    AsyncBindingsResource,
    BindingsResourceWithRawResponse,
    AsyncBindingsResourceWithRawResponse,
    BindingsResourceWithStreamingResponse,
    AsyncBindingsResourceWithStreamingResponse,
)
from .prefixes import (
    PrefixesResource,
    AsyncPrefixesResource,
    PrefixesResourceWithRawResponse,
    AsyncPrefixesResourceWithRawResponse,
    PrefixesResourceWithStreamingResponse,
    AsyncPrefixesResourceWithStreamingResponse,
)
from .statuses import (
    StatusesResource,
    AsyncStatusesResource,
    StatusesResourceWithRawResponse,
    AsyncStatusesResourceWithRawResponse,
    StatusesResourceWithStreamingResponse,
    AsyncStatusesResourceWithStreamingResponse,
)

__all__ = ["BGPResource", "AsyncBGPResource"]


class BGPResource(SyncAPIResource):
    @cached_property
    def bindings(self) -> BindingsResource:
        return BindingsResource(self._client)

    @cached_property
    def prefixes(self) -> PrefixesResource:
        return PrefixesResource(self._client)

    @cached_property
    def statuses(self) -> StatusesResource:
        return StatusesResource(self._client)

    @cached_property
    def with_raw_response(self) -> BGPResourceWithRawResponse:
        return BGPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BGPResourceWithStreamingResponse:
        return BGPResourceWithStreamingResponse(self)


class AsyncBGPResource(AsyncAPIResource):
    @cached_property
    def bindings(self) -> AsyncBindingsResource:
        return AsyncBindingsResource(self._client)

    @cached_property
    def prefixes(self) -> AsyncPrefixesResource:
        return AsyncPrefixesResource(self._client)

    @cached_property
    def statuses(self) -> AsyncStatusesResource:
        return AsyncStatusesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBGPResourceWithRawResponse:
        return AsyncBGPResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBGPResourceWithStreamingResponse:
        return AsyncBGPResourceWithStreamingResponse(self)


class BGPResourceWithRawResponse:
    def __init__(self, bgp: BGPResource) -> None:
        self._bgp = bgp

    @cached_property
    def bindings(self) -> BindingsResourceWithRawResponse:
        return BindingsResourceWithRawResponse(self._bgp.bindings)

    @cached_property
    def prefixes(self) -> PrefixesResourceWithRawResponse:
        return PrefixesResourceWithRawResponse(self._bgp.prefixes)

    @cached_property
    def statuses(self) -> StatusesResourceWithRawResponse:
        return StatusesResourceWithRawResponse(self._bgp.statuses)


class AsyncBGPResourceWithRawResponse:
    def __init__(self, bgp: AsyncBGPResource) -> None:
        self._bgp = bgp

    @cached_property
    def bindings(self) -> AsyncBindingsResourceWithRawResponse:
        return AsyncBindingsResourceWithRawResponse(self._bgp.bindings)

    @cached_property
    def prefixes(self) -> AsyncPrefixesResourceWithRawResponse:
        return AsyncPrefixesResourceWithRawResponse(self._bgp.prefixes)

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithRawResponse:
        return AsyncStatusesResourceWithRawResponse(self._bgp.statuses)


class BGPResourceWithStreamingResponse:
    def __init__(self, bgp: BGPResource) -> None:
        self._bgp = bgp

    @cached_property
    def bindings(self) -> BindingsResourceWithStreamingResponse:
        return BindingsResourceWithStreamingResponse(self._bgp.bindings)

    @cached_property
    def prefixes(self) -> PrefixesResourceWithStreamingResponse:
        return PrefixesResourceWithStreamingResponse(self._bgp.prefixes)

    @cached_property
    def statuses(self) -> StatusesResourceWithStreamingResponse:
        return StatusesResourceWithStreamingResponse(self._bgp.statuses)


class AsyncBGPResourceWithStreamingResponse:
    def __init__(self, bgp: AsyncBGPResource) -> None:
        self._bgp = bgp

    @cached_property
    def bindings(self) -> AsyncBindingsResourceWithStreamingResponse:
        return AsyncBindingsResourceWithStreamingResponse(self._bgp.bindings)

    @cached_property
    def prefixes(self) -> AsyncPrefixesResourceWithStreamingResponse:
        return AsyncPrefixesResourceWithStreamingResponse(self._bgp.prefixes)

    @cached_property
    def statuses(self) -> AsyncStatusesResourceWithStreamingResponse:
        return AsyncStatusesResourceWithStreamingResponse(self._bgp.statuses)
