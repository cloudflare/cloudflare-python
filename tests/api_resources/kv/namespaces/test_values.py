# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.kv.namespaces import (
    ValueDeleteResponse,
    ValueUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestValues:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        value = client.kv.namespaces.values.update(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        )
        assert_matches_type(ValueUpdateResponse, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.values.with_raw_response.update(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(ValueUpdateResponse, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.kv.namespaces.values.with_streaming_response.update(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(ValueUpdateResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.update(
                "My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.update(
                "My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            client.kv.namespaces.values.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        value = client.kv.namespaces.values.delete(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )
        assert_matches_type(ValueDeleteResponse, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.values.with_raw_response.delete(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(ValueDeleteResponse, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.kv.namespaces.values.with_streaming_response.delete(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(ValueDeleteResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.delete(
                "My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.delete(
                "My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            client.kv.namespaces.values.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        value = client.kv.namespaces.values.get(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.kv.namespaces.values.with_raw_response.get(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = response.parse()
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.kv.namespaces.values.with_streaming_response.get(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = response.parse()
            assert_matches_type(str, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.get(
                "My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.kv.namespaces.values.with_raw_response.get(
                "My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            client.kv.namespaces.values.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )


class TestAsyncValues:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        value = await async_client.kv.namespaces.values.update(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        )
        assert_matches_type(ValueUpdateResponse, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.values.with_raw_response.update(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(ValueUpdateResponse, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.values.with_streaming_response.update(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
            metadata='{"someMetadataKey": "someMetadataValue"}',
            value="Some Value",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(ValueUpdateResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.update(
                "My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.update(
                "My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
                metadata='{"someMetadataKey": "someMetadataValue"}',
                value="Some Value",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        value = await async_client.kv.namespaces.values.delete(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )
        assert_matches_type(ValueDeleteResponse, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.values.with_raw_response.delete(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(ValueDeleteResponse, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.values.with_streaming_response.delete(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(ValueDeleteResponse, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.delete(
                "My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.delete(
                "My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        value = await async_client.kv.namespaces.values.get(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.kv.namespaces.values.with_raw_response.get(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        value = await response.parse()
        assert_matches_type(str, value, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.kv.namespaces.values.with_streaming_response.get(
            "My-Key",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            namespace_id="0f2ac74b498b48028cb68387c421e279",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            value = await response.parse()
            assert_matches_type(str, value, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.get(
                "My-Key",
                account_id="",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.get(
                "My-Key",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `key_name` but received ''"):
            await async_client.kv.namespaces.values.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                namespace_id="0f2ac74b498b48028cb68387c421e279",
            )
