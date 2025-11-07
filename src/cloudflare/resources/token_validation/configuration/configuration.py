# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from .credentials import (
    CredentialsResource,
    AsyncCredentialsResource,
    CredentialsResourceWithRawResponse,
    AsyncCredentialsResourceWithRawResponse,
    CredentialsResourceWithStreamingResponse,
    AsyncCredentialsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ...._base_client import AsyncPaginator, make_request_options
from ....types.token_validation import configuration_edit_params, configuration_list_params, configuration_create_params
from ....types.token_validation.token_config import TokenConfig
from ....types.token_validation.configuration_edit_response import ConfigurationEditResponse
from ....types.token_validation.configuration_delete_response import ConfigurationDeleteResponse

__all__ = ["ConfigurationResource", "AsyncConfigurationResource"]


class ConfigurationResource(SyncAPIResource):
    @cached_property
    def credentials(self) -> CredentialsResource:
        return CredentialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ConfigurationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        credentials: configuration_create_params.Credentials,
        description: str,
        title: str,
        token_sources: SequenceNotStr[str],
        token_type: Literal["JWT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenConfig:
        """
        Create a new Token Validation configuration

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/token_validation/config",
            body=maybe_transform(
                {
                    "credentials": credentials,
                    "description": description,
                    "title": title,
                    "token_sources": token_sources,
                    "token_type": token_type,
                },
                configuration_create_params.ConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TokenConfig]._unwrapper,
            ),
            cast_to=cast(Type[TokenConfig], ResultWrapper[TokenConfig]),
        )

    def list(
        self,
        *,
        zone_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncV4PagePaginationArray[TokenConfig]:
        """
        Lists all token validation configurations for this zone

        Args:
          zone_id: Identifier.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/token_validation/config",
            page=SyncV4PagePaginationArray[TokenConfig],
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
                    configuration_list_params.ConfigurationListParams,
                ),
            ),
            model=TokenConfig,
        )

    def delete(
        self,
        config_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationDeleteResponse:
        """
        Delete Token Configuration

        Args:
          zone_id: Identifier.

          config_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._delete(
            f"/zones/{zone_id}/token_validation/config/{config_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigurationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationDeleteResponse], ResultWrapper[ConfigurationDeleteResponse]),
        )

    def edit(
        self,
        config_id: str,
        *,
        zone_id: str,
        description: str | Omit = omit,
        title: str | Omit = omit,
        token_sources: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationEditResponse:
        """
        Edit fields of an existing Token Configuration

        Args:
          zone_id: Identifier.

          config_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._patch(
            f"/zones/{zone_id}/token_validation/config/{config_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "title": title,
                    "token_sources": token_sources,
                },
                configuration_edit_params.ConfigurationEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigurationEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationEditResponse], ResultWrapper[ConfigurationEditResponse]),
        )

    def get(
        self,
        config_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenConfig:
        """
        Get a single Token Configuration

        Args:
          zone_id: Identifier.

          config_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return self._get(
            f"/zones/{zone_id}/token_validation/config/{config_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TokenConfig]._unwrapper,
            ),
            cast_to=cast(Type[TokenConfig], ResultWrapper[TokenConfig]),
        )


class AsyncConfigurationResource(AsyncAPIResource):
    @cached_property
    def credentials(self) -> AsyncCredentialsResource:
        return AsyncCredentialsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncConfigurationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncConfigurationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncConfigurationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        credentials: configuration_create_params.Credentials,
        description: str,
        title: str,
        token_sources: SequenceNotStr[str],
        token_type: Literal["JWT"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenConfig:
        """
        Create a new Token Validation configuration

        Args:
          zone_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/token_validation/config",
            body=await async_maybe_transform(
                {
                    "credentials": credentials,
                    "description": description,
                    "title": title,
                    "token_sources": token_sources,
                    "token_type": token_type,
                },
                configuration_create_params.ConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TokenConfig]._unwrapper,
            ),
            cast_to=cast(Type[TokenConfig], ResultWrapper[TokenConfig]),
        )

    def list(
        self,
        *,
        zone_id: str,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[TokenConfig, AsyncV4PagePaginationArray[TokenConfig]]:
        """
        Lists all token validation configurations for this zone

        Args:
          zone_id: Identifier.

          page: Page number of paginated results.

          per_page: Maximum number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/token_validation/config",
            page=AsyncV4PagePaginationArray[TokenConfig],
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
                    configuration_list_params.ConfigurationListParams,
                ),
            ),
            model=TokenConfig,
        )

    async def delete(
        self,
        config_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationDeleteResponse:
        """
        Delete Token Configuration

        Args:
          zone_id: Identifier.

          config_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/token_validation/config/{config_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigurationDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationDeleteResponse], ResultWrapper[ConfigurationDeleteResponse]),
        )

    async def edit(
        self,
        config_id: str,
        *,
        zone_id: str,
        description: str | Omit = omit,
        title: str | Omit = omit,
        token_sources: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ConfigurationEditResponse:
        """
        Edit fields of an existing Token Configuration

        Args:
          zone_id: Identifier.

          config_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/token_validation/config/{config_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "title": title,
                    "token_sources": token_sources,
                },
                configuration_edit_params.ConfigurationEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ConfigurationEditResponse]._unwrapper,
            ),
            cast_to=cast(Type[ConfigurationEditResponse], ResultWrapper[ConfigurationEditResponse]),
        )

    async def get(
        self,
        config_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> TokenConfig:
        """
        Get a single Token Configuration

        Args:
          zone_id: Identifier.

          config_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not config_id:
            raise ValueError(f"Expected a non-empty value for `config_id` but received {config_id!r}")
        return await self._get(
            f"/zones/{zone_id}/token_validation/config/{config_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[TokenConfig]._unwrapper,
            ),
            cast_to=cast(Type[TokenConfig], ResultWrapper[TokenConfig]),
        )


class ConfigurationResourceWithRawResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

        self.create = to_raw_response_wrapper(
            configuration.create,
        )
        self.list = to_raw_response_wrapper(
            configuration.list,
        )
        self.delete = to_raw_response_wrapper(
            configuration.delete,
        )
        self.edit = to_raw_response_wrapper(
            configuration.edit,
        )
        self.get = to_raw_response_wrapper(
            configuration.get,
        )

    @cached_property
    def credentials(self) -> CredentialsResourceWithRawResponse:
        return CredentialsResourceWithRawResponse(self._configuration.credentials)


class AsyncConfigurationResourceWithRawResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

        self.create = async_to_raw_response_wrapper(
            configuration.create,
        )
        self.list = async_to_raw_response_wrapper(
            configuration.list,
        )
        self.delete = async_to_raw_response_wrapper(
            configuration.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            configuration.edit,
        )
        self.get = async_to_raw_response_wrapper(
            configuration.get,
        )

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithRawResponse:
        return AsyncCredentialsResourceWithRawResponse(self._configuration.credentials)


class ConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: ConfigurationResource) -> None:
        self._configuration = configuration

        self.create = to_streamed_response_wrapper(
            configuration.create,
        )
        self.list = to_streamed_response_wrapper(
            configuration.list,
        )
        self.delete = to_streamed_response_wrapper(
            configuration.delete,
        )
        self.edit = to_streamed_response_wrapper(
            configuration.edit,
        )
        self.get = to_streamed_response_wrapper(
            configuration.get,
        )

    @cached_property
    def credentials(self) -> CredentialsResourceWithStreamingResponse:
        return CredentialsResourceWithStreamingResponse(self._configuration.credentials)


class AsyncConfigurationResourceWithStreamingResponse:
    def __init__(self, configuration: AsyncConfigurationResource) -> None:
        self._configuration = configuration

        self.create = async_to_streamed_response_wrapper(
            configuration.create,
        )
        self.list = async_to_streamed_response_wrapper(
            configuration.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            configuration.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            configuration.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            configuration.get,
        )

    @cached_property
    def credentials(self) -> AsyncCredentialsResourceWithStreamingResponse:
        return AsyncCredentialsResourceWithStreamingResponse(self._configuration.credentials)
