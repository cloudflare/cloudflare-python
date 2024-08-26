# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .rules import RulesResource, AsyncRulesResource

from ..._compat import cached_property

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .rules import RulesResource, AsyncRulesResource, RulesResourceWithRawResponse, AsyncRulesResourceWithRawResponse, RulesResourceWithStreamingResponse, AsyncRulesResourceWithStreamingResponse

__all__ = ["CloudConnectorResource", "AsyncCloudConnectorResource"]

class CloudConnectorResource(SyncAPIResource):
    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> CloudConnectorResourceWithRawResponse:
        return CloudConnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CloudConnectorResourceWithStreamingResponse:
        return CloudConnectorResourceWithStreamingResponse(self)

class AsyncCloudConnectorResource(AsyncAPIResource):
    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCloudConnectorResourceWithRawResponse:
        return AsyncCloudConnectorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCloudConnectorResourceWithStreamingResponse:
        return AsyncCloudConnectorResourceWithStreamingResponse(self)

class CloudConnectorResourceWithRawResponse:
    def __init__(self, cloud_connector: CloudConnectorResource) -> None:
        self._cloud_connector = cloud_connector

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._cloud_connector.rules)

class AsyncCloudConnectorResourceWithRawResponse:
    def __init__(self, cloud_connector: AsyncCloudConnectorResource) -> None:
        self._cloud_connector = cloud_connector

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._cloud_connector.rules)

class CloudConnectorResourceWithStreamingResponse:
    def __init__(self, cloud_connector: CloudConnectorResource) -> None:
        self._cloud_connector = cloud_connector

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._cloud_connector.rules)

class AsyncCloudConnectorResourceWithStreamingResponse:
    def __init__(self, cloud_connector: AsyncCloudConnectorResource) -> None:
        self._cloud_connector = cloud_connector

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._cloud_connector.rules)