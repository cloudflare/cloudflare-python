# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .widgets import Widgets, AsyncWidgets

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
from .widgets import (
    Widgets,
    AsyncWidgets,
    WidgetsWithRawResponse,
    AsyncWidgetsWithRawResponse,
    WidgetsWithStreamingResponse,
    AsyncWidgetsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Challenges", "AsyncChallenges"]


class Challenges(SyncAPIResource):
    @cached_property
    def widgets(self) -> Widgets:
        return Widgets(self._client)

    @cached_property
    def with_raw_response(self) -> ChallengesWithRawResponse:
        return ChallengesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChallengesWithStreamingResponse:
        return ChallengesWithStreamingResponse(self)


class AsyncChallenges(AsyncAPIResource):
    @cached_property
    def widgets(self) -> AsyncWidgets:
        return AsyncWidgets(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChallengesWithRawResponse:
        return AsyncChallengesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChallengesWithStreamingResponse:
        return AsyncChallengesWithStreamingResponse(self)


class ChallengesWithRawResponse:
    def __init__(self, challenges: Challenges) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> WidgetsWithRawResponse:
        return WidgetsWithRawResponse(self._challenges.widgets)


class AsyncChallengesWithRawResponse:
    def __init__(self, challenges: AsyncChallenges) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> AsyncWidgetsWithRawResponse:
        return AsyncWidgetsWithRawResponse(self._challenges.widgets)


class ChallengesWithStreamingResponse:
    def __init__(self, challenges: Challenges) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> WidgetsWithStreamingResponse:
        return WidgetsWithStreamingResponse(self._challenges.widgets)


class AsyncChallengesWithStreamingResponse:
    def __init__(self, challenges: AsyncChallenges) -> None:
        self._challenges = challenges

    @cached_property
    def widgets(self) -> AsyncWidgetsWithStreamingResponse:
        return AsyncWidgetsWithStreamingResponse(self._challenges.widgets)
