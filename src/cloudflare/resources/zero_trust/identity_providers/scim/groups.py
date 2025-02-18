# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ....._utils import maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .....pagination import SyncSinglePage, AsyncSinglePage
from ....._base_client import AsyncPaginator, make_request_options
from .....types.zero_trust.access.zero_trust_group import ZeroTrustGroup
from .....types.zero_trust.identity_providers.scim import group_list_params

__all__ = ["GroupsResource", "AsyncGroupsResource"]


class GroupsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return GroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return GroupsResourceWithStreamingResponse(self)

    def list(
        self,
        identity_provider_id: str,
        *,
        account_id: str,
        cf_resource_id: str | NotGiven = NOT_GIVEN,
        idp_resource_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[ZeroTrustGroup]:
        """
        Lists SCIM Group resources synced to Cloudflare via the System for Cross-domain
        Identity Management (SCIM).

        Args:
          account_id: Identifier

          identity_provider_id: UUID

          cf_resource_id: The unique Cloudflare-generated Id of the SCIM Group resource; also known as the
              "Id".

          idp_resource_id: The IdP-generated Id of the SCIM Group resource; also known as the "external
              Id".

          name: The display name of the SCIM Group resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        return self._get_api_list(
            f"/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups",
            page=SyncSinglePage[ZeroTrustGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cf_resource_id": cf_resource_id,
                        "idp_resource_id": idp_resource_id,
                        "name": name,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            model=ZeroTrustGroup,
        )


class AsyncGroupsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGroupsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGroupsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGroupsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncGroupsResourceWithStreamingResponse(self)

    def list(
        self,
        identity_provider_id: str,
        *,
        account_id: str,
        cf_resource_id: str | NotGiven = NOT_GIVEN,
        idp_resource_id: str | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ZeroTrustGroup, AsyncSinglePage[ZeroTrustGroup]]:
        """
        Lists SCIM Group resources synced to Cloudflare via the System for Cross-domain
        Identity Management (SCIM).

        Args:
          account_id: Identifier

          identity_provider_id: UUID

          cf_resource_id: The unique Cloudflare-generated Id of the SCIM Group resource; also known as the
              "Id".

          idp_resource_id: The IdP-generated Id of the SCIM Group resource; also known as the "external
              Id".

          name: The display name of the SCIM Group resource.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not identity_provider_id:
            raise ValueError(
                f"Expected a non-empty value for `identity_provider_id` but received {identity_provider_id!r}"
            )
        return self._get_api_list(
            f"/accounts/{account_id}/access/identity_providers/{identity_provider_id}/scim/groups",
            page=AsyncSinglePage[ZeroTrustGroup],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cf_resource_id": cf_resource_id,
                        "idp_resource_id": idp_resource_id,
                        "name": name,
                    },
                    group_list_params.GroupListParams,
                ),
            ),
            model=ZeroTrustGroup,
        )


class GroupsResourceWithRawResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.list = to_raw_response_wrapper(
            groups.list,
        )


class AsyncGroupsResourceWithRawResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.list = async_to_raw_response_wrapper(
            groups.list,
        )


class GroupsResourceWithStreamingResponse:
    def __init__(self, groups: GroupsResource) -> None:
        self._groups = groups

        self.list = to_streamed_response_wrapper(
            groups.list,
        )


class AsyncGroupsResourceWithStreamingResponse:
    def __init__(self, groups: AsyncGroupsResource) -> None:
        self._groups = groups

        self.list = async_to_streamed_response_wrapper(
            groups.list,
        )
