# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .configuration.configuration import ConfigurationResource, AsyncConfigurationResource

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .configuration import ConfigurationResource, AsyncConfigurationResource, ConfigurationResourceWithRawResponse, AsyncConfigurationResourceWithRawResponse, ConfigurationResourceWithStreamingResponse, AsyncConfigurationResourceWithStreamingResponse

__all__ = ["R2Resource", "AsyncR2Resource"]

class R2Resource(SyncAPIResource):
    @cached_property
    def configuration(self) -> ConfigurationResource:
        return ConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> R2ResourceWithRawResponse:
        return R2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> R2ResourceWithStreamingResponse:
        return R2ResourceWithStreamingResponse(self)

class AsyncR2Resource(AsyncAPIResource):
    @cached_property
    def configuration(self) -> AsyncConfigurationResource:
        return AsyncConfigurationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncR2ResourceWithRawResponse:
        return AsyncR2ResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncR2ResourceWithStreamingResponse:
        return AsyncR2ResourceWithStreamingResponse(self)

class R2ResourceWithRawResponse:
    def __init__(self, r2: R2Resource) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> ConfigurationResourceWithRawResponse:
        return ConfigurationResourceWithRawResponse(self._r2.configuration)

class AsyncR2ResourceWithRawResponse:
    def __init__(self, r2: AsyncR2Resource) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithRawResponse:
        return AsyncConfigurationResourceWithRawResponse(self._r2.configuration)

class R2ResourceWithStreamingResponse:
    def __init__(self, r2: R2Resource) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> ConfigurationResourceWithStreamingResponse:
        return ConfigurationResourceWithStreamingResponse(self._r2.configuration)

class AsyncR2ResourceWithStreamingResponse:
    def __init__(self, r2: AsyncR2Resource) -> None:
        self._r2 = r2

    @cached_property
    def configuration(self) -> AsyncConfigurationResourceWithStreamingResponse:
        return AsyncConfigurationResourceWithStreamingResponse(self._r2.configuration)