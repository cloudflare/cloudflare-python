# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, cast

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
from ...._wrappers import ResultWrapper
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import (
    AsyncPaginator,
    make_request_options,
)
from ....types.magic_transit.sites import acl_create_params
from ....types.magic_transit.sites.acl import ACL
from ....types.magic_transit.sites.allowed_protocol import AllowedProtocol
from ....types.magic_transit.sites.acl_configuration_param import ACLConfigurationParam

__all__ = ["ACLsResource", "AsyncACLsResource"]


class ACLsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ACLsResourceWithRawResponse:
        return ACLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ACLsResourceWithStreamingResponse:
        return ACLsResourceWithStreamingResponse(self)

    def create(
        self,
        site_id: str,
        *,
        account_id: str,
        lan_1: ACLConfigurationParam,
        lan_2: ACLConfigurationParam,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        forward_locally: bool | NotGiven = NOT_GIVEN,
        protocols: List[AllowedProtocol] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Creates a new Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          name: The name of the ACL.

          description: Description for the ACL.

          forward_locally: The desired forwarding action for this ACL policy. If set to "false", the policy
              will forward traffic to Cloudflare. If set to "true", the policy will forward
              traffic locally on the Magic Connector. If not included in request, will default
              to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls",
            body=maybe_transform(
                {
                    "lan_1": lan_1,
                    "lan_2": lan_2,
                    "name": name,
                    "description": description,
                    "forward_locally": forward_locally,
                    "protocols": protocols,
                },
                acl_create_params.ACLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ACL]._unwrapper,
            ),
            cast_to=cast(Type[ACL], ResultWrapper[ACL]),
        )

    def list(
        self,
        site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[ACL]:
        """
        Lists Site ACLs associated with an account.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls",
            page=SyncSinglePage[ACL],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ACL,
        )


class AsyncACLsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncACLsResourceWithRawResponse:
        return AsyncACLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncACLsResourceWithStreamingResponse:
        return AsyncACLsResourceWithStreamingResponse(self)

    async def create(
        self,
        site_id: str,
        *,
        account_id: str,
        lan_1: ACLConfigurationParam,
        lan_2: ACLConfigurationParam,
        name: str,
        description: str | NotGiven = NOT_GIVEN,
        forward_locally: bool | NotGiven = NOT_GIVEN,
        protocols: List[AllowedProtocol] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Creates a new Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          name: The name of the ACL.

          description: Description for the ACL.

          forward_locally: The desired forwarding action for this ACL policy. If set to "false", the policy
              will forward traffic to Cloudflare. If set to "true", the policy will forward
              traffic locally on the Magic Connector. If not included in request, will default
              to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls",
            body=await async_maybe_transform(
                {
                    "lan_1": lan_1,
                    "lan_2": lan_2,
                    "name": name,
                    "description": description,
                    "forward_locally": forward_locally,
                    "protocols": protocols,
                },
                acl_create_params.ACLCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ACL]._unwrapper,
            ),
            cast_to=cast(Type[ACL], ResultWrapper[ACL]),
        )

    def list(
        self,
        site_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[ACL, AsyncSinglePage[ACL]]:
        """
        Lists Site ACLs associated with an account.

        Args:
          account_id: Identifier

          site_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls",
            page=AsyncSinglePage[ACL],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=ACL,
        )


class ACLsResourceWithRawResponse:
    def __init__(self, acls: ACLsResource) -> None:
        self._acls = acls

        self.create = to_raw_response_wrapper(
            acls.create,
        )
        self.list = to_raw_response_wrapper(
            acls.list,
        )


class AsyncACLsResourceWithRawResponse:
    def __init__(self, acls: AsyncACLsResource) -> None:
        self._acls = acls

        self.create = async_to_raw_response_wrapper(
            acls.create,
        )
        self.list = async_to_raw_response_wrapper(
            acls.list,
        )


class ACLsResourceWithStreamingResponse:
    def __init__(self, acls: ACLsResource) -> None:
        self._acls = acls

        self.create = to_streamed_response_wrapper(
            acls.create,
        )
        self.list = to_streamed_response_wrapper(
            acls.list,
        )


class AsyncACLsResourceWithStreamingResponse:
    def __init__(self, acls: AsyncACLsResource) -> None:
        self._acls = acls

        self.create = async_to_streamed_response_wrapper(
            acls.create,
        )
        self.list = async_to_streamed_response_wrapper(
            acls.list,
        )
