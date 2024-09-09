# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.kv.namespaces import MetadataGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        metadata = client.kv.namespaces.metadata.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )
        assert_matches_type(Optional[MetadataGetResponse], metadata, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.metadata.with_raw_response.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(Optional[MetadataGetResponse], metadata, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.kv.namespaces.metadata.with_streaming_response.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(Optional[MetadataGetResponse], metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.metadata.with_raw_response.get(
                key_name="My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.metadata.with_raw_response.get(
                key_name="My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            client.kv.namespaces.metadata.with_raw_response.get(
                key_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        metadata = await async_client.kv.namespaces.metadata.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )
        assert_matches_type(Optional[MetadataGetResponse], metadata, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.metadata.with_raw_response.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(Optional[MetadataGetResponse], metadata, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.metadata.with_streaming_response.get(
            key_name="My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(Optional[MetadataGetResponse], metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.metadata.with_raw_response.get(
                key_name="My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.metadata.with_raw_response.get(
                key_name="My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            await async_client.kv.namespaces.metadata.with_raw_response.get(
                key_name="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )
