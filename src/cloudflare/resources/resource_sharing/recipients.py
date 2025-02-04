# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ...types.resource_sharing import recipient_list_params, recipient_create_params
from ...types.resource_sharing.recipient_get_response import RecipientGetResponse
from ...types.resource_sharing.recipient_list_response import RecipientListResponse
from ...types.resource_sharing.recipient_create_response import RecipientCreateResponse
from ...types.resource_sharing.recipient_delete_response import RecipientDeleteResponse

__all__ = ["RecipientsResource", "AsyncRecipientsResource"]


class RecipientsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecipientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return RecipientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecipientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return RecipientsResourceWithStreamingResponse(self)

    def create(
        self,
        share_id: str,
        *,
        path_account_id: str,
        body_account_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecipientCreateResponse]:
        """
        Create a new share recipient

        Args:
          path_account_id: Account identifier.

          share_id: Share identifier tag.

          body_account_id: Account identifier.

          organization_id: Organization identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_account_id:
            raise ValueError(f"Expected a non-empty value for `path_account_id` but received {path_account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._post(
            f"/accounts/{path_account_id}/shares/{share_id}/recipients",
            body=maybe_transform(
                {
                    "body_account_id": body_account_id,
                    "organization_id": organization_id,
                },
                recipient_create_params.RecipientCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecipientCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecipientCreateResponse]], ResultWrapper[RecipientCreateResponse]),
        )

    def list(
        self,
        share_id: str,
        *,
        account_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[RecipientListResponse]:
        """
        List share recipients by share ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          page: Page number.

          per_page: Number of objects to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/shares/{share_id}/recipients",
            page=SyncV4PagePaginationArray[RecipientListResponse],
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
                    recipient_list_params.RecipientListParams,
                ),
            ),
            model=RecipientListResponse,
        )

    def delete(
        self,
        recipient_id: str,
        *,
        account_id: str,
        share_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecipientDeleteResponse]:
        """
        Deletion is not immediate, an updated share recipient object with a new status
        will be returned.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          recipient_id: Share Recipient identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        if not recipient_id:
            raise ValueError(f"Expected a non-empty value for `recipient_id` but received {recipient_id!r}")
        return self._delete(
            f"/accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecipientDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecipientDeleteResponse]], ResultWrapper[RecipientDeleteResponse]),
        )

    def get(
        self,
        recipient_id: str,
        *,
        account_id: str,
        share_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecipientGetResponse]:
        """
        Get share recipient by ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          recipient_id: Share Recipient identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        if not recipient_id:
            raise ValueError(f"Expected a non-empty value for `recipient_id` but received {recipient_id!r}")
        return self._get(
            f"/accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecipientGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecipientGetResponse]], ResultWrapper[RecipientGetResponse]),
        )


class AsyncRecipientsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecipientsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecipientsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecipientsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncRecipientsResourceWithStreamingResponse(self)

    async def create(
        self,
        share_id: str,
        *,
        path_account_id: str,
        body_account_id: str | NotGiven = NOT_GIVEN,
        organization_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecipientCreateResponse]:
        """
        Create a new share recipient

        Args:
          path_account_id: Account identifier.

          share_id: Share identifier tag.

          body_account_id: Account identifier.

          organization_id: Organization identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not path_account_id:
            raise ValueError(f"Expected a non-empty value for `path_account_id` but received {path_account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return await self._post(
            f"/accounts/{path_account_id}/shares/{share_id}/recipients",
            body=await async_maybe_transform(
                {
                    "body_account_id": body_account_id,
                    "organization_id": organization_id,
                },
                recipient_create_params.RecipientCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecipientCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecipientCreateResponse]], ResultWrapper[RecipientCreateResponse]),
        )

    def list(
        self,
        share_id: str,
        *,
        account_id: str,
        page: int | NotGiven = NOT_GIVEN,
        per_page: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[RecipientListResponse, AsyncV4PagePaginationArray[RecipientListResponse]]:
        """
        List share recipients by share ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          page: Page number.

          per_page: Number of objects to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/shares/{share_id}/recipients",
            page=AsyncV4PagePaginationArray[RecipientListResponse],
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
                    recipient_list_params.RecipientListParams,
                ),
            ),
            model=RecipientListResponse,
        )

    async def delete(
        self,
        recipient_id: str,
        *,
        account_id: str,
        share_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecipientDeleteResponse]:
        """
        Deletion is not immediate, an updated share recipient object with a new status
        will be returned.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          recipient_id: Share Recipient identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        if not recipient_id:
            raise ValueError(f"Expected a non-empty value for `recipient_id` but received {recipient_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecipientDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecipientDeleteResponse]], ResultWrapper[RecipientDeleteResponse]),
        )

    async def get(
        self,
        recipient_id: str,
        *,
        account_id: str,
        share_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[RecipientGetResponse]:
        """
        Get share recipient by ID.

        Args:
          account_id: Account identifier.

          share_id: Share identifier tag.

          recipient_id: Share Recipient identifier tag.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not share_id:
            raise ValueError(f"Expected a non-empty value for `share_id` but received {share_id!r}")
        if not recipient_id:
            raise ValueError(f"Expected a non-empty value for `recipient_id` but received {recipient_id!r}")
        return await self._get(
            f"/accounts/{account_id}/shares/{share_id}/recipients/{recipient_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[RecipientGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[RecipientGetResponse]], ResultWrapper[RecipientGetResponse]),
        )


class RecipientsResourceWithRawResponse:
    def __init__(self, recipients: RecipientsResource) -> None:
        self._recipients = recipients

        self.create = to_raw_response_wrapper(
            recipients.create,
        )
        self.list = to_raw_response_wrapper(
            recipients.list,
        )
        self.delete = to_raw_response_wrapper(
            recipients.delete,
        )
        self.get = to_raw_response_wrapper(
            recipients.get,
        )


class AsyncRecipientsResourceWithRawResponse:
    def __init__(self, recipients: AsyncRecipientsResource) -> None:
        self._recipients = recipients

        self.create = async_to_raw_response_wrapper(
            recipients.create,
        )
        self.list = async_to_raw_response_wrapper(
            recipients.list,
        )
        self.delete = async_to_raw_response_wrapper(
            recipients.delete,
        )
        self.get = async_to_raw_response_wrapper(
            recipients.get,
        )


class RecipientsResourceWithStreamingResponse:
    def __init__(self, recipients: RecipientsResource) -> None:
        self._recipients = recipients

        self.create = to_streamed_response_wrapper(
            recipients.create,
        )
        self.list = to_streamed_response_wrapper(
            recipients.list,
        )
        self.delete = to_streamed_response_wrapper(
            recipients.delete,
        )
        self.get = to_streamed_response_wrapper(
            recipients.get,
        )


class AsyncRecipientsResourceWithStreamingResponse:
    def __init__(self, recipients: AsyncRecipientsResource) -> None:
        self._recipients = recipients

        self.create = async_to_streamed_response_wrapper(
            recipients.create,
        )
        self.list = async_to_streamed_response_wrapper(
            recipients.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            recipients.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            recipients.get,
        )
