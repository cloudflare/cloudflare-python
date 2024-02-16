# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.stream import (
    KeyDeleteResponse,
    KeyStreamSigningKeysListSigningKeysResponse,
    KeyStreamSigningKeysCreateSigningKeysResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        key = client.stream.keys.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(KeyDeleteResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.stream.keys.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyDeleteResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.stream.keys.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyDeleteResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.keys.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.stream.keys.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_signing_keys_create_signing_keys(self, client: Cloudflare) -> None:
        key = client.stream.keys.stream_signing_keys_create_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(KeyStreamSigningKeysCreateSigningKeysResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_signing_keys_create_signing_keys(self, client: Cloudflare) -> None:
        response = client.stream.keys.with_raw_response.stream_signing_keys_create_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyStreamSigningKeysCreateSigningKeysResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_signing_keys_create_signing_keys(self, client: Cloudflare) -> None:
        with client.stream.keys.with_streaming_response.stream_signing_keys_create_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyStreamSigningKeysCreateSigningKeysResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_signing_keys_create_signing_keys(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.keys.with_raw_response.stream_signing_keys_create_signing_keys(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_stream_signing_keys_list_signing_keys(self, client: Cloudflare) -> None:
        key = client.stream.keys.stream_signing_keys_list_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(KeyStreamSigningKeysListSigningKeysResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_stream_signing_keys_list_signing_keys(self, client: Cloudflare) -> None:
        response = client.stream.keys.with_raw_response.stream_signing_keys_list_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(KeyStreamSigningKeysListSigningKeysResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_stream_signing_keys_list_signing_keys(self, client: Cloudflare) -> None:
        with client.stream.keys.with_streaming_response.stream_signing_keys_list_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(KeyStreamSigningKeysListSigningKeysResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_stream_signing_keys_list_signing_keys(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.stream.keys.with_raw_response.stream_signing_keys_list_signing_keys(
                "",
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        key = await async_client.stream.keys.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(KeyDeleteResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.keys.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyDeleteResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.stream.keys.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyDeleteResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.keys.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.stream.keys.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_signing_keys_create_signing_keys(self, async_client: AsyncCloudflare) -> None:
        key = await async_client.stream.keys.stream_signing_keys_create_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(KeyStreamSigningKeysCreateSigningKeysResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_signing_keys_create_signing_keys(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.keys.with_raw_response.stream_signing_keys_create_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyStreamSigningKeysCreateSigningKeysResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_signing_keys_create_signing_keys(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.keys.with_streaming_response.stream_signing_keys_create_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyStreamSigningKeysCreateSigningKeysResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_signing_keys_create_signing_keys(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.keys.with_raw_response.stream_signing_keys_create_signing_keys(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_stream_signing_keys_list_signing_keys(self, async_client: AsyncCloudflare) -> None:
        key = await async_client.stream.keys.stream_signing_keys_list_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(KeyStreamSigningKeysListSigningKeysResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_stream_signing_keys_list_signing_keys(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.stream.keys.with_raw_response.stream_signing_keys_list_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(KeyStreamSigningKeysListSigningKeysResponse, key, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_stream_signing_keys_list_signing_keys(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.stream.keys.with_streaming_response.stream_signing_keys_list_signing_keys(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(KeyStreamSigningKeysListSigningKeysResponse, key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_stream_signing_keys_list_signing_keys(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.stream.keys.with_raw_response.stream_signing_keys_list_signing_keys(
                "",
            )
