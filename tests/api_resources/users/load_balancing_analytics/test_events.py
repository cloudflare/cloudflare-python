# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.users.load_balancing_analytics import (
    EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.users.load_balancing_analytics import (
    event_load_balancer_healthcheck_events_list_healthcheck_events_params,
)
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_healthcheck_events_list_healthcheck_events(self, client: Cloudflare) -> None:
        event = client.users.load_balancing_analytics.events.load_balancer_healthcheck_events_list_healthcheck_events()
        assert_matches_type(
            Optional[EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse], event, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_load_balancer_healthcheck_events_list_healthcheck_events_with_all_params(
        self, client: Cloudflare
    ) -> None:
        event = client.users.load_balancing_analytics.events.load_balancer_healthcheck_events_list_healthcheck_events(
            origin_healthy=True,
            origin_name="primary-dc-1",
            pool_healthy=True,
            pool_id="17b5962d775c646f3f9725cbc7a53df4",
            pool_name="primary-dc",
            since=parse_datetime("2016-11-11T12:00:00Z"),
            until=parse_datetime("2016-11-11T13:00:00Z"),
        )
        assert_matches_type(
            Optional[EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse], event, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_load_balancer_healthcheck_events_list_healthcheck_events(self, client: Cloudflare) -> None:
        response = client.users.load_balancing_analytics.events.with_raw_response.load_balancer_healthcheck_events_list_healthcheck_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = response.parse()
        assert_matches_type(
            Optional[EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse], event, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_load_balancer_healthcheck_events_list_healthcheck_events(
        self, client: Cloudflare
    ) -> None:
        with client.users.load_balancing_analytics.events.with_streaming_response.load_balancer_healthcheck_events_list_healthcheck_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = response.parse()
            assert_matches_type(
                Optional[EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse], event, path=["response"]
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_healthcheck_events_list_healthcheck_events(
        self, async_client: AsyncCloudflare
    ) -> None:
        event = await async_client.users.load_balancing_analytics.events.load_balancer_healthcheck_events_list_healthcheck_events()
        assert_matches_type(
            Optional[EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse], event, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_load_balancer_healthcheck_events_list_healthcheck_events_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        event = await async_client.users.load_balancing_analytics.events.load_balancer_healthcheck_events_list_healthcheck_events(
            origin_healthy=True,
            origin_name="primary-dc-1",
            pool_healthy=True,
            pool_id="17b5962d775c646f3f9725cbc7a53df4",
            pool_name="primary-dc",
            since=parse_datetime("2016-11-11T12:00:00Z"),
            until=parse_datetime("2016-11-11T13:00:00Z"),
        )
        assert_matches_type(
            Optional[EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse], event, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_load_balancer_healthcheck_events_list_healthcheck_events(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.users.load_balancing_analytics.events.with_raw_response.load_balancer_healthcheck_events_list_healthcheck_events()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        event = await response.parse()
        assert_matches_type(
            Optional[EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse], event, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_load_balancer_healthcheck_events_list_healthcheck_events(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.users.load_balancing_analytics.events.with_streaming_response.load_balancer_healthcheck_events_list_healthcheck_events() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            event = await response.parse()
            assert_matches_type(
                Optional[EventLoadBalancerHealthcheckEventsListHealthcheckEventsResponse], event, path=["response"]
            )

        assert cast(Any, response.is_closed) is True
