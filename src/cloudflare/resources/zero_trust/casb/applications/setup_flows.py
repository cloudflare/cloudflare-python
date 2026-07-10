# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

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
from ....._base_client import make_request_options
from .....types.zero_trust.casb.applications import setup_flow_list_params
from .....types.zero_trust.casb.applications.setup_flow_list_response import SetupFlowListResponse

__all__ = ["SetupFlowsResource", "AsyncSetupFlowsResource"]


class SetupFlowsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SetupFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SetupFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SetupFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SetupFlowsResourceWithStreamingResponse(self)

    def list(
        self,
        slug: str,
        *,
        account_id: str,
        auth_method: str | Omit = omit,
        environment: Literal["fedramp", "standard"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupFlowListResponse:
        """
        Returns all available setup flows for the application, one per auth method.

        Args:
          auth_method: Filter by auth method slug. Get available slugs from GET /v2/applications.

          environment: Filter by environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return self._get(
            path_template(
                "/accounts/{account_id}/one/applications/{slug}/setup-flows", account_id=account_id, slug=slug
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "auth_method": auth_method,
                        "environment": environment,
                    },
                    setup_flow_list_params.SetupFlowListParams,
                ),
            ),
            cast_to=SetupFlowListResponse,
        )


class AsyncSetupFlowsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSetupFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSetupFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSetupFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSetupFlowsResourceWithStreamingResponse(self)

    async def list(
        self,
        slug: str,
        *,
        account_id: str,
        auth_method: str | Omit = omit,
        environment: Literal["fedramp", "standard"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SetupFlowListResponse:
        """
        Returns all available setup flows for the application, one per auth method.

        Args:
          auth_method: Filter by auth method slug. Get available slugs from GET /v2/applications.

          environment: Filter by environment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not slug:
            raise ValueError(f"Expected a non-empty value for `slug` but received {slug!r}")
        return await self._get(
            path_template(
                "/accounts/{account_id}/one/applications/{slug}/setup-flows", account_id=account_id, slug=slug
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "auth_method": auth_method,
                        "environment": environment,
                    },
                    setup_flow_list_params.SetupFlowListParams,
                ),
            ),
            cast_to=SetupFlowListResponse,
        )


class SetupFlowsResourceWithRawResponse:
    def __init__(self, setup_flows: SetupFlowsResource) -> None:
        self._setup_flows = setup_flows

        self.list = to_raw_response_wrapper(
            setup_flows.list,
        )


class AsyncSetupFlowsResourceWithRawResponse:
    def __init__(self, setup_flows: AsyncSetupFlowsResource) -> None:
        self._setup_flows = setup_flows

        self.list = async_to_raw_response_wrapper(
            setup_flows.list,
        )


class SetupFlowsResourceWithStreamingResponse:
    def __init__(self, setup_flows: SetupFlowsResource) -> None:
        self._setup_flows = setup_flows

        self.list = to_streamed_response_wrapper(
            setup_flows.list,
        )


class AsyncSetupFlowsResourceWithStreamingResponse:
    def __init__(self, setup_flows: AsyncSetupFlowsResource) -> None:
        self._setup_flows = setup_flows

        self.list = async_to_streamed_response_wrapper(
            setup_flows.list,
        )
