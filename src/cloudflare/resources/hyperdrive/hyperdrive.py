# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .configs import Configs, AsyncConfigs

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
from .configs import (
    Configs,
    AsyncConfigs,
    ConfigsWithRawResponse,
    AsyncConfigsWithRawResponse,
    ConfigsWithStreamingResponse,
    AsyncConfigsWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["Hyperdrive", "AsyncHyperdrive"]


class Hyperdrive(SyncAPIResource):
    @cached_property
    def configs(self) -> Configs:
        return Configs(self._client)

    @cached_property
    def with_raw_response(self) -> HyperdriveWithRawResponse:
        return HyperdriveWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HyperdriveWithStreamingResponse:
        return HyperdriveWithStreamingResponse(self)


class AsyncHyperdrive(AsyncAPIResource):
    @cached_property
    def configs(self) -> AsyncConfigs:
        return AsyncConfigs(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncHyperdriveWithRawResponse:
        return AsyncHyperdriveWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHyperdriveWithStreamingResponse:
        return AsyncHyperdriveWithStreamingResponse(self)


class HyperdriveWithRawResponse:
    def __init__(self, hyperdrive: Hyperdrive) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> ConfigsWithRawResponse:
        return ConfigsWithRawResponse(self._hyperdrive.configs)


class AsyncHyperdriveWithRawResponse:
    def __init__(self, hyperdrive: AsyncHyperdrive) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> AsyncConfigsWithRawResponse:
        return AsyncConfigsWithRawResponse(self._hyperdrive.configs)


class HyperdriveWithStreamingResponse:
    def __init__(self, hyperdrive: Hyperdrive) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> ConfigsWithStreamingResponse:
        return ConfigsWithStreamingResponse(self._hyperdrive.configs)


class AsyncHyperdriveWithStreamingResponse:
    def __init__(self, hyperdrive: AsyncHyperdrive) -> None:
        self._hyperdrive = hyperdrive

    @cached_property
    def configs(self) -> AsyncConfigsWithStreamingResponse:
        return AsyncConfigsWithStreamingResponse(self._hyperdrive.configs)
