# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast, overload

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    required_args,
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
from ....types.magic_transit.sites import app_configuration_create_params, app_configuration_update_params
from ....types.magic_transit.sites.app_configuration_list_response import AppConfigurationListResponse
from ....types.magic_transit.sites.app_configuration_create_response import AppConfigurationCreateResponse
from ....types.magic_transit.sites.app_configuration_delete_response import AppConfigurationDeleteResponse
from ....types.magic_transit.sites.app_configuration_update_response import AppConfigurationUpdateResponse

__all__ = ["AppConfigurationResource", "AsyncAppConfigurationResource"]


class AppConfigurationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AppConfigurationResourceWithRawResponse:
        return AppConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AppConfigurationResourceWithStreamingResponse:
        return AppConfigurationResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        site_id: str,
        *,
        account_id: str,
        account_app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationCreateResponse]:
        """
        Creates a new App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          account_app_id: Magic account app ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        site_id: str,
        *,
        account_id: str,
        managed_app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationCreateResponse]:
        """
        Creates a new App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          managed_app_id: Managed app ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "account_app_id"], ["account_id", "managed_app_id"])
    def create(
        self,
        site_id: str,
        *,
        account_id: str,
        account_app_id: str | NotGiven = NOT_GIVEN,
        managed_app_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationCreateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/app_configs",
            body=maybe_transform(
                {
                    "account_app_id": account_app_id,
                    "managed_app_id": managed_app_id,
                },
                app_configuration_create_params.AppConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppConfigurationCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppConfigurationCreateResponse]], ResultWrapper[AppConfigurationCreateResponse]),
        )

    @overload
    def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        account_app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          account_app_id: Magic account app ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        managed_app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          managed_app_id: Managed app ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        account_app_id: str,
        managed_app_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          account_app_id: Magic account app ID.

          managed_app_id: **Must be set to null**

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        account_app_id: Optional[str],
        managed_app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          account_app_id: **Must be set to null**

          managed_app_id: Managed app ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "site_id", "body"],
        ["account_id", "site_id", "account_app_id"],
        ["account_id", "site_id", "managed_app_id"],
        ["account_id", "site_id", "account_app_id", "managed_app_id"],
    )
    def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        body: object | NotGiven = NOT_GIVEN,
        account_app_id: str | None | NotGiven = NOT_GIVEN,
        managed_app_id: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not app_config_id:
            raise ValueError(f"Expected a non-empty value for `app_config_id` but received {app_config_id!r}")
        return self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}",
            body=maybe_transform(body, app_configuration_update_params.AppConfigurationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppConfigurationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppConfigurationUpdateResponse]], ResultWrapper[AppConfigurationUpdateResponse]),
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
    ) -> SyncSinglePage[AppConfigurationListResponse]:
        """
        Lists App Configs associated with a site.

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
            f"/accounts/{account_id}/magic/sites/{site_id}/app_configs",
            page=SyncSinglePage[AppConfigurationListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AppConfigurationListResponse,
        )

    def delete(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationDeleteResponse]:
        """
        Deletes specific App Config associated with a site.

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not app_config_id:
            raise ValueError(f"Expected a non-empty value for `app_config_id` but received {app_config_id!r}")
        return self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppConfigurationDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppConfigurationDeleteResponse]], ResultWrapper[AppConfigurationDeleteResponse]),
        )


class AsyncAppConfigurationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAppConfigurationResourceWithRawResponse:
        return AsyncAppConfigurationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAppConfigurationResourceWithStreamingResponse:
        return AsyncAppConfigurationResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        site_id: str,
        *,
        account_id: str,
        account_app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationCreateResponse]:
        """
        Creates a new App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          account_app_id: Magic account app ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        site_id: str,
        *,
        account_id: str,
        managed_app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationCreateResponse]:
        """
        Creates a new App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          managed_app_id: Managed app ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["account_id", "account_app_id"], ["account_id", "managed_app_id"])
    async def create(
        self,
        site_id: str,
        *,
        account_id: str,
        account_app_id: str | NotGiven = NOT_GIVEN,
        managed_app_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationCreateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        return await self._post(
            f"/accounts/{account_id}/magic/sites/{site_id}/app_configs",
            body=await async_maybe_transform(
                {
                    "account_app_id": account_app_id,
                    "managed_app_id": managed_app_id,
                },
                app_configuration_create_params.AppConfigurationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppConfigurationCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppConfigurationCreateResponse]], ResultWrapper[AppConfigurationCreateResponse]),
        )

    @overload
    async def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        account_app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          account_app_id: Magic account app ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        managed_app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          managed_app_id: Managed app ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        account_app_id: str,
        managed_app_id: Optional[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          account_app_id: Magic account app ID.

          managed_app_id: **Must be set to null**

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        account_app_id: Optional[str],
        managed_app_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        """
        Updates an App Config for a site

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          account_app_id: **Must be set to null**

          managed_app_id: Managed app ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["account_id", "site_id", "body"],
        ["account_id", "site_id", "account_app_id"],
        ["account_id", "site_id", "managed_app_id"],
        ["account_id", "site_id", "account_app_id", "managed_app_id"],
    )
    async def update(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        body: object | NotGiven = NOT_GIVEN,
        account_app_id: str | None | NotGiven = NOT_GIVEN,
        managed_app_id: str | None | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationUpdateResponse]:
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not app_config_id:
            raise ValueError(f"Expected a non-empty value for `app_config_id` but received {app_config_id!r}")
        return await self._put(
            f"/accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}",
            body=await async_maybe_transform(body, app_configuration_update_params.AppConfigurationUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppConfigurationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppConfigurationUpdateResponse]], ResultWrapper[AppConfigurationUpdateResponse]),
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
    ) -> AsyncPaginator[AppConfigurationListResponse, AsyncSinglePage[AppConfigurationListResponse]]:
        """
        Lists App Configs associated with a site.

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
            f"/accounts/{account_id}/magic/sites/{site_id}/app_configs",
            page=AsyncSinglePage[AppConfigurationListResponse],
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            model=AppConfigurationListResponse,
        )

    async def delete(
        self,
        app_config_id: str,
        *,
        account_id: str,
        site_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[AppConfigurationDeleteResponse]:
        """
        Deletes specific App Config associated with a site.

        Args:
          account_id: Identifier

          site_id: Identifier

          app_config_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not site_id:
            raise ValueError(f"Expected a non-empty value for `site_id` but received {site_id!r}")
        if not app_config_id:
            raise ValueError(f"Expected a non-empty value for `app_config_id` but received {app_config_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/magic/sites/{site_id}/app_configs/{app_config_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[AppConfigurationDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[AppConfigurationDeleteResponse]], ResultWrapper[AppConfigurationDeleteResponse]),
        )


class AppConfigurationResourceWithRawResponse:
    def __init__(self, app_configuration: AppConfigurationResource) -> None:
        self._app_configuration = app_configuration

        self.create = to_raw_response_wrapper(
            app_configuration.create,
        )
        self.update = to_raw_response_wrapper(
            app_configuration.update,
        )
        self.list = to_raw_response_wrapper(
            app_configuration.list,
        )
        self.delete = to_raw_response_wrapper(
            app_configuration.delete,
        )


class AsyncAppConfigurationResourceWithRawResponse:
    def __init__(self, app_configuration: AsyncAppConfigurationResource) -> None:
        self._app_configuration = app_configuration

        self.create = async_to_raw_response_wrapper(
            app_configuration.create,
        )
        self.update = async_to_raw_response_wrapper(
            app_configuration.update,
        )
        self.list = async_to_raw_response_wrapper(
            app_configuration.list,
        )
        self.delete = async_to_raw_response_wrapper(
            app_configuration.delete,
        )


class AppConfigurationResourceWithStreamingResponse:
    def __init__(self, app_configuration: AppConfigurationResource) -> None:
        self._app_configuration = app_configuration

        self.create = to_streamed_response_wrapper(
            app_configuration.create,
        )
        self.update = to_streamed_response_wrapper(
            app_configuration.update,
        )
        self.list = to_streamed_response_wrapper(
            app_configuration.list,
        )
        self.delete = to_streamed_response_wrapper(
            app_configuration.delete,
        )


class AsyncAppConfigurationResourceWithStreamingResponse:
    def __init__(self, app_configuration: AsyncAppConfigurationResource) -> None:
        self._app_configuration = app_configuration

        self.create = async_to_streamed_response_wrapper(
            app_configuration.create,
        )
        self.update = async_to_streamed_response_wrapper(
            app_configuration.update,
        )
        self.list = async_to_streamed_response_wrapper(
            app_configuration.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            app_configuration.delete,
        )
