# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ....pagination import SyncCursorPagination, AsyncCursorPagination
from ...._base_client import AsyncPaginator, make_request_options
from ....types.zero_trust.devices import (
    registration_list_params,
    registration_revoke_params,
    registration_unrevoke_params,
    registration_bulk_delete_params,
)
from ....types.zero_trust.devices.registration_get_response import RegistrationGetResponse
from ....types.zero_trust.devices.registration_list_response import RegistrationListResponse

__all__ = ["RegistrationsResource", "AsyncRegistrationsResource"]


class RegistrationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RegistrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RegistrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RegistrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RegistrationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        id: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        device: registration_list_params.Device | NotGiven = NOT_GIVEN,
        include: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        seen_after: str | NotGiven = NOT_GIVEN,
        seen_before: str | NotGiven = NOT_GIVEN,
        sort_by: Literal["id", "user.name", "user.email", "last_seen_at", "created_at"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "revoked"] | NotGiven = NOT_GIVEN,
        user: registration_list_params.User | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncCursorPagination[RegistrationListResponse]:
        """
        Lists WARP registrations.

        Args:
          id: Filter by registration ID.

          cursor: Opaque token indicating the starting position when requesting the next set of
              records. A cursor value can be obtained from the result_info.cursor field in the
              response.

          per_page: The maximum number of devices to return in a single response.

          search: Filter by registration details.

          seen_after: Filters by the last_seen timestamp - returns only registrations last seen after
              this timestamp.

          seen_before: Filters by the last_seen timestamp - returns only registrations last seen before
              this timestamp.

          sort_by: The registration field to order results by.

          sort_order: Sort direction.

          status: Filter by registration status. Defaults to 'active'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/registrations",
            page=SyncCursorPagination[RegistrationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cursor": cursor,
                        "device": device,
                        "include": include,
                        "per_page": per_page,
                        "search": search,
                        "seen_after": seen_after,
                        "seen_before": seen_before,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "status": status,
                        "user": user,
                    },
                    registration_list_params.RegistrationListParams,
                ),
            ),
            model=RegistrationListResponse,
        )

    def delete(
        self,
        registration_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a WARP registration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not registration_id:
            raise ValueError(f"Expected a non-empty value for `registration_id` but received {registration_id!r}")
        return self._delete(
            f"/accounts/{account_id}/devices/registrations/{registration_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def bulk_delete(
        self,
        *,
        account_id: str,
        id: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a list of WARP registrations.

        Args:
          id: A list of registration IDs to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._delete(
            f"/accounts/{account_id}/devices/registrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, registration_bulk_delete_params.RegistrationBulkDeleteParams),
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def get(
        self,
        registration_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegistrationGetResponse:
        """
        Fetches a single WARP registration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not registration_id:
            raise ValueError(f"Expected a non-empty value for `registration_id` but received {registration_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/registrations/{registration_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegistrationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegistrationGetResponse], ResultWrapper[RegistrationGetResponse]),
        )

    def revoke(
        self,
        *,
        account_id: str,
        id: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Revokes a list of WARP registrations.

        Args:
          id: A list of registration IDs to revoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/devices/registrations/revoke",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, registration_revoke_params.RegistrationRevokeParams),
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    def unrevoke(
        self,
        *,
        account_id: str,
        id: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Unrevokes a list of WARP registrations.

        Args:
          id: A list of registration IDs to unrevoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/devices/registrations/unrevoke",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"id": id}, registration_unrevoke_params.RegistrationUnrevokeParams),
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncRegistrationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRegistrationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRegistrationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRegistrationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRegistrationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        id: List[str] | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        device: registration_list_params.Device | NotGiven = NOT_GIVEN,
        include: str | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        search: str | NotGiven = NOT_GIVEN,
        seen_after: str | NotGiven = NOT_GIVEN,
        seen_before: str | NotGiven = NOT_GIVEN,
        sort_by: Literal["id", "user.name", "user.email", "last_seen_at", "created_at"] | NotGiven = NOT_GIVEN,
        sort_order: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        status: Literal["active", "all", "revoked"] | NotGiven = NOT_GIVEN,
        user: registration_list_params.User | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RegistrationListResponse, AsyncCursorPagination[RegistrationListResponse]]:
        """
        Lists WARP registrations.

        Args:
          id: Filter by registration ID.

          cursor: Opaque token indicating the starting position when requesting the next set of
              records. A cursor value can be obtained from the result_info.cursor field in the
              response.

          per_page: The maximum number of devices to return in a single response.

          search: Filter by registration details.

          seen_after: Filters by the last_seen timestamp - returns only registrations last seen after
              this timestamp.

          seen_before: Filters by the last_seen timestamp - returns only registrations last seen before
              this timestamp.

          sort_by: The registration field to order results by.

          sort_order: Sort direction.

          status: Filter by registration status. Defaults to 'active'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/registrations",
            page=AsyncCursorPagination[RegistrationListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "cursor": cursor,
                        "device": device,
                        "include": include,
                        "per_page": per_page,
                        "search": search,
                        "seen_after": seen_after,
                        "seen_before": seen_before,
                        "sort_by": sort_by,
                        "sort_order": sort_order,
                        "status": status,
                        "user": user,
                    },
                    registration_list_params.RegistrationListParams,
                ),
            ),
            model=RegistrationListResponse,
        )

    async def delete(
        self,
        registration_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a WARP registration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not registration_id:
            raise ValueError(f"Expected a non-empty value for `registration_id` but received {registration_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/devices/registrations/{registration_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def bulk_delete(
        self,
        *,
        account_id: str,
        id: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Deletes a list of WARP registrations.

        Args:
          id: A list of registration IDs to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/devices/registrations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"id": id}, registration_bulk_delete_params.RegistrationBulkDeleteParams
                ),
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def get(
        self,
        registration_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RegistrationGetResponse:
        """
        Fetches a single WARP registration.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not registration_id:
            raise ValueError(f"Expected a non-empty value for `registration_id` but received {registration_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/registrations/{registration_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[RegistrationGetResponse]._unwrapper,
            ),
            cast_to=cast(Type[RegistrationGetResponse], ResultWrapper[RegistrationGetResponse]),
        )

    async def revoke(
        self,
        *,
        account_id: str,
        id: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Revokes a list of WARP registrations.

        Args:
          id: A list of registration IDs to revoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/devices/registrations/revoke",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, registration_revoke_params.RegistrationRevokeParams),
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )

    async def unrevoke(
        self,
        *,
        account_id: str,
        id: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        Unrevokes a list of WARP registrations.

        Args:
          id: A list of registration IDs to unrevoke.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/devices/registrations/unrevoke",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"id": id}, registration_unrevoke_params.RegistrationUnrevokeParams),
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class RegistrationsResourceWithRawResponse:
    def __init__(self, registrations: RegistrationsResource) -> None:
        self._registrations = registrations

        self.list = to_raw_response_wrapper(
            registrations.list,
        )
        self.delete = to_raw_response_wrapper(
            registrations.delete,
        )
        self.bulk_delete = to_raw_response_wrapper(
            registrations.bulk_delete,
        )
        self.get = to_raw_response_wrapper(
            registrations.get,
        )
        self.revoke = to_raw_response_wrapper(
            registrations.revoke,
        )
        self.unrevoke = to_raw_response_wrapper(
            registrations.unrevoke,
        )


class AsyncRegistrationsResourceWithRawResponse:
    def __init__(self, registrations: AsyncRegistrationsResource) -> None:
        self._registrations = registrations

        self.list = async_to_raw_response_wrapper(
            registrations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            registrations.delete,
        )
        self.bulk_delete = async_to_raw_response_wrapper(
            registrations.bulk_delete,
        )
        self.get = async_to_raw_response_wrapper(
            registrations.get,
        )
        self.revoke = async_to_raw_response_wrapper(
            registrations.revoke,
        )
        self.unrevoke = async_to_raw_response_wrapper(
            registrations.unrevoke,
        )


class RegistrationsResourceWithStreamingResponse:
    def __init__(self, registrations: RegistrationsResource) -> None:
        self._registrations = registrations

        self.list = to_streamed_response_wrapper(
            registrations.list,
        )
        self.delete = to_streamed_response_wrapper(
            registrations.delete,
        )
        self.bulk_delete = to_streamed_response_wrapper(
            registrations.bulk_delete,
        )
        self.get = to_streamed_response_wrapper(
            registrations.get,
        )
        self.revoke = to_streamed_response_wrapper(
            registrations.revoke,
        )
        self.unrevoke = to_streamed_response_wrapper(
            registrations.unrevoke,
        )


class AsyncRegistrationsResourceWithStreamingResponse:
    def __init__(self, registrations: AsyncRegistrationsResource) -> None:
        self._registrations = registrations

        self.list = async_to_streamed_response_wrapper(
            registrations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            registrations.delete,
        )
        self.bulk_delete = async_to_streamed_response_wrapper(
            registrations.bulk_delete,
        )
        self.get = async_to_streamed_response_wrapper(
            registrations.get,
        )
        self.revoke = async_to_streamed_response_wrapper(
            registrations.revoke,
        )
        self.unrevoke = async_to_streamed_response_wrapper(
            registrations.unrevoke,
        )
