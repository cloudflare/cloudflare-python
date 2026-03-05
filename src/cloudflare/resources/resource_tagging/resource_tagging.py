# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, List, cast
from typing_extensions import Literal

import httpx

from .keys import (
    KeysResource,
    AsyncKeysResource,
    KeysResourceWithRawResponse,
    AsyncKeysResourceWithRawResponse,
    KeysResourceWithStreamingResponse,
    AsyncKeysResourceWithStreamingResponse,
)
from .values import (
    ValuesResource,
    AsyncValuesResource,
    ValuesResourceWithRawResponse,
    AsyncValuesResourceWithRawResponse,
    ValuesResourceWithStreamingResponse,
    AsyncValuesResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform
from ..._compat import cached_property
from .zone_tags import (
    ZoneTagsResource,
    AsyncZoneTagsResource,
    ZoneTagsResourceWithRawResponse,
    AsyncZoneTagsResourceWithRawResponse,
    ZoneTagsResourceWithStreamingResponse,
    AsyncZoneTagsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncCursorPaginationAfter, AsyncCursorPaginationAfter
from .account_tags import (
    AccountTagsResource,
    AsyncAccountTagsResource,
    AccountTagsResourceWithRawResponse,
    AsyncAccountTagsResourceWithRawResponse,
    AccountTagsResourceWithStreamingResponse,
    AsyncAccountTagsResourceWithStreamingResponse,
)
from ..._base_client import AsyncPaginator, make_request_options
from ...types.resource_tagging import resource_tagging_list_params
from ...types.resource_tagging.resource_tagging_list_response import ResourceTaggingListResponse

__all__ = ["ResourceTaggingResource", "AsyncResourceTaggingResource"]


class ResourceTaggingResource(SyncAPIResource):
    @cached_property
    def account_tags(self) -> AccountTagsResource:
        return AccountTagsResource(self._client)

    @cached_property
    def zone_tags(self) -> ZoneTagsResource:
        return ZoneTagsResource(self._client)

    @cached_property
    def keys(self) -> KeysResource:
        return KeysResource(self._client)

    @cached_property
    def values(self) -> ValuesResource:
        return ValuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResourceTaggingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ResourceTaggingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResourceTaggingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return ResourceTaggingResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        tag: SequenceNotStr[str] | Omit = omit,
        type: List[
            Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncCursorPaginationAfter[ResourceTaggingListResponse]:
        """
        Lists all tagged resources for an account.

        Args:
          account_id: Identifier.

          cursor: Cursor for pagination.

          tag: Filter resources by tag criteria. This parameter can be repeated multiple times,
              with AND logic between parameters.

              Supported syntax:

              - **Key-only**: `tag=<key>` - Resource must have the tag key (e.g.,
                `tag=production`)
              - **Key-value**: `tag=<key>=<value>` - Resource must have the tag with specific
                value (e.g., `tag=env=prod`)
              - **Multiple values (OR)**: `tag=<key>=<v1>,<v2>` - Resource must have tag with
                any of the values (e.g., `tag=env=prod,staging`)
              - **Negate key-only**: `tag=!<key>` - Resource must not have the tag key (e.g.,
                `tag=!archived`)
              - **Negate key-value**: `tag=<key>!=<value>` - Resource must not have the tag
                with specific value (e.g., `tag=region!=us-west-1`)

              Multiple tag parameters are combined with AND logic.

          type: Filter by resource type. Can be repeated to filter by multiple types (OR logic).
              Example: ?type=zone&type=worker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/tags/resources",
            page=SyncCursorPaginationAfter[ResourceTaggingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "tag": tag,
                        "type": type,
                    },
                    resource_tagging_list_params.ResourceTaggingListParams,
                ),
            ),
            model=cast(
                Any, ResourceTaggingListResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )


class AsyncResourceTaggingResource(AsyncAPIResource):
    @cached_property
    def account_tags(self) -> AsyncAccountTagsResource:
        return AsyncAccountTagsResource(self._client)

    @cached_property
    def zone_tags(self) -> AsyncZoneTagsResource:
        return AsyncZoneTagsResource(self._client)

    @cached_property
    def keys(self) -> AsyncKeysResource:
        return AsyncKeysResource(self._client)

    @cached_property
    def values(self) -> AsyncValuesResource:
        return AsyncValuesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResourceTaggingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncResourceTaggingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResourceTaggingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncResourceTaggingResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        cursor: str | Omit = omit,
        tag: SequenceNotStr[str] | Omit = omit,
        type: List[
            Literal[
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
        ]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ResourceTaggingListResponse, AsyncCursorPaginationAfter[ResourceTaggingListResponse]]:
        """
        Lists all tagged resources for an account.

        Args:
          account_id: Identifier.

          cursor: Cursor for pagination.

          tag: Filter resources by tag criteria. This parameter can be repeated multiple times,
              with AND logic between parameters.

              Supported syntax:

              - **Key-only**: `tag=<key>` - Resource must have the tag key (e.g.,
                `tag=production`)
              - **Key-value**: `tag=<key>=<value>` - Resource must have the tag with specific
                value (e.g., `tag=env=prod`)
              - **Multiple values (OR)**: `tag=<key>=<v1>,<v2>` - Resource must have tag with
                any of the values (e.g., `tag=env=prod,staging`)
              - **Negate key-only**: `tag=!<key>` - Resource must not have the tag key (e.g.,
                `tag=!archived`)
              - **Negate key-value**: `tag=<key>!=<value>` - Resource must not have the tag
                with specific value (e.g., `tag=region!=us-west-1`)

              Multiple tag parameters are combined with AND logic.

          type: Filter by resource type. Can be repeated to filter by multiple types (OR logic).
              Example: ?type=zone&type=worker

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/tags/resources",
            page=AsyncCursorPaginationAfter[ResourceTaggingListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "tag": tag,
                        "type": type,
                    },
                    resource_tagging_list_params.ResourceTaggingListParams,
                ),
            ),
            model=cast(
                Any, ResourceTaggingListResponse
            ),  # Union types cannot be passed in as arguments in the type system
        )


class ResourceTaggingResourceWithRawResponse:
    def __init__(self, resource_tagging: ResourceTaggingResource) -> None:
        self._resource_tagging = resource_tagging

        self.list = to_raw_response_wrapper(
            resource_tagging.list,
        )

    @cached_property
    def account_tags(self) -> AccountTagsResourceWithRawResponse:
        return AccountTagsResourceWithRawResponse(self._resource_tagging.account_tags)

    @cached_property
    def zone_tags(self) -> ZoneTagsResourceWithRawResponse:
        return ZoneTagsResourceWithRawResponse(self._resource_tagging.zone_tags)

    @cached_property
    def keys(self) -> KeysResourceWithRawResponse:
        return KeysResourceWithRawResponse(self._resource_tagging.keys)

    @cached_property
    def values(self) -> ValuesResourceWithRawResponse:
        return ValuesResourceWithRawResponse(self._resource_tagging.values)


class AsyncResourceTaggingResourceWithRawResponse:
    def __init__(self, resource_tagging: AsyncResourceTaggingResource) -> None:
        self._resource_tagging = resource_tagging

        self.list = async_to_raw_response_wrapper(
            resource_tagging.list,
        )

    @cached_property
    def account_tags(self) -> AsyncAccountTagsResourceWithRawResponse:
        return AsyncAccountTagsResourceWithRawResponse(self._resource_tagging.account_tags)

    @cached_property
    def zone_tags(self) -> AsyncZoneTagsResourceWithRawResponse:
        return AsyncZoneTagsResourceWithRawResponse(self._resource_tagging.zone_tags)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithRawResponse:
        return AsyncKeysResourceWithRawResponse(self._resource_tagging.keys)

    @cached_property
    def values(self) -> AsyncValuesResourceWithRawResponse:
        return AsyncValuesResourceWithRawResponse(self._resource_tagging.values)


class ResourceTaggingResourceWithStreamingResponse:
    def __init__(self, resource_tagging: ResourceTaggingResource) -> None:
        self._resource_tagging = resource_tagging

        self.list = to_streamed_response_wrapper(
            resource_tagging.list,
        )

    @cached_property
    def account_tags(self) -> AccountTagsResourceWithStreamingResponse:
        return AccountTagsResourceWithStreamingResponse(self._resource_tagging.account_tags)

    @cached_property
    def zone_tags(self) -> ZoneTagsResourceWithStreamingResponse:
        return ZoneTagsResourceWithStreamingResponse(self._resource_tagging.zone_tags)

    @cached_property
    def keys(self) -> KeysResourceWithStreamingResponse:
        return KeysResourceWithStreamingResponse(self._resource_tagging.keys)

    @cached_property
    def values(self) -> ValuesResourceWithStreamingResponse:
        return ValuesResourceWithStreamingResponse(self._resource_tagging.values)


class AsyncResourceTaggingResourceWithStreamingResponse:
    def __init__(self, resource_tagging: AsyncResourceTaggingResource) -> None:
        self._resource_tagging = resource_tagging

        self.list = async_to_streamed_response_wrapper(
            resource_tagging.list,
        )

    @cached_property
    def account_tags(self) -> AsyncAccountTagsResourceWithStreamingResponse:
        return AsyncAccountTagsResourceWithStreamingResponse(self._resource_tagging.account_tags)

    @cached_property
    def zone_tags(self) -> AsyncZoneTagsResourceWithStreamingResponse:
        return AsyncZoneTagsResourceWithStreamingResponse(self._resource_tagging.zone_tags)

    @cached_property
    def keys(self) -> AsyncKeysResourceWithStreamingResponse:
        return AsyncKeysResourceWithStreamingResponse(self._resource_tagging.keys)

    @cached_property
    def values(self) -> AsyncValuesResourceWithStreamingResponse:
        return AsyncValuesResourceWithStreamingResponse(self._resource_tagging.values)
