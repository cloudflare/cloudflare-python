# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .keys import KeysResource, AsyncKeysResource

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)

__all__ = ["TURNResource", "AsyncTURNResource"]


class TURNResource(SyncAPIResource):
    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> TURNResourceWithRawResponse:
        return TURNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TURNResourceWithStreamingResponse:
        return TURNResourceWithStreamingResponse(self)


class AsyncTURNResource(AsyncAPIResource):
    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTURNResourceWithRawResponse:
        return AsyncTURNResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTURNResourceWithStreamingResponse:
        return AsyncTURNResourceWithStreamingResponse(self)


class TURNResourceWithRawResponse:
    def __init__(self, turn: TURNResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._turn.keys)


class AsyncTURNResourceWithRawResponse:
    def __init__(self, turn: AsyncTURNResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._turn.keys)


class TURNResourceWithStreamingResponse:
    def __init__(self, turn: TURNResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._turn.keys)


class AsyncTURNResourceWithStreamingResponse:
    def __init__(self, turn: AsyncTURNResource) -> None:
        self._turn = turn

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._turn.keys)
