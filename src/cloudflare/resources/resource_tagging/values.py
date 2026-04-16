# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from ..._base_client import AsyncPaginator, make_request_options
from ...types.resource_tagging import value_list_params
from ...types.resource_tagging.value_list_response import ValueListResponse

__all__ = ["ValuesResource", "AsyncValuesResource"]


class ValuesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ValuesResourceWithStreamingResponse(self)

    def list(
        self,
        tag_key: str,
        *,
        account_id: str | None = None,
        cursor: str | Omit = omit,
        type: Literal[
            "access_application",
            "access_application_policy",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "api_gateway_operation",
            "cloudflared_tunnel",
            "custom_certificate",
            "custom_hostname",
            "d1_database",
            "dns_record",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "managed_client_certificate",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
            "worker_version",
            "zone",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPaginationAfter[ValueListResponse]:
        """
        Lists all distinct values for a given tag key, optionally filtered by resource
        type.

        Args:
          account_id: Identifier.

          cursor: Cursor for pagination.

          type: Filter by resource type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tag_key:
            raise ValueError(f"Expected a non-empty value for `tag_key` but received {tag_key!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/tags/values/{tag_key}", account_id=account_id, tag_key=tag_key),
            page=SyncCursorPaginationAfter[ValueListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "type": type,
                    },
                    value_list_params.ValueListParams,
                ),
            ),
            model=str,
        )


class AsyncValuesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValuesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncValuesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValuesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncValuesResourceWithStreamingResponse(self)

    def list(
        self,
        tag_key: str,
        *,
        account_id: str | None = None,
        cursor: str | Omit = omit,
        type: Literal[
            "access_application",
            "access_application_policy",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "api_gateway_operation",
            "cloudflared_tunnel",
            "custom_certificate",
            "custom_hostname",
            "d1_database",
            "dns_record",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "managed_client_certificate",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
            "worker_version",
            "zone",
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ValueListResponse, AsyncCursorPaginationAfter[ValueListResponse]]:
        """
        Lists all distinct values for a given tag key, optionally filtered by resource
        type.

        Args:
          account_id: Identifier.

          cursor: Cursor for pagination.

          type: Filter by resource type.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not tag_key:
            raise ValueError(f"Expected a non-empty value for `tag_key` but received {tag_key!r}")
        return self._get_api_list(
            path_template("/accounts/{account_id}/tags/values/{tag_key}", account_id=account_id, tag_key=tag_key),
            page=AsyncCursorPaginationAfter[ValueListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "type": type,
                    },
                    value_list_params.ValueListParams,
                ),
            ),
            model=str,
        )


class ValuesResourceWithRawResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.list = to_raw_response_wrapper(
            values.list,
        )


class AsyncValuesResourceWithRawResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.list = async_to_raw_response_wrapper(
            values.list,
        )


class ValuesResourceWithStreamingResponse:
    def __init__(self, values: ValuesResource) -> None:
        self._values = values

        self.list = to_streamed_response_wrapper(
            values.list,
        )


class AsyncValuesResourceWithStreamingResponse:
    def __init__(self, values: AsyncValuesResource) -> None:
        self._values = values

        self.list = async_to_streamed_response_wrapper(
            values.list,
        )
