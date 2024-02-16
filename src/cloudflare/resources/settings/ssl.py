# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.settings import SSLUpdateResponse, SSLGetResponse

from typing import Type, Optional

from typing_extensions import Literal

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
from ...types.settings import ssl_update_params
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["SSL", "AsyncSSL"]


class SSL(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SSLWithRawResponse:
        return SSLWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SSLWithStreamingResponse:
        return SSLWithStreamingResponse(self)

    def update(
        self,
        zone_id: str,
        *,
        value: Literal["off", "flexible", "full", "strict"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SSLUpdateResponse]:
        """
        SSL encrypts your visitor's connection and safeguards credit card numbers and
        other personal data to and from your website. SSL can take up to 5 minutes to
        fully activate. Requires Cloudflare active on your root domain or www domain.
        Off: no SSL between the visitor and Cloudflare, and no SSL between Cloudflare
        and your web server (all HTTP traffic). Flexible: SSL between the visitor and
        Cloudflare -- visitor sees HTTPS on your site, but no SSL between Cloudflare and
        your web server. You don't need to have an SSL cert on your web server, but your
        vistors will still see the site as being HTTPS enabled. Full: SSL between the
        visitor and Cloudflare -- visitor sees HTTPS on your site, and SSL between
        Cloudflare and your web server. You'll need to have your own SSL cert or
        self-signed cert at the very least. Full (Strict): SSL between the visitor and
        Cloudflare -- visitor sees HTTPS on your site, and SSL between Cloudflare and
        your web server. You'll need to have a valid SSL certificate installed on your
        web server. This certificate must be signed by a certificate authority, have an
        expiration date in the future, and respond for the request domain name
        (hostname). (https://support.cloudflare.com/hc/en-us/articles/200170416).

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Depends on the zone's plan level

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._patch(
            f"/zones/{zone_id}/settings/ssl",
            body=maybe_transform({"value": value}, ssl_update_params.SSLUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLUpdateResponse]], ResultWrapper[SSLUpdateResponse]),
        )

    def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SSLGetResponse]:
        """
        SSL encrypts your visitor's connection and safeguards credit card numbers and
        other personal data to and from your website. SSL can take up to 5 minutes to
        fully activate. Requires Cloudflare active on your root domain or www domain.
        Off: no SSL between the visitor and Cloudflare, and no SSL between Cloudflare
        and your web server (all HTTP traffic). Flexible: SSL between the visitor and
        Cloudflare -- visitor sees HTTPS on your site, but no SSL between Cloudflare and
        your web server. You don't need to have an SSL cert on your web server, but your
        vistors will still see the site as being HTTPS enabled. Full: SSL between the
        visitor and Cloudflare -- visitor sees HTTPS on your site, and SSL between
        Cloudflare and your web server. You'll need to have your own SSL cert or
        self-signed cert at the very least. Full (Strict): SSL between the visitor and
        Cloudflare -- visitor sees HTTPS on your site, and SSL between Cloudflare and
        your web server. You'll need to have a valid SSL certificate installed on your
        web server. This certificate must be signed by a certificate authority, have an
        expiration date in the future, and respond for the request domain name
        (hostname). (https://support.cloudflare.com/hc/en-us/articles/200170416).

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/settings/ssl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLGetResponse]], ResultWrapper[SSLGetResponse]),
        )


class AsyncSSL(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSSLWithRawResponse:
        return AsyncSSLWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSSLWithStreamingResponse:
        return AsyncSSLWithStreamingResponse(self)

    async def update(
        self,
        zone_id: str,
        *,
        value: Literal["off", "flexible", "full", "strict"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SSLUpdateResponse]:
        """
        SSL encrypts your visitor's connection and safeguards credit card numbers and
        other personal data to and from your website. SSL can take up to 5 minutes to
        fully activate. Requires Cloudflare active on your root domain or www domain.
        Off: no SSL between the visitor and Cloudflare, and no SSL between Cloudflare
        and your web server (all HTTP traffic). Flexible: SSL between the visitor and
        Cloudflare -- visitor sees HTTPS on your site, but no SSL between Cloudflare and
        your web server. You don't need to have an SSL cert on your web server, but your
        vistors will still see the site as being HTTPS enabled. Full: SSL between the
        visitor and Cloudflare -- visitor sees HTTPS on your site, and SSL between
        Cloudflare and your web server. You'll need to have your own SSL cert or
        self-signed cert at the very least. Full (Strict): SSL between the visitor and
        Cloudflare -- visitor sees HTTPS on your site, and SSL between Cloudflare and
        your web server. You'll need to have a valid SSL certificate installed on your
        web server. This certificate must be signed by a certificate authority, have an
        expiration date in the future, and respond for the request domain name
        (hostname). (https://support.cloudflare.com/hc/en-us/articles/200170416).

        Args:
          zone_id: Identifier

          value: Value of the zone setting. Notes: Depends on the zone's plan level

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/settings/ssl",
            body=maybe_transform({"value": value}, ssl_update_params.SSLUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLUpdateResponse]], ResultWrapper[SSLUpdateResponse]),
        )

    async def get(
        self,
        zone_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[SSLGetResponse]:
        """
        SSL encrypts your visitor's connection and safeguards credit card numbers and
        other personal data to and from your website. SSL can take up to 5 minutes to
        fully activate. Requires Cloudflare active on your root domain or www domain.
        Off: no SSL between the visitor and Cloudflare, and no SSL between Cloudflare
        and your web server (all HTTP traffic). Flexible: SSL between the visitor and
        Cloudflare -- visitor sees HTTPS on your site, but no SSL between Cloudflare and
        your web server. You don't need to have an SSL cert on your web server, but your
        vistors will still see the site as being HTTPS enabled. Full: SSL between the
        visitor and Cloudflare -- visitor sees HTTPS on your site, and SSL between
        Cloudflare and your web server. You'll need to have your own SSL cert or
        self-signed cert at the very least. Full (Strict): SSL between the visitor and
        Cloudflare -- visitor sees HTTPS on your site, and SSL between Cloudflare and
        your web server. You'll need to have a valid SSL certificate installed on your
        web server. This certificate must be signed by a certificate authority, have an
        expiration date in the future, and respond for the request domain name
        (hostname). (https://support.cloudflare.com/hc/en-us/articles/200170416).

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/settings/ssl",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[SSLGetResponse]], ResultWrapper[SSLGetResponse]),
        )


class SSLWithRawResponse:
    def __init__(self, ssl: SSL) -> None:
        self._ssl = ssl

        self.update = to_raw_response_wrapper(
            ssl.update,
        )
        self.get = to_raw_response_wrapper(
            ssl.get,
        )


class AsyncSSLWithRawResponse:
    def __init__(self, ssl: AsyncSSL) -> None:
        self._ssl = ssl

        self.update = async_to_raw_response_wrapper(
            ssl.update,
        )
        self.get = async_to_raw_response_wrapper(
            ssl.get,
        )


class SSLWithStreamingResponse:
    def __init__(self, ssl: SSL) -> None:
        self._ssl = ssl

        self.update = to_streamed_response_wrapper(
            ssl.update,
        )
        self.get = to_streamed_response_wrapper(
            ssl.get,
        )


class AsyncSSLWithStreamingResponse:
    def __init__(self, ssl: AsyncSSL) -> None:
        self._ssl = ssl

        self.update = async_to_streamed_response_wrapper(
            ssl.update,
        )
        self.get = async_to_streamed_response_wrapper(
            ssl.get,
        )
