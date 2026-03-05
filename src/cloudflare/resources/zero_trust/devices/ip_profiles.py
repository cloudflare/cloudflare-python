# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
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
from ....types.zero_trust.devices import ip_profile_list_params, ip_profile_create_params, ip_profile_update_params
from ....types.zero_trust.devices.ip_profile import IPProfile
from ....types.zero_trust.devices.ip_profile_delete_response import IPProfileDeleteResponse

__all__ = ["IPProfilesResource", "AsyncIPProfilesResource"]


class IPProfilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IPProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return IPProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IPProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return IPProfilesResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        account_id: str,
        match: str,
        name: str,
        precedence: int,
        subnet_id: str,
        description: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPProfile:
        """Creates a WARP Device IP profile.

        Currently, only IPv4 Device subnets can be
        associated.

        Args:
          match:
              The wirefilter expression to match registrations. Available values:
              "identity.name", "identity.email", "identity.groups.id", "identity.groups.name",
              "identity.groups.email", "identity.saml_attributes".

          name: A user-friendly name for the Device IP profile.

          precedence: The precedence of the Device IP profile. Lower values indicate higher
              precedence. Device IP profile will be evaluated in ascending order of this
              field.

          subnet_id: The ID of the Subnet.

          description: An optional description of the Device IP profile.

          enabled: Whether the Device IP profile will be applied to matching devices.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._post(
            f"/accounts/{account_id}/devices/ip-profiles",
            body=maybe_transform(
                {
                    "match": match,
                    "name": name,
                    "precedence": precedence,
                    "subnet_id": subnet_id,
                    "description": description,
                    "enabled": enabled,
                },
                ip_profile_create_params.IPProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPProfile]._unwrapper,
            ),
            cast_to=cast(Type[IPProfile], ResultWrapper[IPProfile]),
        )

    def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        match: str | Omit = omit,
        name: str | Omit = omit,
        precedence: int | Omit = omit,
        subnet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPProfile:
        """Updates a WARP Device IP profile.

        Currently, only IPv4 Device subnets can be
        associated.

        Args:
          description: An optional description of the Device IP profile.

          enabled: Whether the Device IP profile is enabled.

          match:
              The wirefilter expression to match registrations. Available values:
              "identity.name", "identity.email", "identity.groups.id", "identity.groups.name",
              "identity.groups.email", "identity.saml_attributes".

          name: A user-friendly name for the Device IP profile.

          precedence: The precedence of the Device IP profile. Lower values indicate higher
              precedence. Device IP profile will be evaluated in ascending order of this
              field.

          subnet_id: The ID of the Subnet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._patch(
            f"/accounts/{account_id}/devices/ip-profiles/{profile_id}",
            body=maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "match": match,
                    "name": name,
                    "precedence": precedence,
                    "subnet_id": subnet_id,
                },
                ip_profile_update_params.IPProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPProfile]._unwrapper,
            ),
            cast_to=cast(Type[IPProfile], ResultWrapper[IPProfile]),
        )

    def list(
        self,
        *,
        account_id: str,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncSinglePage[IPProfile]:
        """
        Lists WARP Device IP profiles.

        Args:
          per_page: The number of IP profiles to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/ip-profiles",
            page=SyncSinglePage[IPProfile],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"per_page": per_page}, ip_profile_list_params.IPProfileListParams),
            ),
            model=IPProfile,
        )

    def delete(
        self,
        profile_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPProfileDeleteResponse:
        """
        Delete a WARP Device IP profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._delete(
            f"/accounts/{account_id}/devices/ip-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPProfileDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPProfileDeleteResponse], ResultWrapper[IPProfileDeleteResponse]),
        )

    def get(
        self,
        profile_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPProfile:
        """
        Fetches a single WARP Device IP profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return self._get(
            f"/accounts/{account_id}/devices/ip-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPProfile]._unwrapper,
            ),
            cast_to=cast(Type[IPProfile], ResultWrapper[IPProfile]),
        )


class AsyncIPProfilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIPProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIPProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIPProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncIPProfilesResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        account_id: str,
        match: str,
        name: str,
        precedence: int,
        subnet_id: str,
        description: Optional[str] | Omit = omit,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPProfile:
        """Creates a WARP Device IP profile.

        Currently, only IPv4 Device subnets can be
        associated.

        Args:
          match:
              The wirefilter expression to match registrations. Available values:
              "identity.name", "identity.email", "identity.groups.id", "identity.groups.name",
              "identity.groups.email", "identity.saml_attributes".

          name: A user-friendly name for the Device IP profile.

          precedence: The precedence of the Device IP profile. Lower values indicate higher
              precedence. Device IP profile will be evaluated in ascending order of this
              field.

          subnet_id: The ID of the Subnet.

          description: An optional description of the Device IP profile.

          enabled: Whether the Device IP profile will be applied to matching devices.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._post(
            f"/accounts/{account_id}/devices/ip-profiles",
            body=await async_maybe_transform(
                {
                    "match": match,
                    "name": name,
                    "precedence": precedence,
                    "subnet_id": subnet_id,
                    "description": description,
                    "enabled": enabled,
                },
                ip_profile_create_params.IPProfileCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPProfile]._unwrapper,
            ),
            cast_to=cast(Type[IPProfile], ResultWrapper[IPProfile]),
        )

    async def update(
        self,
        profile_id: str,
        *,
        account_id: str,
        description: str | Omit = omit,
        enabled: bool | Omit = omit,
        match: str | Omit = omit,
        name: str | Omit = omit,
        precedence: int | Omit = omit,
        subnet_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPProfile:
        """Updates a WARP Device IP profile.

        Currently, only IPv4 Device subnets can be
        associated.

        Args:
          description: An optional description of the Device IP profile.

          enabled: Whether the Device IP profile is enabled.

          match:
              The wirefilter expression to match registrations. Available values:
              "identity.name", "identity.email", "identity.groups.id", "identity.groups.name",
              "identity.groups.email", "identity.saml_attributes".

          name: A user-friendly name for the Device IP profile.

          precedence: The precedence of the Device IP profile. Lower values indicate higher
              precedence. Device IP profile will be evaluated in ascending order of this
              field.

          subnet_id: The ID of the Subnet.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._patch(
            f"/accounts/{account_id}/devices/ip-profiles/{profile_id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "enabled": enabled,
                    "match": match,
                    "name": name,
                    "precedence": precedence,
                    "subnet_id": subnet_id,
                },
                ip_profile_update_params.IPProfileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPProfile]._unwrapper,
            ),
            cast_to=cast(Type[IPProfile], ResultWrapper[IPProfile]),
        )

    def list(
        self,
        *,
        account_id: str,
        per_page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[IPProfile, AsyncSinglePage[IPProfile]]:
        """
        Lists WARP Device IP profiles.

        Args:
          per_page: The number of IP profiles to return per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get_api_list(
            f"/accounts/{account_id}/devices/ip-profiles",
            page=AsyncSinglePage[IPProfile],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"per_page": per_page}, ip_profile_list_params.IPProfileListParams),
            ),
            model=IPProfile,
        )

    async def delete(
        self,
        profile_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPProfileDeleteResponse:
        """
        Delete a WARP Device IP profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._delete(
            f"/accounts/{account_id}/devices/ip-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPProfileDeleteResponse]._unwrapper,
            ),
            cast_to=cast(Type[IPProfileDeleteResponse], ResultWrapper[IPProfileDeleteResponse]),
        )

    async def get(
        self,
        profile_id: str,
        *,
        account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> IPProfile:
        """
        Fetches a single WARP Device IP profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        if not profile_id:
            raise ValueError(f"Expected a non-empty value for `profile_id` but received {profile_id!r}")
        return await self._get(
            f"/accounts/{account_id}/devices/ip-profiles/{profile_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[IPProfile]._unwrapper,
            ),
            cast_to=cast(Type[IPProfile], ResultWrapper[IPProfile]),
        )


class IPProfilesResourceWithRawResponse:
    def __init__(self, ip_profiles: IPProfilesResource) -> None:
        self._ip_profiles = ip_profiles

        self.create = to_raw_response_wrapper(
            ip_profiles.create,
        )
        self.update = to_raw_response_wrapper(
            ip_profiles.update,
        )
        self.list = to_raw_response_wrapper(
            ip_profiles.list,
        )
        self.delete = to_raw_response_wrapper(
            ip_profiles.delete,
        )
        self.get = to_raw_response_wrapper(
            ip_profiles.get,
        )


class AsyncIPProfilesResourceWithRawResponse:
    def __init__(self, ip_profiles: AsyncIPProfilesResource) -> None:
        self._ip_profiles = ip_profiles

        self.create = async_to_raw_response_wrapper(
            ip_profiles.create,
        )
        self.update = async_to_raw_response_wrapper(
            ip_profiles.update,
        )
        self.list = async_to_raw_response_wrapper(
            ip_profiles.list,
        )
        self.delete = async_to_raw_response_wrapper(
            ip_profiles.delete,
        )
        self.get = async_to_raw_response_wrapper(
            ip_profiles.get,
        )


class IPProfilesResourceWithStreamingResponse:
    def __init__(self, ip_profiles: IPProfilesResource) -> None:
        self._ip_profiles = ip_profiles

        self.create = to_streamed_response_wrapper(
            ip_profiles.create,
        )
        self.update = to_streamed_response_wrapper(
            ip_profiles.update,
        )
        self.list = to_streamed_response_wrapper(
            ip_profiles.list,
        )
        self.delete = to_streamed_response_wrapper(
            ip_profiles.delete,
        )
        self.get = to_streamed_response_wrapper(
            ip_profiles.get,
        )


class AsyncIPProfilesResourceWithStreamingResponse:
    def __init__(self, ip_profiles: AsyncIPProfilesResource) -> None:
        self._ip_profiles = ip_profiles

        self.create = async_to_streamed_response_wrapper(
            ip_profiles.create,
        )
        self.update = async_to_streamed_response_wrapper(
            ip_profiles.update,
        )
        self.list = async_to_streamed_response_wrapper(
            ip_profiles.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            ip_profiles.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            ip_profiles.get,
        )
