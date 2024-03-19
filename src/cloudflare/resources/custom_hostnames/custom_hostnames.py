# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, cast
from typing_extensions import Literal

import httpx

from ...types import (
    CustomHostnameGetResponse,
    CustomHostnameEditResponse,
    CustomHostnameListResponse,
    CustomHostnameCreateResponse,
    CustomHostnameDeleteResponse,
    custom_hostname_edit_params,
    custom_hostname_list_params,
    custom_hostname_create_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._wrappers import ResultWrapper
from ...pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from ..._base_client import (
    AsyncPaginator,
    make_request_options,
)
from .fallback_origin import (
    FallbackOrigin,
    AsyncFallbackOrigin,
    FallbackOriginWithRawResponse,
    AsyncFallbackOriginWithRawResponse,
    FallbackOriginWithStreamingResponse,
    AsyncFallbackOriginWithStreamingResponse,
)

__all__ = ["CustomHostnames", "AsyncCustomHostnames"]


class CustomHostnames(SyncAPIResource):
    @cached_property
    def fallback_origin(self) -> FallbackOrigin:
        return FallbackOrigin(self._client)

    @cached_property
    def with_raw_response(self) -> CustomHostnamesWithRawResponse:
        return CustomHostnamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomHostnamesWithStreamingResponse:
        return CustomHostnamesWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        hostname: str,
        ssl: custom_hostname_create_params.SSL,
        custom_metadata: custom_hostname_create_params.CustomMetadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomHostnameCreateResponse:
        """
        Add a new custom hostname and request that an SSL certificate be issued for it.
        One of three validation methods—http, txt, email—should be used, with 'http'
        recommended if the CNAME is already in place (or will be soon). Specifying
        'email' will send an email to the WHOIS contacts on file for the base domain
        plus hostmaster, postmaster, webmaster, admin, administrator. If http is used
        and the domain is not already pointing to the Managed CNAME host, the PATCH
        method must be used once it is (to complete validation).

        Args:
          zone_id: Identifier

          hostname: The custom hostname that will point to your hostname via CNAME.

          ssl: SSL properties used when creating the custom hostname.

          custom_metadata: These are per-hostname (customer) settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/custom_hostnames",
            body=maybe_transform(
                {
                    "hostname": hostname,
                    "ssl": ssl,
                    "custom_metadata": custom_metadata,
                },
                custom_hostname_create_params.CustomHostnameCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomHostnameCreateResponse], ResultWrapper[CustomHostnameCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        hostname: str | NotGiven = NOT_GIVEN,
        order: Literal["ssl", "ssl_status"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        ssl: Literal[0, 1] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[CustomHostnameListResponse]:
        """
        List, search, sort, and filter all of your custom hostnames.

        Args:
          zone_id: Identifier

          id: Hostname ID to match against. This ID was generated and returned during the
              initial custom_hostname creation. This parameter cannot be used with the
              'hostname' parameter.

          direction: Direction to order hostnames.

          hostname: Fully qualified domain name to match against. This parameter cannot be used with
              the 'id' parameter.

          order: Field to order hostnames by.

          page: Page number of paginated results.

          per_page: Number of hostnames per page.

          ssl: Whether to filter hostnames based on if they have SSL enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/custom_hostnames",
            page=SyncV4PagePaginationArray[CustomHostnameListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "direction": direction,
                        "hostname": hostname,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "ssl": ssl,
                    },
                    custom_hostname_list_params.CustomHostnameListParams,
                ),
            ),
            model=CustomHostnameListResponse,
        )

    def delete(
        self,
        custom_hostname_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomHostnameDeleteResponse:
        """
        Delete Custom Hostname (and any issued SSL certificates)

        Args:
          zone_id: Identifier

          custom_hostname_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_hostname_id:
            raise ValueError(f"Expected a non-empty value for `custom_hostname_id` but received {custom_hostname_id!r}")
        return self._delete(
            f"/zones/{zone_id}/custom_hostnames/{custom_hostname_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomHostnameDeleteResponse,
        )

    def edit(
        self,
        custom_hostname_id: str,
        *,
        zone_id: str,
        custom_metadata: custom_hostname_edit_params.CustomMetadata | NotGiven = NOT_GIVEN,
        custom_origin_server: str | NotGiven = NOT_GIVEN,
        custom_origin_sni: str | NotGiven = NOT_GIVEN,
        ssl: custom_hostname_edit_params.SSL | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomHostnameEditResponse:
        """Modify SSL configuration for a custom hostname.

        When sent with SSL config that
        matches existing config, used to indicate that hostname should pass domain
        control validation (DCV). Can also be used to change validation type, e.g., from
        'http' to 'email'.

        Args:
          zone_id: Identifier

          custom_hostname_id: Identifier

          custom_metadata: These are per-hostname (customer) settings.

          custom_origin_server: a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME
              record.

          custom_origin_sni: A hostname that will be sent to your custom origin server as SNI for TLS
              handshake. This can be a valid subdomain of the zone or custom origin server
              name or the string ':request_host_header:' which will cause the host header in
              the request to be used as SNI. Not configurable with default/fallback origin
              server.

          ssl: SSL properties used when creating the custom hostname.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_hostname_id:
            raise ValueError(f"Expected a non-empty value for `custom_hostname_id` but received {custom_hostname_id!r}")
        return self._patch(
            f"/zones/{zone_id}/custom_hostnames/{custom_hostname_id}",
            body=maybe_transform(
                {
                    "custom_metadata": custom_metadata,
                    "custom_origin_server": custom_origin_server,
                    "custom_origin_sni": custom_origin_sni,
                    "ssl": ssl,
                },
                custom_hostname_edit_params.CustomHostnameEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomHostnameEditResponse], ResultWrapper[CustomHostnameEditResponse]),
        )

    def get(
        self,
        custom_hostname_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomHostnameGetResponse:
        """
        Custom Hostname Details

        Args:
          zone_id: Identifier

          custom_hostname_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_hostname_id:
            raise ValueError(f"Expected a non-empty value for `custom_hostname_id` but received {custom_hostname_id!r}")
        return self._get(
            f"/zones/{zone_id}/custom_hostnames/{custom_hostname_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomHostnameGetResponse], ResultWrapper[CustomHostnameGetResponse]),
        )


class AsyncCustomHostnames(AsyncAPIResource):
    @cached_property
    def fallback_origin(self) -> AsyncFallbackOrigin:
        return AsyncFallbackOrigin(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomHostnamesWithRawResponse:
        return AsyncCustomHostnamesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomHostnamesWithStreamingResponse:
        return AsyncCustomHostnamesWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        hostname: str,
        ssl: custom_hostname_create_params.SSL,
        custom_metadata: custom_hostname_create_params.CustomMetadata | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomHostnameCreateResponse:
        """
        Add a new custom hostname and request that an SSL certificate be issued for it.
        One of three validation methods—http, txt, email—should be used, with 'http'
        recommended if the CNAME is already in place (or will be soon). Specifying
        'email' will send an email to the WHOIS contacts on file for the base domain
        plus hostmaster, postmaster, webmaster, admin, administrator. If http is used
        and the domain is not already pointing to the Managed CNAME host, the PATCH
        method must be used once it is (to complete validation).

        Args:
          zone_id: Identifier

          hostname: The custom hostname that will point to your hostname via CNAME.

          ssl: SSL properties used when creating the custom hostname.

          custom_metadata: These are per-hostname (customer) settings.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/custom_hostnames",
            body=await async_maybe_transform(
                {
                    "hostname": hostname,
                    "ssl": ssl,
                    "custom_metadata": custom_metadata,
                },
                custom_hostname_create_params.CustomHostnameCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomHostnameCreateResponse], ResultWrapper[CustomHostnameCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        id: str | NotGiven = NOT_GIVEN,
        direction: Literal["asc", "desc"] | NotGiven = NOT_GIVEN,
        hostname: str | NotGiven = NOT_GIVEN,
        order: Literal["ssl", "ssl_status"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        ssl: Literal[0, 1] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[CustomHostnameListResponse, AsyncV4PagePaginationArray[CustomHostnameListResponse]]:
        """
        List, search, sort, and filter all of your custom hostnames.

        Args:
          zone_id: Identifier

          id: Hostname ID to match against. This ID was generated and returned during the
              initial custom_hostname creation. This parameter cannot be used with the
              'hostname' parameter.

          direction: Direction to order hostnames.

          hostname: Fully qualified domain name to match against. This parameter cannot be used with
              the 'id' parameter.

          order: Field to order hostnames by.

          page: Page number of paginated results.

          per_page: Number of hostnames per page.

          ssl: Whether to filter hostnames based on if they have SSL enabled.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/custom_hostnames",
            page=AsyncV4PagePaginationArray[CustomHostnameListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "id": id,
                        "direction": direction,
                        "hostname": hostname,
                        "order": order,
                        "page": page,
                        "per_page": per_page,
                        "ssl": ssl,
                    },
                    custom_hostname_list_params.CustomHostnameListParams,
                ),
            ),
            model=CustomHostnameListResponse,
        )

    async def delete(
        self,
        custom_hostname_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomHostnameDeleteResponse:
        """
        Delete Custom Hostname (and any issued SSL certificates)

        Args:
          zone_id: Identifier

          custom_hostname_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_hostname_id:
            raise ValueError(f"Expected a non-empty value for `custom_hostname_id` but received {custom_hostname_id!r}")
        return await self._delete(
            f"/zones/{zone_id}/custom_hostnames/{custom_hostname_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomHostnameDeleteResponse,
        )

    async def edit(
        self,
        custom_hostname_id: str,
        *,
        zone_id: str,
        custom_metadata: custom_hostname_edit_params.CustomMetadata | NotGiven = NOT_GIVEN,
        custom_origin_server: str | NotGiven = NOT_GIVEN,
        custom_origin_sni: str | NotGiven = NOT_GIVEN,
        ssl: custom_hostname_edit_params.SSL | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomHostnameEditResponse:
        """Modify SSL configuration for a custom hostname.

        When sent with SSL config that
        matches existing config, used to indicate that hostname should pass domain
        control validation (DCV). Can also be used to change validation type, e.g., from
        'http' to 'email'.

        Args:
          zone_id: Identifier

          custom_hostname_id: Identifier

          custom_metadata: These are per-hostname (customer) settings.

          custom_origin_server: a valid hostname that’s been added to your DNS zone as an A, AAAA, or CNAME
              record.

          custom_origin_sni: A hostname that will be sent to your custom origin server as SNI for TLS
              handshake. This can be a valid subdomain of the zone or custom origin server
              name or the string ':request_host_header:' which will cause the host header in
              the request to be used as SNI. Not configurable with default/fallback origin
              server.

          ssl: SSL properties used when creating the custom hostname.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_hostname_id:
            raise ValueError(f"Expected a non-empty value for `custom_hostname_id` but received {custom_hostname_id!r}")
        return await self._patch(
            f"/zones/{zone_id}/custom_hostnames/{custom_hostname_id}",
            body=await async_maybe_transform(
                {
                    "custom_metadata": custom_metadata,
                    "custom_origin_server": custom_origin_server,
                    "custom_origin_sni": custom_origin_sni,
                    "ssl": ssl,
                },
                custom_hostname_edit_params.CustomHostnameEditParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomHostnameEditResponse], ResultWrapper[CustomHostnameEditResponse]),
        )

    async def get(
        self,
        custom_hostname_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomHostnameGetResponse:
        """
        Custom Hostname Details

        Args:
          zone_id: Identifier

          custom_hostname_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_hostname_id:
            raise ValueError(f"Expected a non-empty value for `custom_hostname_id` but received {custom_hostname_id!r}")
        return await self._get(
            f"/zones/{zone_id}/custom_hostnames/{custom_hostname_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomHostnameGetResponse], ResultWrapper[CustomHostnameGetResponse]),
        )


class CustomHostnamesWithRawResponse:
    def __init__(self, custom_hostnames: CustomHostnames) -> None:
        self._custom_hostnames = custom_hostnames

        self.create = to_raw_response_wrapper(
            custom_hostnames.create,
        )
        self.list = to_raw_response_wrapper(
            custom_hostnames.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_hostnames.delete,
        )
        self.edit = to_raw_response_wrapper(
            custom_hostnames.edit,
        )
        self.get = to_raw_response_wrapper(
            custom_hostnames.get,
        )

    @cached_property
    def fallback_origin(self) -> FallbackOriginWithRawResponse:
        return FallbackOriginWithRawResponse(self._custom_hostnames.fallback_origin)


class AsyncCustomHostnamesWithRawResponse:
    def __init__(self, custom_hostnames: AsyncCustomHostnames) -> None:
        self._custom_hostnames = custom_hostnames

        self.create = async_to_raw_response_wrapper(
            custom_hostnames.create,
        )
        self.list = async_to_raw_response_wrapper(
            custom_hostnames.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_hostnames.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            custom_hostnames.edit,
        )
        self.get = async_to_raw_response_wrapper(
            custom_hostnames.get,
        )

    @cached_property
    def fallback_origin(self) -> AsyncFallbackOriginWithRawResponse:
        return AsyncFallbackOriginWithRawResponse(self._custom_hostnames.fallback_origin)


class CustomHostnamesWithStreamingResponse:
    def __init__(self, custom_hostnames: CustomHostnames) -> None:
        self._custom_hostnames = custom_hostnames

        self.create = to_streamed_response_wrapper(
            custom_hostnames.create,
        )
        self.list = to_streamed_response_wrapper(
            custom_hostnames.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_hostnames.delete,
        )
        self.edit = to_streamed_response_wrapper(
            custom_hostnames.edit,
        )
        self.get = to_streamed_response_wrapper(
            custom_hostnames.get,
        )

    @cached_property
    def fallback_origin(self) -> FallbackOriginWithStreamingResponse:
        return FallbackOriginWithStreamingResponse(self._custom_hostnames.fallback_origin)


class AsyncCustomHostnamesWithStreamingResponse:
    def __init__(self, custom_hostnames: AsyncCustomHostnames) -> None:
        self._custom_hostnames = custom_hostnames

        self.create = async_to_streamed_response_wrapper(
            custom_hostnames.create,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_hostnames.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_hostnames.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            custom_hostnames.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_hostnames.get,
        )

    @cached_property
    def fallback_origin(self) -> AsyncFallbackOriginWithStreamingResponse:
        return AsyncFallbackOriginWithStreamingResponse(self._custom_hostnames.fallback_origin)
