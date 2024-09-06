# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .lists.lists import ListsResource, AsyncListsResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .lists import (
    ListsResource,
    AsyncListsResource,
    ListsResourceWithRawResponse,
    AsyncListsResourceWithRawResponse,
    ListsResourceWithStreamingResponse,
    AsyncListsResourceWithStreamingResponse,
)

__all__ = ["RulesResource", "AsyncRulesResource"]


class RulesResource(SyncAPIResource):
    @cached_property
    def lists(self) -> ListsResource:
        return ListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self)


class AsyncRulesResource(AsyncAPIResource):
    @cached_property
    def lists(self) -> AsyncListsResource:
        return AsyncListsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self)


class RulesResourceWithRawResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> ListsResourceWithRawResponse:
        return ListsResourceWithRawResponse(self._rules.lists)


class AsyncRulesResourceWithRawResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> AsyncListsResourceWithRawResponse:
        return AsyncListsResourceWithRawResponse(self._rules.lists)


class RulesResourceWithStreamingResponse:
    def __init__(self, rules: RulesResource) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> ListsResourceWithStreamingResponse:
        return ListsResourceWithStreamingResponse(self._rules.lists)


class AsyncRulesResourceWithStreamingResponse:
    def __init__(self, rules: AsyncRulesResource) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> AsyncListsResourceWithStreamingResponse:
        return AsyncListsResourceWithStreamingResponse(self._rules.lists)
