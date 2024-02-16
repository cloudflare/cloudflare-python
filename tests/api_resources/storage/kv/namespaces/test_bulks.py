# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.storage.kv.namespaces import (
    BulkDeleteResponse,
    BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        bulk = client.storage.kv.namespaces.bulks.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key", "My-Key", "My-Key"],
        )
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.storage.kv.namespaces.bulks.with_raw_response.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key", "My-Key", "My-Key"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.storage.kv.namespaces.bulks.with_streaming_response.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key", "My-Key", "My-Key"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.storage.kv.namespaces.bulks.with_raw_response.delete(
                "0f2ac74b498b48028cb68387c421e279",
                account_id="",
                body=["My-Key", "My-Key", "My-Key"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.storage.kv.namespaces.bulks.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=["My-Key", "My-Key", "My-Key"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_workers_kv_namespace_write_multiple_key_value_pairs(self, client: Cloudflare) -> None:
        bulk = client.storage.kv.namespaces.bulks.workers_kv_namespace_write_multiple_key_value_pairs(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse, bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_workers_kv_namespace_write_multiple_key_value_pairs(self, client: Cloudflare) -> None:
        response = (
            client.storage.kv.namespaces.bulks.with_raw_response.workers_kv_namespace_write_multiple_key_value_pairs(
                "0f2ac74b498b48028cb68387c421e279",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse, bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_workers_kv_namespace_write_multiple_key_value_pairs(self, client: Cloudflare) -> None:
        with client.storage.kv.namespaces.bulks.with_streaming_response.workers_kv_namespace_write_multiple_key_value_pairs(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_workers_kv_namespace_write_multiple_key_value_pairs(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.storage.kv.namespaces.bulks.with_raw_response.workers_kv_namespace_write_multiple_key_value_pairs(
                "0f2ac74b498b48028cb68387c421e279",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            client.storage.kv.namespaces.bulks.with_raw_response.workers_kv_namespace_write_multiple_key_value_pairs(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )


class TestAsyncBulks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        bulk = await async_client.storage.kv.namespaces.bulks.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key", "My-Key", "My-Key"],
        )
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.storage.kv.namespaces.bulks.with_raw_response.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key", "My-Key", "My-Key"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.storage.kv.namespaces.bulks.with_streaming_response.delete(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=["My-Key", "My-Key", "My-Key"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.storage.kv.namespaces.bulks.with_raw_response.delete(
                "0f2ac74b498b48028cb68387c421e279",
                account_id="",
                body=["My-Key", "My-Key", "My-Key"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.storage.kv.namespaces.bulks.with_raw_response.delete(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=["My-Key", "My-Key", "My-Key"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_workers_kv_namespace_write_multiple_key_value_pairs(
        self, async_client: AsyncCloudflare
    ) -> None:
        bulk = await async_client.storage.kv.namespaces.bulks.workers_kv_namespace_write_multiple_key_value_pairs(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )
        assert_matches_type(BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse, bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_workers_kv_namespace_write_multiple_key_value_pairs(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.storage.kv.namespaces.bulks.with_raw_response.workers_kv_namespace_write_multiple_key_value_pairs(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse, bulk, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_workers_kv_namespace_write_multiple_key_value_pairs(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.storage.kv.namespaces.bulks.with_streaming_response.workers_kv_namespace_write_multiple_key_value_pairs(
            "0f2ac74b498b48028cb68387c421e279",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            body=[{}, {}, {}],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkWorkersKvNamespaceWriteMultipleKeyValuePairsResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_workers_kv_namespace_write_multiple_key_value_pairs(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.storage.kv.namespaces.bulks.with_raw_response.workers_kv_namespace_write_multiple_key_value_pairs(
                "0f2ac74b498b48028cb68387c421e279",
                account_id="",
                body=[{}, {}, {}],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `namespace_id` but received ''"):
            await async_client.storage.kv.namespaces.bulks.with_raw_response.workers_kv_namespace_write_multiple_key_value_pairs(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                body=[{}, {}, {}],
            )
