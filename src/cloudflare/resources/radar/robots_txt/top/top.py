# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .directive import DirectiveResource, AsyncDirectiveResource

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .directive import (
    DirectiveResource,
    AsyncDirectiveResource,
    DirectiveResourceWithRawResponse,
    AsyncDirectiveResourceWithRawResponse,
    DirectiveResourceWithStreamingResponse,
    AsyncDirectiveResourceWithStreamingResponse,
)

__all__ = ["TopResource", "AsyncTopResource"]


class TopResource(SyncAPIResource):
    @cached_property
    def directive(self) -> DirectiveResource:
        return DirectiveResource(self._client)

    @cached_property
    def with_raw_response(self) -> TopResourceWithRawResponse:
        return TopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TopResourceWithStreamingResponse:
        return TopResourceWithStreamingResponse(self)


class AsyncTopResource(AsyncAPIResource):
    @cached_property
    def directive(self) -> AsyncDirectiveResource:
        return AsyncDirectiveResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTopResourceWithRawResponse:
        return AsyncTopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTopResourceWithStreamingResponse:
        return AsyncTopResourceWithStreamingResponse(self)


class TopResourceWithRawResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

    @cached_property
    def directive(self) -> DirectiveResourceWithRawResponse:
        return DirectiveResourceWithRawResponse(self._top.directive)


class AsyncTopResourceWithRawResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

    @cached_property
    def directive(self) -> AsyncDirectiveResourceWithRawResponse:
        return AsyncDirectiveResourceWithRawResponse(self._top.directive)


class TopResourceWithStreamingResponse:
    def __init__(self, top: TopResource) -> None:
        self._top = top

    @cached_property
    def directive(self) -> DirectiveResourceWithStreamingResponse:
        return DirectiveResourceWithStreamingResponse(self._top.directive)


class AsyncTopResourceWithStreamingResponse:
    def __init__(self, top: AsyncTopResource) -> None:
        self._top = top

    @cached_property
    def directive(self) -> AsyncDirectiveResourceWithStreamingResponse:
        return AsyncDirectiveResourceWithStreamingResponse(self._top.directive)
