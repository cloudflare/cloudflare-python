# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .dns import DNSResource, AsyncDNSResource

from ..._compat import cached_property

from .rules.rules import RulesResource, AsyncRulesResource

from .addresses import AddressesResource, AsyncAddressesResource

from ...types.email_routing.settings import Settings

from ..._wrappers import ResultWrapper

from ..._utils import maybe_transform, async_maybe_transform

from typing import Optional, Type

from ..._base_client import make_request_options

from ..._response import to_raw_response_wrapper, async_to_raw_response_wrapper, to_streamed_response_wrapper, async_to_streamed_response_wrapper

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ..._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ..._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ..._resource import SyncAPIResource, AsyncAPIResource
from ...types import shared_params
from ...types.email_routing import email_routing_disable_params
from ...types.email_routing import email_routing_enable_params
from .dns import DNSResource, AsyncDNSResource, DNSResourceWithRawResponse, AsyncDNSResourceWithRawResponse, DNSResourceWithStreamingResponse, AsyncDNSResourceWithStreamingResponse
from .rules import RulesResource, AsyncRulesResource, RulesResourceWithRawResponse, AsyncRulesResourceWithRawResponse, RulesResourceWithStreamingResponse, AsyncRulesResourceWithStreamingResponse
from .addresses import AddressesResource, AsyncAddressesResource, AddressesResourceWithRawResponse, AsyncAddressesResourceWithRawResponse, AddressesResourceWithStreamingResponse, AsyncAddressesResourceWithStreamingResponse
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["EmailRoutingResource", "AsyncEmailRoutingResource"]

class EmailRoutingResource(SyncAPIResource):
    @cached_property
    def dns(self) -> DNSResource:
        return DNSResource(self._client)

    @cached_property
    def rules(self) -> RulesResource:
        return RulesResource(self._client)

    @cached_property
    def addresses(self) -> AddressesResource:
        return AddressesResource(self._client)

    @cached_property
    def with_raw_response(self) -> EmailRoutingResourceWithRawResponse:
        return EmailRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EmailRoutingResourceWithStreamingResponse:
        return EmailRoutingResourceWithStreamingResponse(self)

    def disable(self,
    zone_identifier: str,
    *,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Settings]:
        """Disable your Email Routing zone.

        Also removes additional MX records previously
        required for Email Routing to work.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return self._post(
            f"/zones/{zone_identifier}/email/routing/disable",
            body=maybe_transform(body, email_routing_disable_params.EmailRoutingDisableParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Settings]]._unwrapper),
            cast_to=cast(Type[Optional[Settings]], ResultWrapper[Settings]),
        )

    def enable(self,
    zone_identifier: str,
    *,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Settings]:
        """Enable you Email Routing zone.

        Add and lock the necessary MX and SPF records.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return self._post(
            f"/zones/{zone_identifier}/email/routing/enable",
            body=maybe_transform(body, email_routing_enable_params.EmailRoutingEnableParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Settings]]._unwrapper),
            cast_to=cast(Type[Optional[Settings]], ResultWrapper[Settings]),
        )

    def get(self,
    zone_identifier: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Settings]:
        """
        Get information about the settings for your Email Routing zone.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return self._get(
            f"/zones/{zone_identifier}/email/routing",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Settings]]._unwrapper),
            cast_to=cast(Type[Optional[Settings]], ResultWrapper[Settings]),
        )

class AsyncEmailRoutingResource(AsyncAPIResource):
    @cached_property
    def dns(self) -> AsyncDNSResource:
        return AsyncDNSResource(self._client)

    @cached_property
    def rules(self) -> AsyncRulesResource:
        return AsyncRulesResource(self._client)

    @cached_property
    def addresses(self) -> AsyncAddressesResource:
        return AsyncAddressesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncEmailRoutingResourceWithRawResponse:
        return AsyncEmailRoutingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEmailRoutingResourceWithStreamingResponse:
        return AsyncEmailRoutingResourceWithStreamingResponse(self)

    async def disable(self,
    zone_identifier: str,
    *,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Settings]:
        """Disable your Email Routing zone.

        Also removes additional MX records previously
        required for Email Routing to work.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return await self._post(
            f"/zones/{zone_identifier}/email/routing/disable",
            body=await async_maybe_transform(body, email_routing_disable_params.EmailRoutingDisableParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Settings]]._unwrapper),
            cast_to=cast(Type[Optional[Settings]], ResultWrapper[Settings]),
        )

    async def enable(self,
    zone_identifier: str,
    *,
    body: object,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Settings]:
        """Enable you Email Routing zone.

        Add and lock the necessary MX and SPF records.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return await self._post(
            f"/zones/{zone_identifier}/email/routing/enable",
            body=await async_maybe_transform(body, email_routing_enable_params.EmailRoutingEnableParams),
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Settings]]._unwrapper),
            cast_to=cast(Type[Optional[Settings]], ResultWrapper[Settings]),
        )

    async def get(self,
    zone_identifier: str,
    *,
    # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
    # The extra values given here take precedence over values defined on the client or passed to this method.
    extra_headers: Headers | None = None,
    extra_query: Query | None = None,
    extra_body: Body | None = None,
    timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,) -> Optional[Settings]:
        """
        Get information about the settings for your Email Routing zone.

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
          raise ValueError(
            f'Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}'
          )
        return await self._get(
            f"/zones/{zone_identifier}/email/routing",
            options=make_request_options(extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout, post_parser=ResultWrapper[Optional[Settings]]._unwrapper),
            cast_to=cast(Type[Optional[Settings]], ResultWrapper[Settings]),
        )

class EmailRoutingResourceWithRawResponse:
    def __init__(self, email_routing: EmailRoutingResource) -> None:
        self._email_routing = email_routing

        self.disable = to_raw_response_wrapper(
            email_routing.disable,
        )
        self.enable = to_raw_response_wrapper(
            email_routing.enable,
        )
        self.get = to_raw_response_wrapper(
            email_routing.get,
        )

    @cached_property
    def dns(self) -> DNSResourceWithRawResponse:
        return DNSResourceWithRawResponse(self._email_routing.dns)

    @cached_property
    def rules(self) -> RulesResourceWithRawResponse:
        return RulesResourceWithRawResponse(self._email_routing.rules)

    @cached_property
    def addresses(self) -> AddressesResourceWithRawResponse:
        return AddressesResourceWithRawResponse(self._email_routing.addresses)

class AsyncEmailRoutingResourceWithRawResponse:
    def __init__(self, email_routing: AsyncEmailRoutingResource) -> None:
        self._email_routing = email_routing

        self.disable = async_to_raw_response_wrapper(
            email_routing.disable,
        )
        self.enable = async_to_raw_response_wrapper(
            email_routing.enable,
        )
        self.get = async_to_raw_response_wrapper(
            email_routing.get,
        )

    @cached_property
    def dns(self) -> AsyncDNSResourceWithRawResponse:
        return AsyncDNSResourceWithRawResponse(self._email_routing.dns)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithRawResponse:
        return AsyncRulesResourceWithRawResponse(self._email_routing.rules)

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithRawResponse:
        return AsyncAddressesResourceWithRawResponse(self._email_routing.addresses)

class EmailRoutingResourceWithStreamingResponse:
    def __init__(self, email_routing: EmailRoutingResource) -> None:
        self._email_routing = email_routing

        self.disable = to_streamed_response_wrapper(
            email_routing.disable,
        )
        self.enable = to_streamed_response_wrapper(
            email_routing.enable,
        )
        self.get = to_streamed_response_wrapper(
            email_routing.get,
        )

    @cached_property
    def dns(self) -> DNSResourceWithStreamingResponse:
        return DNSResourceWithStreamingResponse(self._email_routing.dns)

    @cached_property
    def rules(self) -> RulesResourceWithStreamingResponse:
        return RulesResourceWithStreamingResponse(self._email_routing.rules)

    @cached_property
    def addresses(self) -> AddressesResourceWithStreamingResponse:
        return AddressesResourceWithStreamingResponse(self._email_routing.addresses)

class AsyncEmailRoutingResourceWithStreamingResponse:
    def __init__(self, email_routing: AsyncEmailRoutingResource) -> None:
        self._email_routing = email_routing

        self.disable = async_to_streamed_response_wrapper(
            email_routing.disable,
        )
        self.enable = async_to_streamed_response_wrapper(
            email_routing.enable,
        )
        self.get = async_to_streamed_response_wrapper(
            email_routing.get,
        )

    @cached_property
    def dns(self) -> AsyncDNSResourceWithStreamingResponse:
        return AsyncDNSResourceWithStreamingResponse(self._email_routing.dns)

    @cached_property
    def rules(self) -> AsyncRulesResourceWithStreamingResponse:
        return AsyncRulesResourceWithStreamingResponse(self._email_routing.rules)

    @cached_property
    def addresses(self) -> AsyncAddressesResourceWithStreamingResponse:
        return AsyncAddressesResourceWithStreamingResponse(self._email_routing.addresses)