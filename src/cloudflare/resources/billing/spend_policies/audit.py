# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform
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
from ....types.billing.spend_policies import audit_list_params
from ....types.billing.spend_policies.audit_list_response import AuditListResponse

__all__ = ["AuditResource", "AsyncAuditResource"]


class AuditResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AuditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AuditResourceWithStreamingResponse(self)

    def list(
        self,
        policy_id: str,
        *,
        account_id: str,
        limit: int | Omit = omit,
        period: Literal["current_billing_cycle", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[AuditListResponse]:
        """Returns the policy's evaluation history, newest first.

        At most one
        threshold-crossing entry (`limit_reached`) is recorded per policy version and
        billing period, so a policy update can record a new entry without any change in
        balance. Disabled policies still return their history; deleted policies return
        `404`. There is no pagination: use `limit` to set how many entries come back.
        Defaults to `period=current_billing_cycle`, resolved from the product's
        canonical aggregates, not calendar months. Crossings match their recorded
        billing-period bounds, even if recorded late. Set `period=all` for history
        across cycles. Filtering happens before LIMIT. No current cycle returns an empty
        array; unavailable or disabled cycle resolution returns `503` with code `1013`,
        never an empty success.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          policy_id: The unique identifier of the spend policy.

          limit: Maximum number of audit entries to return. Defaults to 50. Values above 100 are
              capped at 100 rather than rejected.

          period: Select current subscription billing-cycle history or history across all cycles.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/billing/spend-policies/{policy_id}/audit",
                account_id=account_id,
                policy_id=policy_id,
            ),
            page=SyncSinglePage[AuditListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "period": period,
                    },
                    audit_list_params.AuditListParams,
                ),
            ),
            model=AuditListResponse,
        )


class AsyncAuditResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAuditResourceWithStreamingResponse(self)

    def list(
        self,
        policy_id: str,
        *,
        account_id: str,
        limit: int | Omit = omit,
        period: Literal["current_billing_cycle", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[AuditListResponse, AsyncSinglePage[AuditListResponse]]:
        """Returns the policy's evaluation history, newest first.

        At most one
        threshold-crossing entry (`limit_reached`) is recorded per policy version and
        billing period, so a policy update can record a new entry without any change in
        balance. Disabled policies still return their history; deleted policies return
        `404`. There is no pagination: use `limit` to set how many entries come back.
        Defaults to `period=current_billing_cycle`, resolved from the product's
        canonical aggregates, not calendar months. Crossings match their recorded
        billing-period bounds, even if recorded late. Set `period=all` for history
        across cycles. Filtering happens before LIMIT. No current cycle returns an empty
        array; unavailable or disabled cycle resolution returns `503` with code `1013`,
        never an empty success.

        Args:
          account_id: Represents a Cloudflare resource identifier tag.

          policy_id: The unique identifier of the spend policy.

          limit: Maximum number of audit entries to return. Defaults to 50. Values above 100 are
              capped at 100 rather than rejected.

          period: Select current subscription billing-cycle history or history across all cycles.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not policy_id:
            raise ValueError(f"Expected a non-empty value for `policy_id` but received {policy_id!r}")
        return self._get_api_list(
            path_template(
                "/accounts/{account_id}/billing/spend-policies/{policy_id}/audit",
                account_id=account_id,
                policy_id=policy_id,
            ),
            page=AsyncSinglePage[AuditListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "period": period,
                    },
                    audit_list_params.AuditListParams,
                ),
            ),
            model=AuditListResponse,
        )


class AuditResourceWithRawResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.list = to_raw_response_wrapper(
            audit.list,
        )


class AsyncAuditResourceWithRawResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.list = async_to_raw_response_wrapper(
            audit.list,
        )


class AuditResourceWithStreamingResponse:
    def __init__(self, audit: AuditResource) -> None:
        self._audit = audit

        self.list = to_streamed_response_wrapper(
            audit.list,
        )


class AsyncAuditResourceWithStreamingResponse:
    def __init__(self, audit: AsyncAuditResource) -> None:
        self._audit = audit

        self.list = async_to_streamed_response_wrapper(
            audit.list,
        )
