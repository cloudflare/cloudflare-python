# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one import BinaryStorageCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBinaryStorage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        binary_storage = client.cloudforce_one.binary_storage.create(
            account_id="account_id",
            file=b"raw file contents",
        )
        assert_matches_type(BinaryStorageCreateResponse, binary_storage, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.binary_storage.with_raw_response.create(
            account_id="account_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binary_storage = response.parse()
        assert_matches_type(BinaryStorageCreateResponse, binary_storage, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.cloudforce_one.binary_storage.with_streaming_response.create(
            account_id="account_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binary_storage = response.parse()
            assert_matches_type(BinaryStorageCreateResponse, binary_storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.binary_storage.with_raw_response.create(
                account_id="",
                file=b"raw file contents",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        binary_storage = client.cloudforce_one.binary_storage.get(
            hash="hash",
            account_id="account_id",
        )
        assert binary_storage is None

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.binary_storage.with_raw_response.get(
            hash="hash",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binary_storage = response.parse()
        assert binary_storage is None

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.cloudforce_one.binary_storage.with_streaming_response.get(
            hash="hash",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binary_storage = response.parse()
            assert binary_storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.binary_storage.with_raw_response.get(
                hash="hash",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            client.cloudforce_one.binary_storage.with_raw_response.get(
                hash="",
                account_id="account_id",
            )


class TestAsyncBinaryStorage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        binary_storage = await async_client.cloudforce_one.binary_storage.create(
            account_id="account_id",
            file=b"raw file contents",
        )
        assert_matches_type(BinaryStorageCreateResponse, binary_storage, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.binary_storage.with_raw_response.create(
            account_id="account_id",
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binary_storage = await response.parse()
        assert_matches_type(BinaryStorageCreateResponse, binary_storage, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.binary_storage.with_streaming_response.create(
            account_id="account_id",
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binary_storage = await response.parse()
            assert_matches_type(BinaryStorageCreateResponse, binary_storage, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.binary_storage.with_raw_response.create(
                account_id="",
                file=b"raw file contents",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        binary_storage = await async_client.cloudforce_one.binary_storage.get(
            hash="hash",
            account_id="account_id",
        )
        assert binary_storage is None

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.binary_storage.with_raw_response.get(
            hash="hash",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        binary_storage = await response.parse()
        assert binary_storage is None

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.binary_storage.with_streaming_response.get(
            hash="hash",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            binary_storage = await response.parse()
            assert binary_storage is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.binary_storage.with_raw_response.get(
                hash="hash",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hash` but received ''"):
            await async_client.cloudforce_one.binary_storage.with_raw_response.get(
                hash="",
                account_id="account_id",
            )
