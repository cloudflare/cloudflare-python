# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import AggregateListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAggregate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        aggregate = client.cloudforce_one.threat_events.aggregate.list(
            account_id="account_id",
            aggregate_by="aggregateBy",
        )
        assert_matches_type(AggregateListResponse, aggregate, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        aggregate = client.cloudforce_one.threat_events.aggregate.list(
            account_id="account_id",
            aggregate_by="aggregateBy",
            dataset_id=["string"],
            end_date="endDate",
            group_by_date=True,
            limit=0,
            start_date="startDate",
        )
        assert_matches_type(AggregateListResponse, aggregate, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.aggregate.with_raw_response.list(
            account_id="account_id",
            aggregate_by="aggregateBy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregate = response.parse()
        assert_matches_type(AggregateListResponse, aggregate, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.aggregate.with_streaming_response.list(
            account_id="account_id",
            aggregate_by="aggregateBy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregate = response.parse()
            assert_matches_type(AggregateListResponse, aggregate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.aggregate.with_raw_response.list(
                account_id="",
                aggregate_by="aggregateBy",
            )


class TestAsyncAggregate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        aggregate = await async_client.cloudforce_one.threat_events.aggregate.list(
            account_id="account_id",
            aggregate_by="aggregateBy",
        )
        assert_matches_type(AggregateListResponse, aggregate, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        aggregate = await async_client.cloudforce_one.threat_events.aggregate.list(
            account_id="account_id",
            aggregate_by="aggregateBy",
            dataset_id=["string"],
            end_date="endDate",
            group_by_date=True,
            limit=0,
            start_date="startDate",
        )
        assert_matches_type(AggregateListResponse, aggregate, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.aggregate.with_raw_response.list(
            account_id="account_id",
            aggregate_by="aggregateBy",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        aggregate = await response.parse()
        assert_matches_type(AggregateListResponse, aggregate, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.aggregate.with_streaming_response.list(
            account_id="account_id",
            aggregate_by="aggregateBy",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            aggregate = await response.parse()
            assert_matches_type(AggregateListResponse, aggregate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.aggregate.with_raw_response.list(
                account_id="",
                aggregate_by="aggregateBy",
            )
