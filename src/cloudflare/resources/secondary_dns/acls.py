# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.secondary_dns import (
    ACLUpdateResponse,
    ACLDeleteResponse,
    ACLGetResponse,
    ACLSecondaryDNSACLCreateACLResponse,
    ACLSecondaryDNSACLListACLsResponse,
)

from typing import Type, Optional

from ..._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._base_client import (
    SyncAPIClient,
    AsyncAPIClient,
    _merge_mappings,
    AsyncPaginator,
    make_request_options,
    HttpxBinaryResponseContent,
)
from ...types import shared_params
from ...types.secondary_dns import acl_update_params
from ...types.secondary_dns import acl_secondary_dns_acl_create_acl_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["ACLs", "AsyncACLs"]


class ACLs(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ACLsWithRawResponse:
        return ACLsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ACLsWithStreamingResponse:
        return ACLsWithStreamingResponse(self)

    def update(
        self,
        acl_id: object,
        *,
        account_id: object,
        ip_range: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLUpdateResponse:
        """
        Modify ACL.

        Args:
          ip_range: Allowed IPv4/IPv6 address range of primary or secondary nameservers. This will
              be applied for the entire account. The IP range is used to allow additional
              NOTIFY IPs for secondary zones and IPs Cloudflare allows AXFR/IXFR requests from
              for primary zones. CIDRs are limited to a maximum of /24 for IPv4 and /64 for
              IPv6 respectively.

          name: The name of the acl.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
            body=maybe_transform(
                {
                    "ip_range": ip_range,
                    "name": name,
                },
                acl_update_params.ACLUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLUpdateResponse], ResultWrapper[ACLUpdateResponse]),
        )

    def delete(
        self,
        acl_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLDeleteResponse:
        """
        Delete ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLDeleteResponse], ResultWrapper[ACLDeleteResponse]),
        )

    def get(
        self,
        acl_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLGetResponse:
        """
        Get ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLGetResponse], ResultWrapper[ACLGetResponse]),
        )

    def secondary_dns_acl_create_acl(
        self,
        account_id: object,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLSecondaryDNSACLCreateACLResponse:
        """
        Create ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/accounts/{account_id}/secondary_dns/acls",
            body=maybe_transform(body, acl_secondary_dns_acl_create_acl_params.ACLSecondaryDNSACLCreateACLParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLSecondaryDNSACLCreateACLResponse], ResultWrapper[ACLSecondaryDNSACLCreateACLResponse]),
        )

    def secondary_dns_acl_list_acls(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ACLSecondaryDNSACLListACLsResponse]:
        """
        List ACLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/accounts/{account_id}/secondary_dns/acls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ACLSecondaryDNSACLListACLsResponse]], ResultWrapper[ACLSecondaryDNSACLListACLsResponse]
            ),
        )


class AsyncACLs(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncACLsWithRawResponse:
        return AsyncACLsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncACLsWithStreamingResponse:
        return AsyncACLsWithStreamingResponse(self)

    async def update(
        self,
        acl_id: object,
        *,
        account_id: object,
        ip_range: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLUpdateResponse:
        """
        Modify ACL.

        Args:
          ip_range: Allowed IPv4/IPv6 address range of primary or secondary nameservers. This will
              be applied for the entire account. The IP range is used to allow additional
              NOTIFY IPs for secondary zones and IPs Cloudflare allows AXFR/IXFR requests from
              for primary zones. CIDRs are limited to a maximum of /24 for IPv4 and /64 for
              IPv6 respectively.

          name: The name of the acl.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
            body=maybe_transform(
                {
                    "ip_range": ip_range,
                    "name": name,
                },
                acl_update_params.ACLUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLUpdateResponse], ResultWrapper[ACLUpdateResponse]),
        )

    async def delete(
        self,
        acl_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLDeleteResponse:
        """
        Delete ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLDeleteResponse], ResultWrapper[ACLDeleteResponse]),
        )

    async def get(
        self,
        acl_id: object,
        *,
        account_id: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLGetResponse:
        """
        Get ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/secondary_dns/acls/{acl_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLGetResponse], ResultWrapper[ACLGetResponse]),
        )

    async def secondary_dns_acl_create_acl(
        self,
        account_id: object,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ACLSecondaryDNSACLCreateACLResponse:
        """
        Create ACL.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/accounts/{account_id}/secondary_dns/acls",
            body=maybe_transform(body, acl_secondary_dns_acl_create_acl_params.ACLSecondaryDNSACLCreateACLParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[ACLSecondaryDNSACLCreateACLResponse], ResultWrapper[ACLSecondaryDNSACLCreateACLResponse]),
        )

    async def secondary_dns_acl_list_acls(
        self,
        account_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[ACLSecondaryDNSACLListACLsResponse]:
        """
        List ACLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/accounts/{account_id}/secondary_dns/acls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[ACLSecondaryDNSACLListACLsResponse]], ResultWrapper[ACLSecondaryDNSACLListACLsResponse]
            ),
        )


class ACLsWithRawResponse:
    def __init__(self, acls: ACLs) -> None:
        self._acls = acls

        self.update = to_raw_response_wrapper(
            acls.update,
        )
        self.delete = to_raw_response_wrapper(
            acls.delete,
        )
        self.get = to_raw_response_wrapper(
            acls.get,
        )
        self.secondary_dns_acl_create_acl = to_raw_response_wrapper(
            acls.secondary_dns_acl_create_acl,
        )
        self.secondary_dns_acl_list_acls = to_raw_response_wrapper(
            acls.secondary_dns_acl_list_acls,
        )


class AsyncACLsWithRawResponse:
    def __init__(self, acls: AsyncACLs) -> None:
        self._acls = acls

        self.update = async_to_raw_response_wrapper(
            acls.update,
        )
        self.delete = async_to_raw_response_wrapper(
            acls.delete,
        )
        self.get = async_to_raw_response_wrapper(
            acls.get,
        )
        self.secondary_dns_acl_create_acl = async_to_raw_response_wrapper(
            acls.secondary_dns_acl_create_acl,
        )
        self.secondary_dns_acl_list_acls = async_to_raw_response_wrapper(
            acls.secondary_dns_acl_list_acls,
        )


class ACLsWithStreamingResponse:
    def __init__(self, acls: ACLs) -> None:
        self._acls = acls

        self.update = to_streamed_response_wrapper(
            acls.update,
        )
        self.delete = to_streamed_response_wrapper(
            acls.delete,
        )
        self.get = to_streamed_response_wrapper(
            acls.get,
        )
        self.secondary_dns_acl_create_acl = to_streamed_response_wrapper(
            acls.secondary_dns_acl_create_acl,
        )
        self.secondary_dns_acl_list_acls = to_streamed_response_wrapper(
            acls.secondary_dns_acl_list_acls,
        )


class AsyncACLsWithStreamingResponse:
    def __init__(self, acls: AsyncACLs) -> None:
        self._acls = acls

        self.update = async_to_streamed_response_wrapper(
            acls.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            acls.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            acls.get,
        )
        self.secondary_dns_acl_create_acl = async_to_streamed_response_wrapper(
            acls.secondary_dns_acl_create_acl,
        )
        self.secondary_dns_acl_list_acls = async_to_streamed_response_wrapper(
            acls.secondary_dns_acl_list_acls,
        )
