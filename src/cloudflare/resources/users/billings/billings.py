# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .histories import Histories, AsyncHistories

from ...._compat import cached_property

from .profiles import Profiles, AsyncProfiles

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ....types import shared_params
from .histories import (
    Histories,
    AsyncHistories,
    HistoriesWithRawResponse,
    AsyncHistoriesWithRawResponse,
    HistoriesWithStreamingResponse,
    AsyncHistoriesWithStreamingResponse,
)
from .profiles import (
    Profiles,
    AsyncProfiles,
    ProfilesWithRawResponse,
    AsyncProfilesWithRawResponse,
    ProfilesWithStreamingResponse,
    AsyncProfilesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Billings", "AsyncBillings"]


class Billings(SyncAPIResource):
    @cached_property
    def histories(self) -> Histories:
        return Histories(self._client)

    @cached_property
    def profiles(self) -> Profiles:
        return Profiles(self._client)

    @cached_property
    def with_raw_response(self) -> BillingsWithRawResponse:
        return BillingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BillingsWithStreamingResponse:
        return BillingsWithStreamingResponse(self)


class AsyncBillings(AsyncAPIResource):
    @cached_property
    def histories(self) -> AsyncHistories:
        return AsyncHistories(self._client)

    @cached_property
    def profiles(self) -> AsyncProfiles:
        return AsyncProfiles(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncBillingsWithRawResponse:
        return AsyncBillingsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBillingsWithStreamingResponse:
        return AsyncBillingsWithStreamingResponse(self)


class BillingsWithRawResponse:
    def __init__(self, billings: Billings) -> None:
        self._billings = billings

    @cached_property
    def histories(self) -> HistoriesWithRawResponse:
        return HistoriesWithRawResponse(self._billings.histories)

    @cached_property
    def profiles(self) -> ProfilesWithRawResponse:
        return ProfilesWithRawResponse(self._billings.profiles)


class AsyncBillingsWithRawResponse:
    def __init__(self, billings: AsyncBillings) -> None:
        self._billings = billings

    @cached_property
    def histories(self) -> AsyncHistoriesWithRawResponse:
        return AsyncHistoriesWithRawResponse(self._billings.histories)

    @cached_property
    def profiles(self) -> AsyncProfilesWithRawResponse:
        return AsyncProfilesWithRawResponse(self._billings.profiles)


class BillingsWithStreamingResponse:
    def __init__(self, billings: Billings) -> None:
        self._billings = billings

    @cached_property
    def histories(self) -> HistoriesWithStreamingResponse:
        return HistoriesWithStreamingResponse(self._billings.histories)

    @cached_property
    def profiles(self) -> ProfilesWithStreamingResponse:
        return ProfilesWithStreamingResponse(self._billings.profiles)


class AsyncBillingsWithStreamingResponse:
    def __init__(self, billings: AsyncBillings) -> None:
        self._billings = billings

    @cached_property
    def histories(self) -> AsyncHistoriesWithStreamingResponse:
        return AsyncHistoriesWithStreamingResponse(self._billings.histories)

    @cached_property
    def profiles(self) -> AsyncProfilesWithStreamingResponse:
        return AsyncProfilesWithStreamingResponse(self._billings.profiles)
