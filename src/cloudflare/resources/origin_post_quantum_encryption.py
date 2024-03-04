# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal

import httpx

from ..types import (
    OriginPostQuantumEncryptionGetResponse,
    OriginPostQuantumEncryptionUpdateResponse,
    origin_post_quantum_encryption_update_params,
)
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
from .._base_client import (
    make_request_options,
)

__all__ = ["OriginPostQuantumEncryption", "AsyncOriginPostQuantumEncryption"]


class OriginPostQuantumEncryption(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginPostQuantumEncryptionWithRawResponse:
        return OriginPostQuantumEncryptionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginPostQuantumEncryptionWithStreamingResponse:
        return OriginPostQuantumEncryptionWithStreamingResponse(self)

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
    ) -> OriginPostQuantumEncryptionUpdateResponse:
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
        return cast(
            OriginPostQuantumEncryptionUpdateResponse,
            self._put(
                f"/zones/{zone_id}/cache/origin_post_quantum_encryption",
                body=maybe_transform(
                    {"value": value},
                    origin_post_quantum_encryption_update_params.OriginPostQuantumEncryptionUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginPostQuantumEncryptionUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> OriginPostQuantumEncryptionGetResponse:
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
        return cast(
            OriginPostQuantumEncryptionGetResponse,
            self._get(
                f"/zones/{zone_id}/cache/origin_post_quantum_encryption",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginPostQuantumEncryptionGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncOriginPostQuantumEncryption(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginPostQuantumEncryptionWithRawResponse:
        return AsyncOriginPostQuantumEncryptionWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginPostQuantumEncryptionWithStreamingResponse:
        return AsyncOriginPostQuantumEncryptionWithStreamingResponse(self)

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
    ) -> OriginPostQuantumEncryptionUpdateResponse:
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
        return cast(
            OriginPostQuantumEncryptionUpdateResponse,
            await self._put(
                f"/zones/{zone_id}/cache/origin_post_quantum_encryption",
                body=await async_maybe_transform(
                    {"value": value},
                    origin_post_quantum_encryption_update_params.OriginPostQuantumEncryptionUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginPostQuantumEncryptionUpdateResponse]
                ),  # Union types cannot be passed in as arguments in the type system
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
    ) -> OriginPostQuantumEncryptionGetResponse:
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
        return cast(
            OriginPostQuantumEncryptionGetResponse,
            await self._get(
                f"/zones/{zone_id}/cache/origin_post_quantum_encryption",
                options=make_request_options(
                    extra_headers=extra_headers,
                    extra_query=extra_query,
                    extra_body=extra_body,
                    timeout=timeout,
                    post_parser=ResultWrapper._unwrapper,
                ),
                cast_to=cast(
                    Any, ResultWrapper[OriginPostQuantumEncryptionGetResponse]
                ),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class OriginPostQuantumEncryptionWithRawResponse:
    def __init__(self, origin_post_quantum_encryption: OriginPostQuantumEncryption) -> None:
        self._origin_post_quantum_encryption = origin_post_quantum_encryption

        self.update = to_raw_response_wrapper(
            origin_post_quantum_encryption.update,
        )
        self.get = to_raw_response_wrapper(
            origin_post_quantum_encryption.get,
        )


class AsyncOriginPostQuantumEncryptionWithRawResponse:
    def __init__(self, origin_post_quantum_encryption: AsyncOriginPostQuantumEncryption) -> None:
        self._origin_post_quantum_encryption = origin_post_quantum_encryption

        self.update = async_to_raw_response_wrapper(
            origin_post_quantum_encryption.update,
        )
        self.get = async_to_raw_response_wrapper(
            origin_post_quantum_encryption.get,
        )


class OriginPostQuantumEncryptionWithStreamingResponse:
    def __init__(self, origin_post_quantum_encryption: OriginPostQuantumEncryption) -> None:
        self._origin_post_quantum_encryption = origin_post_quantum_encryption

        self.update = to_streamed_response_wrapper(
            origin_post_quantum_encryption.update,
        )
        self.get = to_streamed_response_wrapper(
            origin_post_quantum_encryption.get,
        )


class AsyncOriginPostQuantumEncryptionWithStreamingResponse:
    def __init__(self, origin_post_quantum_encryption: AsyncOriginPostQuantumEncryption) -> None:
        self._origin_post_quantum_encryption = origin_post_quantum_encryption

        self.update = async_to_streamed_response_wrapper(
            origin_post_quantum_encryption.update,
        )
        self.get = async_to_streamed_response_wrapper(
            origin_post_quantum_encryption.get,
        )
