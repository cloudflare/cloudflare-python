# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.pipelines import (
    SinkGetResponse,
    SinkListResponse,
    SinkCreateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSinks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        sink = client.pipelines.sinks.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_sink",
            type="r2",
        )
        assert_matches_type(SinkCreateResponse, sink, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        sink = client.pipelines.sinks.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_sink",
            type="r2",
            config={
                "account_id": "account_id",
                "bucket": "bucket",
                "credentials": {
                    "access_key_id": "access_key_id",
                    "secret_access_key": "secret_access_key",
                },
                "file_naming": {
                    "prefix": "prefix",
                    "strategy": "serial",
                    "suffix": "suffix",
                },
                "jurisdiction": "jurisdiction",
                "partitioning": {"time_pattern": "year=%Y/month=%m/day=%d/hour=%H"},
                "path": "path",
                "rolling_policy": {
                    "file_size_bytes": 0,
                    "inactivity_seconds": 1,
                    "interval_seconds": 1,
                },
            },
            format={
                "type": "json",
                "decimal_encoding": "number",
                "timestamp_format": "rfc3339",
                "unstructured": True,
            },
            schema={
                "fields": [
                    {
                        "type": "int32",
                        "metadata_key": "metadata_key",
                        "name": "name",
                        "required": True,
                        "sql_name": "sql_name",
                    }
                ],
                "format": {
                    "type": "json",
                    "decimal_encoding": "number",
                    "timestamp_format": "rfc3339",
                    "unstructured": True,
                },
                "inferred": True,
            },
        )
        assert_matches_type(SinkCreateResponse, sink, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.pipelines.sinks.with_raw_response.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_sink",
            type="r2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sink = response.parse()
        assert_matches_type(SinkCreateResponse, sink, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.pipelines.sinks.with_streaming_response.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_sink",
            type="r2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sink = response.parse()
            assert_matches_type(SinkCreateResponse, sink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.sinks.with_raw_response.create(
                account_id="",
                name="my_sink",
                type="r2",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        sink = client.pipelines.sinks.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[SinkListResponse], sink, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        sink = client.pipelines.sinks.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=0,
            pipeline_id="pipeline_id",
        )
        assert_matches_type(SyncV4PagePaginationArray[SinkListResponse], sink, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.pipelines.sinks.with_raw_response.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sink = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[SinkListResponse], sink, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.pipelines.sinks.with_streaming_response.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sink = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[SinkListResponse], sink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.sinks.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        sink = client.pipelines.sinks.delete(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert sink is None

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        sink = client.pipelines.sinks.delete(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            force="force",
        )
        assert sink is None

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.pipelines.sinks.with_raw_response.delete(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sink = response.parse()
        assert sink is None

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.pipelines.sinks.with_streaming_response.delete(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sink = response.parse()
            assert sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.sinks.with_raw_response.delete(
                sink_id="0223105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sink_id` but received ''"):
            client.pipelines.sinks.with_raw_response.delete(
                sink_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        sink = client.pipelines.sinks.get(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SinkGetResponse, sink, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.pipelines.sinks.with_raw_response.get(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sink = response.parse()
        assert_matches_type(SinkGetResponse, sink, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.pipelines.sinks.with_streaming_response.get(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sink = response.parse()
            assert_matches_type(SinkGetResponse, sink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.pipelines.sinks.with_raw_response.get(
                sink_id="0223105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sink_id` but received ''"):
            client.pipelines.sinks.with_raw_response.get(
                sink_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSinks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        sink = await async_client.pipelines.sinks.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_sink",
            type="r2",
        )
        assert_matches_type(SinkCreateResponse, sink, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        sink = await async_client.pipelines.sinks.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_sink",
            type="r2",
            config={
                "account_id": "account_id",
                "bucket": "bucket",
                "credentials": {
                    "access_key_id": "access_key_id",
                    "secret_access_key": "secret_access_key",
                },
                "file_naming": {
                    "prefix": "prefix",
                    "strategy": "serial",
                    "suffix": "suffix",
                },
                "jurisdiction": "jurisdiction",
                "partitioning": {"time_pattern": "year=%Y/month=%m/day=%d/hour=%H"},
                "path": "path",
                "rolling_policy": {
                    "file_size_bytes": 0,
                    "inactivity_seconds": 1,
                    "interval_seconds": 1,
                },
            },
            format={
                "type": "json",
                "decimal_encoding": "number",
                "timestamp_format": "rfc3339",
                "unstructured": True,
            },
            schema={
                "fields": [
                    {
                        "type": "int32",
                        "metadata_key": "metadata_key",
                        "name": "name",
                        "required": True,
                        "sql_name": "sql_name",
                    }
                ],
                "format": {
                    "type": "json",
                    "decimal_encoding": "number",
                    "timestamp_format": "rfc3339",
                    "unstructured": True,
                },
                "inferred": True,
            },
        )
        assert_matches_type(SinkCreateResponse, sink, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.sinks.with_raw_response.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_sink",
            type="r2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sink = await response.parse()
        assert_matches_type(SinkCreateResponse, sink, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.sinks.with_streaming_response.create(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            name="my_sink",
            type="r2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sink = await response.parse()
            assert_matches_type(SinkCreateResponse, sink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.sinks.with_raw_response.create(
                account_id="",
                name="my_sink",
                type="r2",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        sink = await async_client.pipelines.sinks.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[SinkListResponse], sink, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        sink = await async_client.pipelines.sinks.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            page=0,
            per_page=0,
            pipeline_id="pipeline_id",
        )
        assert_matches_type(AsyncV4PagePaginationArray[SinkListResponse], sink, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.sinks.with_raw_response.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sink = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[SinkListResponse], sink, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.sinks.with_streaming_response.list(
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sink = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[SinkListResponse], sink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.sinks.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        sink = await async_client.pipelines.sinks.delete(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert sink is None

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        sink = await async_client.pipelines.sinks.delete(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
            force="force",
        )
        assert sink is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.sinks.with_raw_response.delete(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sink = await response.parse()
        assert sink is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.sinks.with_streaming_response.delete(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sink = await response.parse()
            assert sink is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.sinks.with_raw_response.delete(
                sink_id="0223105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sink_id` but received ''"):
            await async_client.pipelines.sinks.with_raw_response.delete(
                sink_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        sink = await async_client.pipelines.sinks.get(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SinkGetResponse, sink, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.pipelines.sinks.with_raw_response.get(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sink = await response.parse()
        assert_matches_type(SinkGetResponse, sink, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.pipelines.sinks.with_streaming_response.get(
            sink_id="0223105f4ecef8ad9ca31a8372d0c353",
            account_id="0123105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sink = await response.parse()
            assert_matches_type(SinkGetResponse, sink, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.pipelines.sinks.with_raw_response.get(
                sink_id="0223105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sink_id` but received ''"):
            await async_client.pipelines.sinks.with_raw_response.get(
                sink_id="",
                account_id="0123105f4ecef8ad9ca31a8372d0c353",
            )
