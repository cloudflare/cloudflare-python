# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, Type, Optional, cast
from typing_extensions import Literal

import httpx

from .order import (
    Order,
    AsyncOrder,
    OrderWithRawResponse,
    AsyncOrderWithRawResponse,
    OrderWithStreamingResponse,
    AsyncOrderWithStreamingResponse,
)
from .quota import (
    Quota,
    AsyncQuota,
    QuotaWithRawResponse,
    AsyncQuotaWithRawResponse,
    QuotaWithStreamingResponse,
    AsyncQuotaWithStreamingResponse,
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
from ....types.ssl import (
    CertificatePackGetResponse,
    CertificatePackEditResponse,
    CertificatePackListResponse,
    CertificatePackDeleteResponse,
    certificate_pack_list_params,
)
from ...._base_client import (
    make_request_options,
)

__all__ = ["CertificatePacks", "AsyncCertificatePacks"]


class CertificatePacks(SyncAPIResource):
    @cached_property
    def order(self) -> Order:
        return Order(self._client)

    @cached_property
    def quota(self) -> Quota:
        return Quota(self._client)

    @cached_property
    def with_raw_response(self) -> CertificatePacksWithRawResponse:
        return CertificatePacksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatePacksWithStreamingResponse:
        return CertificatePacksWithStreamingResponse(self)

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
    ) -> Optional[CertificatePackListResponse]:
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
        return self._get(
            f"/zones/{zone_id}/ssl/certificate_packs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"status": status}, certificate_pack_list_params.CertificatePackListParams),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificatePackListResponse]], ResultWrapper[CertificatePackListResponse]),
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
    ) -> CertificatePackDeleteResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CertificatePackDeleteResponse], ResultWrapper[CertificatePackDeleteResponse]),
        )

    def edit(
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
    ) -> CertificatePackEditResponse:
        """For a given zone, restart validation for an advanced certificate pack.

        This is
        only a validation operation for a Certificate Pack in a validation_timed_out
        status.

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
        return self._patch(
            f"/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CertificatePackEditResponse], ResultWrapper[CertificatePackEditResponse]),
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
    ) -> CertificatePackGetResponse:
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
        return cast(
            CertificatePackGetResponse,
            self._get(
                f"/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CertificatePackGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncCertificatePacks(AsyncAPIResource):
    @cached_property
    def order(self) -> AsyncOrder:
        return AsyncOrder(self._client)

    @cached_property
    def quota(self) -> AsyncQuota:
        return AsyncQuota(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCertificatePacksWithRawResponse:
        return AsyncCertificatePacksWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatePacksWithStreamingResponse:
        return AsyncCertificatePacksWithStreamingResponse(self)

    async def list(
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
    ) -> Optional[CertificatePackListResponse]:
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
        return await self._get(
            f"/zones/{zone_id}/ssl/certificate_packs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"status": status}, certificate_pack_list_params.CertificatePackListParams
                ),
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[Optional[CertificatePackListResponse]], ResultWrapper[CertificatePackListResponse]),
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
    ) -> CertificatePackDeleteResponse:
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
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CertificatePackDeleteResponse], ResultWrapper[CertificatePackDeleteResponse]),
        )

    async def edit(
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
    ) -> CertificatePackEditResponse:
        """For a given zone, restart validation for an advanced certificate pack.

        This is
        only a validation operation for a Certificate Pack in a validation_timed_out
        status.

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
        return await self._patch(
            f"/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper._unwrapper,
            ),
            cast_to=cast(Type[CertificatePackEditResponse], ResultWrapper[CertificatePackEditResponse]),
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
    ) -> CertificatePackGetResponse:
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
        return cast(
            CertificatePackGetResponse,
            await self._get(
                f"/zones/{zone_id}/ssl/certificate_packs/{certificate_pack_id}",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[CertificatePackGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class CertificatePacksWithRawResponse:
    def __init__(self, certificate_packs: CertificatePacks) -> None:
        self._certificate_packs = certificate_packs

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
    def order(self) -> OrderWithRawResponse:
        return OrderWithRawResponse(self._certificate_packs.order)

    @cached_property
    def quota(self) -> QuotaWithRawResponse:
        return QuotaWithRawResponse(self._certificate_packs.quota)


class AsyncCertificatePacksWithRawResponse:
    def __init__(self, certificate_packs: AsyncCertificatePacks) -> None:
        self._certificate_packs = certificate_packs

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
    def order(self) -> AsyncOrderWithRawResponse:
        return AsyncOrderWithRawResponse(self._certificate_packs.order)

    @cached_property
    def quota(self) -> AsyncQuotaWithRawResponse:
        return AsyncQuotaWithRawResponse(self._certificate_packs.quota)


class CertificatePacksWithStreamingResponse:
    def __init__(self, certificate_packs: CertificatePacks) -> None:
        self._certificate_packs = certificate_packs

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
    def order(self) -> OrderWithStreamingResponse:
        return OrderWithStreamingResponse(self._certificate_packs.order)

    @cached_property
    def quota(self) -> QuotaWithStreamingResponse:
        return QuotaWithStreamingResponse(self._certificate_packs.quota)


class AsyncCertificatePacksWithStreamingResponse:
    def __init__(self, certificate_packs: AsyncCertificatePacks) -> None:
        self._certificate_packs = certificate_packs

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
    def order(self) -> AsyncOrderWithStreamingResponse:
        return AsyncOrderWithStreamingResponse(self._certificate_packs.order)

    @cached_property
    def quota(self) -> AsyncQuotaWithStreamingResponse:
        return AsyncQuotaWithStreamingResponse(self._certificate_packs.quota)
