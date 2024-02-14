# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .eligibles import Eligibles, AsyncEligibles

from ....._compat import cached_property

from .pagerduties import Pagerduties, AsyncPagerduties

from .webhooks import Webhooks, AsyncWebhooks

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from .....types import shared_params
from .eligibles import (
    Eligibles,
    AsyncEligibles,
    EligiblesWithRawResponse,
    AsyncEligiblesWithRawResponse,
    EligiblesWithStreamingResponse,
    AsyncEligiblesWithStreamingResponse,
)
from .pagerduties import (
    Pagerduties,
    AsyncPagerduties,
    PagerdutiesWithRawResponse,
    AsyncPagerdutiesWithRawResponse,
    PagerdutiesWithStreamingResponse,
    AsyncPagerdutiesWithStreamingResponse,
)
from .webhooks import (
    Webhooks,
    AsyncWebhooks,
    WebhooksWithRawResponse,
    AsyncWebhooksWithRawResponse,
    WebhooksWithStreamingResponse,
    AsyncWebhooksWithStreamingResponse,
)
from ....._wrappers import ResultWrapper

__all__ = ["Destinations", "AsyncDestinations"]


class Destinations(SyncAPIResource):
    @cached_property
    def eligibles(self) -> Eligibles:
        return Eligibles(self._client)

    @cached_property
    def pagerduties(self) -> Pagerduties:
        return Pagerduties(self._client)

    @cached_property
    def webhooks(self) -> Webhooks:
        return Webhooks(self._client)

    @cached_property
    def with_raw_response(self) -> DestinationsWithRawResponse:
        return DestinationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DestinationsWithStreamingResponse:
        return DestinationsWithStreamingResponse(self)


class AsyncDestinations(AsyncAPIResource):
    @cached_property
    def eligibles(self) -> AsyncEligibles:
        return AsyncEligibles(self._client)

    @cached_property
    def pagerduties(self) -> AsyncPagerduties:
        return AsyncPagerduties(self._client)

    @cached_property
    def webhooks(self) -> AsyncWebhooks:
        return AsyncWebhooks(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDestinationsWithRawResponse:
        return AsyncDestinationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDestinationsWithStreamingResponse:
        return AsyncDestinationsWithStreamingResponse(self)


class DestinationsWithRawResponse:
    def __init__(self, destinations: Destinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligibles(self) -> EligiblesWithRawResponse:
        return EligiblesWithRawResponse(self._destinations.eligibles)

    @cached_property
    def pagerduties(self) -> PagerdutiesWithRawResponse:
        return PagerdutiesWithRawResponse(self._destinations.pagerduties)

    @cached_property
    def webhooks(self) -> WebhooksWithRawResponse:
        return WebhooksWithRawResponse(self._destinations.webhooks)


class AsyncDestinationsWithRawResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligibles(self) -> AsyncEligiblesWithRawResponse:
        return AsyncEligiblesWithRawResponse(self._destinations.eligibles)

    @cached_property
    def pagerduties(self) -> AsyncPagerdutiesWithRawResponse:
        return AsyncPagerdutiesWithRawResponse(self._destinations.pagerduties)

    @cached_property
    def webhooks(self) -> AsyncWebhooksWithRawResponse:
        return AsyncWebhooksWithRawResponse(self._destinations.webhooks)


class DestinationsWithStreamingResponse:
    def __init__(self, destinations: Destinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligibles(self) -> EligiblesWithStreamingResponse:
        return EligiblesWithStreamingResponse(self._destinations.eligibles)

    @cached_property
    def pagerduties(self) -> PagerdutiesWithStreamingResponse:
        return PagerdutiesWithStreamingResponse(self._destinations.pagerduties)

    @cached_property
    def webhooks(self) -> WebhooksWithStreamingResponse:
        return WebhooksWithStreamingResponse(self._destinations.webhooks)


class AsyncDestinationsWithStreamingResponse:
    def __init__(self, destinations: AsyncDestinations) -> None:
        self._destinations = destinations

    @cached_property
    def eligibles(self) -> AsyncEligiblesWithStreamingResponse:
        return AsyncEligiblesWithStreamingResponse(self._destinations.eligibles)

    @cached_property
    def pagerduties(self) -> AsyncPagerdutiesWithStreamingResponse:
        return AsyncPagerdutiesWithStreamingResponse(self._destinations.pagerduties)

    @cached_property
    def webhooks(self) -> AsyncWebhooksWithStreamingResponse:
        return AsyncWebhooksWithStreamingResponse(self._destinations.webhooks)
