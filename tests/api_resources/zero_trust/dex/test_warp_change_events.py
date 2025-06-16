# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dex import WARPChangeEventGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWARPChangeEvents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        warp_change_event = client.zero_trust.dex.warp_change_events.get(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-09-20T17:00:00Z",
            page=1,
            per_page=1,
            to="2023-09-20T17:00:00Z",
        )
        assert_matches_type(Optional[WARPChangeEventGetResponse], warp_change_event, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Cloudflare) -> None:
        warp_change_event = client.zero_trust.dex.warp_change_events.get(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-09-20T17:00:00Z",
            page=1,
            per_page=1,
            to="2023-09-20T17:00:00Z",
            account_name="Myorg",
            config_name="MASQUE",
            sort_order="ASC",
            toggle="on",
            type="config",
        )
        assert_matches_type(Optional[WARPChangeEventGetResponse], warp_change_event, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dex.warp_change_events.with_raw_response.get(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-09-20T17:00:00Z",
            page=1,
            per_page=1,
            to="2023-09-20T17:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_change_event = response.parse()
        assert_matches_type(Optional[WARPChangeEventGetResponse], warp_change_event, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dex.warp_change_events.with_streaming_response.get(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-09-20T17:00:00Z",
            page=1,
            per_page=1,
            to="2023-09-20T17:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_change_event = response.parse()
            assert_matches_type(Optional[WARPChangeEventGetResponse], warp_change_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dex.warp_change_events.with_raw_response.get(
                account_id="",
                from_="2023-09-20T17:00:00Z",
                page=1,
                per_page=1,
                to="2023-09-20T17:00:00Z",
            )


class TestAsyncWARPChangeEvents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        warp_change_event = await async_client.zero_trust.dex.warp_change_events.get(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-09-20T17:00:00Z",
            page=1,
            per_page=1,
            to="2023-09-20T17:00:00Z",
        )
        assert_matches_type(Optional[WARPChangeEventGetResponse], warp_change_event, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncCloudflare) -> None:
        warp_change_event = await async_client.zero_trust.dex.warp_change_events.get(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-09-20T17:00:00Z",
            page=1,
            per_page=1,
            to="2023-09-20T17:00:00Z",
            account_name="Myorg",
            config_name="MASQUE",
            sort_order="ASC",
            toggle="on",
            type="config",
        )
        assert_matches_type(Optional[WARPChangeEventGetResponse], warp_change_event, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dex.warp_change_events.with_raw_response.get(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-09-20T17:00:00Z",
            page=1,
            per_page=1,
            to="2023-09-20T17:00:00Z",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        warp_change_event = await response.parse()
        assert_matches_type(Optional[WARPChangeEventGetResponse], warp_change_event, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dex.warp_change_events.with_streaming_response.get(
            account_id="01a7362d577a6c3019a474fd6f485823",
            from_="2023-09-20T17:00:00Z",
            page=1,
            per_page=1,
            to="2023-09-20T17:00:00Z",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            warp_change_event = await response.parse()
            assert_matches_type(Optional[WARPChangeEventGetResponse], warp_change_event, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dex.warp_change_events.with_raw_response.get(
                account_id="",
                from_="2023-09-20T17:00:00Z",
                page=1,
                per_page=1,
                to="2023-09-20T17:00:00Z",
            )
