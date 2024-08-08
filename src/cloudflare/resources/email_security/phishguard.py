# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncSinglePage, AsyncSinglePage
from ..._base_client import AsyncPaginator, make_request_options
from ...types.email_security import phishguard_list_params
from ...types.email_security.phishguard_list_response import PhishguardListResponse

__all__ = ["PhishguardResource", "AsyncPhishguardResource"]


class PhishguardResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PhishguardResourceWithRawResponse:
        return PhishguardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PhishguardResourceWithStreamingResponse:
        return PhishguardResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        from_date: Union[str, date],
        to_date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PhishguardListResponse]:
        """
        Get PhishGuard reports

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/phishguard/reports",
            page=SyncSinglePage[PhishguardListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    phishguard_list_params.PhishguardListParams,
                ),
            ),
            model=PhishguardListResponse,
        )


class AsyncPhishguardResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPhishguardResourceWithRawResponse:
        return AsyncPhishguardResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPhishguardResourceWithStreamingResponse:
        return AsyncPhishguardResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        from_date: Union[str, date],
        to_date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PhishguardListResponse, AsyncSinglePage[PhishguardListResponse]]:
        """
        Get PhishGuard reports

        Args:
          account_id: Account Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/email-security/phishguard/reports",
            page=AsyncSinglePage[PhishguardListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "from_date": from_date,
                        "to_date": to_date,
                    },
                    phishguard_list_params.PhishguardListParams,
                ),
            ),
            model=PhishguardListResponse,
        )


class PhishguardResourceWithRawResponse:
    def __init__(self, phishguard: PhishguardResource) -> None:
        self._phishguard = phishguard

        self.list = to_raw_response_wrapper(
            phishguard.list,
        )


class AsyncPhishguardResourceWithRawResponse:
    def __init__(self, phishguard: AsyncPhishguardResource) -> None:
        self._phishguard = phishguard

        self.list = async_to_raw_response_wrapper(
            phishguard.list,
        )


class PhishguardResourceWithStreamingResponse:
    def __init__(self, phishguard: PhishguardResource) -> None:
        self._phishguard = phishguard

        self.list = to_streamed_response_wrapper(
            phishguard.list,
        )


class AsyncPhishguardResourceWithStreamingResponse:
    def __init__(self, phishguard: AsyncPhishguardResource) -> None:
        self._phishguard = phishguard

        self.list = async_to_streamed_response_wrapper(
            phishguard.list,
        )
