# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import httpx

from ..._compat import cached_property

from ...types.certificate_authorities import (
    HostnameAssociationClientCertificateForAZoneListHostnameAssociationsResponse,
    HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse,
)

from typing import Type, List

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
from ...types.certificate_authorities import (
    hostname_association_client_certificate_for_a_zone_list_hostname_associations_params,
)
from ...types.certificate_authorities import (
    hostname_association_client_certificate_for_a_zone_put_hostname_associations_params,
)
from ..._wrappers import ResultWrapper
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["HostnameAssociations", "AsyncHostnameAssociations"]


class HostnameAssociations(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> HostnameAssociationsWithRawResponse:
        return HostnameAssociationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> HostnameAssociationsWithStreamingResponse:
        return HostnameAssociationsWithStreamingResponse(self)

    def client_certificate_for_a_zone_list_hostname_associations(
        self,
        zone_id: str,
        *,
        mtls_certificate_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostnameAssociationClientCertificateForAZoneListHostnameAssociationsResponse:
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
                    hostname_association_client_certificate_for_a_zone_list_hostname_associations_params.HostnameAssociationClientCertificateForAZoneListHostnameAssociationsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[HostnameAssociationClientCertificateForAZoneListHostnameAssociationsResponse],
                ResultWrapper[HostnameAssociationClientCertificateForAZoneListHostnameAssociationsResponse],
            ),
        )

    def client_certificate_for_a_zone_put_hostname_associations(
        self,
        zone_id: str,
        *,
        hostnames: List[str] | NotGiven = NOT_GIVEN,
        mtls_certificate_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse:
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
                hostname_association_client_certificate_for_a_zone_put_hostname_associations_params.HostnameAssociationClientCertificateForAZonePutHostnameAssociationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse],
                ResultWrapper[HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse],
            ),
        )


class AsyncHostnameAssociations(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncHostnameAssociationsWithRawResponse:
        return AsyncHostnameAssociationsWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncHostnameAssociationsWithStreamingResponse:
        return AsyncHostnameAssociationsWithStreamingResponse(self)

    async def client_certificate_for_a_zone_list_hostname_associations(
        self,
        zone_id: str,
        *,
        mtls_certificate_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostnameAssociationClientCertificateForAZoneListHostnameAssociationsResponse:
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
                query=maybe_transform(
                    {"mtls_certificate_id": mtls_certificate_id},
                    hostname_association_client_certificate_for_a_zone_list_hostname_associations_params.HostnameAssociationClientCertificateForAZoneListHostnameAssociationsParams,
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[HostnameAssociationClientCertificateForAZoneListHostnameAssociationsResponse],
                ResultWrapper[HostnameAssociationClientCertificateForAZoneListHostnameAssociationsResponse],
            ),
        )

    async def client_certificate_for_a_zone_put_hostname_associations(
        self,
        zone_id: str,
        *,
        hostnames: List[str] | NotGiven = NOT_GIVEN,
        mtls_certificate_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse:
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
            body=maybe_transform(
                {
                    "hostnames": hostnames,
                    "mtls_certificate_id": mtls_certificate_id,
                },
                hostname_association_client_certificate_for_a_zone_put_hostname_associations_params.HostnameAssociationClientCertificateForAZonePutHostnameAssociationsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(
                Type[HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse],
                ResultWrapper[HostnameAssociationClientCertificateForAZonePutHostnameAssociationsResponse],
            ),
        )


class HostnameAssociationsWithRawResponse:
    def __init__(self, hostname_associations: HostnameAssociations) -> None:
        self._hostname_associations = hostname_associations

        self.client_certificate_for_a_zone_list_hostname_associations = to_raw_response_wrapper(
            hostname_associations.client_certificate_for_a_zone_list_hostname_associations,
        )
        self.client_certificate_for_a_zone_put_hostname_associations = to_raw_response_wrapper(
            hostname_associations.client_certificate_for_a_zone_put_hostname_associations,
        )


class AsyncHostnameAssociationsWithRawResponse:
    def __init__(self, hostname_associations: AsyncHostnameAssociations) -> None:
        self._hostname_associations = hostname_associations

        self.client_certificate_for_a_zone_list_hostname_associations = async_to_raw_response_wrapper(
            hostname_associations.client_certificate_for_a_zone_list_hostname_associations,
        )
        self.client_certificate_for_a_zone_put_hostname_associations = async_to_raw_response_wrapper(
            hostname_associations.client_certificate_for_a_zone_put_hostname_associations,
        )


class HostnameAssociationsWithStreamingResponse:
    def __init__(self, hostname_associations: HostnameAssociations) -> None:
        self._hostname_associations = hostname_associations

        self.client_certificate_for_a_zone_list_hostname_associations = to_streamed_response_wrapper(
            hostname_associations.client_certificate_for_a_zone_list_hostname_associations,
        )
        self.client_certificate_for_a_zone_put_hostname_associations = to_streamed_response_wrapper(
            hostname_associations.client_certificate_for_a_zone_put_hostname_associations,
        )


class AsyncHostnameAssociationsWithStreamingResponse:
    def __init__(self, hostname_associations: AsyncHostnameAssociations) -> None:
        self._hostname_associations = hostname_associations

        self.client_certificate_for_a_zone_list_hostname_associations = async_to_streamed_response_wrapper(
            hostname_associations.client_certificate_for_a_zone_list_hostname_associations,
        )
        self.client_certificate_for_a_zone_put_hostname_associations = async_to_streamed_response_wrapper(
            hostname_associations.client_certificate_for_a_zone_put_hostname_associations,
        )
