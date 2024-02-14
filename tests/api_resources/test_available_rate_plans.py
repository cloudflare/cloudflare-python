# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types import AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAvailableRatePlans:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_zone_rate_plan_list_available_rate_plans(self, client: Cloudflare) -> None:
        available_rate_plan = client.available_rate_plans.zone_rate_plan_list_available_rate_plans(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse],
            available_rate_plan,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zone_rate_plan_list_available_rate_plans(self, client: Cloudflare) -> None:
        response = client.available_rate_plans.with_raw_response.zone_rate_plan_list_available_rate_plans(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        available_rate_plan = response.parse()
        assert_matches_type(
            Optional[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse],
            available_rate_plan,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zone_rate_plan_list_available_rate_plans(self, client: Cloudflare) -> None:
        with client.available_rate_plans.with_streaming_response.zone_rate_plan_list_available_rate_plans(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            available_rate_plan = response.parse()
            assert_matches_type(
                Optional[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse],
                available_rate_plan,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_zone_rate_plan_list_available_rate_plans(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.available_rate_plans.with_raw_response.zone_rate_plan_list_available_rate_plans(
                "",
            )


class TestAsyncAvailableRatePlans:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_zone_rate_plan_list_available_rate_plans(self, async_client: AsyncCloudflare) -> None:
        available_rate_plan = await async_client.available_rate_plans.zone_rate_plan_list_available_rate_plans(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse],
            available_rate_plan,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zone_rate_plan_list_available_rate_plans(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.available_rate_plans.with_raw_response.zone_rate_plan_list_available_rate_plans(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        available_rate_plan = await response.parse()
        assert_matches_type(
            Optional[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse],
            available_rate_plan,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zone_rate_plan_list_available_rate_plans(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.available_rate_plans.with_streaming_response.zone_rate_plan_list_available_rate_plans(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            available_rate_plan = await response.parse()
            assert_matches_type(
                Optional[AvailableRatePlanZoneRatePlanListAvailableRatePlansResponse],
                available_rate_plan,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_zone_rate_plan_list_available_rate_plans(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.available_rate_plans.with_raw_response.zone_rate_plan_list_available_rate_plans(
                "",
            )
