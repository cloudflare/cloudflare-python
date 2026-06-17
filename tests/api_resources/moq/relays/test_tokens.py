# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.moq.relays import TokenRotateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_rotate(self, client: Cloudflare) -> None:
        token = client.moq.relays.tokens.rotate(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="publish_subscribe",
        )
        assert_matches_type(Optional[TokenRotateResponse], token, path=["response"])

    @parametrize
    def test_raw_response_rotate(self, client: Cloudflare) -> None:
        response = client.moq.relays.tokens.with_raw_response.rotate(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="publish_subscribe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(Optional[TokenRotateResponse], token, path=["response"])

    @parametrize
    def test_streaming_response_rotate(self, client: Cloudflare) -> None:
        with client.moq.relays.tokens.with_streaming_response.rotate(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="publish_subscribe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(Optional[TokenRotateResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rotate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.moq.relays.tokens.with_raw_response.rotate(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
                type="publish_subscribe",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            client.moq.relays.tokens.with_raw_response.rotate(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="publish_subscribe",
            )


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_rotate(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.moq.relays.tokens.rotate(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="publish_subscribe",
        )
        assert_matches_type(Optional[TokenRotateResponse], token, path=["response"])

    @parametrize
    async def test_raw_response_rotate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.moq.relays.tokens.with_raw_response.rotate(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="publish_subscribe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(Optional[TokenRotateResponse], token, path=["response"])

    @parametrize
    async def test_streaming_response_rotate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.moq.relays.tokens.with_streaming_response.rotate(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            type="publish_subscribe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(Optional[TokenRotateResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rotate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.moq.relays.tokens.with_raw_response.rotate(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
                type="publish_subscribe",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            await async_client.moq.relays.tokens.with_raw_response.rotate(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                type="publish_subscribe",
            )
