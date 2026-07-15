# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.zero_trust.casb import application_list_params
from ....types.zero_trust.casb.application_list_response import ApplicationListResponse

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationListResponse:
        """
        Returns a list of available applications with use cases and permissions.

        Args:
          environment: Filter by supported environment (standard, fedramp).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            path_template("/accounts/{account_id}/one/applications", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"environment": environment}, application_list_params.ApplicationListParams),
            ),
            cast_to=ApplicationListResponse,
        )


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        environment: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ApplicationListResponse:
        """
        Returns a list of available applications with use cases and permissions.

        Args:
          environment: Filter by supported environment (standard, fedramp).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            path_template("/accounts/{account_id}/one/applications", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"environment": environment}, application_list_params.ApplicationListParams
                ),
            ),
            cast_to=ApplicationListResponse,
        )


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.list = to_raw_response_wrapper(
            applications.list,
        )


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.list = async_to_raw_response_wrapper(
            applications.list,
        )


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.list = to_streamed_response_wrapper(
            applications.list,
        )


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.list = async_to_streamed_response_wrapper(
            applications.list,
        )
