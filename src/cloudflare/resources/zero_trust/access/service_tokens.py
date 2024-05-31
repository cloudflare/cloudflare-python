# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.zero_trust.access import service_token_create_params
from ....types.zero_trust.access.service_token import ServiceToken
from ....types.zero_trust.access.service_token_create_response import ServiceTokenCreateResponse

__all__ = ["ServiceTokensResource", "AsyncServiceTokensResource"]


class ServiceTokensResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ServiceTokensResourceWithRawResponse:
        return ServiceTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceTokensResourceWithStreamingResponse:
        return ServiceTokensResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ServiceTokenCreateResponse]:
        """Generates a new service token.

        **Note:** This is the only time you can get the
        Client Secret. If you lose the Client Secret, you will have to rotate the Client
        Secret or create a new service token.

        Args:
          name: The name of the service token.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          duration: The duration for how long the service token will be valid. Must be in the format
              `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The
              default is 1 year in hours (8760h).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens",
            body=maybe_transform(
                {
                    "name": name,
                    "duration": duration,
                },
                service_token_create_params.ServiceTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceTokenCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceTokenCreateResponse]], ResultWrapper[ServiceTokenCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[ServiceToken]:
        """
        Lists all service tokens.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens",
            page=SyncSinglePage[ServiceToken],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ServiceToken,
        )


class AsyncServiceTokensResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncServiceTokensResourceWithRawResponse:
        return AsyncServiceTokensResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceTokensResourceWithStreamingResponse:
        return AsyncServiceTokensResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ServiceTokenCreateResponse]:
        """Generates a new service token.

        **Note:** This is the only time you can get the
        Client Secret. If you lose the Client Secret, you will have to rotate the Client
        Secret or create a new service token.

        Args:
          name: The name of the service token.

          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          duration: The duration for how long the service token will be valid. Must be in the format
              `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The
              default is 1 year in hours (8760h).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "duration": duration,
                },
                service_token_create_params.ServiceTokenCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[ServiceTokenCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[ServiceTokenCreateResponse]], ResultWrapper[ServiceTokenCreateResponse]),
        )

    def list(
        self,
        *,
        account_id: str | NotGiven = NOT_GIVEN,
        zone_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ServiceToken, AsyncSinglePage[ServiceToken]]:
        """
        Lists all service tokens.

        Args:
          account_id: The Account ID to use for this endpoint. Mutually exclusive with the Zone ID.

          zone_id: The Zone ID to use for this endpoint. Mutually exclusive with the Account ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id and zone_id:
            raise ValueError("You cannot provide both account_id and zone_id")

        if account_id:
            account_or_zone = "accounts"
            account_or_zone_id = account_id
        else:
            if not zone_id:
                raise ValueError("You must provide either account_id or zone_id")

            account_or_zone = "zones"
            account_or_zone_id = zone_id
        return self._get_api_list(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens",
            page=AsyncSinglePage[ServiceToken],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ServiceToken,
        )


class ServiceTokensResourceWithRawResponse:
    def __init__(self, service_tokens: ServiceTokensResource) -> None:
        self._service_tokens = service_tokens

        self.create = to_raw_response_wrapper(
            service_tokens.create,
        )
        self.list = to_raw_response_wrapper(
            service_tokens.list,
        )


class AsyncServiceTokensResourceWithRawResponse:
    def __init__(self, service_tokens: AsyncServiceTokensResource) -> None:
        self._service_tokens = service_tokens

        self.create = async_to_raw_response_wrapper(
            service_tokens.create,
        )
        self.list = async_to_raw_response_wrapper(
            service_tokens.list,
        )


class ServiceTokensResourceWithStreamingResponse:
    def __init__(self, service_tokens: ServiceTokensResource) -> None:
        self._service_tokens = service_tokens

        self.create = to_streamed_response_wrapper(
            service_tokens.create,
        )
        self.list = to_streamed_response_wrapper(
            service_tokens.list,
        )


class AsyncServiceTokensResourceWithStreamingResponse:
    def __init__(self, service_tokens: AsyncServiceTokensResource) -> None:
        self._service_tokens = service_tokens

        self.create = async_to_streamed_response_wrapper(
            service_tokens.create,
        )
        self.list = async_to_streamed_response_wrapper(
            service_tokens.list,
        )
