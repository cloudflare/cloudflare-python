# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from ..pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from .._base_client import AsyncPaginator, make_request_options
from ..types.memberships import membership_list_params, membership_update_params
from ..types.memberships.membership import Membership
from ..types.memberships.membership_get_response import MembershipGetResponse
from ..types.memberships.membership_delete_response import MembershipDeleteResponse
from ..types.memberships.membership_update_response import MembershipUpdateResponse

__all__ = ["MembershipsResource", "AsyncMembershipsResource"]


class MembershipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return MembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return MembershipsResourceWithStreamingResponse(self)

    def update(
        self,
        membership_id: str,
        *,
        status: Literal["accepted", "rejected"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MembershipUpdateResponse]:
        """
        Accept or reject this account invitation.

        Args:
          membership_id: Membership identifier tag.

          status: Whether to accept or reject this account invitation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return self._put(
            f"/memberships/{membership_id}",
            body=maybe_transform({"status": status}, membership_update_params.MembershipUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MembershipUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MembershipUpdateResponse]], ResultWrapper[MembershipUpdateResponse]),
        )

    def list(
        self,
        *,
        account: membership_list_params.Account | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["id", "account.name", "status"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "pending", "rejected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[Membership]:
        """
        List memberships of accounts the user can access.

        Args:
          direction: Direction to order memberships.

          name: Account name

          order: Field to order memberships by.

          page: Page number of paginated results.

          per_page: Number of memberships per page.

          status: Status of this membership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/memberships",
            page=SyncV4PagePaginationArray[Membership],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account": account,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    membership_list_params.MembershipListParams,
                ),
            ),
            model=Membership,
        )

    def delete(
        self,
        membership_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MembershipDeleteResponse]:
        """
        Remove the associated member from an account.

        Args:
          membership_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return self._delete(
            f"/memberships/{membership_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MembershipDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MembershipDeleteResponse]], ResultWrapper[MembershipDeleteResponse]),
        )

    def get(
        self,
        membership_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MembershipGetResponse]:
        """
        Get a specific membership.

        Args:
          membership_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return self._get(
            f"/memberships/{membership_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MembershipGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MembershipGetResponse]], ResultWrapper[MembershipGetResponse]),
        )


class AsyncMembershipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMembershipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMembershipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMembershipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncMembershipsResourceWithStreamingResponse(self)

    async def update(
        self,
        membership_id: str,
        *,
        status: Literal["accepted", "rejected"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MembershipUpdateResponse]:
        """
        Accept or reject this account invitation.

        Args:
          membership_id: Membership identifier tag.

          status: Whether to accept or reject this account invitation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return await self._put(
            f"/memberships/{membership_id}",
            body=await async_maybe_transform({"status": status}, membership_update_params.MembershipUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MembershipUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MembershipUpdateResponse]], ResultWrapper[MembershipUpdateResponse]),
        )

    def list(
        self,
        *,
        account: membership_list_params.Account | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        order: Literal["id", "account.name", "status"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "pending", "rejected"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[Membership, AsyncV4PagePaginationArray[Membership]]:
        """
        List memberships of accounts the user can access.

        Args:
          direction: Direction to order memberships.

          name: Account name

          order: Field to order memberships by.

          page: Page number of paginated results.

          per_page: Number of memberships per page.

          status: Status of this membership.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/memberships",
            page=AsyncV4PagePaginationArray[Membership],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "account": account,
                        "direction": direction,
                        "name": name,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "status": status,
                    },
                    membership_list_params.MembershipListParams,
                ),
            ),
            model=Membership,
        )

    async def delete(
        self,
        membership_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MembershipDeleteResponse]:
        """
        Remove the associated member from an account.

        Args:
          membership_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return await self._delete(
            f"/memberships/{membership_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MembershipDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MembershipDeleteResponse]], ResultWrapper[MembershipDeleteResponse]),
        )

    async def get(
        self,
        membership_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[MembershipGetResponse]:
        """
        Get a specific membership.

        Args:
          membership_id: Membership identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not membership_id:
            raise ValueError(f"Expected a non-empty value for `membership_id` but received {membership_id!r}")
        return await self._get(
            f"/memberships/{membership_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[MembershipGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[MembershipGetResponse]], ResultWrapper[MembershipGetResponse]),
        )


class MembershipsResourceWithRawResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.update = to_raw_response_wrapper(
            memberships.update,
        )
        self.list = to_raw_response_wrapper(
            memberships.list,
        )
        self.delete = to_raw_response_wrapper(
            memberships.delete,
        )
        self.get = to_raw_response_wrapper(
            memberships.get,
        )


class AsyncMembershipsResourceWithRawResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.update = async_to_raw_response_wrapper(
            memberships.update,
        )
        self.list = async_to_raw_response_wrapper(
            memberships.list,
        )
        self.delete = async_to_raw_response_wrapper(
            memberships.delete,
        )
        self.get = async_to_raw_response_wrapper(
            memberships.get,
        )


class MembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: MembershipsResource) -> None:
        self._memberships = memberships

        self.update = to_streamed_response_wrapper(
            memberships.update,
        )
        self.list = to_streamed_response_wrapper(
            memberships.list,
        )
        self.delete = to_streamed_response_wrapper(
            memberships.delete,
        )
        self.get = to_streamed_response_wrapper(
            memberships.get,
        )


class AsyncMembershipsResourceWithStreamingResponse:
    def __init__(self, memberships: AsyncMembershipsResource) -> None:
        self._memberships = memberships

        self.update = async_to_streamed_response_wrapper(
            memberships.update,
        )
        self.list = async_to_streamed_response_wrapper(
            memberships.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            memberships.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            memberships.get,
        )
