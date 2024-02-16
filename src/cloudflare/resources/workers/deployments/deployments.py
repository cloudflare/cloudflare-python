# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .by_scripts.by_scripts import ByScripts, AsyncByScripts

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
from .by_scripts import (
    ByScripts,
    AsyncByScripts,
    ByScriptsWithRawResponse,
    AsyncByScriptsWithRawResponse,
    ByScriptsWithStreamingResponse,
    AsyncByScriptsWithStreamingResponse,
)
from ...._wrappers import ResultWrapper

__all__ = ["Deployments", "AsyncDeployments"]


class Deployments(SyncAPIResource):
    @cached_property
    def by_scripts(self) -> ByScripts:
        return ByScripts(self._client)

    @cached_property
    def with_raw_response(self) -> DeploymentsWithRawResponse:
        return DeploymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeploymentsWithStreamingResponse:
        return DeploymentsWithStreamingResponse(self)


class AsyncDeployments(AsyncAPIResource):
    @cached_property
    def by_scripts(self) -> AsyncByScripts:
        return AsyncByScripts(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDeploymentsWithRawResponse:
        return AsyncDeploymentsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeploymentsWithStreamingResponse:
        return AsyncDeploymentsWithStreamingResponse(self)


class DeploymentsWithRawResponse:
    def __init__(self, deployments: Deployments) -> None:
        self._deployments = deployments

    @cached_property
    def by_scripts(self) -> ByScriptsWithRawResponse:
        return ByScriptsWithRawResponse(self._deployments.by_scripts)


class AsyncDeploymentsWithRawResponse:
    def __init__(self, deployments: AsyncDeployments) -> None:
        self._deployments = deployments

    @cached_property
    def by_scripts(self) -> AsyncByScriptsWithRawResponse:
        return AsyncByScriptsWithRawResponse(self._deployments.by_scripts)


class DeploymentsWithStreamingResponse:
    def __init__(self, deployments: Deployments) -> None:
        self._deployments = deployments

    @cached_property
    def by_scripts(self) -> ByScriptsWithStreamingResponse:
        return ByScriptsWithStreamingResponse(self._deployments.by_scripts)


class AsyncDeploymentsWithStreamingResponse:
    def __init__(self, deployments: AsyncDeployments) -> None:
        self._deployments = deployments

    @cached_property
    def by_scripts(self) -> AsyncByScriptsWithStreamingResponse:
        return AsyncByScriptsWithStreamingResponse(self._deployments.by_scripts)
