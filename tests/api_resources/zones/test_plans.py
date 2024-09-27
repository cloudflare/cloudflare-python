# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zones import AvailableRatePlan

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        plan = client.zones.plans.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[AvailableRatePlan], plan, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zones.plans.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(SyncSinglePage[AvailableRatePlan], plan, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zones.plans.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(SyncSinglePage[AvailableRatePlan], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.plans.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        plan = client.zones.plans.get(
            plan_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AvailableRatePlan, plan, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zones.plans.with_raw_response.get(
            plan_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = response.parse()
        assert_matches_type(AvailableRatePlan, plan, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zones.plans.with_streaming_response.get(
            plan_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = response.parse()
            assert_matches_type(AvailableRatePlan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.plans.with_raw_response.get(
                plan_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_identifier` but received ''"):
            client.zones.plans.with_raw_response.get(
                plan_identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPlans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        plan = await async_client.zones.plans.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[AvailableRatePlan], plan, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.plans.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AsyncSinglePage[AvailableRatePlan], plan, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.plans.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AsyncSinglePage[AvailableRatePlan], plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.plans.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        plan = await async_client.zones.plans.get(
            plan_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AvailableRatePlan, plan, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.plans.with_raw_response.get(
            plan_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        plan = await response.parse()
        assert_matches_type(AvailableRatePlan, plan, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.plans.with_streaming_response.get(
            plan_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            plan = await response.parse()
            assert_matches_type(AvailableRatePlan, plan, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.plans.with_raw_response.get(
                plan_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `plan_identifier` but received ''"):
            await async_client.zones.plans.with_raw_response.get(
                plan_identifier="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
