# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Type, Optional, cast
from typing_extensions import Literal

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._wrappers import ResultWrapper
from .._base_client import make_request_options
from ..types.origin_post_quantum_encryption import origin_post_quantum_encryption_update_params
from ..types.origin_post_quantum_encryption.origin_post_quantum_encryption_get_response import (
    OriginPostQuantumEncryptionGetResponse,
)
from ..types.origin_post_quantum_encryption.origin_post_quantum_encryption_update_response import (
    OriginPostQuantumEncryptionUpdateResponse,
)

__all__ = ["OriginPostQuantumEncryptionResource", "AsyncOriginPostQuantumEncryptionResource"]


class OriginPostQuantumEncryptionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginPostQuantumEncryptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return OriginPostQuantumEncryptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginPostQuantumEncryptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return OriginPostQuantumEncryptionResourceWithStreamingResponse(self)

    def update(
        self,
        *,
        zone_id: str,
        value: Literal["preferred", "supported", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginPostQuantumEncryptionUpdateResponse]:
        """
        Instructs Cloudflare to use Post-Quantum (PQ) key agreement algorithms when
        connecting to your origin. Preferred instructs Cloudflare to opportunistically
        send a Post-Quantum keyshare in the first message to the origin (for fastest
        connections when the origin supports and prefers PQ), supported means that PQ
        algorithms are advertised but only used when requested by the origin, and off
        means that PQ algorithms are not advertised

        Args:
          zone_id: Identifier

          value: Value of the Origin Post Quantum Encryption Setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._put(
            f"/zones/{zone_id}/cache/origin_post_quantum_encryption",
            body=maybe_transform(
                {"value": value}, origin_post_quantum_encryption_update_params.OriginPostQuantumEncryptionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginPostQuantumEncryptionUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginPostQuantumEncryptionUpdateResponse]],
                ResultWrapper[OriginPostQuantumEncryptionUpdateResponse],
            ),
        )

    def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginPostQuantumEncryptionGetResponse]:
        """
        Instructs Cloudflare to use Post-Quantum (PQ) key agreement algorithms when
        connecting to your origin. Preferred instructs Cloudflare to opportunistically
        send a Post-Quantum keyshare in the first message to the origin (for fastest
        connections when the origin supports and prefers PQ), supported means that PQ
        algorithms are advertised but only used when requested by the origin, and off
        means that PQ algorithms are not advertised

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return self._get(
            f"/zones/{zone_id}/cache/origin_post_quantum_encryption",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginPostQuantumEncryptionGetResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginPostQuantumEncryptionGetResponse]],
                ResultWrapper[OriginPostQuantumEncryptionGetResponse],
            ),
        )


class AsyncOriginPostQuantumEncryptionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginPostQuantumEncryptionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOriginPostQuantumEncryptionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginPostQuantumEncryptionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/cloudflare/cloudflare-python#with_streaming_response
        """
        return AsyncOriginPostQuantumEncryptionResourceWithStreamingResponse(self)

    async def update(
        self,
        *,
        zone_id: str,
        value: Literal["preferred", "supported", "off"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginPostQuantumEncryptionUpdateResponse]:
        """
        Instructs Cloudflare to use Post-Quantum (PQ) key agreement algorithms when
        connecting to your origin. Preferred instructs Cloudflare to opportunistically
        send a Post-Quantum keyshare in the first message to the origin (for fastest
        connections when the origin supports and prefers PQ), supported means that PQ
        algorithms are advertised but only used when requested by the origin, and off
        means that PQ algorithms are not advertised

        Args:
          zone_id: Identifier

          value: Value of the Origin Post Quantum Encryption Setting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._put(
            f"/zones/{zone_id}/cache/origin_post_quantum_encryption",
            body=await async_maybe_transform(
                {"value": value}, origin_post_quantum_encryption_update_params.OriginPostQuantumEncryptionUpdateParams
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginPostQuantumEncryptionUpdateResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginPostQuantumEncryptionUpdateResponse]],
                ResultWrapper[OriginPostQuantumEncryptionUpdateResponse],
            ),
        )

    async def get(
        self,
        *,
        zone_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> Optional[OriginPostQuantumEncryptionGetResponse]:
        """
        Instructs Cloudflare to use Post-Quantum (PQ) key agreement algorithms when
        connecting to your origin. Preferred instructs Cloudflare to opportunistically
        send a Post-Quantum keyshare in the first message to the origin (for fastest
        connections when the origin supports and prefers PQ), supported means that PQ
        algorithms are advertised but only used when requested by the origin, and off
        means that PQ algorithms are not advertised

        Args:
          zone_id: Identifier

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not zone_id:
            raise ValueError(f"Expected a non-empty value for `zone_id` but received {zone_id!r}")
        return await self._get(
            f"/zones/{zone_id}/cache/origin_post_quantum_encryption",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                post_parser=ResultWrapper[Optional[OriginPostQuantumEncryptionGetResponse]]._unwrapper,
            ),
            cast_to=cast(
                Type[Optional[OriginPostQuantumEncryptionGetResponse]],
                ResultWrapper[OriginPostQuantumEncryptionGetResponse],
            ),
        )


class OriginPostQuantumEncryptionResourceWithRawResponse:
    def __init__(self, origin_post_quantum_encryption: OriginPostQuantumEncryptionResource) -> None:
        self._origin_post_quantum_encryption = origin_post_quantum_encryption

        self.update = to_raw_response_wrapper(
            origin_post_quantum_encryption.update,
        )
        self.get = to_raw_response_wrapper(
            origin_post_quantum_encryption.get,
        )


class AsyncOriginPostQuantumEncryptionResourceWithRawResponse:
    def __init__(self, origin_post_quantum_encryption: AsyncOriginPostQuantumEncryptionResource) -> None:
        self._origin_post_quantum_encryption = origin_post_quantum_encryption

        self.update = async_to_raw_response_wrapper(
            origin_post_quantum_encryption.update,
        )
        self.get = async_to_raw_response_wrapper(
            origin_post_quantum_encryption.get,
        )


class OriginPostQuantumEncryptionResourceWithStreamingResponse:
    def __init__(self, origin_post_quantum_encryption: OriginPostQuantumEncryptionResource) -> None:
        self._origin_post_quantum_encryption = origin_post_quantum_encryption

        self.update = to_streamed_response_wrapper(
            origin_post_quantum_encryption.update,
        )
        self.get = to_streamed_response_wrapper(
            origin_post_quantum_encryption.get,
        )


class AsyncOriginPostQuantumEncryptionResourceWithStreamingResponse:
    def __init__(self, origin_post_quantum_encryption: AsyncOriginPostQuantumEncryptionResource) -> None:
        self._origin_post_quantum_encryption = origin_post_quantum_encryption

        self.update = async_to_streamed_response_wrapper(
            origin_post_quantum_encryption.update,
        )
        self.get = async_to_streamed_response_wrapper(
            origin_post_quantum_encryption.get,
        )
