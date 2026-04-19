# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Dict, Optional, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ..._base_client import make_request_options
from ...types.resource_tagging import account_tag_get_params, account_tag_update_params
from ...types.resource_tagging.account_tag_get_response import AccountTagGetResponse
from ...types.resource_tagging.account_tag_update_response import AccountTagUpdateResponse

__all__ = ["AccountTagsResource", "AsyncAccountTagsResource"]


class AccountTagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccountTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AccountTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AccountTagsResourceWithStreamingResponse(self)

    @overload
    def update(
        self,
        *,
        account_id: str | None = None,
        resource_id: str,
        resource_type: Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
            "worker_version",
        ],
        worker_id: str,
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountTagUpdateResponse]:
        """
        Creates or updates tags for a specific account-level resource.

        Args:
          account_id: Identifier.

          resource_id: Identifies the unique resource.

          resource_type: Enum for base account-level resource types (those with no extra required
              fields).

          worker_id: Worker ID is required only for worker_version resources

          tags: Contains key-value pairs of tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        *,
        account_id: str | None = None,
        resource_id: str,
        resource_type: Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
        ],
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountTagUpdateResponse]:
        """
        Creates or updates tags for a specific account-level resource.

        Args:
          account_id: Identifier.

          resource_id: Identifies the unique resource.

          resource_type: Enum for base account-level resource types (those with no extra required
              fields).

          tags: Contains key-value pairs of tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["resource_id", "resource_type", "worker_id"], ["resource_id", "resource_type"])
    def update(
        self,
        *,
        account_id: str | None = None,
        resource_id: str,
        resource_type: Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
            "worker_version",
        ]
        | Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
        ],
        worker_id: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountTagUpdateResponse]:
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return cast(
            Optional[AccountTagUpdateResponse],
            self._put(
                path_template("/accounts/{account_id}/tags", account_id=account_id),
                body=maybe_transform(
                    {
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "worker_id": worker_id,
                        "tags": tags,
                    },
                    account_tag_update_params.AccountTagUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[AccountTagUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccountTagUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def delete(
        self,
        *,
        account_id: str | None = None,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes all tags from a specific account-level resource.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return self._delete(
            path_template("/accounts/{account_id}/tags", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        *,
        account_id: str | None = None,
        resource_id: str,
        resource_type: Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
            "worker_version",
        ],
        worker_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountTagGetResponse]:
        """
        Retrieves tags for a specific account-level resource.

        Args:
          account_id: Identifier.

          resource_id: The ID of the resource to retrieve tags for.

          resource_type: The type of the resource.

          worker_id: Worker identifier. Required for worker_version resources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[AccountTagGetResponse],
            self._get(
                path_template("/accounts/{account_id}/tags", account_id=account_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=maybe_transform(
                        {
                            "resource_id": resource_id,
                            "resource_type": resource_type,
                            "worker_id": worker_id,
                        },
                        account_tag_get_params.AccountTagGetParams,
                    ),
                    post_parser=ResultWrapper[Optional[AccountTagGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccountTagGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncAccountTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccountTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAccountTagsResourceWithStreamingResponse(self)

    @overload
    async def update(
        self,
        *,
        account_id: str | None = None,
        resource_id: str,
        resource_type: Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
            "worker_version",
        ],
        worker_id: str,
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountTagUpdateResponse]:
        """
        Creates or updates tags for a specific account-level resource.

        Args:
          account_id: Identifier.

          resource_id: Identifies the unique resource.

          resource_type: Enum for base account-level resource types (those with no extra required
              fields).

          worker_id: Worker ID is required only for worker_version resources

          tags: Contains key-value pairs of tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        *,
        account_id: str | None = None,
        resource_id: str,
        resource_type: Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
        ],
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountTagUpdateResponse]:
        """
        Creates or updates tags for a specific account-level resource.

        Args:
          account_id: Identifier.

          resource_id: Identifies the unique resource.

          resource_type: Enum for base account-level resource types (those with no extra required
              fields).

          tags: Contains key-value pairs of tags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["resource_id", "resource_type", "worker_id"], ["resource_id", "resource_type"])
    async def update(
        self,
        *,
        account_id: str | None = None,
        resource_id: str,
        resource_type: Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
            "worker_version",
        ]
        | Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
        ],
        worker_id: str | Omit = omit,
        tags: Dict[str, str] | Omit = omit,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountTagUpdateResponse]:
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return cast(
            Optional[AccountTagUpdateResponse],
            await self._put(
                path_template("/accounts/{account_id}/tags", account_id=account_id),
                body=await async_maybe_transform(
                    {
                        "resource_id": resource_id,
                        "resource_type": resource_type,
                        "worker_id": worker_id,
                        "tags": tags,
                    },
                    account_tag_update_params.AccountTagUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper[Optional[AccountTagUpdateResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccountTagUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def delete(
        self,
        *,
        account_id: str | None = None,
        if_match: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes all tags from a specific account-level resource.

        Args:
          account_id: Identifier.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        extra_headers = {**strip_not_given({"If-Match": if_match}), **(extra_headers or {})}
        return await self._delete(
            path_template("/accounts/{account_id}/tags", account_id=account_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        *,
        account_id: str | None = None,
        resource_id: str,
        resource_type: Literal[
            "access_application",
            "access_group",
            "account",
            "ai_gateway",
            "alerting_policy",
            "alerting_webhook",
            "cloudflared_tunnel",
            "d1_database",
            "durable_object_namespace",
            "gateway_list",
            "gateway_rule",
            "image",
            "kv_namespace",
            "queue",
            "r2_bucket",
            "resource_share",
            "stream_live_input",
            "stream_video",
            "worker",
            "worker_version",
        ],
        worker_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccountTagGetResponse]:
        """
        Retrieves tags for a specific account-level resource.

        Args:
          account_id: Identifier.

          resource_id: The ID of the resource to retrieve tags for.

          resource_type: The type of the resource.

          worker_id: Worker identifier. Required for worker_version resources.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if account_id is None:
            account_id = self._client._get_account_id_path_param()
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return cast(
            Optional[AccountTagGetResponse],
            await self._get(
                path_template("/accounts/{account_id}/tags", account_id=account_id),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    query=await async_maybe_transform(
                        {
                            "resource_id": resource_id,
                            "resource_type": resource_type,
                            "worker_id": worker_id,
                        },
                        account_tag_get_params.AccountTagGetParams,
                    ),
                    post_parser=ResultWrapper[Optional[AccountTagGetResponse]]._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[AccountTagGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AccountTagsResourceWithRawResponse:
    def __init__(self, account_tags: AccountTagsResource) -> None:
        self._account_tags = account_tags

        self.update = to_raw_response_wrapper(
            account_tags.update,
        )
        self.delete = to_raw_response_wrapper(
            account_tags.delete,
        )
        self.get = to_raw_response_wrapper(
            account_tags.get,
        )


class AsyncAccountTagsResourceWithRawResponse:
    def __init__(self, account_tags: AsyncAccountTagsResource) -> None:
        self._account_tags = account_tags

        self.update = async_to_raw_response_wrapper(
            account_tags.update,
        )
        self.delete = async_to_raw_response_wrapper(
            account_tags.delete,
        )
        self.get = async_to_raw_response_wrapper(
            account_tags.get,
        )


class AccountTagsResourceWithStreamingResponse:
    def __init__(self, account_tags: AccountTagsResource) -> None:
        self._account_tags = account_tags

        self.update = to_streamed_response_wrapper(
            account_tags.update,
        )
        self.delete = to_streamed_response_wrapper(
            account_tags.delete,
        )
        self.get = to_streamed_response_wrapper(
            account_tags.get,
        )


class AsyncAccountTagsResourceWithStreamingResponse:
    def __init__(self, account_tags: AsyncAccountTagsResource) -> None:
        self._account_tags = account_tags

        self.update = async_to_streamed_response_wrapper(
            account_tags.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            account_tags.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            account_tags.get,
        )
