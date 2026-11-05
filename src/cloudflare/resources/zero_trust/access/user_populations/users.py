# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Iterable, Optional, cast

import httpx

from ....._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ....._base_client import make_request_options
from .....types.zero_trust.access.user_populations import (
    user_get_params,
    user_list_params,
    user_create_params,
    user_update_params,
    user_replace_params,
)
from .....types.zero_trust.access.user_populations.user_get_response import UserGetResponse
from .....types.zero_trust.access.user_populations.user_list_response import UserListResponse
from .....types.zero_trust.access.user_populations.user_create_response import UserCreateResponse
from .....types.zero_trust.access.user_populations.user_update_response import UserUpdateResponse
from .....types.zero_trust.access.user_populations.user_replace_response import UserReplaceResponse

__all__ = ["UsersResource", "AsyncUsersResource"]


class UsersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return UsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return UsersResourceWithStreamingResponse(self)

    def create(
        self,
        user_population_id: str,
        *,
        account_id: str,
        active: bool | Omit = omit,
        display_name: str | Omit = omit,
        emails: Iterable[user_create_params.Email] | Omit = omit,
        external_id: str | Omit = omit,
        meta: user_create_params.Meta | Omit = omit,
        name: user_create_params.Name | Omit = omit,
        schemas: SequenceNotStr[str] | Omit = omit,
        user_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserCreateResponse]:
        """
        Creates a SCIM user in a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          schemas: The SCIM schemas that apply to this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        return self._post(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users",
                account_id=account_id,
                user_population_id=user_population_id,
            ),
            body=maybe_transform(
                {
                    "active": active,
                    "display_name": display_name,
                    "emails": emails,
                    "external_id": external_id,
                    "meta": meta,
                    "name": name,
                    "schemas": schemas,
                    "user_name": user_name,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserCreateResponse]], ResultWrapper[UserCreateResponse]),
        )

    def update(
        self,
        user_id: str,
        *,
        account_id: str,
        user_population_id: str,
        operations: Iterable[user_update_params.Operation],
        schemas: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserUpdateResponse]:
        """
        Updates a SCIM user in a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          user_id: The SCIM user identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._patch(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users/{user_id}",
                account_id=account_id,
                user_population_id=user_population_id,
                user_id=user_id,
            ),
            body=maybe_transform(
                {
                    "operations": operations,
                    "schemas": schemas,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserUpdateResponse]], ResultWrapper[UserUpdateResponse]),
        )

    def list(
        self,
        user_population_id: str,
        *,
        account_id: str,
        attributes: str | Omit = omit,
        count: int | Omit = omit,
        excluded_attributes: str | Omit = omit,
        filter: str | Omit = omit,
        start_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserListResponse]:
        """
        Lists SCIM users in a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          attributes: Comma-separated SCIM attributes to return.

          count: The maximum number of results to return.

          excluded_attributes: Comma-separated SCIM attributes to exclude from the response.

          filter: A SCIM filter expression.

          start_index: The 1-based index of the first result to return.

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
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users",
                account_id=account_id,
                user_population_id=user_population_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "attributes": attributes,
                        "count": count,
                        "excluded_attributes": excluded_attributes,
                        "filter": filter,
                        "start_index": start_index,
                    },
                    user_list_params.UserListParams,
                ),
                post_parser=ResultWrapper[Optional[UserListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserListResponse]], ResultWrapper[UserListResponse]),
        )

    def delete(
        self,
        user_id: str,
        *,
        account_id: str,
        user_population_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a SCIM user from a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          user_id: The SCIM user identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users/{user_id}",
                account_id=account_id,
                user_population_id=user_population_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        user_id: str,
        *,
        account_id: str,
        user_population_id: str,
        attributes: str | Omit = omit,
        excluded_attributes: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserGetResponse]:
        """
        Fetches a SCIM user from a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          user_id: The SCIM user identifier.

          attributes: Comma-separated SCIM attributes to return.

          excluded_attributes: Comma-separated SCIM attributes to exclude from the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users/{user_id}",
                account_id=account_id,
                user_population_id=user_population_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "attributes": attributes,
                        "excluded_attributes": excluded_attributes,
                    },
                    user_get_params.UserGetParams,
                ),
                post_parser=ResultWrapper[Optional[UserGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserGetResponse]], ResultWrapper[UserGetResponse]),
        )

    def replace(
        self,
        user_id: str,
        *,
        account_id: str,
        user_population_id: str,
        active: bool | Omit = omit,
        display_name: str | Omit = omit,
        emails: Iterable[user_replace_params.Email] | Omit = omit,
        external_id: str | Omit = omit,
        meta: user_replace_params.Meta | Omit = omit,
        name: user_replace_params.Name | Omit = omit,
        schemas: SequenceNotStr[str] | Omit = omit,
        user_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserReplaceResponse]:
        """
        Replaces a SCIM user in a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          user_id: The SCIM user identifier.

          schemas: The SCIM schemas that apply to this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return self._put(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users/{user_id}",
                account_id=account_id,
                user_population_id=user_population_id,
                user_id=user_id,
            ),
            body=maybe_transform(
                {
                    "active": active,
                    "display_name": display_name,
                    "emails": emails,
                    "external_id": external_id,
                    "meta": meta,
                    "name": name,
                    "schemas": schemas,
                    "user_name": user_name,
                },
                user_replace_params.UserReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserReplaceResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserReplaceResponse]], ResultWrapper[UserReplaceResponse]),
        )


class AsyncUsersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncUsersResourceWithStreamingResponse(self)

    async def create(
        self,
        user_population_id: str,
        *,
        account_id: str,
        active: bool | Omit = omit,
        display_name: str | Omit = omit,
        emails: Iterable[user_create_params.Email] | Omit = omit,
        external_id: str | Omit = omit,
        meta: user_create_params.Meta | Omit = omit,
        name: user_create_params.Name | Omit = omit,
        schemas: SequenceNotStr[str] | Omit = omit,
        user_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserCreateResponse]:
        """
        Creates a SCIM user in a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          schemas: The SCIM schemas that apply to this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        return await self._post(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users",
                account_id=account_id,
                user_population_id=user_population_id,
            ),
            body=await async_maybe_transform(
                {
                    "active": active,
                    "display_name": display_name,
                    "emails": emails,
                    "external_id": external_id,
                    "meta": meta,
                    "name": name,
                    "schemas": schemas,
                    "user_name": user_name,
                },
                user_create_params.UserCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserCreateResponse]], ResultWrapper[UserCreateResponse]),
        )

    async def update(
        self,
        user_id: str,
        *,
        account_id: str,
        user_population_id: str,
        operations: Iterable[user_update_params.Operation],
        schemas: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserUpdateResponse]:
        """
        Updates a SCIM user in a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          user_id: The SCIM user identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._patch(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users/{user_id}",
                account_id=account_id,
                user_population_id=user_population_id,
                user_id=user_id,
            ),
            body=await async_maybe_transform(
                {
                    "operations": operations,
                    "schemas": schemas,
                },
                user_update_params.UserUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserUpdateResponse]], ResultWrapper[UserUpdateResponse]),
        )

    async def list(
        self,
        user_population_id: str,
        *,
        account_id: str,
        attributes: str | Omit = omit,
        count: int | Omit = omit,
        excluded_attributes: str | Omit = omit,
        filter: str | Omit = omit,
        start_index: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserListResponse]:
        """
        Lists SCIM users in a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          attributes: Comma-separated SCIM attributes to return.

          count: The maximum number of results to return.

          excluded_attributes: Comma-separated SCIM attributes to exclude from the response.

          filter: A SCIM filter expression.

          start_index: The 1-based index of the first result to return.

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
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users",
                account_id=account_id,
                user_population_id=user_population_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "attributes": attributes,
                        "count": count,
                        "excluded_attributes": excluded_attributes,
                        "filter": filter,
                        "start_index": start_index,
                    },
                    user_list_params.UserListParams,
                ),
                post_parser=ResultWrapper[Optional[UserListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserListResponse]], ResultWrapper[UserListResponse]),
        )

    async def delete(
        self,
        user_id: str,
        *,
        account_id: str,
        user_population_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a SCIM user from a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          user_id: The SCIM user identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users/{user_id}",
                account_id=account_id,
                user_population_id=user_population_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        user_id: str,
        *,
        account_id: str,
        user_population_id: str,
        attributes: str | Omit = omit,
        excluded_attributes: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserGetResponse]:
        """
        Fetches a SCIM user from a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          user_id: The SCIM user identifier.

          attributes: Comma-separated SCIM attributes to return.

          excluded_attributes: Comma-separated SCIM attributes to exclude from the response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users/{user_id}",
                account_id=account_id,
                user_population_id=user_population_id,
                user_id=user_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "attributes": attributes,
                        "excluded_attributes": excluded_attributes,
                    },
                    user_get_params.UserGetParams,
                ),
                post_parser=ResultWrapper[Optional[UserGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserGetResponse]], ResultWrapper[UserGetResponse]),
        )

    async def replace(
        self,
        user_id: str,
        *,
        account_id: str,
        user_population_id: str,
        active: bool | Omit = omit,
        display_name: str | Omit = omit,
        emails: Iterable[user_replace_params.Email] | Omit = omit,
        external_id: str | Omit = omit,
        meta: user_replace_params.Meta | Omit = omit,
        name: user_replace_params.Name | Omit = omit,
        schemas: SequenceNotStr[str] | Omit = omit,
        user_name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[UserReplaceResponse]:
        """
        Replaces a SCIM user in a user population.

        Args:
          account_id: Identifier.

          user_population_id: UUID.

          user_id: The SCIM user identifier.

          schemas: The SCIM schemas that apply to this resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not user_population_id:
            raise ValueError(f"Expected a non-empty value for `user_population_id` but received {user_population_id!r}")
        if not user_id:
            raise ValueError(f"Expected a non-empty value for `user_id` but received {user_id!r}")
        return await self._put(
            path_template(
                "/accounts/{account_id}/access/user_populations/{user_population_id}/users/{user_id}",
                account_id=account_id,
                user_population_id=user_population_id,
                user_id=user_id,
            ),
            body=await async_maybe_transform(
                {
                    "active": active,
                    "display_name": display_name,
                    "emails": emails,
                    "external_id": external_id,
                    "meta": meta,
                    "name": name,
                    "schemas": schemas,
                    "user_name": user_name,
                },
                user_replace_params.UserReplaceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[UserReplaceResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[UserReplaceResponse]], ResultWrapper[UserReplaceResponse]),
        )


class UsersResourceWithRawResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_raw_response_wrapper(
            users.create,
        )
        self.update = to_raw_response_wrapper(
            users.update,
        )
        self.list = to_raw_response_wrapper(
            users.list,
        )
        self.delete = to_raw_response_wrapper(
            users.delete,
        )
        self.get = to_raw_response_wrapper(
            users.get,
        )
        self.replace = to_raw_response_wrapper(
            users.replace,
        )


class AsyncUsersResourceWithRawResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_raw_response_wrapper(
            users.create,
        )
        self.update = async_to_raw_response_wrapper(
            users.update,
        )
        self.list = async_to_raw_response_wrapper(
            users.list,
        )
        self.delete = async_to_raw_response_wrapper(
            users.delete,
        )
        self.get = async_to_raw_response_wrapper(
            users.get,
        )
        self.replace = async_to_raw_response_wrapper(
            users.replace,
        )


class UsersResourceWithStreamingResponse:
    def __init__(self, users: UsersResource) -> None:
        self._users = users

        self.create = to_streamed_response_wrapper(
            users.create,
        )
        self.update = to_streamed_response_wrapper(
            users.update,
        )
        self.list = to_streamed_response_wrapper(
            users.list,
        )
        self.delete = to_streamed_response_wrapper(
            users.delete,
        )
        self.get = to_streamed_response_wrapper(
            users.get,
        )
        self.replace = to_streamed_response_wrapper(
            users.replace,
        )


class AsyncUsersResourceWithStreamingResponse:
    def __init__(self, users: AsyncUsersResource) -> None:
        self._users = users

        self.create = async_to_streamed_response_wrapper(
            users.create,
        )
        self.update = async_to_streamed_response_wrapper(
            users.update,
        )
        self.list = async_to_streamed_response_wrapper(
            users.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            users.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            users.get,
        )
        self.replace = async_to_streamed_response_wrapper(
            users.replace,
        )
