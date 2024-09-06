# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .config import ConfigResource, AsyncConfigResource

from ....._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ....._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ....._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ....._resource import SyncAPIResource, AsyncAPIResource
from .....types import shared_params
from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)

__all__ = ["CmbResource", "AsyncCmbResource"]


class CmbResource(SyncAPIResource):
    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> CmbResourceWithRawResponse:
        return CmbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CmbResourceWithStreamingResponse:
        return CmbResourceWithStreamingResponse(self)


class AsyncCmbResource(AsyncAPIResource):
    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCmbResourceWithRawResponse:
        return AsyncCmbResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCmbResourceWithStreamingResponse:
        return AsyncCmbResourceWithStreamingResponse(self)


class CmbResourceWithRawResponse:
    def __init__(self, cmb: CmbResource) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._cmb.config)


class AsyncCmbResourceWithRawResponse:
    def __init__(self, cmb: AsyncCmbResource) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._cmb.config)


class CmbResourceWithStreamingResponse:
    def __init__(self, cmb: CmbResource) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._cmb.config)


class AsyncCmbResourceWithStreamingResponse:
    def __init__(self, cmb: AsyncCmbResource) -> None:
        self._cmb = cmb

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._cmb.config)
