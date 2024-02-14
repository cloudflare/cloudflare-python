# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._wrappers import ResultWrapper
from ...._base_client import (
    make_request_options,
)
from ....types.firewalls.waf import (
    OverrideGetResponse,
    OverrideDeleteResponse,
    OverrideUpdateResponse,
    OverrideWAFOverridesListWAFOverridesResponse,
    OverrideWAFOverridesCreateAWAFOverrideResponse,
    override_update_params,
    override_waf_overrides_list_waf_overrides_params,
    override_waf_overrides_create_a_waf_override_params,
)

__all__ = ["Overrides", "AsyncOverrides"]


class Overrides(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OverridesWithRawResponse:
        return OverridesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OverridesWithStreamingResponse:
        return OverridesWithStreamingResponse(self)

    def update(
        self,
        id: str,
        *,
        zone_identifier: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideUpdateResponse]:
        """
        Updates an existing URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the WAF override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/zones/{zone_identifier}/firewall/waf/overrides/{id}",
            body=maybe_transform(body, override_update_params.OverrideUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OverrideUpdateResponse]], ResultWrapper[OverrideUpdateResponse]),
        )

    def delete(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideDeleteResponse]:
        """
        Deletes an existing URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the WAF override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/zones/{zone_identifier}/firewall/waf/overrides/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OverrideDeleteResponse]], ResultWrapper[OverrideDeleteResponse]),
        )

    def get(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideGetResponse]:
        """
        Fetches the details of a URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the WAF override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/zones/{zone_identifier}/firewall/waf/overrides/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OverrideGetResponse]], ResultWrapper[OverrideGetResponse]),
        )

    def waf_overrides_create_a_waf_override(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideWAFOverridesCreateAWAFOverrideResponse]:
        """
        Creates a URI-based WAF override for a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._post(
            f"/zones/{zone_identifier}/firewall/waf/overrides",
            body=maybe_transform(
                body, override_waf_overrides_create_a_waf_override_params.OverrideWAFOverridesCreateAWAFOverrideParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OverrideWAFOverridesCreateAWAFOverrideResponse]],
                ResultWrapper[OverrideWAFOverridesCreateAWAFOverrideResponse],
            ),
        )

    def waf_overrides_list_waf_overrides(
        self,
        zone_identifier: str,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideWAFOverridesListWAFOverridesResponse]:
        """
        Fetches the URI-based WAF overrides in a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          page: The page number of paginated results.

          per_page: The number of WAF overrides per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return self._get(
            f"/zones/{zone_identifier}/firewall/waf/overrides",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    override_waf_overrides_list_waf_overrides_params.OverrideWAFOverridesListWAFOverridesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OverrideWAFOverridesListWAFOverridesResponse]],
                ResultWrapper[OverrideWAFOverridesListWAFOverridesResponse],
            ),
        )


class AsyncOverrides(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOverridesWithRawResponse:
        return AsyncOverridesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOverridesWithStreamingResponse:
        return AsyncOverridesWithStreamingResponse(self)

    async def update(
        self,
        id: str,
        *,
        zone_identifier: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideUpdateResponse]:
        """
        Updates an existing URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the WAF override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/zones/{zone_identifier}/firewall/waf/overrides/{id}",
            body=maybe_transform(body, override_update_params.OverrideUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OverrideUpdateResponse]], ResultWrapper[OverrideUpdateResponse]),
        )

    async def delete(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideDeleteResponse]:
        """
        Deletes an existing URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the WAF override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/zones/{zone_identifier}/firewall/waf/overrides/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OverrideDeleteResponse]], ResultWrapper[OverrideDeleteResponse]),
        )

    async def get(
        self,
        id: str,
        *,
        zone_identifier: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideGetResponse]:
        """
        Fetches the details of a URI-based WAF override.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          id: The unique identifier of the WAF override.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/zones/{zone_identifier}/firewall/waf/overrides/{id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[OverrideGetResponse]], ResultWrapper[OverrideGetResponse]),
        )

    async def waf_overrides_create_a_waf_override(
        self,
        zone_identifier: str,
        *,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideWAFOverridesCreateAWAFOverrideResponse]:
        """
        Creates a URI-based WAF override for a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._post(
            f"/zones/{zone_identifier}/firewall/waf/overrides",
            body=maybe_transform(
                body, override_waf_overrides_create_a_waf_override_params.OverrideWAFOverridesCreateAWAFOverrideParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OverrideWAFOverridesCreateAWAFOverrideResponse]],
                ResultWrapper[OverrideWAFOverridesCreateAWAFOverrideResponse],
            ),
        )

    async def waf_overrides_list_waf_overrides(
        self,
        zone_identifier: str,
        *,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OverrideWAFOverridesListWAFOverridesResponse]:
        """
        Fetches the URI-based WAF overrides in a zone.

        **Note:** Applies only to the
        [previous version of WAF managed rules](https://developers.cloudflare.com/support/firewall/managed-rules-web-application-firewall-waf/understanding-waf-managed-rules-web-application-firewall/).

        Args:
          zone_identifier: Identifier

          page: The page number of paginated results.

          per_page: The number of WAF overrides per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_identifier:
            raise ValueError(f"Expected a non-empty value for `zone_identifier` but received {zone_identifier!r}")
        return await self._get(
            f"/zones/{zone_identifier}/firewall/waf/overrides",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page": page,
                        "per_page": per_page,
                    },
                    override_waf_overrides_list_waf_overrides_params.OverrideWAFOverridesListWAFOverridesParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OverrideWAFOverridesListWAFOverridesResponse]],
                ResultWrapper[OverrideWAFOverridesListWAFOverridesResponse],
            ),
        )


class OverridesWithRawResponse:
    def __init__(self, overrides: Overrides) -> None:
        self._overrides = overrides

        self.update = to_raw_response_wrapper(
            overrides.update,
        )
        self.delete = to_raw_response_wrapper(
            overrides.delete,
        )
        self.get = to_raw_response_wrapper(
            overrides.get,
        )
        self.waf_overrides_create_a_waf_override = to_raw_response_wrapper(
            overrides.waf_overrides_create_a_waf_override,
        )
        self.waf_overrides_list_waf_overrides = to_raw_response_wrapper(
            overrides.waf_overrides_list_waf_overrides,
        )


class AsyncOverridesWithRawResponse:
    def __init__(self, overrides: AsyncOverrides) -> None:
        self._overrides = overrides

        self.update = async_to_raw_response_wrapper(
            overrides.update,
        )
        self.delete = async_to_raw_response_wrapper(
            overrides.delete,
        )
        self.get = async_to_raw_response_wrapper(
            overrides.get,
        )
        self.waf_overrides_create_a_waf_override = async_to_raw_response_wrapper(
            overrides.waf_overrides_create_a_waf_override,
        )
        self.waf_overrides_list_waf_overrides = async_to_raw_response_wrapper(
            overrides.waf_overrides_list_waf_overrides,
        )


class OverridesWithStreamingResponse:
    def __init__(self, overrides: Overrides) -> None:
        self._overrides = overrides

        self.update = to_streamed_response_wrapper(
            overrides.update,
        )
        self.delete = to_streamed_response_wrapper(
            overrides.delete,
        )
        self.get = to_streamed_response_wrapper(
            overrides.get,
        )
        self.waf_overrides_create_a_waf_override = to_streamed_response_wrapper(
            overrides.waf_overrides_create_a_waf_override,
        )
        self.waf_overrides_list_waf_overrides = to_streamed_response_wrapper(
            overrides.waf_overrides_list_waf_overrides,
        )


class AsyncOverridesWithStreamingResponse:
    def __init__(self, overrides: AsyncOverrides) -> None:
        self._overrides = overrides

        self.update = async_to_streamed_response_wrapper(
            overrides.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            overrides.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            overrides.get,
        )
        self.waf_overrides_create_a_waf_override = async_to_streamed_response_wrapper(
            overrides.waf_overrides_create_a_waf_override,
        )
        self.waf_overrides_list_waf_overrides = async_to_streamed_response_wrapper(
            overrides.waf_overrides_list_waf_overrides,
        )
