# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.dex.fleet_status import over_time_list_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOverTime:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        over_time = client.dex.fleet_status.over_time.list(
            "01a7362d577a6c3019a474fd6f485823",
            time_end="2023-10-11T00:00:00Z",
            time_start="2023-10-11T00:00:00Z",
        )
        assert over_time is None

    @pytest.mark.skip()
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        over_time = client.dex.fleet_status.over_time.list(
            "01a7362d577a6c3019a474fd6f485823",
            time_end="2023-10-11T00:00:00Z",
            time_start="2023-10-11T00:00:00Z",
            colo="SJC",
            device_id="cb49c27f-7f97-49c5-b6f3-f7c01ead0fd7",
        )
        assert over_time is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.dex.fleet_status.over_time.with_raw_response.list(
            "01a7362d577a6c3019a474fd6f485823",
            time_end="2023-10-11T00:00:00Z",
            time_start="2023-10-11T00:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        over_time = response.parse()
        assert over_time is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.dex.fleet_status.over_time.with_streaming_response.list(
            "01a7362d577a6c3019a474fd6f485823",
            time_end="2023-10-11T00:00:00Z",
            time_start="2023-10-11T00:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            over_time = response.parse()
            assert over_time is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.dex.fleet_status.over_time.with_raw_response.list(
                "",
                time_end="2023-10-11T00:00:00Z",
                time_start="2023-10-11T00:00:00Z",
            )


class TestAsyncOverTime:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        over_time = await async_client.dex.fleet_status.over_time.list(
            "01a7362d577a6c3019a474fd6f485823",
            time_end="2023-10-11T00:00:00Z",
            time_start="2023-10-11T00:00:00Z",
        )
        assert over_time is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        over_time = await async_client.dex.fleet_status.over_time.list(
            "01a7362d577a6c3019a474fd6f485823",
            time_end="2023-10-11T00:00:00Z",
            time_start="2023-10-11T00:00:00Z",
            colo="SJC",
            device_id="cb49c27f-7f97-49c5-b6f3-f7c01ead0fd7",
        )
        assert over_time is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.dex.fleet_status.over_time.with_raw_response.list(
            "01a7362d577a6c3019a474fd6f485823",
            time_end="2023-10-11T00:00:00Z",
            time_start="2023-10-11T00:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        over_time = await response.parse()
        assert over_time is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.dex.fleet_status.over_time.with_streaming_response.list(
            "01a7362d577a6c3019a474fd6f485823",
            time_end="2023-10-11T00:00:00Z",
            time_start="2023-10-11T00:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            over_time = await response.parse()
            assert over_time is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.dex.fleet_status.over_time.with_raw_response.list(
                "",
                time_end="2023-10-11T00:00:00Z",
                time_start="2023-10-11T00:00:00Z",
            )
