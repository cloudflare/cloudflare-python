# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.alerting.destinations.pagerduty_get_response import PagerdutyGetResponse
from ....types.alerting.destinations.pagerduty_link_response import PagerdutyLinkResponse
from ....types.alerting.destinations.pagerduty_create_response import PagerdutyCreateResponse
from ....types.alerting.destinations.pagerduty_delete_response import PagerdutyDeleteResponse

__all__ = ["PagerdutyResource", "AsyncPagerdutyResource"]


class PagerdutyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PagerdutyResourceWithRawResponse:
        return PagerdutyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PagerdutyResourceWithStreamingResponse:
        return PagerdutyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PagerdutyCreateResponse:
        """
        Creates a new token for integrating with PagerDuty.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/alerting/v3/destinations/pagerduty/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PagerdutyCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PagerdutyCreateResponse], ResultWrapper[PagerdutyCreateResponse]),
        )

    def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PagerdutyDeleteResponse]:
        """
        Deletes all the PagerDuty Services connected to the account.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[PagerdutyDeleteResponse],
            self._delete(
                f"/accounts/{account_id}/alerting/v3/destinations/pagerduty",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[PagerdutyDeleteResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PagerdutyDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PagerdutyGetResponse]:
        """
        Get a list of all configured PagerDuty services.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/alerting/v3/destinations/pagerduty",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PagerdutyGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PagerdutyGetResponse]], ResultWrapper[PagerdutyGetResponse]),
        )

    def link(
        self,
        token_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PagerdutyLinkResponse:
        """
        Links PagerDuty with the account using the integration token.

        Args:
          account_id: The account id

          token_id: The token integration key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not token_id:
            raise ValueError(f"Expected a non-empty value for `token_id` but received {token_id!r}")
        return self._get(
            f"/accounts/{account_id}/alerting/v3/destinations/pagerduty/connect/{token_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PagerdutyLinkResponse]._unwrapper,
            ),
            cast_to=cast(Type[PagerdutyLinkResponse], ResultWrapper[PagerdutyLinkResponse]),
        )


class AsyncPagerdutyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPagerdutyResourceWithRawResponse:
        return AsyncPagerdutyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPagerdutyResourceWithStreamingResponse:
        return AsyncPagerdutyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PagerdutyCreateResponse:
        """
        Creates a new token for integrating with PagerDuty.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/alerting/v3/destinations/pagerduty/connect",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PagerdutyCreateResponse]._unwrapper,
            ),
            cast_to=cast(Type[PagerdutyCreateResponse], ResultWrapper[PagerdutyCreateResponse]),
        )

    async def delete(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PagerdutyDeleteResponse]:
        """
        Deletes all the PagerDuty Services connected to the account.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[PagerdutyDeleteResponse],
            await self._delete(
                f"/accounts/{account_id}/alerting/v3/destinations/pagerduty",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[PagerdutyDeleteResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[PagerdutyDeleteResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[PagerdutyGetResponse]:
        """
        Get a list of all configured PagerDuty services.

        Args:
          account_id: The account id

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/alerting/v3/destinations/pagerduty",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[PagerdutyGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[PagerdutyGetResponse]], ResultWrapper[PagerdutyGetResponse]),
        )

    async def link(
        self,
        token_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PagerdutyLinkResponse:
        """
        Links PagerDuty with the account using the integration token.

        Args:
          account_id: The account id

          token_id: The token integration key

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not token_id:
            raise ValueError(f"Expected a non-empty value for `token_id` but received {token_id!r}")
        return await self._get(
            f"/accounts/{account_id}/alerting/v3/destinations/pagerduty/connect/{token_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[PagerdutyLinkResponse]._unwrapper,
            ),
            cast_to=cast(Type[PagerdutyLinkResponse], ResultWrapper[PagerdutyLinkResponse]),
        )


class PagerdutyResourceWithRawResponse:
    def __init__(self, pagerduty: PagerdutyResource) -> None:
        self._pagerduty = pagerduty

        self.create = to_raw_response_wrapper(
            pagerduty.create,
        )
        self.delete = to_raw_response_wrapper(
            pagerduty.delete,
        )
        self.get = to_raw_response_wrapper(
            pagerduty.get,
        )
        self.link = to_raw_response_wrapper(
            pagerduty.link,
        )


class AsyncPagerdutyResourceWithRawResponse:
    def __init__(self, pagerduty: AsyncPagerdutyResource) -> None:
        self._pagerduty = pagerduty

        self.create = async_to_raw_response_wrapper(
            pagerduty.create,
        )
        self.delete = async_to_raw_response_wrapper(
            pagerduty.delete,
        )
        self.get = async_to_raw_response_wrapper(
            pagerduty.get,
        )
        self.link = async_to_raw_response_wrapper(
            pagerduty.link,
        )


class PagerdutyResourceWithStreamingResponse:
    def __init__(self, pagerduty: PagerdutyResource) -> None:
        self._pagerduty = pagerduty

        self.create = to_streamed_response_wrapper(
            pagerduty.create,
        )
        self.delete = to_streamed_response_wrapper(
            pagerduty.delete,
        )
        self.get = to_streamed_response_wrapper(
            pagerduty.get,
        )
        self.link = to_streamed_response_wrapper(
            pagerduty.link,
        )


class AsyncPagerdutyResourceWithStreamingResponse:
    def __init__(self, pagerduty: AsyncPagerdutyResource) -> None:
        self._pagerduty = pagerduty

        self.create = async_to_streamed_response_wrapper(
            pagerduty.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            pagerduty.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            pagerduty.get,
        )
        self.link = async_to_streamed_response_wrapper(
            pagerduty.link,
        )
