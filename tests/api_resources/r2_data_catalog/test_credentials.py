# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        credential = client.r2_data_catalog.credentials.create(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
            token="your-cloudflare-api-token-here",
        )
        assert_matches_type(object, credential, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.r2_data_catalog.credentials.with_raw_response.create(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
            token="your-cloudflare-api-token-here",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = response.parse()
        assert_matches_type(object, credential, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.r2_data_catalog.credentials.with_streaming_response.create(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
            token="your-cloudflare-api-token-here",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = response.parse()
            assert_matches_type(object, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.r2_data_catalog.credentials.with_raw_response.create(
                bucket_name="my-data-bucket",
                account_id="",
                token="your-cloudflare-api-token-here",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            client.r2_data_catalog.credentials.with_raw_response.create(
                bucket_name="",
                account_id="0123456789abcdef0123456789abcdef",
                token="your-cloudflare-api-token-here",
            )


class TestAsyncCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        credential = await async_client.r2_data_catalog.credentials.create(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
            token="your-cloudflare-api-token-here",
        )
        assert_matches_type(object, credential, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.r2_data_catalog.credentials.with_raw_response.create(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
            token="your-cloudflare-api-token-here",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        credential = await response.parse()
        assert_matches_type(object, credential, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.r2_data_catalog.credentials.with_streaming_response.create(
            bucket_name="my-data-bucket",
            account_id="0123456789abcdef0123456789abcdef",
            token="your-cloudflare-api-token-here",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            credential = await response.parse()
            assert_matches_type(object, credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.r2_data_catalog.credentials.with_raw_response.create(
                bucket_name="my-data-bucket",
                account_id="",
                token="your-cloudflare-api-token-here",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bucket_name` but received ''"):
            await async_client.r2_data_catalog.credentials.with_raw_response.create(
                bucket_name="",
                account_id="0123456789abcdef0123456789abcdef",
                token="your-cloudflare-api-token-here",
            )
