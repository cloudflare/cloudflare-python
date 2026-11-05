# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from .users import (
    UsersResource,
    AsyncUsersResource,
    UsersResourceWithRawResponse,
    AsyncUsersResourceWithRawResponse,
    UsersResourceWithStreamingResponse,
    AsyncUsersResourceWithStreamingResponse,
)
from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from .....pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.access import (
    user_population_list_params,
    user_population_create_params,
    user_population_update_params,
)
from .....types.zero_trust.access.user_population_get_response import UserPopulationGetResponse
from .....types.zero_trust.access.user_population_list_response import UserPopulationListResponse
from .....types.zero_trust.access.user_population_create_response import UserPopulationCreateResponse
from .....types.zero_trust.access.user_population_delete_response import UserPopulationDeleteResponse
from .....types.zero_trust.access.user_population_update_response import UserPopulationUpdateResponse

__all__ = ["UserPopulationsResource", "AsyncUserPopulationsResource"]


class UserPopulationsResource(SyncAPIResource):
    @cached_property
    def users(self) -> UsersResource:
        return UsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> UserPopulationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UserPopulationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserPopulationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UserPopulationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserPopulationCreateResponse]:
        """
        Creates a user population in an account.

        Args:
          account_id: Identifier.

          name: The name of the user population. Leading and trailing whitespace is trimmed
              before validation. After trimming, the name must contain at least one
              non-whitespace character and must not exceed 128 UTF-8 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            path_template("/accounts/{account_id}/access/user_populations", account_id=account_id),
            body=maybe_transform({"name": name}, user_population_create_params.UserPopulationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserPopulationCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserPopulationCreateResponse]], ResultWrapper[UserPopulationCreateResponse]),
        )

    def update(
        self,
        user_population_id: str,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserPopulationUpdateResponse]:
        """
        Updates a user population's name.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          name: The name of the user population. Leading and trailing whitespace is trimmed
              before validation. After trimming, the name must contain at least one
              non-whitespace character and must not exceed 128 UTF-8 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}",
                account_id=account_id,
                user_population_id=user_population_id,
            ),
            body=maybe_transform({"name": name}, user_population_update_params.UserPopulationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserPopulationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserPopulationUpdateResponse]], ResultWrapper[UserPopulationUpdateResponse]),
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
    ) -> SyncV4PagePaginationArray[UserPopulationListResponse]:
        """
        Lists the user populations in an account.

        Args:
          account_id: Identifier.

          page: Page number of results.

          per_page: Number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/access/user_populations", account_id=account_id),
            page=SyncV4PagePaginationArray[UserPopulationListResponse],
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
                    user_population_list_params.UserPopulationListParams,
                ),
            ),
            model=UserPopulationListResponse,
        )

    def delete(
        self,
        user_population_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserPopulationDeleteResponse]:
        """
        Deletes a user population that is not attached to an application.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        return self._delete(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}",
                account_id=account_id,
                user_population_id=user_population_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserPopulationDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserPopulationDeleteResponse]], ResultWrapper[UserPopulationDeleteResponse]),
        )

    def get(
        self,
        user_population_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserPopulationGetResponse]:
        """
        Fetches a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}",
                account_id=account_id,
                user_population_id=user_population_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserPopulationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserPopulationGetResponse]], ResultWrapper[UserPopulationGetResponse]),
        )


class AsyncUserPopulationsResource(AsyncAPIResource):
    @cached_property
    def users(self) -> AsyncUsersResource:
        return AsyncUsersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncUserPopulationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserPopulationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserPopulationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUserPopulationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserPopulationCreateResponse]:
        """
        Creates a user population in an account.

        Args:
          account_id: Identifier.

          name: The name of the user population. Leading and trailing whitespace is trimmed
              before validation. After trimming, the name must contain at least one
              non-whitespace character and must not exceed 128 UTF-8 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            path_template("/accounts/{account_id}/access/user_populations", account_id=account_id),
            body=await async_maybe_transform({"name": name}, user_population_create_params.UserPopulationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserPopulationCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserPopulationCreateResponse]], ResultWrapper[UserPopulationCreateResponse]),
        )

    async def update(
        self,
        user_population_id: str,
        *,
        account_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserPopulationUpdateResponse]:
        """
        Updates a user population's name.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          name: The name of the user population. Leading and trailing whitespace is trimmed
              before validation. After trimming, the name must contain at least one
              non-whitespace character and must not exceed 128 UTF-8 bytes.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}",
                account_id=account_id,
                user_population_id=user_population_id,
            ),
            body=await async_maybe_transform({"name": name}, user_population_update_params.UserPopulationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserPopulationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserPopulationUpdateResponse]], ResultWrapper[UserPopulationUpdateResponse]),
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
    ) -> AsyncPaginator[UserPopulationListResponse, AsyncV4PagePaginationArray[UserPopulationListResponse]]:
        """
        Lists the user populations in an account.

        Args:
          account_id: Identifier.

          page: Page number of results.

          per_page: Number of results per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/access/user_populations", account_id=account_id),
            page=AsyncV4PagePaginationArray[UserPopulationListResponse],
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
                    user_population_list_params.UserPopulationListParams,
                ),
            ),
            model=UserPopulationListResponse,
        )

    async def delete(
        self,
        user_population_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserPopulationDeleteResponse]:
        """
        Deletes a user population that is not attached to an application.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        return await self._delete(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}",
                account_id=account_id,
                user_population_id=user_population_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserPopulationDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserPopulationDeleteResponse]], ResultWrapper[UserPopulationDeleteResponse]),
        )

    async def get(
        self,
        user_population_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserPopulationGetResponse]:
        """
        Fetches a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}",
                account_id=account_id,
                user_population_id=user_population_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserPopulationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserPopulationGetResponse]], ResultWrapper[UserPopulationGetResponse]),
        )


class UserPopulationsResourceWithRawResponse:
    def __init__(self, user_populations: UserPopulationsResource) -> None:
        self._user_populations = user_populations

        self.create = to_raw_response_wrapper(
            user_populations.create,
        )
        self.update = to_raw_response_wrapper(
            user_populations.update,
        )
        self.list = to_raw_response_wrapper(
            user_populations.list,
        )
        self.delete = to_raw_response_wrapper(
            user_populations.delete,
        )
        self.get = to_raw_response_wrapper(
            user_populations.get,
        )

    @cached_property
    def users(self) -> UsersResourceWithRawResponse:
        return UsersResourceWithRawResponse(self._user_populations.users)


class AsyncUserPopulationsResourceWithRawResponse:
    def __init__(self, user_populations: AsyncUserPopulationsResource) -> None:
        self._user_populations = user_populations

        self.create = async_to_raw_response_wrapper(
            user_populations.create,
        )
        self.update = async_to_raw_response_wrapper(
            user_populations.update,
        )
        self.list = async_to_raw_response_wrapper(
            user_populations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            user_populations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            user_populations.get,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithRawResponse:
        return AsyncUsersResourceWithRawResponse(self._user_populations.users)


class UserPopulationsResourceWithStreamingResponse:
    def __init__(self, user_populations: UserPopulationsResource) -> None:
        self._user_populations = user_populations

        self.create = to_streamed_response_wrapper(
            user_populations.create,
        )
        self.update = to_streamed_response_wrapper(
            user_populations.update,
        )
        self.list = to_streamed_response_wrapper(
            user_populations.list,
        )
        self.delete = to_streamed_response_wrapper(
            user_populations.delete,
        )
        self.get = to_streamed_response_wrapper(
            user_populations.get,
        )

    @cached_property
    def users(self) -> UsersResourceWithStreamingResponse:
        return UsersResourceWithStreamingResponse(self._user_populations.users)


class AsyncUserPopulationsResourceWithStreamingResponse:
    def __init__(self, user_populations: AsyncUserPopulationsResource) -> None:
        self._user_populations = user_populations

        self.create = async_to_streamed_response_wrapper(
            user_populations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            user_populations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            user_populations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            user_populations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            user_populations.get,
        )

    @cached_property
    def users(self) -> AsyncUsersResourceWithStreamingResponse:
        return AsyncUsersResourceWithStreamingResponse(self._user_populations.users)
