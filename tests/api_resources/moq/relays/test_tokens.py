# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.moq.relays import TokenListResponse, TokenCreateResponse, TokenDeleteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTokens:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        token = client.moq.relays.tokens.create(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            operations=["publish", "subscribe"],
        )
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        token = client.moq.relays.tokens.create(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            operations=["publish", "subscribe"],
            expires=parse_datetime("2027-03-27T15:00:00Z"),
            label="primary-encoder",
        )
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.moq.relays.tokens.with_raw_response.create(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            operations=["publish", "subscribe"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.moq.relays.tokens.with_streaming_response.create(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            operations=["publish", "subscribe"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.moq.relays.tokens.with_raw_response.create(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
                operations=["publish", "subscribe"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            client.moq.relays.tokens.with_raw_response.create(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                operations=["publish", "subscribe"],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        token = client.moq.relays.tokens.list(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TokenListResponse], token, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.moq.relays.tokens.with_raw_response.list(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(Optional[TokenListResponse], token, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.moq.relays.tokens.with_streaming_response.list(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(Optional[TokenListResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.moq.relays.tokens.with_raw_response.list(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            client.moq.relays.tokens.with_raw_response.list(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        token = client.moq.relays.tokens.delete(
            jti="f3a1b2c3d4e5f67890a1b2c3d4e5f678",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
        )
        assert_matches_type(TokenDeleteResponse, token, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.moq.relays.tokens.with_raw_response.delete(
            jti="f3a1b2c3d4e5f67890a1b2c3d4e5f678",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = response.parse()
        assert_matches_type(TokenDeleteResponse, token, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.moq.relays.tokens.with_streaming_response.delete(
            jti="f3a1b2c3d4e5f67890a1b2c3d4e5f678",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = response.parse()
            assert_matches_type(TokenDeleteResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.moq.relays.tokens.with_raw_response.delete(
                jti="f3a1b2c3d4e5f67890a1b2c3d4e5f678",
                account_id="",
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            client.moq.relays.tokens.with_raw_response.delete(
                jti="f3a1b2c3d4e5f67890a1b2c3d4e5f678",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                relay_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `jti` but received ''"):
            client.moq.relays.tokens.with_raw_response.delete(
                jti="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            )


class TestAsyncTokens:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.moq.relays.tokens.create(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            operations=["publish", "subscribe"],
        )
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.moq.relays.tokens.create(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            operations=["publish", "subscribe"],
            expires=parse_datetime("2027-03-27T15:00:00Z"),
            label="primary-encoder",
        )
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.moq.relays.tokens.with_raw_response.create(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            operations=["publish", "subscribe"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.moq.relays.tokens.with_streaming_response.create(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            operations=["publish", "subscribe"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(Optional[TokenCreateResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.moq.relays.tokens.with_raw_response.create(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
                operations=["publish", "subscribe"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            await async_client.moq.relays.tokens.with_raw_response.create(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                operations=["publish", "subscribe"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.moq.relays.tokens.list(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[TokenListResponse], token, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.moq.relays.tokens.with_raw_response.list(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(Optional[TokenListResponse], token, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.moq.relays.tokens.with_streaming_response.list(
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(Optional[TokenListResponse], token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.moq.relays.tokens.with_raw_response.list(
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            await async_client.moq.relays.tokens.with_raw_response.list(
                relay_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        token = await async_client.moq.relays.tokens.delete(
            jti="f3a1b2c3d4e5f67890a1b2c3d4e5f678",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
        )
        assert_matches_type(TokenDeleteResponse, token, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.moq.relays.tokens.with_raw_response.delete(
            jti="f3a1b2c3d4e5f67890a1b2c3d4e5f678",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        token = await response.parse()
        assert_matches_type(TokenDeleteResponse, token, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.moq.relays.tokens.with_streaming_response.delete(
            jti="f3a1b2c3d4e5f67890a1b2c3d4e5f678",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            token = await response.parse()
            assert_matches_type(TokenDeleteResponse, token, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.moq.relays.tokens.with_raw_response.delete(
                jti="f3a1b2c3d4e5f67890a1b2c3d4e5f678",
                account_id="",
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `relay_id` but received ''"):
            await async_client.moq.relays.tokens.with_raw_response.delete(
                jti="f3a1b2c3d4e5f67890a1b2c3d4e5f678",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                relay_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `jti` but received ''"):
            await async_client.moq.relays.tokens.with_raw_response.delete(
                jti="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                relay_id="a1b2c3d4e5f67890a1b2c3d4e5f67890",
            )
