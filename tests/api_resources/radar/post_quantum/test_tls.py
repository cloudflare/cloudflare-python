# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.post_quantum import TLSSupportResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTLS:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_support(self, client: Cloudflare) -> None:
        tls = client.radar.post_quantum.tls.support(
            host="cloudflare.com",
        )
        assert_matches_type(TLSSupportResponse, tls, path=["response"])

    @parametrize
    def test_raw_response_support(self, client: Cloudflare) -> None:
        response = client.radar.post_quantum.tls.with_raw_response.support(
            host="cloudflare.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tls = response.parse()
        assert_matches_type(TLSSupportResponse, tls, path=["response"])

    @parametrize
    def test_streaming_response_support(self, client: Cloudflare) -> None:
        with client.radar.post_quantum.tls.with_streaming_response.support(
            host="cloudflare.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tls = response.parse()
            assert_matches_type(TLSSupportResponse, tls, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTLS:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_support(self, async_client: AsyncCloudflare) -> None:
        tls = await async_client.radar.post_quantum.tls.support(
            host="cloudflare.com",
        )
        assert_matches_type(TLSSupportResponse, tls, path=["response"])

    @parametrize
    async def test_raw_response_support(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.post_quantum.tls.with_raw_response.support(
            host="cloudflare.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        tls = await response.parse()
        assert_matches_type(TLSSupportResponse, tls, path=["response"])

    @parametrize
    async def test_streaming_response_support(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.post_quantum.tls.with_streaming_response.support(
            host="cloudflare.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            tls = await response.parse()
            assert_matches_type(TLSSupportResponse, tls, path=["response"])

        assert cast(Any, response.is_closed) is True
