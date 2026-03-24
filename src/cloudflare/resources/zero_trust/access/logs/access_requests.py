# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Union, Optional, cast
from datetime import datetime
from typing_extensions import Literal

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._wrappers import ResultWrapper
from ....._base_client import make_request_options
from .....types.zero_trust.access.logs import access_request_list_params
from .....types.zero_trust.access.logs.access_request_list_response import AccessRequestListResponse

__all__ = ["AccessRequestsResource", "AsyncAccessRequestsResource"]


class AccessRequestsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AccessRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AccessRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccessRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AccessRequestsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        account_id: str,
        allowed_op: Literal["eq", "neq"] | Omit = omit,
        app_type_op: Literal["eq", "neq"] | Omit = omit,
        app_uid_op: Literal["eq", "neq"] | Omit = omit,
        country_code_op: Literal["eq", "neq"] | Omit = omit,
        direction: Literal["desc", "asc"] | Omit = omit,
        email: str | Omit = omit,
        email_exact: bool | Omit = omit,
        email_op: Literal["eq", "neq"] | Omit = omit,
        fields: str | Omit = omit,
        idp_op: Literal["eq", "neq"] | Omit = omit,
        limit: int | Omit = omit,
        non_identity_op: Literal["eq", "neq"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        rayid_op: Literal["eq", "neq"] | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        user_id: str | Omit = omit,
        user_id_op: Literal["eq", "neq"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccessRequestListResponse]:
        """
        Gets a list of Access authentication audit logs for an account.

        Args:
          account_id: Identifier.

          allowed_op: Operator for the `allowed` filter.

          app_type_op: Operator for the `app_type` filter.

          app_uid_op: Operator for the `app_uid` filter.

          country_code_op: Operator for the `country_code` filter.

          direction: The chronological sorting order for the logs.

          email: Filter by user email. Defaults to substring matching. To force exact matching,
              set `email_exact=true`. Example (default): `email=@example.com` returns all
              events with that domain. Example (exact):
              `email=user@example.com&email_exact=true` returns only that user.

          email_exact: When true, `email` is matched exactly instead of substring matching.

          email_op: Operator for the `email` filter.

          fields: Comma-separated list of fields to include in the response. When omitted, all
              fields are returned.

          idp_op: Operator for the `idp` filter.

          limit: The maximum number of log entries to retrieve.

          non_identity_op: Operator for the `non_identity` filter.

          page: Page number of results.

          per_page: Number of results per page.

          rayid_op: Operator for the `ray_id` filter.

          since: The earliest event timestamp to query.

          until: The latest event timestamp to query.

          user_id: Filter by user UUID.

          user_id_op: Operator for the `user_id` filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/access/logs/access_requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "allowed_op": allowed_op,
                        "app_type_op": app_type_op,
                        "app_uid_op": app_uid_op,
                        "country_code_op": country_code_op,
                        "direction": direction,
                        "email": email,
                        "email_exact": email_exact,
                        "email_op": email_op,
                        "fields": fields,
                        "idp_op": idp_op,
                        "limit": limit,
                        "non_identity_op": non_identity_op,
                        "page": page,
                        "per_page": per_page,
                        "rayid_op": rayid_op,
                        "since": since,
                        "until": until,
                        "user_id": user_id,
                        "user_id_op": user_id_op,
                    },
                    access_request_list_params.AccessRequestListParams,
                ),
                post_parser=ResultWrapper[Optional[AccessRequestListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccessRequestListResponse]], ResultWrapper[AccessRequestListResponse]),
        )


class AsyncAccessRequestsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAccessRequestsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccessRequestsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccessRequestsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncAccessRequestsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        account_id: str,
        allowed_op: Literal["eq", "neq"] | Omit = omit,
        app_type_op: Literal["eq", "neq"] | Omit = omit,
        app_uid_op: Literal["eq", "neq"] | Omit = omit,
        country_code_op: Literal["eq", "neq"] | Omit = omit,
        direction: Literal["desc", "asc"] | Omit = omit,
        email: str | Omit = omit,
        email_exact: bool | Omit = omit,
        email_op: Literal["eq", "neq"] | Omit = omit,
        fields: str | Omit = omit,
        idp_op: Literal["eq", "neq"] | Omit = omit,
        limit: int | Omit = omit,
        non_identity_op: Literal["eq", "neq"] | Omit = omit,
        page: int | Omit = omit,
        per_page: int | Omit = omit,
        rayid_op: Literal["eq", "neq"] | Omit = omit,
        since: Union[str, datetime] | Omit = omit,
        until: Union[str, datetime] | Omit = omit,
        user_id: str | Omit = omit,
        user_id_op: Literal["eq", "neq"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Optional[AccessRequestListResponse]:
        """
        Gets a list of Access authentication audit logs for an account.

        Args:
          account_id: Identifier.

          allowed_op: Operator for the `allowed` filter.

          app_type_op: Operator for the `app_type` filter.

          app_uid_op: Operator for the `app_uid` filter.

          country_code_op: Operator for the `country_code` filter.

          direction: The chronological sorting order for the logs.

          email: Filter by user email. Defaults to substring matching. To force exact matching,
              set `email_exact=true`. Example (default): `email=@example.com` returns all
              events with that domain. Example (exact):
              `email=user@example.com&email_exact=true` returns only that user.

          email_exact: When true, `email` is matched exactly instead of substring matching.

          email_op: Operator for the `email` filter.

          fields: Comma-separated list of fields to include in the response. When omitted, all
              fields are returned.

          idp_op: Operator for the `idp` filter.

          limit: The maximum number of log entries to retrieve.

          non_identity_op: Operator for the `non_identity` filter.

          page: Page number of results.

          per_page: Number of results per page.

          rayid_op: Operator for the `ray_id` filter.

          since: The earliest event timestamp to query.

          until: The latest event timestamp to query.

          user_id: Filter by user UUID.

          user_id_op: Operator for the `user_id` filter.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/access/logs/access_requests",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "allowed_op": allowed_op,
                        "app_type_op": app_type_op,
                        "app_uid_op": app_uid_op,
                        "country_code_op": country_code_op,
                        "direction": direction,
                        "email": email,
                        "email_exact": email_exact,
                        "email_op": email_op,
                        "fields": fields,
                        "idp_op": idp_op,
                        "limit": limit,
                        "non_identity_op": non_identity_op,
                        "page": page,
                        "per_page": per_page,
                        "rayid_op": rayid_op,
                        "since": since,
                        "until": until,
                        "user_id": user_id,
                        "user_id_op": user_id_op,
                    },
                    access_request_list_params.AccessRequestListParams,
                ),
                post_parser=ResultWrapper[Optional[AccessRequestListResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AccessRequestListResponse]], ResultWrapper[AccessRequestListResponse]),
        )


class AccessRequestsResourceWithRawResponse:
    def __init__(self, access_requests: AccessRequestsResource) -> None:
        self._access_requests = access_requests

        self.list = to_raw_response_wrapper(
            access_requests.list,
        )


class AsyncAccessRequestsResourceWithRawResponse:
    def __init__(self, access_requests: AsyncAccessRequestsResource) -> None:
        self._access_requests = access_requests

        self.list = async_to_raw_response_wrapper(
            access_requests.list,
        )


class AccessRequestsResourceWithStreamingResponse:
    def __init__(self, access_requests: AccessRequestsResource) -> None:
        self._access_requests = access_requests

        self.list = to_streamed_response_wrapper(
            access_requests.list,
        )


class AsyncAccessRequestsResourceWithStreamingResponse:
    def __init__(self, access_requests: AsyncAccessRequestsResource) -> None:
        self._access_requests = access_requests

        self.list = async_to_streamed_response_wrapper(
            access_requests.list,
        )
