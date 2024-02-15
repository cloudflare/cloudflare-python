# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .destinations.destinations import Destinations, AsyncDestinations

from ...._compat import cached_property

from .histories import Histories, AsyncHistories

from .policies import Policies, AsyncPolicies

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
from .destinations import (
    Destinations,
    AsyncDestinations,
    DestinationsWithRawResponse,
    AsyncDestinationsWithRawResponse,
    DestinationsWithStreamingResponse,
    AsyncDestinationsWithStreamingResponse,
)
from .histories import (
    Histories,
    AsyncHistories,
    HistoriesWithRawResponse,
    AsyncHistoriesWithRawResponse,
    HistoriesWithStreamingResponse,
    AsyncHistoriesWithStreamingResponse,
)
from .policies import (
    Policies,
    AsyncPolicies,
    PoliciesWithRawResponse,
    AsyncPoliciesWithRawResponse,
    PoliciesWithStreamingResponse,
    AsyncPoliciesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["V3s", "AsyncV3s"]


class V3s(SyncAPIResource):
    @cached_property
    def destinations(self) -> Destinations:
        return Destinations(self._client)

    @cached_property
    def histories(self) -> Histories:
        return Histories(self._client)

    @cached_property
    def policies(self) -> Policies:
        return Policies(self._client)

    @cached_property
    def with_raw_response(self) -> V3sWithRawResponse:
        return V3sWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> V3sWithStreamingResponse:
        return V3sWithStreamingResponse(self)


class AsyncV3s(AsyncAPIResource):
    @cached_property
    def destinations(self) -> AsyncDestinations:
        return AsyncDestinations(self._client)

    @cached_property
    def histories(self) -> AsyncHistories:
        return AsyncHistories(self._client)

    @cached_property
    def policies(self) -> AsyncPolicies:
        return AsyncPolicies(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncV3sWithRawResponse:
        return AsyncV3sWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncV3sWithStreamingResponse:
        return AsyncV3sWithStreamingResponse(self)


class V3sWithRawResponse:
    def __init__(self, v3s: V3s) -> None:
        self._v3s = v3s

    @cached_property
    def destinations(self) -> DestinationsWithRawResponse:
        return DestinationsWithRawResponse(self._v3s.destinations)

    @cached_property
    def histories(self) -> HistoriesWithRawResponse:
        return HistoriesWithRawResponse(self._v3s.histories)

    @cached_property
    def policies(self) -> PoliciesWithRawResponse:
        return PoliciesWithRawResponse(self._v3s.policies)


class AsyncV3sWithRawResponse:
    def __init__(self, v3s: AsyncV3s) -> None:
        self._v3s = v3s

    @cached_property
    def destinations(self) -> AsyncDestinationsWithRawResponse:
        return AsyncDestinationsWithRawResponse(self._v3s.destinations)

    @cached_property
    def histories(self) -> AsyncHistoriesWithRawResponse:
        return AsyncHistoriesWithRawResponse(self._v3s.histories)

    @cached_property
    def policies(self) -> AsyncPoliciesWithRawResponse:
        return AsyncPoliciesWithRawResponse(self._v3s.policies)


class V3sWithStreamingResponse:
    def __init__(self, v3s: V3s) -> None:
        self._v3s = v3s

    @cached_property
    def destinations(self) -> DestinationsWithStreamingResponse:
        return DestinationsWithStreamingResponse(self._v3s.destinations)

    @cached_property
    def histories(self) -> HistoriesWithStreamingResponse:
        return HistoriesWithStreamingResponse(self._v3s.histories)

    @cached_property
    def policies(self) -> PoliciesWithStreamingResponse:
        return PoliciesWithStreamingResponse(self._v3s.policies)


class AsyncV3sWithStreamingResponse:
    def __init__(self, v3s: AsyncV3s) -> None:
        self._v3s = v3s

    @cached_property
    def destinations(self) -> AsyncDestinationsWithStreamingResponse:
        return AsyncDestinationsWithStreamingResponse(self._v3s.destinations)

    @cached_property
    def histories(self) -> AsyncHistoriesWithStreamingResponse:
        return AsyncHistoriesWithStreamingResponse(self._v3s.histories)

    @cached_property
    def policies(self) -> AsyncPoliciesWithStreamingResponse:
        return AsyncPoliciesWithStreamingResponse(self._v3s.policies)
