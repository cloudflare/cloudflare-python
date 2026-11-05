# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import AsyncPaginator, make_request_options
from ...types.hyperdrive import config_edit_params, config_list_params, config_create_params, config_update_params
from ...types.hyperdrive.config_get_response import ConfigGetResponse
from ...types.hyperdrive.config_edit_response import ConfigEditResponse
from ...types.hyperdrive.config_list_response import ConfigListResponse
from ...types.hyperdrive.config_create_response import ConfigCreateResponse
from ...types.hyperdrive.config_update_response import ConfigUpdateResponse
from ...types.hyperdrive.config_restart_response import ConfigRestartResponse

__all__ = ["ConfigsResource", "AsyncConfigsResource"]


class ConfigsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConfigsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        account_id: str,
        name: str,
        origin: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginOrigin,
        caching: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginCaching | Omit = omit,
        integration: Optional[object] | Omit = omit,
        mtls: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginMTLS | Omit = omit,
        origin_connection_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        """Creates and returns a new Hyperdrive configuration.

        For a PlanetScale
        integration, the Cloudflare account must already be linked to PlanetScale in the
        Hyperdrive dashboard.

        Args:
          account_id: Define configurations using a unique string identifier.

          name: The name of the Hyperdrive configuration. Used to identify the configuration in
              the Cloudflare dashboard and API.

          origin: Combines database connection fields with exactly one supported network location.

          mtls: mTLS configuration for the origin connection. Cannot be used with VPC Service
              origins; TLS must be managed on the VPC Service.

          origin_connection_limit: The (soft) maximum number of connections the Hyperdrive is allowed to make to
              the origin database.

              Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
              specified, defaults to 20 for free tier and 60 for paid tier. Certain
              Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
              if you need a higher limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_id: str,
        integration: config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationIntegration,
        name: str,
        caching: config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationCaching | Omit = omit,
        mtls: config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationMTLS | Omit = omit,
        origin: Optional[object] | Omit = omit,
        origin_connection_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        """Creates and returns a new Hyperdrive configuration.

        For a PlanetScale
        integration, the Cloudflare account must already be linked to PlanetScale in the
        Hyperdrive dashboard.

        Args:
          account_id: Define configurations using a unique string identifier.

          integration: Selects a PlanetScale database and provisions credentials managed by Cloudflare
              when creating a Hyperdrive configuration. The Cloudflare account must already be
              linked to PlanetScale in the Hyperdrive dashboard. The selection is returned as
              read-only metadata and cannot be changed with replace or update operations.

          name: The name of the Hyperdrive configuration. Used to identify the configuration in
              the Cloudflare dashboard and API.

          mtls: mTLS configuration for the origin connection. Cannot be used with VPC Service
              origins; TLS must be managed on the VPC Service.

          origin_connection_limit: The (soft) maximum number of connections the Hyperdrive is allowed to make to
              the origin database.

              Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
              specified, defaults to 20 for free tier and 60 for paid tier. Certain
              Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
              if you need a higher limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "name", "origin"], ["account_id", "integration", "name"])
    def create(
        self,
        *,
        account_id: str,
        name: str,
        origin: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginOrigin | Optional[object] | Omit = omit,
        caching: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginCaching
        | config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationCaching
        | Omit = omit,
        integration: Optional[object]
        | config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationIntegration
        | Omit = omit,
        mtls: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginMTLS
        | config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationMTLS
        | Omit = omit,
        origin_connection_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/hyperdrive/configs", account_id=account_id),
            body=maybe_transform(
                {
                    "name": name,
                    "origin": origin,
                    "caching": caching,
                    "integration": integration,
                    "mtls": mtls,
                    "origin_connection_limit": origin_connection_limit,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigCreateResponse], ResultWrapper[ConfigCreateResponse]),
        )

    def update(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        name: str,
        origin: config_update_params.Origin,
        caching: config_update_params.Caching | Omit = omit,
        mtls: config_update_params.MTLS | Omit = omit,
        origin_connection_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigUpdateResponse:
        """Replaces and returns the specified Hyperdrive configuration.

        The request must
        include the name and complete origin connection details. Omitted caching
        settings are reset to their defaults, while omitted mTLS settings and origin
        connection limits are preserved. The integration association is set only during
        creation and cannot be changed; omit the integration field even when replacing
        an integration-backed configuration. Use the update operation to modify only
        selected fields.

        Args:
          account_id: Define configurations using a unique string identifier.

          hyperdrive_id: Define configurations using a unique string identifier.

          name: The name of the Hyperdrive configuration. Used to identify the configuration in
              the Cloudflare dashboard and API.

          origin: Combines database connection fields with exactly one supported network location.

          mtls: mTLS configuration for the origin connection. Cannot be used with VPC Service
              origins; TLS must be managed on the VPC Service.

          origin_connection_limit: The (soft) maximum number of connections the Hyperdrive is allowed to make to
              the origin database.

              Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
              specified, defaults to 20 for free tier and 60 for paid tier. Certain
              Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
              if you need a higher limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
                account_id=account_id,
                hyperdrive_id=hyperdrive_id,
            ),
            body=maybe_transform(
                {
                    "name": name,
                    "origin": origin,
                    "caching": caching,
                    "mtls": mtls,
                    "origin_connection_limit": origin_connection_limit,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigUpdateResponse], ResultWrapper[ConfigUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[ConfigListResponse]:
        """
        Returns a list of Hyperdrives.

        Args:
          account_id: Define configurations using a unique string identifier.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/hyperdrive/configs", account_id=account_id),
            page=SyncV4PagePaginationArray[ConfigListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    config_list_params.ConfigListParams,
                ),
            ),
            model=ConfigListResponse,
        )

    def delete(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes the specified Hyperdrive.

        Args:
          account_id: Define configurations using a unique string identifier.

          hyperdrive_id: Define configurations using a unique string identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
                account_id=account_id,
                hyperdrive_id=hyperdrive_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def edit(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        caching: config_edit_params.Caching | Omit = omit,
        mtls: config_edit_params.MTLS | Omit = omit,
        name: str | Omit = omit,
        origin: config_edit_params.Origin | Omit = omit,
        origin_connection_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigEditResponse:
        """Updates and returns the specified fields of the Hyperdrive configuration.

        Custom
        caching settings are not kept if caching is disabled. For an integration-backed
        configuration, the integration association is preserved but cannot be changed;
        omit the integration field.

        Args:
          account_id: Define configurations using a unique string identifier.

          hyperdrive_id: Define configurations using a unique string identifier.

          mtls: mTLS configuration for the origin connection. Cannot be used with VPC Service
              origins; TLS must be managed on the VPC Service.

          name: The name of the Hyperdrive configuration. Used to identify the configuration in
              the Cloudflare dashboard and API. An empty value leaves the name unchanged.

          origin: Connect to a database through a Workers VPC Service. TLS settings (mTLS,
              sslmode) cannot be configured on the Hyperdrive when using a VPC Service origin;
              TLS must be managed on the VPC Service itself.

          origin_connection_limit: The (soft) maximum number of connections the Hyperdrive is allowed to make to
              the origin database.

              Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
              specified, defaults to 20 for free tier and 60 for paid tier. Certain
              Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
              if you need a higher limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
                account_id=account_id,
                hyperdrive_id=hyperdrive_id,
            ),
            body=maybe_transform(
                {
                    "caching": caching,
                    "mtls": mtls,
                    "name": name,
                    "origin": origin,
                    "origin_connection_limit": origin_connection_limit,
                },
                config_edit_params.ConfigEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigEditResponse], ResultWrapper[ConfigEditResponse]),
        )

    def get(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigGetResponse:
        """
        Returns the specified Hyperdrive configuration.

        Args:
          account_id: Define configurations using a unique string identifier.

          hyperdrive_id: Define configurations using a unique string identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
                account_id=account_id,
                hyperdrive_id=hyperdrive_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigGetResponse], ResultWrapper[ConfigGetResponse]),
        )

    def restart(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRestartResponse:
        """
        Restarts the connection pool for the specified Hyperdrive configuration without
        changing its configuration. Existing connections are drained and a new pool is
        established at the edge.

        Args:
          account_id: Define configurations using a unique string identifier.

          hyperdrive_id: Define configurations using a unique string identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}/restart",
                account_id=account_id,
                hyperdrive_id=hyperdrive_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigRestartResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigRestartResponse], ResultWrapper[ConfigRestartResponse]),
        )


class AsyncConfigsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncConfigsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConfigsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        account_id: str,
        name: str,
        origin: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginOrigin,
        caching: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginCaching | Omit = omit,
        integration: Optional[object] | Omit = omit,
        mtls: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginMTLS | Omit = omit,
        origin_connection_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        """Creates and returns a new Hyperdrive configuration.

        For a PlanetScale
        integration, the Cloudflare account must already be linked to PlanetScale in the
        Hyperdrive dashboard.

        Args:
          account_id: Define configurations using a unique string identifier.

          name: The name of the Hyperdrive configuration. Used to identify the configuration in
              the Cloudflare dashboard and API.

          origin: Combines database connection fields with exactly one supported network location.

          mtls: mTLS configuration for the origin connection. Cannot be used with VPC Service
              origins; TLS must be managed on the VPC Service.

          origin_connection_limit: The (soft) maximum number of connections the Hyperdrive is allowed to make to
              the origin database.

              Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
              specified, defaults to 20 for free tier and 60 for paid tier. Certain
              Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
              if you need a higher limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_id: str,
        integration: config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationIntegration,
        name: str,
        caching: config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationCaching | Omit = omit,
        mtls: config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationMTLS | Omit = omit,
        origin: Optional[object] | Omit = omit,
        origin_connection_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        """Creates and returns a new Hyperdrive configuration.

        For a PlanetScale
        integration, the Cloudflare account must already be linked to PlanetScale in the
        Hyperdrive dashboard.

        Args:
          account_id: Define configurations using a unique string identifier.

          integration: Selects a PlanetScale database and provisions credentials managed by Cloudflare
              when creating a Hyperdrive configuration. The Cloudflare account must already be
              linked to PlanetScale in the Hyperdrive dashboard. The selection is returned as
              read-only metadata and cannot be changed with replace or update operations.

          name: The name of the Hyperdrive configuration. Used to identify the configuration in
              the Cloudflare dashboard and API.

          mtls: mTLS configuration for the origin connection. Cannot be used with VPC Service
              origins; TLS must be managed on the VPC Service.

          origin_connection_limit: The (soft) maximum number of connections the Hyperdrive is allowed to make to
              the origin database.

              Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
              specified, defaults to 20 for free tier and 60 for paid tier. Certain
              Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
              if you need a higher limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "name", "origin"], ["account_id", "integration", "name"])
    async def create(
        self,
        *,
        account_id: str,
        name: str,
        origin: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginOrigin | Optional[object] | Omit = omit,
        caching: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginCaching
        | config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationCaching
        | Omit = omit,
        integration: Optional[object]
        | config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationIntegration
        | Omit = omit,
        mtls: config_create_params.HyperdriveHyperdriveConfigCreateWithOriginMTLS
        | config_create_params.HyperdriveHyperdriveConfigCreateWithIntegrationMTLS
        | Omit = omit,
        origin_connection_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigCreateResponse:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/hyperdrive/configs", account_id=account_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "origin": origin,
                    "caching": caching,
                    "integration": integration,
                    "mtls": mtls,
                    "origin_connection_limit": origin_connection_limit,
                },
                config_create_params.ConfigCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigCreateResponse], ResultWrapper[ConfigCreateResponse]),
        )

    async def update(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        name: str,
        origin: config_update_params.Origin,
        caching: config_update_params.Caching | Omit = omit,
        mtls: config_update_params.MTLS | Omit = omit,
        origin_connection_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigUpdateResponse:
        """Replaces and returns the specified Hyperdrive configuration.

        The request must
        include the name and complete origin connection details. Omitted caching
        settings are reset to their defaults, while omitted mTLS settings and origin
        connection limits are preserved. The integration association is set only during
        creation and cannot be changed; omit the integration field even when replacing
        an integration-backed configuration. Use the update operation to modify only
        selected fields.

        Args:
          account_id: Define configurations using a unique string identifier.

          hyperdrive_id: Define configurations using a unique string identifier.

          name: The name of the Hyperdrive configuration. Used to identify the configuration in
              the Cloudflare dashboard and API.

          origin: Combines database connection fields with exactly one supported network location.

          mtls: mTLS configuration for the origin connection. Cannot be used with VPC Service
              origins; TLS must be managed on the VPC Service.

          origin_connection_limit: The (soft) maximum number of connections the Hyperdrive is allowed to make to
              the origin database.

              Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
              specified, defaults to 20 for free tier and 60 for paid tier. Certain
              Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
              if you need a higher limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
                account_id=account_id,
                hyperdrive_id=hyperdrive_id,
            ),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "origin": origin,
                    "caching": caching,
                    "mtls": mtls,
                    "origin_connection_limit": origin_connection_limit,
                },
                config_update_params.ConfigUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigUpdateResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigUpdateResponse], ResultWrapper[ConfigUpdateResponse]),
        )

    def list(
        self,
        *,
        account_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ConfigListResponse, AsyncV4PagePaginationArray[ConfigListResponse]]:
        """
        Returns a list of Hyperdrives.

        Args:
          account_id: Define configurations using a unique string identifier.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/hyperdrive/configs", account_id=account_id),
            page=AsyncV4PagePaginationArray[ConfigListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    config_list_params.ConfigListParams,
                ),
            ),
            model=ConfigListResponse,
        )

    async def delete(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> object:
        """
        Deletes the specified Hyperdrive.

        Args:
          account_id: Define configurations using a unique string identifier.

          hyperdrive_id: Define configurations using a unique string identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
                account_id=account_id,
                hyperdrive_id=hyperdrive_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def edit(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        caching: config_edit_params.Caching | Omit = omit,
        mtls: config_edit_params.MTLS | Omit = omit,
        name: str | Omit = omit,
        origin: config_edit_params.Origin | Omit = omit,
        origin_connection_limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigEditResponse:
        """Updates and returns the specified fields of the Hyperdrive configuration.

        Custom
        caching settings are not kept if caching is disabled. For an integration-backed
        configuration, the integration association is preserved but cannot be changed;
        omit the integration field.

        Args:
          account_id: Define configurations using a unique string identifier.

          hyperdrive_id: Define configurations using a unique string identifier.

          mtls: mTLS configuration for the origin connection. Cannot be used with VPC Service
              origins; TLS must be managed on the VPC Service.

          name: The name of the Hyperdrive configuration. Used to identify the configuration in
              the Cloudflare dashboard and API. An empty value leaves the name unchanged.

          origin: Connect to a database through a Workers VPC Service. TLS settings (mTLS,
              sslmode) cannot be configured on the Hyperdrive when using a VPC Service origin;
              TLS must be managed on the VPC Service itself.

          origin_connection_limit: The (soft) maximum number of connections the Hyperdrive is allowed to make to
              the origin database.

              Maximum allowed: 20 for free tier accounts, 100 for paid tier accounts. If not
              specified, defaults to 20 for free tier and 60 for paid tier. Certain
              Cloudflare-managed origins may be permitted a higher limit. Contact Cloudflare
              if you need a higher limit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
                account_id=account_id,
                hyperdrive_id=hyperdrive_id,
            ),
            body=await async_maybe_transform(
                {
                    "caching": caching,
                    "mtls": mtls,
                    "name": name,
                    "origin": origin,
                    "origin_connection_limit": origin_connection_limit,
                },
                config_edit_params.ConfigEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigEditResponse], ResultWrapper[ConfigEditResponse]),
        )

    async def get(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigGetResponse:
        """
        Returns the specified Hyperdrive configuration.

        Args:
          account_id: Define configurations using a unique string identifier.

          hyperdrive_id: Define configurations using a unique string identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}",
                account_id=account_id,
                hyperdrive_id=hyperdrive_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigGetResponse], ResultWrapper[ConfigGetResponse]),
        )

    async def restart(
        self,
        hyperdrive_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigRestartResponse:
        """
        Restarts the connection pool for the specified Hyperdrive configuration without
        changing its configuration. Existing connections are drained and a new pool is
        established at the edge.

        Args:
          account_id: Define configurations using a unique string identifier.

          hyperdrive_id: Define configurations using a unique string identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not hyperdrive_id:
            raise ValueError(f"Expected a non-empty value for `hyperdrive_id` but received {hyperdrive_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/hyperdrive/configs/{hyperdrive_id}/restart",
                account_id=account_id,
                hyperdrive_id=hyperdrive_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigRestartResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigRestartResponse], ResultWrapper[ConfigRestartResponse]),
        )


class ConfigsResourceWithRawResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.create = to_raw_response_wrapper(
            configs.create,
        )
        self.update = to_raw_response_wrapper(
            configs.update,
        )
        self.list = to_raw_response_wrapper(
            configs.list,
        )
        self.delete = to_raw_response_wrapper(
            configs.delete,
        )
        self.edit = to_raw_response_wrapper(
            configs.edit,
        )
        self.get = to_raw_response_wrapper(
            configs.get,
        )
        self.restart = to_raw_response_wrapper(
            configs.restart,
        )


class AsyncConfigsResourceWithRawResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.create = async_to_raw_response_wrapper(
            configs.create,
        )
        self.update = async_to_raw_response_wrapper(
            configs.update,
        )
        self.list = async_to_raw_response_wrapper(
            configs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            configs.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            configs.edit,
        )
        self.get = async_to_raw_response_wrapper(
            configs.get,
        )
        self.restart = async_to_raw_response_wrapper(
            configs.restart,
        )


class ConfigsResourceWithStreamingResponse:
    def __init__(self, configs: ConfigsResource) -> None:
        self._configs = configs

        self.create = to_streamed_response_wrapper(
            configs.create,
        )
        self.update = to_streamed_response_wrapper(
            configs.update,
        )
        self.list = to_streamed_response_wrapper(
            configs.list,
        )
        self.delete = to_streamed_response_wrapper(
            configs.delete,
        )
        self.edit = to_streamed_response_wrapper(
            configs.edit,
        )
        self.get = to_streamed_response_wrapper(
            configs.get,
        )
        self.restart = to_streamed_response_wrapper(
            configs.restart,
        )


class AsyncConfigsResourceWithStreamingResponse:
    def __init__(self, configs: AsyncConfigsResource) -> None:
        self._configs = configs

        self.create = async_to_streamed_response_wrapper(
            configs.create,
        )
        self.update = async_to_streamed_response_wrapper(
            configs.update,
        )
        self.list = async_to_streamed_response_wrapper(
            configs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            configs.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            configs.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            configs.get,
        )
        self.restart = async_to_streamed_response_wrapper(
            configs.restart,
        )
