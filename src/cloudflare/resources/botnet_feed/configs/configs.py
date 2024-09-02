# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .asn import ASNResource, AsyncASNResource

from ...._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from .asn import (
    ASNResource,
    AsyncASNResource,
    ASNResourceWithRawResponse,
    AsyncASNResourceWithRawResponse,
    ASNResourceWithStreamingResponse,
    AsyncASNResourceWithStreamingResponse,
)

__all__ = ["ConfigsResource", "AsyncConfigsResource"]


class ConfigsResource(SyncAPIResource):
    @cached_property
    def asn(self) -> ASNResource:
        return ASNResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigsResourceWithRawResponse:
        return ConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsResourceWithStreamingResponse:
        return ConfigsResourceWithStreamingResponse(self)


class AsyncConfigsResource(AsyncAPIResource):
    @cached_property
    def asn(self) -> AsyncASNResource:
        return AsyncASNResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigsResourceWithRawResponse:
        return AsyncConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsResourceWithStreamingResponse:
        return AsyncConfigsResourceWithStreamingResponse(self)


class ConfigsResourceWithRawResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

    @cached_property
    def asn(self) -> ASNResourceWithRawResponse:
        return ASNResourceWithRawResponse(self._configs.asn)


class AsyncConfigsResourceWithRawResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

    @cached_property
    def asn(self) -> AsyncASNResourceWithRawResponse:
        return AsyncASNResourceWithRawResponse(self._configs.asn)


class ConfigsResourceWithStreamingResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

    @cached_property
    def asn(self) -> ASNResourceWithStreamingResponse:
        return ASNResourceWithStreamingResponse(self._configs.asn)


class AsyncConfigsResourceWithStreamingResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

    @cached_property
    def asn(self) -> AsyncASNResourceWithStreamingResponse:
        return AsyncASNResourceWithStreamingResponse(self._configs.asn)
