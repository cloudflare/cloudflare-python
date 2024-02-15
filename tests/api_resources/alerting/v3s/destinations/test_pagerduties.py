# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.alerting.v3s.destinations import (
    PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPagerduties:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_notification_destinations_with_pager_duty_list_pager_duty_services(
        self, client: Cloudflare
    ) -> None:
        pagerduty = client.alerting.v3s.destinations.pagerduties.notification_destinations_with_pager_duty_list_pager_duty_services(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse],
            pagerduty,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_notification_destinations_with_pager_duty_list_pager_duty_services(
        self, client: Cloudflare
    ) -> None:
        response = client.alerting.v3s.destinations.pagerduties.with_raw_response.notification_destinations_with_pager_duty_list_pager_duty_services(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = response.parse()
        assert_matches_type(
            Optional[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse],
            pagerduty,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_notification_destinations_with_pager_duty_list_pager_duty_services(
        self, client: Cloudflare
    ) -> None:
        with client.alerting.v3s.destinations.pagerduties.with_streaming_response.notification_destinations_with_pager_duty_list_pager_duty_services(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = response.parse()
            assert_matches_type(
                Optional[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse],
                pagerduty,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_notification_destinations_with_pager_duty_list_pager_duty_services(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.alerting.v3s.destinations.pagerduties.with_raw_response.notification_destinations_with_pager_duty_list_pager_duty_services(
                "",
            )


class TestAsyncPagerduties:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_notification_destinations_with_pager_duty_list_pager_duty_services(
        self, async_client: AsyncCloudflare
    ) -> None:
        pagerduty = await async_client.alerting.v3s.destinations.pagerduties.notification_destinations_with_pager_duty_list_pager_duty_services(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse],
            pagerduty,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_notification_destinations_with_pager_duty_list_pager_duty_services(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.alerting.v3s.destinations.pagerduties.with_raw_response.notification_destinations_with_pager_duty_list_pager_duty_services(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pagerduty = await response.parse()
        assert_matches_type(
            Optional[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse],
            pagerduty,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_notification_destinations_with_pager_duty_list_pager_duty_services(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.alerting.v3s.destinations.pagerduties.with_streaming_response.notification_destinations_with_pager_duty_list_pager_duty_services(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pagerduty = await response.parse()
            assert_matches_type(
                Optional[PagerdutyNotificationDestinationsWithPagerDutyListPagerDutyServicesResponse],
                pagerduty,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_notification_destinations_with_pager_duty_list_pager_duty_services(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.alerting.v3s.destinations.pagerduties.with_raw_response.notification_destinations_with_pager_duty_list_pager_duty_services(
                "",
            )
