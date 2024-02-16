# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .environments.environments import Environments, AsyncEnvironments

from ...._compat import cached_property

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
from .environments import (
    Environments,
    AsyncEnvironments,
    EnvironmentsWithRawResponse,
    AsyncEnvironmentsWithRawResponse,
    EnvironmentsWithStreamingResponse,
    AsyncEnvironmentsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Services", "AsyncServices"]


class Services(SyncAPIResource):
    @cached_property
    def environments(self) -> Environments:
        return Environments(self._client)

    @cached_property
    def with_raw_response(self) -> ServicesWithRawResponse:
        return ServicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServicesWithStreamingResponse:
        return ServicesWithStreamingResponse(self)


class AsyncServices(AsyncAPIResource):
    @cached_property
    def environments(self) -> AsyncEnvironments:
        return AsyncEnvironments(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncServicesWithRawResponse:
        return AsyncServicesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServicesWithStreamingResponse:
        return AsyncServicesWithStreamingResponse(self)


class ServicesWithRawResponse:
    def __init__(self, services: Services) -> None:
        self._services = services

    @cached_property
    def environments(self) -> EnvironmentsWithRawResponse:
        return EnvironmentsWithRawResponse(self._services.environments)


class AsyncServicesWithRawResponse:
    def __init__(self, services: AsyncServices) -> None:
        self._services = services

    @cached_property
    def environments(self) -> AsyncEnvironmentsWithRawResponse:
        return AsyncEnvironmentsWithRawResponse(self._services.environments)


class ServicesWithStreamingResponse:
    def __init__(self, services: Services) -> None:
        self._services = services

    @cached_property
    def environments(self) -> EnvironmentsWithStreamingResponse:
        return EnvironmentsWithStreamingResponse(self._services.environments)


class AsyncServicesWithStreamingResponse:
    def __init__(self, services: AsyncServices) -> None:
        self._services = services

    @cached_property
    def environments(self) -> AsyncEnvironmentsWithStreamingResponse:
        return AsyncEnvironmentsWithStreamingResponse(self._services.environments)
