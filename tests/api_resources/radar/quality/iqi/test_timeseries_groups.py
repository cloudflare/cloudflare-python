# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.radar.quality.iqi import TimeseriesGroupListResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.quality.iqi import timeseries_group_list_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTimeseriesGroups:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.quality.iqi.timeseries_groups.list(
            metric="BANDWIDTH",
        )
        assert_matches_type(TimeseriesGroupListResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        timeseries_group = client.radar.quality.iqi.timeseries_groups.list(
            metric="BANDWIDTH",
            agg_interval="1h",
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            interpolation=True,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
        )
        assert_matches_type(TimeseriesGroupListResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.radar.quality.iqi.timeseries_groups.with_raw_response.list(
            metric="BANDWIDTH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = response.parse()
        assert_matches_type(TimeseriesGroupListResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.radar.quality.iqi.timeseries_groups.with_streaming_response.list(
            metric="BANDWIDTH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = response.parse()
            assert_matches_type(TimeseriesGroupListResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTimeseriesGroups:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.quality.iqi.timeseries_groups.list(
            metric="BANDWIDTH",
        )
        assert_matches_type(TimeseriesGroupListResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        timeseries_group = await async_client.radar.quality.iqi.timeseries_groups.list(
            metric="BANDWIDTH",
            agg_interval="1h",
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            interpolation=True,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
        )
        assert_matches_type(TimeseriesGroupListResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.quality.iqi.timeseries_groups.with_raw_response.list(
            metric="BANDWIDTH",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        timeseries_group = await response.parse()
        assert_matches_type(TimeseriesGroupListResponse, timeseries_group, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.quality.iqi.timeseries_groups.with_streaming_response.list(
            metric="BANDWIDTH",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            timeseries_group = await response.parse()
            assert_matches_type(TimeseriesGroupListResponse, timeseries_group, path=["response"])

        assert cast(Any, response.is_closed) is True
