# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.dlp.sensitivity_groups.levels import (
    OrderGetResponse,
    OrderUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrder:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        order = client.zero_trust.dlp.sensitivity_groups.levels.order.update(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            level_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(Optional[OrderUpdateResponse], order, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.update(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            level_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Optional[OrderUpdateResponse], order, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.sensitivity_groups.levels.order.with_streaming_response.update(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            level_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Optional[OrderUpdateResponse], order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.update(
                sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                level_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sensitivity_group_id` but received ''"):
            client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.update(
                sensitivity_group_id="",
                account_id="account_id",
                level_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        order = client.zero_trust.dlp.sensitivity_groups.levels.order.get(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[OrderGetResponse], order, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.get(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = response.parse()
        assert_matches_type(Optional[OrderGetResponse], order, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.dlp.sensitivity_groups.levels.order.with_streaming_response.get(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = response.parse()
            assert_matches_type(Optional[OrderGetResponse], order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.get(
                sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sensitivity_group_id` but received ''"):
            client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.get(
                sensitivity_group_id="",
                account_id="account_id",
            )


class TestAsyncOrder:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        order = await async_client.zero_trust.dlp.sensitivity_groups.levels.order.update(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            level_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(Optional[OrderUpdateResponse], order, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.update(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            level_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Optional[OrderUpdateResponse], order, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.sensitivity_groups.levels.order.with_streaming_response.update(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
            level_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Optional[OrderUpdateResponse], order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.update(
                sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
                level_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sensitivity_group_id` but received ''"):
            await async_client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.update(
                sensitivity_group_id="",
                account_id="account_id",
                level_ids=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        order = await async_client.zero_trust.dlp.sensitivity_groups.levels.order.get(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )
        assert_matches_type(Optional[OrderGetResponse], order, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.get(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        order = await response.parse()
        assert_matches_type(Optional[OrderGetResponse], order, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.dlp.sensitivity_groups.levels.order.with_streaming_response.get(
            sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            account_id="account_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            order = await response.parse()
            assert_matches_type(Optional[OrderGetResponse], order, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.get(
                sensitivity_group_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `sensitivity_group_id` but received ''"):
            await async_client.zero_trust.dlp.sensitivity_groups.levels.order.with_raw_response.get(
                sensitivity_group_id="",
                account_id="account_id",
            )
