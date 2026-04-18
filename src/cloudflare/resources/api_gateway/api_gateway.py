# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .schemas import (
    SchemasResource,
    AsyncSchemasResource,
    SchemasResourceWithRawResponse,
    AsyncSchemasResourceWithRawResponse,
    SchemasResourceWithStreamingResponse,
    AsyncSchemasResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .configurations import (
    ConfigurationsResource,
    AsyncConfigurationsResource,
    ConfigurationsResourceWithRawResponse,
    AsyncConfigurationsResourceWithRawResponse,
    ConfigurationsResourceWithStreamingResponse,
    AsyncConfigurationsResourceWithStreamingResponse,
)
from .settings.settings import (
    SettingsResource,
    AsyncSettingsResource,
    SettingsResourceWithRawResponse,
    AsyncSettingsResourceWithRawResponse,
    SettingsResourceWithStreamingResponse,
    AsyncSettingsResourceWithStreamingResponse,
)
from .discovery.discovery import (
    DiscoveryResource,
    AsyncDiscoveryResource,
    DiscoveryResourceWithRawResponse,
    AsyncDiscoveryResourceWithRawResponse,
    DiscoveryResourceWithStreamingResponse,
    AsyncDiscoveryResourceWithStreamingResponse,
)
from .operations.operations import (
    OperationsResource,
    AsyncOperationsResource,
    OperationsResourceWithRawResponse,
    AsyncOperationsResourceWithRawResponse,
    OperationsResourceWithStreamingResponse,
    AsyncOperationsResourceWithStreamingResponse,
)
from .user_schemas.user_schemas import (
    UserSchemasResource,
    AsyncUserSchemasResource,
    UserSchemasResourceWithRawResponse,
    AsyncUserSchemasResourceWithRawResponse,
    UserSchemasResourceWithStreamingResponse,
    AsyncUserSchemasResourceWithStreamingResponse,
)
from .expression_template.expression_template import (
    ExpressionTemplateResource,
    AsyncExpressionTemplateResource,
    ExpressionTemplateResourceWithRawResponse,
    AsyncExpressionTemplateResourceWithRawResponse,
    ExpressionTemplateResourceWithStreamingResponse,
    AsyncExpressionTemplateResourceWithStreamingResponse,
)

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
    def expression_template(self) -> ExpressionTemplateResource:
        return ExpressionTemplateResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return APIGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIGatewayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
    def expression_template(self) -> AsyncExpressionTemplateResource:
        return AsyncExpressionTemplateResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIGatewayResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIGatewayResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIGatewayResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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

    @cached_property
    def expression_template(self) -> ExpressionTemplateResourceWithRawResponse:
        return ExpressionTemplateResourceWithRawResponse(self._api_gateway.expression_template)


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

    @cached_property
    def expression_template(self) -> AsyncExpressionTemplateResourceWithRawResponse:
        return AsyncExpressionTemplateResourceWithRawResponse(self._api_gateway.expression_template)


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

    @cached_property
    def expression_template(self) -> ExpressionTemplateResourceWithStreamingResponse:
        return ExpressionTemplateResourceWithStreamingResponse(self._api_gateway.expression_template)


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

    @cached_property
    def expression_template(self) -> AsyncExpressionTemplateResourceWithStreamingResponse:
        return AsyncExpressionTemplateResourceWithStreamingResponse(self._api_gateway.expression_template)
