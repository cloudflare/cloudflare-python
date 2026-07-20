# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.cloudforce_one.threat_events import RelationshipListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRelationships:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        relationship = client.cloudforce_one.threat_events.relationships.list(
            event_id="event_id",
            account_id="account_id",
            dataset_id="datasetId",
        )
        assert_matches_type(RelationshipListResponse, relationship, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        relationship = client.cloudforce_one.threat_events.relationships.list(
            event_id="event_id",
            account_id="account_id",
            dataset_id="datasetId",
            direction="ancestors",
            include_parent=True,
            indicator_type_ids=["string"],
            max_depth=0,
            page=0,
            page_size=0,
            relationship_types="string",
        )
        assert_matches_type(RelationshipListResponse, relationship, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.cloudforce_one.threat_events.relationships.with_raw_response.list(
            event_id="event_id",
            account_id="account_id",
            dataset_id="datasetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = response.parse()
        assert_matches_type(RelationshipListResponse, relationship, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.cloudforce_one.threat_events.relationships.with_streaming_response.list(
            event_id="event_id",
            account_id="account_id",
            dataset_id="datasetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = response.parse()
            assert_matches_type(RelationshipListResponse, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.cloudforce_one.threat_events.relationships.with_raw_response.list(
                event_id="event_id",
                account_id="",
                dataset_id="datasetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            client.cloudforce_one.threat_events.relationships.with_raw_response.list(
                event_id="",
                account_id="account_id",
                dataset_id="datasetId",
            )


class TestAsyncRelationships:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        relationship = await async_client.cloudforce_one.threat_events.relationships.list(
            event_id="event_id",
            account_id="account_id",
            dataset_id="datasetId",
        )
        assert_matches_type(RelationshipListResponse, relationship, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        relationship = await async_client.cloudforce_one.threat_events.relationships.list(
            event_id="event_id",
            account_id="account_id",
            dataset_id="datasetId",
            direction="ancestors",
            include_parent=True,
            indicator_type_ids=["string"],
            max_depth=0,
            page=0,
            page_size=0,
            relationship_types="string",
        )
        assert_matches_type(RelationshipListResponse, relationship, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.cloudforce_one.threat_events.relationships.with_raw_response.list(
            event_id="event_id",
            account_id="account_id",
            dataset_id="datasetId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        relationship = await response.parse()
        assert_matches_type(RelationshipListResponse, relationship, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.cloudforce_one.threat_events.relationships.with_streaming_response.list(
            event_id="event_id",
            account_id="account_id",
            dataset_id="datasetId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            relationship = await response.parse()
            assert_matches_type(RelationshipListResponse, relationship, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.cloudforce_one.threat_events.relationships.with_raw_response.list(
                event_id="event_id",
                account_id="",
                dataset_id="datasetId",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `event_id` but received ''"):
            await async_client.cloudforce_one.threat_events.relationships.with_raw_response.list(
                event_id="",
                account_id="account_id",
                dataset_id="datasetId",
            )
