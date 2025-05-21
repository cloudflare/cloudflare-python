# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.workers.observability import (
    TelemetryKeysResponse,
    TelemetryQueryResponse,
    TelemetryValuesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTelemetry:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_keys(self, client: Cloudflare) -> None:
        telemetry = client.workers.observability.telemetry.keys(
            account_id="account_id",
        )
        assert_matches_type(SyncSinglePage[TelemetryKeysResponse], telemetry, path=["response"])

    @parametrize
    def test_method_keys_with_all_params(self, client: Cloudflare) -> None:
        telemetry = client.workers.observability.telemetry.keys(
            account_id="account_id",
            datasets=["string"],
            filters=[
                {
                    "key": "key",
                    "operation": "includes",
                    "type": "string",
                    "value": "string",
                }
            ],
            key_needle={
                "value": "string",
                "is_regex": True,
                "match_case": True,
            },
            limit=0,
            needle={
                "value": "string",
                "is_regex": True,
                "match_case": True,
            },
            timeframe={
                "from": 0,
                "to": 0,
            },
        )
        assert_matches_type(SyncSinglePage[TelemetryKeysResponse], telemetry, path=["response"])

    @parametrize
    def test_raw_response_keys(self, client: Cloudflare) -> None:
        response = client.workers.observability.telemetry.with_raw_response.keys(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(SyncSinglePage[TelemetryKeysResponse], telemetry, path=["response"])

    @parametrize
    def test_streaming_response_keys(self, client: Cloudflare) -> None:
        with client.workers.observability.telemetry.with_streaming_response.keys(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(SyncSinglePage[TelemetryKeysResponse], telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_keys(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.telemetry.with_raw_response.keys(
                account_id="",
            )

    @parametrize
    def test_method_query(self, client: Cloudflare) -> None:
        telemetry = client.workers.observability.telemetry.query(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        )
        assert_matches_type(TelemetryQueryResponse, telemetry, path=["response"])

    @parametrize
    def test_method_query_with_all_params(self, client: Cloudflare) -> None:
        telemetry = client.workers.observability.telemetry.query(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
            chart=True,
            compare=True,
            dry=True,
            granularity=0,
            ignore_series=True,
            limit=100,
            offset="offset",
            offset_by=0,
            offset_direction="offsetDirection",
            parameters={
                "calculations": [
                    {
                        "operator": "uniq",
                        "alias": "alias",
                        "key": "key",
                        "key_type": "string",
                    }
                ],
                "datasets": ["string"],
                "filter_combination": "and",
                "filters": [
                    {
                        "key": "key",
                        "operation": "includes",
                        "type": "string",
                        "value": "string",
                    }
                ],
                "group_bys": [
                    {
                        "type": "string",
                        "value": "value",
                    }
                ],
                "havings": [
                    {
                        "key": "key",
                        "operation": "eq",
                        "value": 0,
                    }
                ],
                "limit": 0,
                "needle": {
                    "value": "string",
                    "is_regex": True,
                    "match_case": True,
                },
                "order_by": {
                    "value": "value",
                    "order": "asc",
                },
            },
            pattern_type="message",
            view="traces",
        )
        assert_matches_type(TelemetryQueryResponse, telemetry, path=["response"])

    @parametrize
    def test_raw_response_query(self, client: Cloudflare) -> None:
        response = client.workers.observability.telemetry.with_raw_response.query(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(TelemetryQueryResponse, telemetry, path=["response"])

    @parametrize
    def test_streaming_response_query(self, client: Cloudflare) -> None:
        with client.workers.observability.telemetry.with_streaming_response.query(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(TelemetryQueryResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_query(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.telemetry.with_raw_response.query(
                account_id="",
                query_id="queryId",
                timeframe={
                    "from": 0,
                    "to": 0,
                },
            )

    @parametrize
    def test_method_values(self, client: Cloudflare) -> None:
        telemetry = client.workers.observability.telemetry.values(
            account_id="account_id",
            datasets=["string"],
            key="key",
            timeframe={
                "from": 0,
                "to": 0,
            },
            type="string",
        )
        assert_matches_type(SyncSinglePage[TelemetryValuesResponse], telemetry, path=["response"])

    @parametrize
    def test_method_values_with_all_params(self, client: Cloudflare) -> None:
        telemetry = client.workers.observability.telemetry.values(
            account_id="account_id",
            datasets=["string"],
            key="key",
            timeframe={
                "from": 0,
                "to": 0,
            },
            type="string",
            filters=[
                {
                    "key": "key",
                    "operation": "includes",
                    "type": "string",
                    "value": "string",
                }
            ],
            limit=0,
            needle={
                "value": "string",
                "is_regex": True,
                "match_case": True,
            },
        )
        assert_matches_type(SyncSinglePage[TelemetryValuesResponse], telemetry, path=["response"])

    @parametrize
    def test_raw_response_values(self, client: Cloudflare) -> None:
        response = client.workers.observability.telemetry.with_raw_response.values(
            account_id="account_id",
            datasets=["string"],
            key="key",
            timeframe={
                "from": 0,
                "to": 0,
            },
            type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = response.parse()
        assert_matches_type(SyncSinglePage[TelemetryValuesResponse], telemetry, path=["response"])

    @parametrize
    def test_streaming_response_values(self, client: Cloudflare) -> None:
        with client.workers.observability.telemetry.with_streaming_response.values(
            account_id="account_id",
            datasets=["string"],
            key="key",
            timeframe={
                "from": 0,
                "to": 0,
            },
            type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = response.parse()
            assert_matches_type(SyncSinglePage[TelemetryValuesResponse], telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_values(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.workers.observability.telemetry.with_raw_response.values(
                account_id="",
                datasets=["string"],
                key="key",
                timeframe={
                    "from": 0,
                    "to": 0,
                },
                type="string",
            )


class TestAsyncTelemetry:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_keys(self, async_client: AsyncCloudflare) -> None:
        telemetry = await async_client.workers.observability.telemetry.keys(
            account_id="account_id",
        )
        assert_matches_type(AsyncSinglePage[TelemetryKeysResponse], telemetry, path=["response"])

    @parametrize
    async def test_method_keys_with_all_params(self, async_client: AsyncCloudflare) -> None:
        telemetry = await async_client.workers.observability.telemetry.keys(
            account_id="account_id",
            datasets=["string"],
            filters=[
                {
                    "key": "key",
                    "operation": "includes",
                    "type": "string",
                    "value": "string",
                }
            ],
            key_needle={
                "value": "string",
                "is_regex": True,
                "match_case": True,
            },
            limit=0,
            needle={
                "value": "string",
                "is_regex": True,
                "match_case": True,
            },
            timeframe={
                "from": 0,
                "to": 0,
            },
        )
        assert_matches_type(AsyncSinglePage[TelemetryKeysResponse], telemetry, path=["response"])

    @parametrize
    async def test_raw_response_keys(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.telemetry.with_raw_response.keys(
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(AsyncSinglePage[TelemetryKeysResponse], telemetry, path=["response"])

    @parametrize
    async def test_streaming_response_keys(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.telemetry.with_streaming_response.keys(
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(AsyncSinglePage[TelemetryKeysResponse], telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_keys(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.telemetry.with_raw_response.keys(
                account_id="",
            )

    @parametrize
    async def test_method_query(self, async_client: AsyncCloudflare) -> None:
        telemetry = await async_client.workers.observability.telemetry.query(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        )
        assert_matches_type(TelemetryQueryResponse, telemetry, path=["response"])

    @parametrize
    async def test_method_query_with_all_params(self, async_client: AsyncCloudflare) -> None:
        telemetry = await async_client.workers.observability.telemetry.query(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
            chart=True,
            compare=True,
            dry=True,
            granularity=0,
            ignore_series=True,
            limit=100,
            offset="offset",
            offset_by=0,
            offset_direction="offsetDirection",
            parameters={
                "calculations": [
                    {
                        "operator": "uniq",
                        "alias": "alias",
                        "key": "key",
                        "key_type": "string",
                    }
                ],
                "datasets": ["string"],
                "filter_combination": "and",
                "filters": [
                    {
                        "key": "key",
                        "operation": "includes",
                        "type": "string",
                        "value": "string",
                    }
                ],
                "group_bys": [
                    {
                        "type": "string",
                        "value": "value",
                    }
                ],
                "havings": [
                    {
                        "key": "key",
                        "operation": "eq",
                        "value": 0,
                    }
                ],
                "limit": 0,
                "needle": {
                    "value": "string",
                    "is_regex": True,
                    "match_case": True,
                },
                "order_by": {
                    "value": "value",
                    "order": "asc",
                },
            },
            pattern_type="message",
            view="traces",
        )
        assert_matches_type(TelemetryQueryResponse, telemetry, path=["response"])

    @parametrize
    async def test_raw_response_query(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.telemetry.with_raw_response.query(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(TelemetryQueryResponse, telemetry, path=["response"])

    @parametrize
    async def test_streaming_response_query(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.telemetry.with_streaming_response.query(
            account_id="account_id",
            query_id="queryId",
            timeframe={
                "from": 0,
                "to": 0,
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(TelemetryQueryResponse, telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_query(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.telemetry.with_raw_response.query(
                account_id="",
                query_id="queryId",
                timeframe={
                    "from": 0,
                    "to": 0,
                },
            )

    @parametrize
    async def test_method_values(self, async_client: AsyncCloudflare) -> None:
        telemetry = await async_client.workers.observability.telemetry.values(
            account_id="account_id",
            datasets=["string"],
            key="key",
            timeframe={
                "from": 0,
                "to": 0,
            },
            type="string",
        )
        assert_matches_type(AsyncSinglePage[TelemetryValuesResponse], telemetry, path=["response"])

    @parametrize
    async def test_method_values_with_all_params(self, async_client: AsyncCloudflare) -> None:
        telemetry = await async_client.workers.observability.telemetry.values(
            account_id="account_id",
            datasets=["string"],
            key="key",
            timeframe={
                "from": 0,
                "to": 0,
            },
            type="string",
            filters=[
                {
                    "key": "key",
                    "operation": "includes",
                    "type": "string",
                    "value": "string",
                }
            ],
            limit=0,
            needle={
                "value": "string",
                "is_regex": True,
                "match_case": True,
            },
        )
        assert_matches_type(AsyncSinglePage[TelemetryValuesResponse], telemetry, path=["response"])

    @parametrize
    async def test_raw_response_values(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.workers.observability.telemetry.with_raw_response.values(
            account_id="account_id",
            datasets=["string"],
            key="key",
            timeframe={
                "from": 0,
                "to": 0,
            },
            type="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        telemetry = await response.parse()
        assert_matches_type(AsyncSinglePage[TelemetryValuesResponse], telemetry, path=["response"])

    @parametrize
    async def test_streaming_response_values(self, async_client: AsyncCloudflare) -> None:
        async with async_client.workers.observability.telemetry.with_streaming_response.values(
            account_id="account_id",
            datasets=["string"],
            key="key",
            timeframe={
                "from": 0,
                "to": 0,
            },
            type="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            telemetry = await response.parse()
            assert_matches_type(AsyncSinglePage[TelemetryValuesResponse], telemetry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_values(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.workers.observability.telemetry.with_raw_response.values(
                account_id="",
                datasets=["string"],
                key="key",
                timeframe={
                    "from": 0,
                    "to": 0,
                },
                type="string",
            )
