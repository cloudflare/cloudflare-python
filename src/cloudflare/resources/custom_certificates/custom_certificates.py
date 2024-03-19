# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, cast
from typing_extensions import Literal

import httpx

from ...types import (
    CustomCertificateGetResponse,
    CustomCertificateEditResponse,
    CustomCertificateCreateResponse,
    CustomCertificateDeleteResponse,
    TLSCertificatesAndHostnamesCustomCertificate,
    custom_certificate_edit_params,
    custom_certificate_list_params,
    custom_certificate_create_params,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from .prioritize import (
    Prioritize,
    AsyncPrioritize,
    PrioritizeWithRawResponse,
    AsyncPrioritizeWithRawResponse,
    PrioritizeWithStreamingResponse,
    AsyncPrioritizeWithStreamingResponse,
)
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

__all__ = ["CustomCertificates", "AsyncCustomCertificates"]


class CustomCertificates(SyncAPIResource):
    @cached_property
    def prioritize(self) -> Prioritize:
        return Prioritize(self._client)

    @cached_property
    def with_raw_response(self) -> CustomCertificatesWithRawResponse:
        return CustomCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomCertificatesWithStreamingResponse:
        return CustomCertificatesWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        certificate: str,
        private_key: str,
        bundle_method: Literal["ubiquitous", "optimal", "force"] | NotGiven = NOT_GIVEN,
        geo_restrictions: custom_certificate_create_params.GeoRestrictions | NotGiven = NOT_GIVEN,
        policy: str | NotGiven = NOT_GIVEN,
        type: Literal["legacy_custom", "sni_custom"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCertificateCreateResponse:
        """
        Upload a new SSL certificate for a zone.

        Args:
          zone_id: Identifier

          certificate: The zone's SSL certificate or certificate and the intermediate(s).

          private_key: The zone's private key.

          bundle_method: A ubiquitous bundle has the highest probability of being verified everywhere,
              even by clients using outdated or unusual trust stores. An optimal bundle uses
              the shortest chain and newest intermediates. And the force bundle verifies the
              chain, but does not otherwise modify it.

          geo_restrictions: Specify the region where your private key can be held locally for optimal TLS
              performance. HTTPS connections to any excluded data center will still be fully
              encrypted, but will incur some latency while Keyless SSL is used to complete the
              handshake with the nearest allowed data center. Options allow distribution to
              only to U.S. data centers, only to E.U. data centers, or only to highest
              security data centers. Default distribution is to all Cloudflare datacenters,
              for optimal performance.

          policy: Specify the policy that determines the region where your private key will be
              held locally. HTTPS connections to any excluded data center will still be fully
              encrypted, but will incur some latency while Keyless SSL is used to complete the
              handshake with the nearest allowed data center. Any combination of countries,
              specified by their two letter country code
              (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)
              can be chosen, such as 'country: IN', as well as 'region: EU' which refers to
              the EU region. If there are too few data centers satisfying the policy, it will
              be rejected.

          type: The type 'legacy_custom' enables support for legacy clients which do not include
              SNI in the TLS handshake.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            CustomCertificateCreateResponse,
            self._post(
                f"/zones/{zone_id}/custom_certificates",
                body=maybe_transform(
                    {
                        "certificate": certificate,
                        "private_key": private_key,
                        "bundle_method": bundle_method,
                        "geo_restrictions": geo_restrictions,
                        "policy": policy,
                        "type": type,
                    },
                    custom_certificate_create_params.CustomCertificateCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomCertificateCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncV4PagePaginationArray[TLSCertificatesAndHostnamesCustomCertificate]:
        """List, search, and filter all of your custom SSL certificates.

        The higher
        priority will break ties across overlapping 'legacy_custom' certificates, but
        'legacy_custom' certificates will always supercede 'sni_custom' certificates.

        Args:
          zone_id: Identifier

          match: Whether to match all search requirements or at least one (any).

          page: Page number of paginated results.

          per_page: Number of zones per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/custom_certificates",
            page=SyncV4PagePaginationArray[TLSCertificatesAndHostnamesCustomCertificate],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "match": match,
                        "page": page,
                        "per_page": per_page,
                    },
                    custom_certificate_list_params.CustomCertificateListParams,
                ),
            ),
            model=TLSCertificatesAndHostnamesCustomCertificate,
        )

    def delete(
        self,
        custom_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCertificateDeleteResponse:
        """
        Remove a SSL certificate from a zone.

        Args:
          zone_id: Identifier

          custom_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `custom_certificate_id` but received {custom_certificate_id!r}"
            )
        return self._delete(
            f"/zones/{zone_id}/custom_certificates/{custom_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomCertificateDeleteResponse], ResultWrapper[CustomCertificateDeleteResponse]),
        )

    def edit(
        self,
        custom_certificate_id: str,
        *,
        zone_id: str,
        bundle_method: Literal["ubiquitous", "optimal", "force"] | NotGiven = NOT_GIVEN,
        certificate: str | NotGiven = NOT_GIVEN,
        geo_restrictions: custom_certificate_edit_params.GeoRestrictions | NotGiven = NOT_GIVEN,
        policy: str | NotGiven = NOT_GIVEN,
        private_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCertificateEditResponse:
        """Upload a new private key and/or PEM/CRT for the SSL certificate.

        Note: PATCHing
        a configuration for sni_custom certificates will result in a new resource id
        being returned, and the previous one being deleted.

        Args:
          zone_id: Identifier

          custom_certificate_id: Identifier

          bundle_method: A ubiquitous bundle has the highest probability of being verified everywhere,
              even by clients using outdated or unusual trust stores. An optimal bundle uses
              the shortest chain and newest intermediates. And the force bundle verifies the
              chain, but does not otherwise modify it.

          certificate: The zone's SSL certificate or certificate and the intermediate(s).

          geo_restrictions: Specify the region where your private key can be held locally for optimal TLS
              performance. HTTPS connections to any excluded data center will still be fully
              encrypted, but will incur some latency while Keyless SSL is used to complete the
              handshake with the nearest allowed data center. Options allow distribution to
              only to U.S. data centers, only to E.U. data centers, or only to highest
              security data centers. Default distribution is to all Cloudflare datacenters,
              for optimal performance.

          policy: Specify the policy that determines the region where your private key will be
              held locally. HTTPS connections to any excluded data center will still be fully
              encrypted, but will incur some latency while Keyless SSL is used to complete the
              handshake with the nearest allowed data center. Any combination of countries,
              specified by their two letter country code
              (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)
              can be chosen, such as 'country: IN', as well as 'region: EU' which refers to
              the EU region. If there are too few data centers satisfying the policy, it will
              be rejected.

          private_key: The zone's private key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `custom_certificate_id` but received {custom_certificate_id!r}"
            )
        return cast(
            CustomCertificateEditResponse,
            self._patch(
                f"/zones/{zone_id}/custom_certificates/{custom_certificate_id}",
                body=maybe_transform(
                    {
                        "bundle_method": bundle_method,
                        "certificate": certificate,
                        "geo_restrictions": geo_restrictions,
                        "policy": policy,
                        "private_key": private_key,
                    },
                    custom_certificate_edit_params.CustomCertificateEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomCertificateEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def get(
        self,
        custom_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCertificateGetResponse:
        """
        SSL Configuration Details

        Args:
          zone_id: Identifier

          custom_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `custom_certificate_id` but received {custom_certificate_id!r}"
            )
        return cast(
            CustomCertificateGetResponse,
            self._get(
                f"/zones/{zone_id}/custom_certificates/{custom_certificate_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomCertificateGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCustomCertificates(AsyncAPIResource):
    @cached_property
    def prioritize(self) -> AsyncPrioritize:
        return AsyncPrioritize(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCustomCertificatesWithRawResponse:
        return AsyncCustomCertificatesWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomCertificatesWithStreamingResponse:
        return AsyncCustomCertificatesWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        certificate: str,
        private_key: str,
        bundle_method: Literal["ubiquitous", "optimal", "force"] | NotGiven = NOT_GIVEN,
        geo_restrictions: custom_certificate_create_params.GeoRestrictions | NotGiven = NOT_GIVEN,
        policy: str | NotGiven = NOT_GIVEN,
        type: Literal["legacy_custom", "sni_custom"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCertificateCreateResponse:
        """
        Upload a new SSL certificate for a zone.

        Args:
          zone_id: Identifier

          certificate: The zone's SSL certificate or certificate and the intermediate(s).

          private_key: The zone's private key.

          bundle_method: A ubiquitous bundle has the highest probability of being verified everywhere,
              even by clients using outdated or unusual trust stores. An optimal bundle uses
              the shortest chain and newest intermediates. And the force bundle verifies the
              chain, but does not otherwise modify it.

          geo_restrictions: Specify the region where your private key can be held locally for optimal TLS
              performance. HTTPS connections to any excluded data center will still be fully
              encrypted, but will incur some latency while Keyless SSL is used to complete the
              handshake with the nearest allowed data center. Options allow distribution to
              only to U.S. data centers, only to E.U. data centers, or only to highest
              security data centers. Default distribution is to all Cloudflare datacenters,
              for optimal performance.

          policy: Specify the policy that determines the region where your private key will be
              held locally. HTTPS connections to any excluded data center will still be fully
              encrypted, but will incur some latency while Keyless SSL is used to complete the
              handshake with the nearest allowed data center. Any combination of countries,
              specified by their two letter country code
              (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)
              can be chosen, such as 'country: IN', as well as 'region: EU' which refers to
              the EU region. If there are too few data centers satisfying the policy, it will
              be rejected.

          type: The type 'legacy_custom' enables support for legacy clients which do not include
              SNI in the TLS handshake.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return cast(
            CustomCertificateCreateResponse,
            await self._post(
                f"/zones/{zone_id}/custom_certificates",
                body=await async_maybe_transform(
                    {
                        "certificate": certificate,
                        "private_key": private_key,
                        "bundle_method": bundle_method,
                        "geo_restrictions": geo_restrictions,
                        "policy": policy,
                        "type": type,
                    },
                    custom_certificate_create_params.CustomCertificateCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomCertificateCreateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        zone_id: str,
        match: Literal["any", "all"] | NotGiven = NOT_GIVEN,
        page: float | NotGiven = NOT_GIVEN,
        per_page: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[
        TLSCertificatesAndHostnamesCustomCertificate,
        AsyncV4PagePaginationArray[TLSCertificatesAndHostnamesCustomCertificate],
    ]:
        """List, search, and filter all of your custom SSL certificates.

        The higher
        priority will break ties across overlapping 'legacy_custom' certificates, but
        'legacy_custom' certificates will always supercede 'sni_custom' certificates.

        Args:
          zone_id: Identifier

          match: Whether to match all search requirements or at least one (any).

          page: Page number of paginated results.

          per_page: Number of zones per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/custom_certificates",
            page=AsyncV4PagePaginationArray[TLSCertificatesAndHostnamesCustomCertificate],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "match": match,
                        "page": page,
                        "per_page": per_page,
                    },
                    custom_certificate_list_params.CustomCertificateListParams,
                ),
            ),
            model=TLSCertificatesAndHostnamesCustomCertificate,
        )

    async def delete(
        self,
        custom_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCertificateDeleteResponse:
        """
        Remove a SSL certificate from a zone.

        Args:
          zone_id: Identifier

          custom_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `custom_certificate_id` but received {custom_certificate_id!r}"
            )
        return await self._delete(
            f"/zones/{zone_id}/custom_certificates/{custom_certificate_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CustomCertificateDeleteResponse], ResultWrapper[CustomCertificateDeleteResponse]),
        )

    async def edit(
        self,
        custom_certificate_id: str,
        *,
        zone_id: str,
        bundle_method: Literal["ubiquitous", "optimal", "force"] | NotGiven = NOT_GIVEN,
        certificate: str | NotGiven = NOT_GIVEN,
        geo_restrictions: custom_certificate_edit_params.GeoRestrictions | NotGiven = NOT_GIVEN,
        policy: str | NotGiven = NOT_GIVEN,
        private_key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCertificateEditResponse:
        """Upload a new private key and/or PEM/CRT for the SSL certificate.

        Note: PATCHing
        a configuration for sni_custom certificates will result in a new resource id
        being returned, and the previous one being deleted.

        Args:
          zone_id: Identifier

          custom_certificate_id: Identifier

          bundle_method: A ubiquitous bundle has the highest probability of being verified everywhere,
              even by clients using outdated or unusual trust stores. An optimal bundle uses
              the shortest chain and newest intermediates. And the force bundle verifies the
              chain, but does not otherwise modify it.

          certificate: The zone's SSL certificate or certificate and the intermediate(s).

          geo_restrictions: Specify the region where your private key can be held locally for optimal TLS
              performance. HTTPS connections to any excluded data center will still be fully
              encrypted, but will incur some latency while Keyless SSL is used to complete the
              handshake with the nearest allowed data center. Options allow distribution to
              only to U.S. data centers, only to E.U. data centers, or only to highest
              security data centers. Default distribution is to all Cloudflare datacenters,
              for optimal performance.

          policy: Specify the policy that determines the region where your private key will be
              held locally. HTTPS connections to any excluded data center will still be fully
              encrypted, but will incur some latency while Keyless SSL is used to complete the
              handshake with the nearest allowed data center. Any combination of countries,
              specified by their two letter country code
              (https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements)
              can be chosen, such as 'country: IN', as well as 'region: EU' which refers to
              the EU region. If there are too few data centers satisfying the policy, it will
              be rejected.

          private_key: The zone's private key.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `custom_certificate_id` but received {custom_certificate_id!r}"
            )
        return cast(
            CustomCertificateEditResponse,
            await self._patch(
                f"/zones/{zone_id}/custom_certificates/{custom_certificate_id}",
                body=await async_maybe_transform(
                    {
                        "bundle_method": bundle_method,
                        "certificate": certificate,
                        "geo_restrictions": geo_restrictions,
                        "policy": policy,
                        "private_key": private_key,
                    },
                    custom_certificate_edit_params.CustomCertificateEditParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomCertificateEditResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def get(
        self,
        custom_certificate_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CustomCertificateGetResponse:
        """
        SSL Configuration Details

        Args:
          zone_id: Identifier

          custom_certificate_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not custom_certificate_id:
            raise ValueError(
                f"Expected a non-empty value for `custom_certificate_id` but received {custom_certificate_id!r}"
            )
        return cast(
            CustomCertificateGetResponse,
            await self._get(
                f"/zones/{zone_id}/custom_certificates/{custom_certificate_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CustomCertificateGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CustomCertificatesWithRawResponse:
    def __init__(self, custom_certificates: CustomCertificates) -> None:
        self._custom_certificates = custom_certificates

        self.create = to_raw_response_wrapper(
            custom_certificates.create,
        )
        self.list = to_raw_response_wrapper(
            custom_certificates.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_certificates.delete,
        )
        self.edit = to_raw_response_wrapper(
            custom_certificates.edit,
        )
        self.get = to_raw_response_wrapper(
            custom_certificates.get,
        )

    @cached_property
    def prioritize(self) -> PrioritizeWithRawResponse:
        return PrioritizeWithRawResponse(self._custom_certificates.prioritize)


class AsyncCustomCertificatesWithRawResponse:
    def __init__(self, custom_certificates: AsyncCustomCertificates) -> None:
        self._custom_certificates = custom_certificates

        self.create = async_to_raw_response_wrapper(
            custom_certificates.create,
        )
        self.list = async_to_raw_response_wrapper(
            custom_certificates.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_certificates.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            custom_certificates.edit,
        )
        self.get = async_to_raw_response_wrapper(
            custom_certificates.get,
        )

    @cached_property
    def prioritize(self) -> AsyncPrioritizeWithRawResponse:
        return AsyncPrioritizeWithRawResponse(self._custom_certificates.prioritize)


class CustomCertificatesWithStreamingResponse:
    def __init__(self, custom_certificates: CustomCertificates) -> None:
        self._custom_certificates = custom_certificates

        self.create = to_streamed_response_wrapper(
            custom_certificates.create,
        )
        self.list = to_streamed_response_wrapper(
            custom_certificates.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_certificates.delete,
        )
        self.edit = to_streamed_response_wrapper(
            custom_certificates.edit,
        )
        self.get = to_streamed_response_wrapper(
            custom_certificates.get,
        )

    @cached_property
    def prioritize(self) -> PrioritizeWithStreamingResponse:
        return PrioritizeWithStreamingResponse(self._custom_certificates.prioritize)


class AsyncCustomCertificatesWithStreamingResponse:
    def __init__(self, custom_certificates: AsyncCustomCertificates) -> None:
        self._custom_certificates = custom_certificates

        self.create = async_to_streamed_response_wrapper(
            custom_certificates.create,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_certificates.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_certificates.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            custom_certificates.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            custom_certificates.get,
        )

    @cached_property
    def prioritize(self) -> AsyncPrioritizeWithStreamingResponse:
        return AsyncPrioritizeWithStreamingResponse(self._custom_certificates.prioritize)
