# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.magic_cloud_networking.catalog_syncs import prebuilt_policy_list_params
from ....types.magic_cloud_networking.catalog_syncs.prebuilt_policy_list_response import PrebuiltPolicyListResponse

__all__ = ["PrebuiltPoliciesResource", "AsyncPrebuiltPoliciesResource"]


class PrebuiltPoliciesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PrebuiltPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return PrebuiltPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PrebuiltPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return PrebuiltPoliciesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        destination_type: Literal["NONE", "ZERO_TRUST_LIST"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[PrebuiltPolicyListResponse]:
        """
        List prebuilt catalog sync policies (Closed Beta)

        Args:
          destination_type: specify type of destination, omit to return all

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/prebuilt-policies",
            page=SyncSinglePage[PrebuiltPolicyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"destination_type": destination_type}, prebuilt_policy_list_params.PrebuiltPolicyListParams
                ),
            ),
            model=PrebuiltPolicyListResponse,
        )


class AsyncPrebuiltPoliciesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPrebuiltPoliciesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPrebuiltPoliciesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPrebuiltPoliciesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncPrebuiltPoliciesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        destination_type: Literal["NONE", "ZERO_TRUST_LIST"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[PrebuiltPolicyListResponse, AsyncSinglePage[PrebuiltPolicyListResponse]]:
        """
        List prebuilt catalog sync policies (Closed Beta)

        Args:
          destination_type: specify type of destination, omit to return all

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/cloud/catalog-syncs/prebuilt-policies",
            page=AsyncSinglePage[PrebuiltPolicyListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"destination_type": destination_type}, prebuilt_policy_list_params.PrebuiltPolicyListParams
                ),
            ),
            model=PrebuiltPolicyListResponse,
        )


class PrebuiltPoliciesResourceWithRawResponse:
    def __init__(self, prebuilt_policies: PrebuiltPoliciesResource) -> None:
        self._prebuilt_policies = prebuilt_policies

        self.list = to_raw_response_wrapper(
            prebuilt_policies.list,
        )


class AsyncPrebuiltPoliciesResourceWithRawResponse:
    def __init__(self, prebuilt_policies: AsyncPrebuiltPoliciesResource) -> None:
        self._prebuilt_policies = prebuilt_policies

        self.list = async_to_raw_response_wrapper(
            prebuilt_policies.list,
        )


class PrebuiltPoliciesResourceWithStreamingResponse:
    def __init__(self, prebuilt_policies: PrebuiltPoliciesResource) -> None:
        self._prebuilt_policies = prebuilt_policies

        self.list = to_streamed_response_wrapper(
            prebuilt_policies.list,
        )


class AsyncPrebuiltPoliciesResourceWithStreamingResponse:
    def __init__(self, prebuilt_policies: AsyncPrebuiltPoliciesResource) -> None:
        self._prebuilt_policies = prebuilt_policies

        self.list = async_to_streamed_response_wrapper(
            prebuilt_policies.list,
        )
