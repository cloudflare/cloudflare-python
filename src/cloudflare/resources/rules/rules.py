# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .lists.lists import Lists, AsyncLists

from ..._compat import cached_property

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
from .lists import (
    Lists,
    AsyncLists,
    ListsWithRawResponse,
    AsyncListsWithRawResponse,
    ListsWithStreamingResponse,
    AsyncListsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Rules", "AsyncRules"]


class Rules(SyncAPIResource):
    @cached_property
    def lists(self) -> Lists:
        return Lists(self._client)

    @cached_property
    def with_raw_response(self) -> RulesWithRawResponse:
        return RulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RulesWithStreamingResponse:
        return RulesWithStreamingResponse(self)


class AsyncRules(AsyncAPIResource):
    @cached_property
    def lists(self) -> AsyncLists:
        return AsyncLists(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncRulesWithRawResponse:
        return AsyncRulesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRulesWithStreamingResponse:
        return AsyncRulesWithStreamingResponse(self)


class RulesWithRawResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> ListsWithRawResponse:
        return ListsWithRawResponse(self._rules.lists)


class AsyncRulesWithRawResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> AsyncListsWithRawResponse:
        return AsyncListsWithRawResponse(self._rules.lists)


class RulesWithStreamingResponse:
    def __init__(self, rules: Rules) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> ListsWithStreamingResponse:
        return ListsWithStreamingResponse(self._rules.lists)


class AsyncRulesWithStreamingResponse:
    def __init__(self, rules: AsyncRules) -> None:
        self._rules = rules

    @cached_property
    def lists(self) -> AsyncListsWithStreamingResponse:
        return AsyncListsWithStreamingResponse(self._rules.lists)
