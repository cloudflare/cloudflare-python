# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Type, Optional, cast
from typing_extensions import Literal

import httpx

from .quota import (
    QuotaResource,
    AsyncQuotaResource,
    QuotaResourceWithRawResponse,
    AsyncQuotaResourceWithRawResponse,
    QuotaResourceWithStreamingResponse,
    AsyncQuotaResourceWithStreamingResponse,
)
from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
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
from ....types.ssl import certificate_pack_edit_params, certificate_pack_list_params, certificate_pack_create_params
from ....pagination import SyncSinglePage, AsyncSinglePage
from ...._base_client import AsyncPaginator, make_request_options
from ....types.ssl.host import Host
from ....types.ssl.certificate_pack_edit_response import CertificatePackEditResponse
from ....types.ssl.certificate_pack_create_response import CertificatePackCreateResponse
from ....types.ssl.certificate_pack_delete_response import CertificatePackDeleteResponse

__all__ = ["CertificatePacksResource", "AsyncCertificatePacksResource"]


class CertificatePacksResource(SyncAPIResource):
    @cached_property
    def quota(self) -> QuotaResource:
        return QuotaResource(self._client)

    @cached_property
    def with_raw_response(self) -> CertificatePacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return CertificatePacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatePacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return CertificatePacksResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        zone_id: str,
        certificate_authority: Literal["google", "lets_encrypt", "ssl_com"],
        hosts: List[Host],
        type: Literal["advanced"],
        validation_method: Literal["txt", "http", "email"],
        validity_days: Literal[14, 30, 90, 365],
        cloudflare_branding: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificatePackCreateResponse]:
        """
        For a given zone, order an advanced certificate pack.

        Args:
          zone_id: Identifier

          certificate_authority: Certificate Authority selected for the order. For information on any certificate
              authority specific details or restrictions
              [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities)

          hosts: Comma separated list of valid host names for the certificate packs. Must contain
              the zone apex, may not contain more than 50 hosts, and may not be empty.

          type: Type of certificate pack.

          validation_method: Validation Method selected for the order.

          validity_days: Validity Days selected for the order.

          cloudflare_branding: Whether or not to add Cloudflare Branding for the order. This will add a
              subdomain of sni.cloudflaressl.com as the Common Name if set to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._post(
            f"/zones/{zone_id}/ssl/certificate_packs/order",
            body=maybe_transform(
                {
                    "certificate_authority": certificate_authority,
                    "hosts": hosts,
                    "type": type,
                    "validation_method": validation_method,
                    "validity_days": validity_days,
                    "cloudflare_branding": cloudflare_branding,
                },
                certificate_pack_create_params.CertificatePackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CertificatePackCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificatePackCreateResponse]], ResultWrapper[CertificatePackCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        status: Literal["all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SyncSinglePage[object]:
        """
        For a given zone, list all active certificate packs.

        Args:
          zone_id: Identifier

          status: Include Certificate Packs of all statuses, not just active ones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/ssl/certificate_packs",
            page=SyncSinglePage[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, certificate_pack_list_params.CertificatePackListParams),
            ),
            model=object,
        )

    def delete(
        self,
        certificate_pack_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificatePackDeleteResponse]:
        """
        For a given zone, delete an advanced certificate pack.

        Args:
          zone_id: Identifier

          certificate_pack_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        return self._delete(
            f"/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CertificatePackDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificatePackDeleteResponse]], ResultWrapper[CertificatePackDeleteResponse]),
        )

    def edit(
        self,
        certificate_pack_id: str,
        *,
        zone_id: str,
        cloudflare_branding: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificatePackEditResponse]:
        """
        For a given zone, restart validation or add cloudflare branding for an advanced
        certificate pack. The former is only a validation operation for a Certificate
        Pack in a validation_timed_out status.

        Args:
          zone_id: Identifier

          certificate_pack_id: Identifier

          cloudflare_branding: Whether or not to add Cloudflare Branding for the order. This will add a
              subdomain of sni.cloudflaressl.com as the Common Name if set to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        return self._patch(
            f"/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}",
            body=maybe_transform(
                {"cloudflare_branding": cloudflare_branding}, certificate_pack_edit_params.CertificatePackEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CertificatePackEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificatePackEditResponse]], ResultWrapper[CertificatePackEditResponse]),
        )

    def get(
        self,
        certificate_pack_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        For a given zone, get a certificate pack.

        Args:
          zone_id: Identifier

          certificate_pack_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        return self._get(
            f"/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class AsyncCertificatePacksResource(AsyncAPIResource):
    @cached_property
    def quota(self) -> AsyncQuotaResource:
        return AsyncQuotaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCertificatePacksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCertificatePacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatePacksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncCertificatePacksResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        zone_id: str,
        certificate_authority: Literal["google", "lets_encrypt", "ssl_com"],
        hosts: List[Host],
        type: Literal["advanced"],
        validation_method: Literal["txt", "http", "email"],
        validity_days: Literal[14, 30, 90, 365],
        cloudflare_branding: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificatePackCreateResponse]:
        """
        For a given zone, order an advanced certificate pack.

        Args:
          zone_id: Identifier

          certificate_authority: Certificate Authority selected for the order. For information on any certificate
              authority specific details or restrictions
              [see this page for more details.](https://developers.cloudflare.com/ssl/reference/certificate-authorities)

          hosts: Comma separated list of valid host names for the certificate packs. Must contain
              the zone apex, may not contain more than 50 hosts, and may not be empty.

          type: Type of certificate pack.

          validation_method: Validation Method selected for the order.

          validity_days: Validity Days selected for the order.

          cloudflare_branding: Whether or not to add Cloudflare Branding for the order. This will add a
              subdomain of sni.cloudflaressl.com as the Common Name if set to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._post(
            f"/zones/{zone_id}/ssl/certificate_packs/order",
            body=await async_maybe_transform(
                {
                    "certificate_authority": certificate_authority,
                    "hosts": hosts,
                    "type": type,
                    "validation_method": validation_method,
                    "validity_days": validity_days,
                    "cloudflare_branding": cloudflare_branding,
                },
                certificate_pack_create_params.CertificatePackCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CertificatePackCreateResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificatePackCreateResponse]], ResultWrapper[CertificatePackCreateResponse]),
        )

    def list(
        self,
        *,
        zone_id: str,
        status: Literal["all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AsyncPaginator[object, AsyncSinglePage[object]]:
        """
        For a given zone, list all active certificate packs.

        Args:
          zone_id: Identifier

          status: Include Certificate Packs of all statuses, not just active ones.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get_api_list(
            f"/zones/{zone_id}/ssl/certificate_packs",
            page=AsyncSinglePage[object],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, certificate_pack_list_params.CertificatePackListParams),
            ),
            model=object,
        )

    async def delete(
        self,
        certificate_pack_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificatePackDeleteResponse]:
        """
        For a given zone, delete an advanced certificate pack.

        Args:
          zone_id: Identifier

          certificate_pack_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        return await self._delete(
            f"/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CertificatePackDeleteResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificatePackDeleteResponse]], ResultWrapper[CertificatePackDeleteResponse]),
        )

    async def edit(
        self,
        certificate_pack_id: str,
        *,
        zone_id: str,
        cloudflare_branding: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificatePackEditResponse]:
        """
        For a given zone, restart validation or add cloudflare branding for an advanced
        certificate pack. The former is only a validation operation for a Certificate
        Pack in a validation_timed_out status.

        Args:
          zone_id: Identifier

          certificate_pack_id: Identifier

          cloudflare_branding: Whether or not to add Cloudflare Branding for the order. This will add a
              subdomain of sni.cloudflaressl.com as the Common Name if set to true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        return await self._patch(
            f"/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}",
            body=await async_maybe_transform(
                {"cloudflare_branding": cloudflare_branding}, certificate_pack_edit_params.CertificatePackEditParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[CertificatePackEditResponse]]._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificatePackEditResponse]], ResultWrapper[CertificatePackEditResponse]),
        )

    async def get(
        self,
        certificate_pack_id: str,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """
        For a given zone, get a certificate pack.

        Args:
          zone_id: Identifier

          certificate_pack_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        if not certificate_pack_id:
            raise ValueError(
                f"Expected a non-empty value for `certificate_pack_id` but received {certificate_pack_id!r}"
            )
        return await self._get(
            f"/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[object]]._unwrapper,
            ),
            cast_to=cast(Type[object], ResultWrapper[object]),
        )


class CertificatePacksResourceWithRawResponse:
    def __init__(self, certificate_packs: CertificatePacksResource) -> None:
        self._certificate_packs = certificate_packs

        self.create = to_raw_response_wrapper(
            certificate_packs.create,
        )
        self.list = to_raw_response_wrapper(
            certificate_packs.list,
        )
        self.delete = to_raw_response_wrapper(
            certificate_packs.delete,
        )
        self.edit = to_raw_response_wrapper(
            certificate_packs.edit,
        )
        self.get = to_raw_response_wrapper(
            certificate_packs.get,
        )

    @cached_property
    def quota(self) -> QuotaResourceWithRawResponse:
        return QuotaResourceWithRawResponse(self._certificate_packs.quota)


class AsyncCertificatePacksResourceWithRawResponse:
    def __init__(self, certificate_packs: AsyncCertificatePacksResource) -> None:
        self._certificate_packs = certificate_packs

        self.create = async_to_raw_response_wrapper(
            certificate_packs.create,
        )
        self.list = async_to_raw_response_wrapper(
            certificate_packs.list,
        )
        self.delete = async_to_raw_response_wrapper(
            certificate_packs.delete,
        )
        self.edit = async_to_raw_response_wrapper(
            certificate_packs.edit,
        )
        self.get = async_to_raw_response_wrapper(
            certificate_packs.get,
        )

    @cached_property
    def quota(self) -> AsyncQuotaResourceWithRawResponse:
        return AsyncQuotaResourceWithRawResponse(self._certificate_packs.quota)


class CertificatePacksResourceWithStreamingResponse:
    def __init__(self, certificate_packs: CertificatePacksResource) -> None:
        self._certificate_packs = certificate_packs

        self.create = to_streamed_response_wrapper(
            certificate_packs.create,
        )
        self.list = to_streamed_response_wrapper(
            certificate_packs.list,
        )
        self.delete = to_streamed_response_wrapper(
            certificate_packs.delete,
        )
        self.edit = to_streamed_response_wrapper(
            certificate_packs.edit,
        )
        self.get = to_streamed_response_wrapper(
            certificate_packs.get,
        )

    @cached_property
    def quota(self) -> QuotaResourceWithStreamingResponse:
        return QuotaResourceWithStreamingResponse(self._certificate_packs.quota)


class AsyncCertificatePacksResourceWithStreamingResponse:
    def __init__(self, certificate_packs: AsyncCertificatePacksResource) -> None:
        self._certificate_packs = certificate_packs

        self.create = async_to_streamed_response_wrapper(
            certificate_packs.create,
        )
        self.list = async_to_streamed_response_wrapper(
            certificate_packs.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            certificate_packs.delete,
        )
        self.edit = async_to_streamed_response_wrapper(
            certificate_packs.edit,
        )
        self.get = async_to_streamed_response_wrapper(
            certificate_packs.get,
        )

    @cached_property
    def quota(self) -> AsyncQuotaResourceWithStreamingResponse:
        return AsyncQuotaResourceWithStreamingResponse(self._certificate_packs.quota)
