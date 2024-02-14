# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .monitors.monitors import Monitors, AsyncMonitors

from ...._compat import cached_property

from .pools.pools import Pools, AsyncPools

from .previews import Previews, AsyncPreviews

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
from .monitors import (
    Monitors,
    AsyncMonitors,
    MonitorsWithRawResponse,
    AsyncMonitorsWithRawResponse,
    MonitorsWithStreamingResponse,
    AsyncMonitorsWithStreamingResponse,
)
from .pools import (
    Pools,
    AsyncPools,
    PoolsWithRawResponse,
    AsyncPoolsWithRawResponse,
    PoolsWithStreamingResponse,
    AsyncPoolsWithStreamingResponse,
)
from .previews import (
    Previews,
    AsyncPreviews,
    PreviewsWithRawResponse,
    AsyncPreviewsWithRawResponse,
    PreviewsWithStreamingResponse,
    AsyncPreviewsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["LoadBalancers", "AsyncLoadBalancers"]


class LoadBalancers(SyncAPIResource):
    @cached_property
    def monitors(self) -> Monitors:
        return Monitors(self._client)

    @cached_property
    def pools(self) -> Pools:
        return Pools(self._client)

    @cached_property
    def previews(self) -> Previews:
        return Previews(self._client)

    @cached_property
    def with_raw_response(self) -> LoadBalancersWithRawResponse:
        return LoadBalancersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LoadBalancersWithStreamingResponse:
        return LoadBalancersWithStreamingResponse(self)


class AsyncLoadBalancers(AsyncAPIResource):
    @cached_property
    def monitors(self) -> AsyncMonitors:
        return AsyncMonitors(self._client)

    @cached_property
    def pools(self) -> AsyncPools:
        return AsyncPools(self._client)

    @cached_property
    def previews(self) -> AsyncPreviews:
        return AsyncPreviews(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLoadBalancersWithRawResponse:
        return AsyncLoadBalancersWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLoadBalancersWithStreamingResponse:
        return AsyncLoadBalancersWithStreamingResponse(self)


class LoadBalancersWithRawResponse:
    def __init__(self, load_balancers: LoadBalancers) -> None:
        self._load_balancers = load_balancers

    @cached_property
    def monitors(self) -> MonitorsWithRawResponse:
        return MonitorsWithRawResponse(self._load_balancers.monitors)

    @cached_property
    def pools(self) -> PoolsWithRawResponse:
        return PoolsWithRawResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> PreviewsWithRawResponse:
        return PreviewsWithRawResponse(self._load_balancers.previews)


class AsyncLoadBalancersWithRawResponse:
    def __init__(self, load_balancers: AsyncLoadBalancers) -> None:
        self._load_balancers = load_balancers

    @cached_property
    def monitors(self) -> AsyncMonitorsWithRawResponse:
        return AsyncMonitorsWithRawResponse(self._load_balancers.monitors)

    @cached_property
    def pools(self) -> AsyncPoolsWithRawResponse:
        return AsyncPoolsWithRawResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> AsyncPreviewsWithRawResponse:
        return AsyncPreviewsWithRawResponse(self._load_balancers.previews)


class LoadBalancersWithStreamingResponse:
    def __init__(self, load_balancers: LoadBalancers) -> None:
        self._load_balancers = load_balancers

    @cached_property
    def monitors(self) -> MonitorsWithStreamingResponse:
        return MonitorsWithStreamingResponse(self._load_balancers.monitors)

    @cached_property
    def pools(self) -> PoolsWithStreamingResponse:
        return PoolsWithStreamingResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> PreviewsWithStreamingResponse:
        return PreviewsWithStreamingResponse(self._load_balancers.previews)


class AsyncLoadBalancersWithStreamingResponse:
    def __init__(self, load_balancers: AsyncLoadBalancers) -> None:
        self._load_balancers = load_balancers

    @cached_property
    def monitors(self) -> AsyncMonitorsWithStreamingResponse:
        return AsyncMonitorsWithStreamingResponse(self._load_balancers.monitors)

    @cached_property
    def pools(self) -> AsyncPoolsWithStreamingResponse:
        return AsyncPoolsWithStreamingResponse(self._load_balancers.pools)

    @cached_property
    def previews(self) -> AsyncPreviewsWithStreamingResponse:
        return AsyncPreviewsWithStreamingResponse(self._load_balancers.previews)
