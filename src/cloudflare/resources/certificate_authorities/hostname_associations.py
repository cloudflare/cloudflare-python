# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast

import httpx

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
from ..._base_client import make_request_options
from ...types.certificate_authorities import hostname_association_get_params, hostname_association_update_params
from ...types.certificate_authorities.hostname_association import HostnameAssociation
from ...types.certificate_authorities.hostname_association_get_response import HostnameAssociationGetResponse
from ...types.certificate_authorities.hostname_association_update_response import HostnameAssociationUpdateResponse

__all__ = ["HostnameAssociationsResource", "AsyncHostnameAssociationsResource"]


class HostnameAssociationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HostnameAssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return HostnameAssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnameAssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return HostnameAssociationsResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        hostnames: List[HostnameAssociation] | NotGiven = NOT_GIVEN,
        mtls_certificate_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameAssociationUpdateResponse]:
        """
        Replace Hostname Associations

        Args:
          zone_id: Identifier

          mtls_certificate_id: The UUID for a certificate that was uploaded to the mTLS Certificate Management
              endpoint. If no mtls_certificate_id is given, the hostnames will be associated
              to your active Cloudflare Managed CA.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/certificate_authorities/hostname_associations",
            body=maybe_transform(
                {
                    "hostnames": hostnames,
                    "mtls_certificate_id": mtls_certificate_id,
                },
                hostname_association_update_params.HostnameAssociationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HostnameAssociationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[HostnameAssociationUpdateResponse]], ResultWrapper[HostnameAssociationUpdateResponse]
            ),
        )

    def get(
        self,
        *,
        zone_id: str,
        mtls_certificate_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameAssociationGetResponse]:
        """
        List Hostname Associations

        Args:
          zone_id: Identifier

          mtls_certificate_id: The UUID to match against for a certificate that was uploaded to the mTLS
              Certificate Management endpoint. If no mtls_certificate_id is given, the results
              will be the hostnames associated to your active Cloudflare Managed CA.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/certificate_authorities/hostname_associations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"mtls_certificate_id": mtls_certificate_id},
                    hostname_association_get_params.HostnameAssociationGetParams,
                ),
                post_parser=ResultWrapper[Optional[HostnameAssociationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HostnameAssociationGetResponse]], ResultWrapper[HostnameAssociationGetResponse]),
        )


class AsyncHostnameAssociationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHostnameAssociationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncHostnameAssociationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnameAssociationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncHostnameAssociationsResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        hostnames: List[HostnameAssociation] | NotGiven = NOT_GIVEN,
        mtls_certificate_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameAssociationUpdateResponse]:
        """
        Replace Hostname Associations

        Args:
          zone_id: Identifier

          mtls_certificate_id: The UUID for a certificate that was uploaded to the mTLS Certificate Management
              endpoint. If no mtls_certificate_id is given, the hostnames will be associated
              to your active Cloudflare Managed CA.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/certificate_authorities/hostname_associations",
            body=await async_maybe_transform(
                {
                    "hostnames": hostnames,
                    "mtls_certificate_id": mtls_certificate_id,
                },
                hostname_association_update_params.HostnameAssociationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[HostnameAssociationUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[HostnameAssociationUpdateResponse]], ResultWrapper[HostnameAssociationUpdateResponse]
            ),
        )

    async def get(
        self,
        *,
        zone_id: str,
        mtls_certificate_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[HostnameAssociationGetResponse]:
        """
        List Hostname Associations

        Args:
          zone_id: Identifier

          mtls_certificate_id: The UUID to match against for a certificate that was uploaded to the mTLS
              Certificate Management endpoint. If no mtls_certificate_id is given, the results
              will be the hostnames associated to your active Cloudflare Managed CA.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/certificate_authorities/hostname_associations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"mtls_certificate_id": mtls_certificate_id},
                    hostname_association_get_params.HostnameAssociationGetParams,
                ),
                post_parser=ResultWrapper[Optional[HostnameAssociationGetResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[HostnameAssociationGetResponse]], ResultWrapper[HostnameAssociationGetResponse]),
        )


class HostnameAssociationsResourceWithRawResponse:
    def __init__(self, hostname_associations: HostnameAssociationsResource) -> None:
        self._hostname_associations = hostname_associations

        self.update = to_raw_response_wrapper(
            hostname_associations.update,
        )
        self.get = to_raw_response_wrapper(
            hostname_associations.get,
        )


class AsyncHostnameAssociationsResourceWithRawResponse:
    def __init__(self, hostname_associations: AsyncHostnameAssociationsResource) -> None:
        self._hostname_associations = hostname_associations

        self.update = async_to_raw_response_wrapper(
            hostname_associations.update,
        )
        self.get = async_to_raw_response_wrapper(
            hostname_associations.get,
        )


class HostnameAssociationsResourceWithStreamingResponse:
    def __init__(self, hostname_associations: HostnameAssociationsResource) -> None:
        self._hostname_associations = hostname_associations

        self.update = to_streamed_response_wrapper(
            hostname_associations.update,
        )
        self.get = to_streamed_response_wrapper(
            hostname_associations.get,
        )


class AsyncHostnameAssociationsResourceWithStreamingResponse:
    def __init__(self, hostname_associations: AsyncHostnameAssociationsResource) -> None:
        self._hostname_associations = hostname_associations

        self.update = async_to_streamed_response_wrapper(
            hostname_associations.update,
        )
        self.get = async_to_streamed_response_wrapper(
            hostname_associations.get,
        )
