# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from .configurations import Configurations, AsyncConfigurations

from ..._compat import cached_property

from .discoveries import Discoveries, AsyncDiscoveries

from .operations import Operations, AsyncOperations

from .schemas import Schemas, AsyncSchemas

from .settings.settings import Settings, AsyncSettings

from .user_schemas.user_schemas import UserSchemas, AsyncUserSchemas

from .discovery.discovery import Discovery, AsyncDiscovery

from .schema_validation import SchemaValidation, AsyncSchemaValidation

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
from .configurations import (
    Configurations,
    AsyncConfigurations,
    ConfigurationsWithRawResponse,
    AsyncConfigurationsWithRawResponse,
    ConfigurationsWithStreamingResponse,
    AsyncConfigurationsWithStreamingResponse,
)
from .discoveries import (
    Discoveries,
    AsyncDiscoveries,
    DiscoveriesWithRawResponse,
    AsyncDiscoveriesWithRawResponse,
    DiscoveriesWithStreamingResponse,
    AsyncDiscoveriesWithStreamingResponse,
)
from .operations import (
    Operations,
    AsyncOperations,
    OperationsWithRawResponse,
    AsyncOperationsWithRawResponse,
    OperationsWithStreamingResponse,
    AsyncOperationsWithStreamingResponse,
)
from .schemas import (
    Schemas,
    AsyncSchemas,
    SchemasWithRawResponse,
    AsyncSchemasWithRawResponse,
    SchemasWithStreamingResponse,
    AsyncSchemasWithStreamingResponse,
)
from .settings import (
    Settings,
    AsyncSettings,
    SettingsWithRawResponse,
    AsyncSettingsWithRawResponse,
    SettingsWithStreamingResponse,
    AsyncSettingsWithStreamingResponse,
)
from .user_schemas import (
    UserSchemas,
    AsyncUserSchemas,
    UserSchemasWithRawResponse,
    AsyncUserSchemasWithRawResponse,
    UserSchemasWithStreamingResponse,
    AsyncUserSchemasWithStreamingResponse,
)
from .discovery import (
    Discovery,
    AsyncDiscovery,
    DiscoveryWithRawResponse,
    AsyncDiscoveryWithRawResponse,
    DiscoveryWithStreamingResponse,
    AsyncDiscoveryWithStreamingResponse,
)
from .schema_validation import (
    SchemaValidation,
    AsyncSchemaValidation,
    SchemaValidationWithRawResponse,
    AsyncSchemaValidationWithRawResponse,
    SchemaValidationWithStreamingResponse,
    AsyncSchemaValidationWithStreamingResponse,
)
from ..._wrappers import ResultWrapper

__all__ = ["APIGateways", "AsyncAPIGateways"]


class APIGateways(SyncAPIResource):
    @cached_property
    def configurations(self) -> Configurations:
        return Configurations(self._client)

    @cached_property
    def discoveries(self) -> Discoveries:
        return Discoveries(self._client)

    @cached_property
    def operations(self) -> Operations:
        return Operations(self._client)

    @cached_property
    def schemas(self) -> Schemas:
        return Schemas(self._client)

    @cached_property
    def settings(self) -> Settings:
        return Settings(self._client)

    @cached_property
    def user_schemas(self) -> UserSchemas:
        return UserSchemas(self._client)

    @cached_property
    def discovery(self) -> Discovery:
        return Discovery(self._client)

    @cached_property
    def schema_validation(self) -> SchemaValidation:
        return SchemaValidation(self._client)

    @cached_property
    def with_raw_response(self) -> APIGatewaysWithRawResponse:
        return APIGatewaysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIGatewaysWithStreamingResponse:
        return APIGatewaysWithStreamingResponse(self)


class AsyncAPIGateways(AsyncAPIResource):
    @cached_property
    def configurations(self) -> AsyncConfigurations:
        return AsyncConfigurations(self._client)

    @cached_property
    def discoveries(self) -> AsyncDiscoveries:
        return AsyncDiscoveries(self._client)

    @cached_property
    def operations(self) -> AsyncOperations:
        return AsyncOperations(self._client)

    @cached_property
    def schemas(self) -> AsyncSchemas:
        return AsyncSchemas(self._client)

    @cached_property
    def settings(self) -> AsyncSettings:
        return AsyncSettings(self._client)

    @cached_property
    def user_schemas(self) -> AsyncUserSchemas:
        return AsyncUserSchemas(self._client)

    @cached_property
    def discovery(self) -> AsyncDiscovery:
        return AsyncDiscovery(self._client)

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidation:
        return AsyncSchemaValidation(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIGatewaysWithRawResponse:
        return AsyncAPIGatewaysWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIGatewaysWithStreamingResponse:
        return AsyncAPIGatewaysWithStreamingResponse(self)


class APIGatewaysWithRawResponse:
    def __init__(self, api_gateways: APIGateways) -> None:
        self._api_gateways = api_gateways

    @cached_property
    def configurations(self) -> ConfigurationsWithRawResponse:
        return ConfigurationsWithRawResponse(self._api_gateways.configurations)

    @cached_property
    def discoveries(self) -> DiscoveriesWithRawResponse:
        return DiscoveriesWithRawResponse(self._api_gateways.discoveries)

    @cached_property
    def operations(self) -> OperationsWithRawResponse:
        return OperationsWithRawResponse(self._api_gateways.operations)

    @cached_property
    def schemas(self) -> SchemasWithRawResponse:
        return SchemasWithRawResponse(self._api_gateways.schemas)

    @cached_property
    def settings(self) -> SettingsWithRawResponse:
        return SettingsWithRawResponse(self._api_gateways.settings)

    @cached_property
    def user_schemas(self) -> UserSchemasWithRawResponse:
        return UserSchemasWithRawResponse(self._api_gateways.user_schemas)

    @cached_property
    def discovery(self) -> DiscoveryWithRawResponse:
        return DiscoveryWithRawResponse(self._api_gateways.discovery)

    @cached_property
    def schema_validation(self) -> SchemaValidationWithRawResponse:
        return SchemaValidationWithRawResponse(self._api_gateways.schema_validation)


class AsyncAPIGatewaysWithRawResponse:
    def __init__(self, api_gateways: AsyncAPIGateways) -> None:
        self._api_gateways = api_gateways

    @cached_property
    def configurations(self) -> AsyncConfigurationsWithRawResponse:
        return AsyncConfigurationsWithRawResponse(self._api_gateways.configurations)

    @cached_property
    def discoveries(self) -> AsyncDiscoveriesWithRawResponse:
        return AsyncDiscoveriesWithRawResponse(self._api_gateways.discoveries)

    @cached_property
    def operations(self) -> AsyncOperationsWithRawResponse:
        return AsyncOperationsWithRawResponse(self._api_gateways.operations)

    @cached_property
    def schemas(self) -> AsyncSchemasWithRawResponse:
        return AsyncSchemasWithRawResponse(self._api_gateways.schemas)

    @cached_property
    def settings(self) -> AsyncSettingsWithRawResponse:
        return AsyncSettingsWithRawResponse(self._api_gateways.settings)

    @cached_property
    def user_schemas(self) -> AsyncUserSchemasWithRawResponse:
        return AsyncUserSchemasWithRawResponse(self._api_gateways.user_schemas)

    @cached_property
    def discovery(self) -> AsyncDiscoveryWithRawResponse:
        return AsyncDiscoveryWithRawResponse(self._api_gateways.discovery)

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationWithRawResponse:
        return AsyncSchemaValidationWithRawResponse(self._api_gateways.schema_validation)


class APIGatewaysWithStreamingResponse:
    def __init__(self, api_gateways: APIGateways) -> None:
        self._api_gateways = api_gateways

    @cached_property
    def configurations(self) -> ConfigurationsWithStreamingResponse:
        return ConfigurationsWithStreamingResponse(self._api_gateways.configurations)

    @cached_property
    def discoveries(self) -> DiscoveriesWithStreamingResponse:
        return DiscoveriesWithStreamingResponse(self._api_gateways.discoveries)

    @cached_property
    def operations(self) -> OperationsWithStreamingResponse:
        return OperationsWithStreamingResponse(self._api_gateways.operations)

    @cached_property
    def schemas(self) -> SchemasWithStreamingResponse:
        return SchemasWithStreamingResponse(self._api_gateways.schemas)

    @cached_property
    def settings(self) -> SettingsWithStreamingResponse:
        return SettingsWithStreamingResponse(self._api_gateways.settings)

    @cached_property
    def user_schemas(self) -> UserSchemasWithStreamingResponse:
        return UserSchemasWithStreamingResponse(self._api_gateways.user_schemas)

    @cached_property
    def discovery(self) -> DiscoveryWithStreamingResponse:
        return DiscoveryWithStreamingResponse(self._api_gateways.discovery)

    @cached_property
    def schema_validation(self) -> SchemaValidationWithStreamingResponse:
        return SchemaValidationWithStreamingResponse(self._api_gateways.schema_validation)


class AsyncAPIGatewaysWithStreamingResponse:
    def __init__(self, api_gateways: AsyncAPIGateways) -> None:
        self._api_gateways = api_gateways

    @cached_property
    def configurations(self) -> AsyncConfigurationsWithStreamingResponse:
        return AsyncConfigurationsWithStreamingResponse(self._api_gateways.configurations)

    @cached_property
    def discoveries(self) -> AsyncDiscoveriesWithStreamingResponse:
        return AsyncDiscoveriesWithStreamingResponse(self._api_gateways.discoveries)

    @cached_property
    def operations(self) -> AsyncOperationsWithStreamingResponse:
        return AsyncOperationsWithStreamingResponse(self._api_gateways.operations)

    @cached_property
    def schemas(self) -> AsyncSchemasWithStreamingResponse:
        return AsyncSchemasWithStreamingResponse(self._api_gateways.schemas)

    @cached_property
    def settings(self) -> AsyncSettingsWithStreamingResponse:
        return AsyncSettingsWithStreamingResponse(self._api_gateways.settings)

    @cached_property
    def user_schemas(self) -> AsyncUserSchemasWithStreamingResponse:
        return AsyncUserSchemasWithStreamingResponse(self._api_gateways.user_schemas)

    @cached_property
    def discovery(self) -> AsyncDiscoveryWithStreamingResponse:
        return AsyncDiscoveryWithStreamingResponse(self._api_gateways.discovery)

    @cached_property
    def schema_validation(self) -> AsyncSchemaValidationWithStreamingResponse:
        return AsyncSchemaValidationWithStreamingResponse(self._api_gateways.schema_validation)
