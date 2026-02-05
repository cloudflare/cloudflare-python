# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._utils import parse_datetime
from cloudflare.types.radar import (
    LeakedCredentialSummaryV2Response,
    LeakedCredentialTimeseriesGroupsV2Response,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLeakedCredentials:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_summary_v2(self, client: Cloudflare) -> None:
        leaked_credential = client.radar.leaked_credentials.summary_v2(
            dimension="COMPROMISED",
        )
        assert_matches_type(LeakedCredentialSummaryV2Response, leaked_credential, path=["response"])

    @parametrize
    def test_method_summary_v2_with_all_params(self, client: Cloudflare) -> None:
        leaked_credential = client.radar.leaked_credentials.summary_v2(
            dimension="COMPROMISED",
            asn=["string"],
            bot_class=["LIKELY_AUTOMATED"],
            compromised=["CLEAN"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(LeakedCredentialSummaryV2Response, leaked_credential, path=["response"])

    @parametrize
    def test_raw_response_summary_v2(self, client: Cloudflare) -> None:
        response = client.radar.leaked_credentials.with_raw_response.summary_v2(
            dimension="COMPROMISED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        leaked_credential = response.parse()
        assert_matches_type(LeakedCredentialSummaryV2Response, leaked_credential, path=["response"])

    @parametrize
    def test_streaming_response_summary_v2(self, client: Cloudflare) -> None:
        with client.radar.leaked_credentials.with_streaming_response.summary_v2(
            dimension="COMPROMISED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            leaked_credential = response.parse()
            assert_matches_type(LeakedCredentialSummaryV2Response, leaked_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_timeseries_groups_v2(self, client: Cloudflare) -> None:
        leaked_credential = client.radar.leaked_credentials.timeseries_groups_v2(
            dimension="COMPROMISED",
        )
        assert_matches_type(LeakedCredentialTimeseriesGroupsV2Response, leaked_credential, path=["response"])

    @parametrize
    def test_method_timeseries_groups_v2_with_all_params(self, client: Cloudflare) -> None:
        leaked_credential = client.radar.leaked_credentials.timeseries_groups_v2(
            dimension="COMPROMISED",
            agg_interval="1h",
            asn=["string"],
            bot_class=["LIKELY_AUTOMATED"],
            check_result=["CLEAN"],
            compromised=["CLEAN"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            normalization="MIN0_MAX",
        )
        assert_matches_type(LeakedCredentialTimeseriesGroupsV2Response, leaked_credential, path=["response"])

    @parametrize
    def test_raw_response_timeseries_groups_v2(self, client: Cloudflare) -> None:
        response = client.radar.leaked_credentials.with_raw_response.timeseries_groups_v2(
            dimension="COMPROMISED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        leaked_credential = response.parse()
        assert_matches_type(LeakedCredentialTimeseriesGroupsV2Response, leaked_credential, path=["response"])

    @parametrize
    def test_streaming_response_timeseries_groups_v2(self, client: Cloudflare) -> None:
        with client.radar.leaked_credentials.with_streaming_response.timeseries_groups_v2(
            dimension="COMPROMISED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            leaked_credential = response.parse()
            assert_matches_type(LeakedCredentialTimeseriesGroupsV2Response, leaked_credential, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLeakedCredentials:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_summary_v2(self, async_client: AsyncCloudflare) -> None:
        leaked_credential = await async_client.radar.leaked_credentials.summary_v2(
            dimension="COMPROMISED",
        )
        assert_matches_type(LeakedCredentialSummaryV2Response, leaked_credential, path=["response"])

    @parametrize
    async def test_method_summary_v2_with_all_params(self, async_client: AsyncCloudflare) -> None:
        leaked_credential = await async_client.radar.leaked_credentials.summary_v2(
            dimension="COMPROMISED",
            asn=["string"],
            bot_class=["LIKELY_AUTOMATED"],
            compromised=["CLEAN"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
        )
        assert_matches_type(LeakedCredentialSummaryV2Response, leaked_credential, path=["response"])

    @parametrize
    async def test_raw_response_summary_v2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.leaked_credentials.with_raw_response.summary_v2(
            dimension="COMPROMISED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        leaked_credential = await response.parse()
        assert_matches_type(LeakedCredentialSummaryV2Response, leaked_credential, path=["response"])

    @parametrize
    async def test_streaming_response_summary_v2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.leaked_credentials.with_streaming_response.summary_v2(
            dimension="COMPROMISED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            leaked_credential = await response.parse()
            assert_matches_type(LeakedCredentialSummaryV2Response, leaked_credential, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_timeseries_groups_v2(self, async_client: AsyncCloudflare) -> None:
        leaked_credential = await async_client.radar.leaked_credentials.timeseries_groups_v2(
            dimension="COMPROMISED",
        )
        assert_matches_type(LeakedCredentialTimeseriesGroupsV2Response, leaked_credential, path=["response"])

    @parametrize
    async def test_method_timeseries_groups_v2_with_all_params(self, async_client: AsyncCloudflare) -> None:
        leaked_credential = await async_client.radar.leaked_credentials.timeseries_groups_v2(
            dimension="COMPROMISED",
            agg_interval="1h",
            asn=["string"],
            bot_class=["LIKELY_AUTOMATED"],
            check_result=["CLEAN"],
            compromised=["CLEAN"],
            continent=["string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            limit_per_group=10,
            location=["string"],
            name=["main_series"],
            normalization="MIN0_MAX",
        )
        assert_matches_type(LeakedCredentialTimeseriesGroupsV2Response, leaked_credential, path=["response"])

    @parametrize
    async def test_raw_response_timeseries_groups_v2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.leaked_credentials.with_raw_response.timeseries_groups_v2(
            dimension="COMPROMISED",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        leaked_credential = await response.parse()
        assert_matches_type(LeakedCredentialTimeseriesGroupsV2Response, leaked_credential, path=["response"])

    @parametrize
    async def test_streaming_response_timeseries_groups_v2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.leaked_credentials.with_streaming_response.timeseries_groups_v2(
            dimension="COMPROMISED",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            leaked_credential = await response.parse()
            assert_matches_type(LeakedCredentialTimeseriesGroupsV2Response, leaked_credential, path=["response"])

        assert cast(Any, response.is_closed) is True
