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
from ...._base_client import AsyncPaginator, make_request_options
from ....types.magic_transit.sites import acl_edit_params, acl_create_params, acl_update_params
from ....types.magic_transit.sites.acl import ACL
from ....types.magic_transit.sites.allowed_protocol import AllowedProtocol
from ....types.magic_transit.sites.acl_configuration_param import ACLConfigurationParam

__all__ = ["ACLsResource", "AsyncACLsResource"]


class ACLsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ACLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return ACLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ACLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
        unidirectional: bool | NotGiven = NOT_GIVEN,
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

          unidirectional: The desired traffic direction for this ACL policy. If set to "false", the policy
              will allow bidirectional traffic. If set to "true", the policy will only allow
              traffic in one direction. If not included in request, will default to false.

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
                    "unidirectional": unidirectional,
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

    def update(
        self,
        acl_id: str,
        *,
        account_id: str,
        site_id: str,
        description: str | NotGiven = NOT_GIVEN,
        forward_locally: bool | NotGiven = NOT_GIVEN,
        lan_1: ACLConfigurationParam | NotGiven = NOT_GIVEN,
        lan_2: ACLConfigurationParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        protocols: List[AllowedProtocol] | NotGiven = NOT_GIVEN,
        unidirectional: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Update a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_id: Identifier

          description: Description for the ACL.

          forward_locally: The desired forwarding action for this ACL policy. If set to "false", the policy
              will forward traffic to Cloudflare. If set to "true", the policy will forward
              traffic locally on the Magic Connector. If not included in request, will default
              to false.

          name: The name of the ACL.

          unidirectional: The desired traffic direction for this ACL policy. If set to "false", the policy
              will allow bidirectional traffic. If set to "true", the policy will only allow
              traffic in one direction. If not included in request, will default to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "forward_locally": forward_locally,
                    "lan_1": lan_1,
                    "lan_2": lan_2,
                    "name": name,
                    "protocols": protocols,
                    "unidirectional": unidirectional,
                },
                acl_update_params.ACLUpdateParams,
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

    def delete(
        self,
        acl_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Remove a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ACL]._unwrapper,
            ),
            cast_to=cast(Type[ACL], ResultWrapper[ACL]),
        )

    def edit(
        self,
        acl_id: str,
        *,
        account_id: str,
        site_id: str,
        description: str | NotGiven = NOT_GIVEN,
        forward_locally: bool | NotGiven = NOT_GIVEN,
        lan_1: ACLConfigurationParam | NotGiven = NOT_GIVEN,
        lan_2: ACLConfigurationParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        protocols: List[AllowedProtocol] | NotGiven = NOT_GIVEN,
        unidirectional: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Patch a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_id: Identifier

          description: Description for the ACL.

          forward_locally: The desired forwarding action for this ACL policy. If set to "false", the policy
              will forward traffic to Cloudflare. If set to "true", the policy will forward
              traffic locally on the Magic Connector. If not included in request, will default
              to false.

          name: The name of the ACL.

          unidirectional: The desired traffic direction for this ACL policy. If set to "false", the policy
              will allow bidirectional traffic. If set to "true", the policy will only allow
              traffic in one direction. If not included in request, will default to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return self._patch(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "forward_locally": forward_locally,
                    "lan_1": lan_1,
                    "lan_2": lan_2,
                    "name": name,
                    "protocols": protocols,
                    "unidirectional": unidirectional,
                },
                acl_edit_params.ACLEditParams,
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

    def get(
        self,
        acl_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Get a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ACL]._unwrapper,
            ),
            cast_to=cast(Type[ACL], ResultWrapper[ACL]),
        )


class AsyncACLsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncACLsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncACLsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncACLsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
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
        unidirectional: bool | NotGiven = NOT_GIVEN,
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

          unidirectional: The desired traffic direction for this ACL policy. If set to "false", the policy
              will allow bidirectional traffic. If set to "true", the policy will only allow
              traffic in one direction. If not included in request, will default to false.

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
                    "unidirectional": unidirectional,
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

    async def update(
        self,
        acl_id: str,
        *,
        account_id: str,
        site_id: str,
        description: str | NotGiven = NOT_GIVEN,
        forward_locally: bool | NotGiven = NOT_GIVEN,
        lan_1: ACLConfigurationParam | NotGiven = NOT_GIVEN,
        lan_2: ACLConfigurationParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        protocols: List[AllowedProtocol] | NotGiven = NOT_GIVEN,
        unidirectional: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Update a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_id: Identifier

          description: Description for the ACL.

          forward_locally: The desired forwarding action for this ACL policy. If set to "false", the policy
              will forward traffic to Cloudflare. If set to "true", the policy will forward
              traffic locally on the Magic Connector. If not included in request, will default
              to false.

          name: The name of the ACL.

          unidirectional: The desired traffic direction for this ACL policy. If set to "false", the policy
              will allow bidirectional traffic. If set to "true", the policy will only allow
              traffic in one direction. If not included in request, will default to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "forward_locally": forward_locally,
                    "lan_1": lan_1,
                    "lan_2": lan_2,
                    "name": name,
                    "protocols": protocols,
                    "unidirectional": unidirectional,
                },
                acl_update_params.ACLUpdateParams,
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

    async def delete(
        self,
        acl_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Remove a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ACL]._unwrapper,
            ),
            cast_to=cast(Type[ACL], ResultWrapper[ACL]),
        )

    async def edit(
        self,
        acl_id: str,
        *,
        account_id: str,
        site_id: str,
        description: str | NotGiven = NOT_GIVEN,
        forward_locally: bool | NotGiven = NOT_GIVEN,
        lan_1: ACLConfigurationParam | NotGiven = NOT_GIVEN,
        lan_2: ACLConfigurationParam | NotGiven = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        protocols: List[AllowedProtocol] | NotGiven = NOT_GIVEN,
        unidirectional: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Patch a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_id: Identifier

          description: Description for the ACL.

          forward_locally: The desired forwarding action for this ACL policy. If set to "false", the policy
              will forward traffic to Cloudflare. If set to "true", the policy will forward
              traffic locally on the Magic Connector. If not included in request, will default
              to false.

          name: The name of the ACL.

          unidirectional: The desired traffic direction for this ACL policy. If set to "false", the policy
              will allow bidirectional traffic. If set to "true", the policy will only allow
              traffic in one direction. If not included in request, will default to false.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "forward_locally": forward_locally,
                    "lan_1": lan_1,
                    "lan_2": lan_2,
                    "name": name,
                    "protocols": protocols,
                    "unidirectional": unidirectional,
                },
                acl_edit_params.ACLEditParams,
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

    async def get(
        self,
        acl_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACL:
        """
        Get a specific Site ACL.

        Args:
          account_id: Identifier

          site_id: Identifier

          acl_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not acl_id:
            raise ValueError(f"Expected a non-empty value for `acl_id` but received {acl_id!r}")
        return await self._get(
            f"/accounts/{account_id}/magic/sites/{site_id}/acls/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[ACL]._unwrapper,
            ),
            cast_to=cast(Type[ACL], ResultWrapper[ACL]),
        )


class ACLsResourceWithRawResponse:
    def __init__(self, acls: ACLsResource) -> None:
        self._acls = acls

        self.create = to_raw_response_wrapper(
            acls.create,
        )
        self.update = to_raw_response_wrapper(
            acls.update,
        )
        self.list = to_raw_response_wrapper(
            acls.list,
        )
        self.delete = to_raw_response_wrapper(
            acls.delete,
        )
        self.edit = to_raw_response_wrapper(
            acls.edit,
        )
        self.get = to_raw_response_wrapper(
            acls.get,
        )


class AsyncACLsResourceWithRawResponse:
    def __init__(self, acls: AsyncACLsResource) -> None:
        self._acls = acls

        self.create = async_to_raw_response_wrapper(
            acls.create,
        )
        self.update = async_to_raw_response_wrapper(
            acls.update,
        )
        self.list = async_to_raw_response_wrapper(
            acls.list,
        )
        self.delete = async_to_raw_response_wrapper(
            acls.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            acls.edit,
        )
        self.get = async_to_raw_response_wrapper(
            acls.get,
        )


class ACLsResourceWithStreamingResponse:
    def __init__(self, acls: ACLsResource) -> None:
        self._acls = acls

        self.create = to_streamed_response_wrapper(
            acls.create,
        )
        self.update = to_streamed_response_wrapper(
            acls.update,
        )
        self.list = to_streamed_response_wrapper(
            acls.list,
        )
        self.delete = to_streamed_response_wrapper(
            acls.delete,
        )
        self.edit = to_streamed_response_wrapper(
            acls.edit,
        )
        self.get = to_streamed_response_wrapper(
            acls.get,
        )


class AsyncACLsResourceWithStreamingResponse:
    def __init__(self, acls: AsyncACLsResource) -> None:
        self._acls = acls

        self.create = async_to_streamed_response_wrapper(
            acls.create,
        )
        self.update = async_to_streamed_response_wrapper(
            acls.update,
        )
        self.list = async_to_streamed_response_wrapper(
            acls.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            acls.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            acls.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            acls.get,
        )
