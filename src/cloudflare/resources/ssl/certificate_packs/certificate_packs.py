# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .order import OrderResource, AsyncOrderResource

from ...._compat import cached_property

from .quota import QuotaResource, AsyncQuotaResource

from ....pagination import SyncSinglePage, AsyncSinglePage

from ...._utils import maybe_transform, async_maybe_transform

from ...._base_client import make_request_options, AsyncPaginator

from typing_extensions import Literal

from ....types.ssl.certificate_pack_delete_response import CertificatePackDeleteResponse

from ...._wrappers import ResultWrapper

from typing import Optional, Type

from ....types.ssl.certificate_pack_edit_response import CertificatePackEditResponse

from ...._response import (
    to_raw_response_wrapper,
    async_to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_streamed_response_wrapper,
)

import warnings
from typing import TYPE_CHECKING, Optional, Union, List, Dict, Any, Mapping, cast, overload
from typing_extensions import Literal
from ...._utils import extract_files, maybe_transform, required_args, deepcopy_minimal, strip_not_given
from ...._types import NotGiven, Timeout, Headers, NoneType, Query, Body, NOT_GIVEN, FileTypes, BinaryResponseContent
from ...._resource import SyncAPIResource, AsyncAPIResource
from ....types import shared_params
from ....types.ssl import certificate_pack_list_params
from ....types.ssl import certificate_pack_edit_params
from .order import (
    OrderResource,
    AsyncOrderResource,
    OrderResourceWithRawResponse,
    AsyncOrderResourceWithRawResponse,
    OrderResourceWithStreamingResponse,
    AsyncOrderResourceWithStreamingResponse,
)
from .quota import (
    QuotaResource,
    AsyncQuotaResource,
    QuotaResourceWithRawResponse,
    AsyncQuotaResourceWithRawResponse,
    QuotaResourceWithStreamingResponse,
    AsyncQuotaResourceWithStreamingResponse,
)
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast
from typing import cast

__all__ = ["CertificatePacksResource", "AsyncCertificatePacksResource"]


class CertificatePacksResource(SyncAPIResource):
    @cached_property
    def order(self) -> OrderResource:
        return OrderResource(self._client)

    @cached_property
    def quota(self) -> QuotaResource:
        return QuotaResource(self._client)

    @cached_property
    def with_raw_response(self) -> CertificatePacksResourceWithRawResponse:
        return CertificatePacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CertificatePacksResourceWithStreamingResponse:
        return CertificatePacksResourceWithStreamingResponse(self)

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
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificatePackEditResponse]:
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
            body=maybe_transform(body, certificate_pack_edit_params.CertificatePackEditParams),
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
    def order(self) -> AsyncOrderResource:
        return AsyncOrderResource(self._client)

    @cached_property
    def quota(self) -> AsyncQuotaResource:
        return AsyncQuotaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCertificatePacksResourceWithRawResponse:
        return AsyncCertificatePacksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCertificatePacksResourceWithStreamingResponse:
        return AsyncCertificatePacksResourceWithStreamingResponse(self)

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
        body: object,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[CertificatePackEditResponse]:
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
            body=await async_maybe_transform(body, certificate_pack_edit_params.CertificatePackEditParams),
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
    def order(self) -> OrderResourceWithRawResponse:
        return OrderResourceWithRawResponse(self._certificate_packs.order)

    @cached_property
    def quota(self) -> QuotaResourceWithRawResponse:
        return QuotaResourceWithRawResponse(self._certificate_packs.quota)


class AsyncCertificatePacksResourceWithRawResponse:
    def __init__(self, certificate_packs: AsyncCertificatePacksResource) -> None:
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
    def order(self) -> AsyncOrderResourceWithRawResponse:
        return AsyncOrderResourceWithRawResponse(self._certificate_packs.order)

    @cached_property
    def quota(self) -> AsyncQuotaResourceWithRawResponse:
        return AsyncQuotaResourceWithRawResponse(self._certificate_packs.quota)


class CertificatePacksResourceWithStreamingResponse:
    def __init__(self, certificate_packs: CertificatePacksResource) -> None:
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
    def order(self) -> OrderResourceWithStreamingResponse:
        return OrderResourceWithStreamingResponse(self._certificate_packs.order)

    @cached_property
    def quota(self) -> QuotaResourceWithStreamingResponse:
        return QuotaResourceWithStreamingResponse(self._certificate_packs.quota)


class AsyncCertificatePacksResourceWithStreamingResponse:
    def __init__(self, certificate_packs: AsyncCertificatePacksResource) -> None:
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
    def order(self) -> AsyncOrderResourceWithStreamingResponse:
        return AsyncOrderResourceWithStreamingResponse(self._certificate_packs.order)

    @cached_property
    def quota(self) -> AsyncQuotaResourceWithStreamingResponse:
        return AsyncQuotaResourceWithStreamingResponse(self._certificate_packs.quota)
