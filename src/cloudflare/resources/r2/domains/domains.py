# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .custom import CustomResource, AsyncCustomResource

from ...._compat import cached_property

from .managed import ManagedResource, AsyncManagedResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .custom import (
    CustomResource,
    AsyncCustomResource,
    CustomResourceWithRawResponse,
    AsyncCustomResourceWithRawResponse,
    CustomResourceWithStreamingResponse,
    AsyncCustomResourceWithStreamingResponse,
)
from .managed import (
    ManagedResource,
    AsyncManagedResource,
    ManagedResourceWithRawResponse,
    AsyncManagedResourceWithRawResponse,
    ManagedResourceWithStreamingResponse,
    AsyncManagedResourceWithStreamingResponse,
)

__all__ = ["DomainsResource", "AsyncDomainsResource"]


class DomainsResource(SyncAPIResource):
    @cached_property
    def custom(self) -> CustomResource:
        return CustomResource(self._client)

    @cached_property
    def managed(self) -> ManagedResource:
        return ManagedResource(self._client)

    @cached_property
    def with_raw_response(self) -> DomainsResourceWithRawResponse:
        return DomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DomainsResourceWithStreamingResponse:
        return DomainsResourceWithStreamingResponse(self)


class AsyncDomainsResource(AsyncAPIResource):
    @cached_property
    def custom(self) -> AsyncCustomResource:
        return AsyncCustomResource(self._client)

    @cached_property
    def managed(self) -> AsyncManagedResource:
        return AsyncManagedResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDomainsResourceWithRawResponse:
        return AsyncDomainsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDomainsResourceWithStreamingResponse:
        return AsyncDomainsResourceWithStreamingResponse(self)


class DomainsResourceWithRawResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

    @cached_property
    def custom(self) -> CustomResourceWithRawResponse:
        return CustomResourceWithRawResponse(self._domains.custom)

    @cached_property
    def managed(self) -> ManagedResourceWithRawResponse:
        return ManagedResourceWithRawResponse(self._domains.managed)


class AsyncDomainsResourceWithRawResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

    @cached_property
    def custom(self) -> AsyncCustomResourceWithRawResponse:
        return AsyncCustomResourceWithRawResponse(self._domains.custom)

    @cached_property
    def managed(self) -> AsyncManagedResourceWithRawResponse:
        return AsyncManagedResourceWithRawResponse(self._domains.managed)


class DomainsResourceWithStreamingResponse:
    def __init__(self, domains: DomainsResource) -> None:
        self._domains = domains

    @cached_property
    def custom(self) -> CustomResourceWithStreamingResponse:
        return CustomResourceWithStreamingResponse(self._domains.custom)

    @cached_property
    def managed(self) -> ManagedResourceWithStreamingResponse:
        return ManagedResourceWithStreamingResponse(self._domains.managed)


class AsyncDomainsResourceWithStreamingResponse:
    def __init__(self, domains: AsyncDomainsResource) -> None:
        self._domains = domains

    @cached_property
    def custom(self) -> AsyncCustomResourceWithStreamingResponse:
        return AsyncCustomResourceWithStreamingResponse(self._domains.custom)

    @cached_property
    def managed(self) -> AsyncManagedResourceWithStreamingResponse:
        return AsyncManagedResourceWithStreamingResponse(self._domains.managed)
