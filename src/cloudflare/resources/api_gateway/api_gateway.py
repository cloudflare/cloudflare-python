# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .configurations import ConfigurationsResource, AsyncConfigurationsResource

from ..._compat import cached_property

from .discovery.discovery import DiscoveryResource, AsyncDiscoveryResource

from .operations.operations import OperationsResource, AsyncOperationsResource

from .schemas import SchemasResource, AsyncSchemasResource

from .settings.settings import SettingsResource, AsyncSettingsResource

from .user_schemas.user_schemas import UserSchemasResource, AsyncUserSchemasResource

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from .configurations import ConfigurationsResource, AsyncConfigurationsResource, ConfigurationsResourceWithRawResponse, AsyncConfigurationsResourceWithRawResponse, ConfigurationsResourceWithStreamingResponse, AsyncConfigurationsResourceWithStreamingResponse
from .discovery import DiscoveryResource, AsyncDiscoveryResource, DiscoveryResourceWithRawResponse, AsyncDiscoveryResourceWithRawResponse, DiscoveryResourceWithStreamingResponse, AsyncDiscoveryResourceWithStreamingResponse
from .operations import OperationsResource, AsyncOperationsResource, OperationsResourceWithRawResponse, AsyncOperationsResourceWithRawResponse, OperationsResourceWithStreamingResponse, AsyncOperationsResourceWithStreamingResponse
from .schemas import SchemasResource, AsyncSchemasResource, SchemasResourceWithRawResponse, AsyncSchemasResourceWithRawResponse, SchemasResourceWithStreamingResponse, AsyncSchemasResourceWithStreamingResponse
from .settings import SettingsResource, AsyncSettingsResource, SettingsResourceWithRawResponse, AsyncSettingsResourceWithRawResponse, SettingsResourceWithStreamingResponse, AsyncSettingsResourceWithStreamingResponse
from .user_schemas import UserSchemasResource, AsyncUserSchemasResource, UserSchemasResourceWithRawResponse, AsyncUserSchemasResourceWithRawResponse, UserSchemasResourceWithStreamingResponse, AsyncUserSchemasResourceWithStreamingResponse

__all__ = ["APIGatewayResource", "AsyncAPIGatewayResource"]

class APIGatewayResource(SyncAPIResource):
    @cached_property
    def configurations(self) -> ConfigurationsResource:
        return ConfigurationsResource(self._client)

    @cached_property
    def discovery(self) -> DiscoveryResource:
        return DiscoveryResource(self._client)

    @cached_property
    def operations(self) -> OperationsResource:
        return OperationsResource(self._client)

    @cached_property
    def schemas(self) -> SchemasResource:
        return SchemasResource(self._client)

    @cached_property
    def settings(self) -> SettingsResource:
        return SettingsResource(self._client)

    @cached_property
    def user_schemas(self) -> UserSchemasResource:
        return UserSchemasResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIGatewayResourceWithRawResponse:
        return APIGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIGatewayResourceWithStreamingResponse:
        return APIGatewayResourceWithStreamingResponse(self)

class AsyncAPIGatewayResource(AsyncAPIResource):
    @cached_property
    def configurations(self) -> AsyncConfigurationsResource:
        return AsyncConfigurationsResource(self._client)

    @cached_property
    def discovery(self) -> AsyncDiscoveryResource:
        return AsyncDiscoveryResource(self._client)

    @cached_property
    def operations(self) -> AsyncOperationsResource:
        return AsyncOperationsResource(self._client)

    @cached_property
    def schemas(self) -> AsyncSchemasResource:
        return AsyncSchemasResource(self._client)

    @cached_property
    def settings(self) -> AsyncSettingsResource:
        return AsyncSettingsResource(self._client)

    @cached_property
    def user_schemas(self) -> AsyncUserSchemasResource:
        return AsyncUserSchemasResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIGatewayResourceWithRawResponse:
        return AsyncAPIGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIGatewayResourceWithStreamingResponse:
        return AsyncAPIGatewayResourceWithStreamingResponse(self)

class APIGatewayResourceWithRawResponse:
    def __init__(self, api_gateway: APIGatewayResource) -> None:
        self._api_gateway = api_gateway

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithRawResponse:
        return ConfigurationsResourceWithRawResponse(self._api_gateway.configurations)

    @cached_property
    def discovery(self) -> DiscoveryResourceWithRawResponse:
        return DiscoveryResourceWithRawResponse(self._api_gateway.discovery)

    @cached_property
    def operations(self) -> OperationsResourceWithRawResponse:
        return OperationsResourceWithRawResponse(self._api_gateway.operations)

    @cached_property
    def schemas(self) -> SchemasResourceWithRawResponse:
        return SchemasResourceWithRawResponse(self._api_gateway.schemas)

    @cached_property
    def settings(self) -> SettingsResourceWithRawResponse:
        return SettingsResourceWithRawResponse(self._api_gateway.settings)

    @cached_property
    def user_schemas(self) -> UserSchemasResourceWithRawResponse:
        return UserSchemasResourceWithRawResponse(self._api_gateway.user_schemas)

class AsyncAPIGatewayResourceWithRawResponse:
    def __init__(self, api_gateway: AsyncAPIGatewayResource) -> None:
        self._api_gateway = api_gateway

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithRawResponse:
        return AsyncConfigurationsResourceWithRawResponse(self._api_gateway.configurations)

    @cached_property
    def discovery(self) -> AsyncDiscoveryResourceWithRawResponse:
        return AsyncDiscoveryResourceWithRawResponse(self._api_gateway.discovery)

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithRawResponse:
        return AsyncOperationsResourceWithRawResponse(self._api_gateway.operations)

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithRawResponse:
        return AsyncSchemasResourceWithRawResponse(self._api_gateway.schemas)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithRawResponse:
        return AsyncSettingsResourceWithRawResponse(self._api_gateway.settings)

    @cached_property
    def user_schemas(self) -> AsyncUserSchemasResourceWithRawResponse:
        return AsyncUserSchemasResourceWithRawResponse(self._api_gateway.user_schemas)

class APIGatewayResourceWithStreamingResponse:
    def __init__(self, api_gateway: APIGatewayResource) -> None:
        self._api_gateway = api_gateway

    @cached_property
    def configurations(self) -> ConfigurationsResourceWithStreamingResponse:
        return ConfigurationsResourceWithStreamingResponse(self._api_gateway.configurations)

    @cached_property
    def discovery(self) -> DiscoveryResourceWithStreamingResponse:
        return DiscoveryResourceWithStreamingResponse(self._api_gateway.discovery)

    @cached_property
    def operations(self) -> OperationsResourceWithStreamingResponse:
        return OperationsResourceWithStreamingResponse(self._api_gateway.operations)

    @cached_property
    def schemas(self) -> SchemasResourceWithStreamingResponse:
        return SchemasResourceWithStreamingResponse(self._api_gateway.schemas)

    @cached_property
    def settings(self) -> SettingsResourceWithStreamingResponse:
        return SettingsResourceWithStreamingResponse(self._api_gateway.settings)

    @cached_property
    def user_schemas(self) -> UserSchemasResourceWithStreamingResponse:
        return UserSchemasResourceWithStreamingResponse(self._api_gateway.user_schemas)

class AsyncAPIGatewayResourceWithStreamingResponse:
    def __init__(self, api_gateway: AsyncAPIGatewayResource) -> None:
        self._api_gateway = api_gateway

    @cached_property
    def configurations(self) -> AsyncConfigurationsResourceWithStreamingResponse:
        return AsyncConfigurationsResourceWithStreamingResponse(self._api_gateway.configurations)

    @cached_property
    def discovery(self) -> AsyncDiscoveryResourceWithStreamingResponse:
        return AsyncDiscoveryResourceWithStreamingResponse(self._api_gateway.discovery)

    @cached_property
    def operations(self) -> AsyncOperationsResourceWithStreamingResponse:
        return AsyncOperationsResourceWithStreamingResponse(self._api_gateway.operations)

    @cached_property
    def schemas(self) -> AsyncSchemasResourceWithStreamingResponse:
        return AsyncSchemasResourceWithStreamingResponse(self._api_gateway.schemas)

    @cached_property
    def settings(self) -> AsyncSettingsResourceWithStreamingResponse:
        return AsyncSettingsResourceWithStreamingResponse(self._api_gateway.settings)

    @cached_property
    def user_schemas(self) -> AsyncUserSchemasResourceWithStreamingResponse:
        return AsyncUserSchemasResourceWithStreamingResponse(self._api_gateway.user_schemas)