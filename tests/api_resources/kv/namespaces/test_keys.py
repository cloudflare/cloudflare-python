# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncCursorLimitPagination, AsyncCursorLimitPagination
from cloudflare.types.kv.namespaces import Key

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKeys:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        key = client.kv.namespaces.keys.list(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncCursorLimitPagination[Key], key, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        key = client.kv.namespaces.keys.list(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="6Ck1la0VxJ0djhidm1MdX2FyDGxLKVeeHZZmORS_8XeSuhz9SjIJRaSa2lnsF01tQOHrfTGAP3R5X1Kv5iVUuMbNKhWNAXHOl6ePB0TUL8nw",
            limit=10,
            prefix="My-Prefix",
        )
        assert_matches_type(SyncCursorLimitPagination[Key], key, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.keys.with_raw_response.list(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = response.parse()
        assert_matches_type(SyncCursorLimitPagination[Key], key, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.kv.namespaces.keys.with_streaming_response.list(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = response.parse()
            assert_matches_type(SyncCursorLimitPagination[Key], key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.keys.with_raw_response.list(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.keys.with_raw_response.list(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncKeys:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        key = await async_client.kv.namespaces.keys.list(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncCursorLimitPagination[Key], key, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        key = await async_client.kv.namespaces.keys.list(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            cursor="6Ck1la0VxJ0djhidm1MdX2FyDGxLKVeeHZZmORS_8XeSuhz9SjIJRaSa2lnsF01tQOHrfTGAP3R5X1Kv5iVUuMbNKhWNAXHOl6ePB0TUL8nw",
            limit=10,
            prefix="My-Prefix",
        )
        assert_matches_type(AsyncCursorLimitPagination[Key], key, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.keys.with_raw_response.list(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        key = await response.parse()
        assert_matches_type(AsyncCursorLimitPagination[Key], key, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.keys.with_streaming_response.list(
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            key = await response.parse()
            assert_matches_type(AsyncCursorLimitPagination[Key], key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.keys.with_raw_response.list(
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.keys.with_raw_response.list(
                namespace_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
