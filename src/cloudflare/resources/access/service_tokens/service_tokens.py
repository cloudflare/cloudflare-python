# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from .refreshes import Refreshes, AsyncRefreshes

from ...._compat import cached_property

from .rotates import Rotates, AsyncRotates

from ....types.access import (
    ServiceTokenUpdateResponse,
    ServiceTokenDeleteResponse,
    ServiceTokenAccessServiceTokensCreateAServiceTokenResponse,
    ServiceTokenAccessServiceTokensListServiceTokensResponse,
)

from typing import Type, Optional

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

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
from ....types.access import service_token_update_params
from ....types.access import service_token_access_service_tokens_create_a_service_token_params
from .refreshes import (
    Refreshes,
    AsyncRefreshes,
    RefreshesWithRawResponse,
    AsyncRefreshesWithRawResponse,
    RefreshesWithStreamingResponse,
    AsyncRefreshesWithStreamingResponse,
)
from .rotates import (
    Rotates,
    AsyncRotates,
    RotatesWithRawResponse,
    AsyncRotatesWithRawResponse,
    RotatesWithStreamingResponse,
    AsyncRotatesWithStreamingResponse,
)
from ...._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ServiceTokens", "AsyncServiceTokens"]


class ServiceTokens(SyncAPIResource):
    @cached_property
    def refreshes(self) -> Refreshes:
        return Refreshes(self._client)

    @cached_property
    def rotates(self) -> Rotates:
        return Rotates(self._client)

    @cached_property
    def with_raw_response(self) -> ServiceTokensWithRawResponse:
        return ServiceTokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ServiceTokensWithStreamingResponse:
        return ServiceTokensWithStreamingResponse(self)

    def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        duration: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenUpdateResponse:
        """
        Updates a configured service token.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          duration: The duration for how long the service token will be valid. Must be in the format
              `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The
              default is 1 year in hours (8760h).

          name: The name of the service token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens/{uuid}",
            body=maybe_transform(
                {
                    "duration": duration,
                    "name": name,
                },
                service_token_update_params.ServiceTokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenUpdateResponse], ResultWrapper[ServiceTokenUpdateResponse]),
        )

    def delete(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenDeleteResponse:
        """
        Deletes a service token.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenDeleteResponse], ResultWrapper[ServiceTokenDeleteResponse]),
        )

    def access_service_tokens_create_a_service_token(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        name: str,
        duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenAccessServiceTokensCreateAServiceTokenResponse:
        """Generates a new service token.

        **Note:** This is the only time you can get the
        Client Secret. If you lose the Client Secret, you will have to rotate the Client
        Secret or create a new service token.

        Args:
          account_or_zone_id: Identifier

          name: The name of the service token.

          duration: The duration for how long the service token will be valid. Must be in the format
              `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The
              default is 1 year in hours (8760h).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens",
            body=maybe_transform(
                {
                    "name": name,
                    "duration": duration,
                },
                service_token_access_service_tokens_create_a_service_token_params.ServiceTokenAccessServiceTokensCreateAServiceTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ServiceTokenAccessServiceTokensCreateAServiceTokenResponse],
                ResultWrapper[ServiceTokenAccessServiceTokensCreateAServiceTokenResponse],
            ),
        )

    def access_service_tokens_list_service_tokens(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ServiceTokenAccessServiceTokensListServiceTokensResponse]:
        """
        Lists all service tokens.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ServiceTokenAccessServiceTokensListServiceTokensResponse]],
                ResultWrapper[ServiceTokenAccessServiceTokensListServiceTokensResponse],
            ),
        )


class AsyncServiceTokens(AsyncAPIResource):
    @cached_property
    def refreshes(self) -> AsyncRefreshes:
        return AsyncRefreshes(self._client)

    @cached_property
    def rotates(self) -> AsyncRotates:
        return AsyncRotates(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncServiceTokensWithRawResponse:
        return AsyncServiceTokensWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncServiceTokensWithStreamingResponse:
        return AsyncServiceTokensWithStreamingResponse(self)

    async def update(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        duration: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenUpdateResponse:
        """
        Updates a configured service token.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          duration: The duration for how long the service token will be valid. Must be in the format
              `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The
              default is 1 year in hours (8760h).

          name: The name of the service token.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._put(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens/{uuid}",
            body=maybe_transform(
                {
                    "duration": duration,
                    "name": name,
                },
                service_token_update_params.ServiceTokenUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenUpdateResponse], ResultWrapper[ServiceTokenUpdateResponse]),
        )

    async def delete(
        self,
        uuid: str,
        *,
        account_or_zone: str,
        account_or_zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenDeleteResponse:
        """
        Deletes a service token.

        Args:
          account_or_zone_id: Identifier

          uuid: UUID

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        if not uuid:
            raise ValueError(f"Expected a non-empty value for `uuid` but received {uuid!r}")
        return await self._delete(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens/{uuid}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ServiceTokenDeleteResponse], ResultWrapper[ServiceTokenDeleteResponse]),
        )

    async def access_service_tokens_create_a_service_token(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        name: str,
        duration: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ServiceTokenAccessServiceTokensCreateAServiceTokenResponse:
        """Generates a new service token.

        **Note:** This is the only time you can get the
        Client Secret. If you lose the Client Secret, you will have to rotate the Client
        Secret or create a new service token.

        Args:
          account_or_zone_id: Identifier

          name: The name of the service token.

          duration: The duration for how long the service token will be valid. Must be in the format
              `300ms` or `2h45m`. Valid time units are: ns, us (or µs), ms, s, m, h. The
              default is 1 year in hours (8760h).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._post(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens",
            body=maybe_transform(
                {
                    "name": name,
                    "duration": duration,
                },
                service_token_access_service_tokens_create_a_service_token_params.ServiceTokenAccessServiceTokensCreateAServiceTokenParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[ServiceTokenAccessServiceTokensCreateAServiceTokenResponse],
                ResultWrapper[ServiceTokenAccessServiceTokensCreateAServiceTokenResponse],
            ),
        )

    async def access_service_tokens_list_service_tokens(
        self,
        account_or_zone_id: str,
        *,
        account_or_zone: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ServiceTokenAccessServiceTokensListServiceTokensResponse]:
        """
        Lists all service tokens.

        Args:
          account_or_zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_or_zone:
            raise ValueError(f"Expected a non-empty value for `account_or_zone` but received {account_or_zone!r}")
        if not account_or_zone_id:
            raise ValueError(f"Expected a non-empty value for `account_or_zone_id` but received {account_or_zone_id!r}")
        return await self._get(
            f"/{account_or_zone}/{account_or_zone_id}/access/service_tokens",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ServiceTokenAccessServiceTokensListServiceTokensResponse]],
                ResultWrapper[ServiceTokenAccessServiceTokensListServiceTokensResponse],
            ),
        )


class ServiceTokensWithRawResponse:
    def __init__(self, service_tokens: ServiceTokens) -> None:
        self._service_tokens = service_tokens

        self.update = to_raw_response_wrapper(
            service_tokens.update,
        )
        self.delete = to_raw_response_wrapper(
            service_tokens.delete,
        )
        self.access_service_tokens_create_a_service_token = to_raw_response_wrapper(
            service_tokens.access_service_tokens_create_a_service_token,
        )
        self.access_service_tokens_list_service_tokens = to_raw_response_wrapper(
            service_tokens.access_service_tokens_list_service_tokens,
        )

    @cached_property
    def refreshes(self) -> RefreshesWithRawResponse:
        return RefreshesWithRawResponse(self._service_tokens.refreshes)

    @cached_property
    def rotates(self) -> RotatesWithRawResponse:
        return RotatesWithRawResponse(self._service_tokens.rotates)


class AsyncServiceTokensWithRawResponse:
    def __init__(self, service_tokens: AsyncServiceTokens) -> None:
        self._service_tokens = service_tokens

        self.update = async_to_raw_response_wrapper(
            service_tokens.update,
        )
        self.delete = async_to_raw_response_wrapper(
            service_tokens.delete,
        )
        self.access_service_tokens_create_a_service_token = async_to_raw_response_wrapper(
            service_tokens.access_service_tokens_create_a_service_token,
        )
        self.access_service_tokens_list_service_tokens = async_to_raw_response_wrapper(
            service_tokens.access_service_tokens_list_service_tokens,
        )

    @cached_property
    def refreshes(self) -> AsyncRefreshesWithRawResponse:
        return AsyncRefreshesWithRawResponse(self._service_tokens.refreshes)

    @cached_property
    def rotates(self) -> AsyncRotatesWithRawResponse:
        return AsyncRotatesWithRawResponse(self._service_tokens.rotates)


class ServiceTokensWithStreamingResponse:
    def __init__(self, service_tokens: ServiceTokens) -> None:
        self._service_tokens = service_tokens

        self.update = to_streamed_response_wrapper(
            service_tokens.update,
        )
        self.delete = to_streamed_response_wrapper(
            service_tokens.delete,
        )
        self.access_service_tokens_create_a_service_token = to_streamed_response_wrapper(
            service_tokens.access_service_tokens_create_a_service_token,
        )
        self.access_service_tokens_list_service_tokens = to_streamed_response_wrapper(
            service_tokens.access_service_tokens_list_service_tokens,
        )

    @cached_property
    def refreshes(self) -> RefreshesWithStreamingResponse:
        return RefreshesWithStreamingResponse(self._service_tokens.refreshes)

    @cached_property
    def rotates(self) -> RotatesWithStreamingResponse:
        return RotatesWithStreamingResponse(self._service_tokens.rotates)


class AsyncServiceTokensWithStreamingResponse:
    def __init__(self, service_tokens: AsyncServiceTokens) -> None:
        self._service_tokens = service_tokens

        self.update = async_to_streamed_response_wrapper(
            service_tokens.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            service_tokens.delete,
        )
        self.access_service_tokens_create_a_service_token = async_to_streamed_response_wrapper(
            service_tokens.access_service_tokens_create_a_service_token,
        )
        self.access_service_tokens_list_service_tokens = async_to_streamed_response_wrapper(
            service_tokens.access_service_tokens_list_service_tokens,
        )

    @cached_property
    def refreshes(self) -> AsyncRefreshesWithStreamingResponse:
        return AsyncRefreshesWithStreamingResponse(self._service_tokens.refreshes)

    @cached_property
    def rotates(self) -> AsyncRotatesWithStreamingResponse:
        return AsyncRotatesWithStreamingResponse(self._service_tokens.rotates)
