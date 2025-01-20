# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.workers.scripts import subdomain_create_params
from ....types.workers.scripts.subdomain_get_response import SubdomainGetResponse
from ....types.workers.scripts.subdomain_create_response import SubdomainCreateResponse

__all__ = ["SubdomainResource", "AsyncSubdomainResource"]


class SubdomainResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubdomainResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return SubdomainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubdomainResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return SubdomainResourceWithStreamingResponse(self)

    def create(
        self,
        script_name: str,
        *,
        account_id: str,
        enabled: bool,
        previews_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainCreateResponse:
        """
        Enable or disable the Worker on the workers.dev subdomain.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          enabled: Whether the Worker should be available on the workers.dev subdomain.

          previews_enabled: Whether the Worker's Preview URLs should be available on the workers.dev
              subdomain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._post(
            f"/accounts/{account_id}/workers/scripts/{script_name}/subdomain",
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "previews_enabled": previews_enabled,
                },
                subdomain_create_params.SubdomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubdomainCreateResponse,
        )

    def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainGetResponse:
        """
        Get if the Worker is available on the workers.dev subdomain.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/subdomain",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubdomainGetResponse,
        )


class AsyncSubdomainResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubdomainResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubdomainResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubdomainResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncSubdomainResourceWithStreamingResponse(self)

    async def create(
        self,
        script_name: str,
        *,
        account_id: str,
        enabled: bool,
        previews_enabled: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainCreateResponse:
        """
        Enable or disable the Worker on the workers.dev subdomain.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          enabled: Whether the Worker should be available on the workers.dev subdomain.

          previews_enabled: Whether the Worker's Preview URLs should be available on the workers.dev
              subdomain.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._post(
            f"/accounts/{account_id}/workers/scripts/{script_name}/subdomain",
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "previews_enabled": previews_enabled,
                },
                subdomain_create_params.SubdomainCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubdomainCreateResponse,
        )

    async def get(
        self,
        script_name: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SubdomainGetResponse:
        """
        Get if the Worker is available on the workers.dev subdomain.

        Args:
          account_id: Identifier

          script_name: Name of the script, used in URLs and route configuration.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not script_name:
            raise ValueError(f"Expected a non-empty value for `script_name` but received {script_name!r}")
        return await self._get(
            f"/accounts/{account_id}/workers/scripts/{script_name}/subdomain",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubdomainGetResponse,
        )


class SubdomainResourceWithRawResponse:
    def __init__(self, subdomain: SubdomainResource) -> None:
        self._subdomain = subdomain

        self.create = to_raw_response_wrapper(
            subdomain.create,
        )
        self.get = to_raw_response_wrapper(
            subdomain.get,
        )


class AsyncSubdomainResourceWithRawResponse:
    def __init__(self, subdomain: AsyncSubdomainResource) -> None:
        self._subdomain = subdomain

        self.create = async_to_raw_response_wrapper(
            subdomain.create,
        )
        self.get = async_to_raw_response_wrapper(
            subdomain.get,
        )


class SubdomainResourceWithStreamingResponse:
    def __init__(self, subdomain: SubdomainResource) -> None:
        self._subdomain = subdomain

        self.create = to_streamed_response_wrapper(
            subdomain.create,
        )
        self.get = to_streamed_response_wrapper(
            subdomain.get,
        )


class AsyncSubdomainResourceWithStreamingResponse:
    def __init__(self, subdomain: AsyncSubdomainResource) -> None:
        self._subdomain = subdomain

        self.create = async_to_streamed_response_wrapper(
            subdomain.create,
        )
        self.get = async_to_streamed_response_wrapper(
            subdomain.get,
        )
