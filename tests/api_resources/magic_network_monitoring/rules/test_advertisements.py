# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.magic_network_monitoring.rules import Advertisement

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAdvertisements:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        advertisement = client.magic_network_monitoring.rules.advertisements.edit(
            rule_id="2890e6fa406311ed9b5a23f70f6fb8cf",
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )
        assert_matches_type(Optional[Advertisement], advertisement, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.magic_network_monitoring.rules.advertisements.with_raw_response.edit(
            rule_id="2890e6fa406311ed9b5a23f70f6fb8cf",
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advertisement = response.parse()
        assert_matches_type(Optional[Advertisement], advertisement, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.magic_network_monitoring.rules.advertisements.with_streaming_response.edit(
            rule_id="2890e6fa406311ed9b5a23f70f6fb8cf",
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advertisement = response.parse()
            assert_matches_type(Optional[Advertisement], advertisement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.magic_network_monitoring.rules.advertisements.with_raw_response.edit(
                rule_id="2890e6fa406311ed9b5a23f70f6fb8cf",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            client.magic_network_monitoring.rules.advertisements.with_raw_response.edit(
                rule_id="",
                account_id="6f91088a406011ed95aed352566e8d4c",
                body={},
            )


class TestAsyncAdvertisements:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        advertisement = await async_client.magic_network_monitoring.rules.advertisements.edit(
            rule_id="2890e6fa406311ed9b5a23f70f6fb8cf",
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )
        assert_matches_type(Optional[Advertisement], advertisement, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.magic_network_monitoring.rules.advertisements.with_raw_response.edit(
            rule_id="2890e6fa406311ed9b5a23f70f6fb8cf",
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        advertisement = await response.parse()
        assert_matches_type(Optional[Advertisement], advertisement, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.magic_network_monitoring.rules.advertisements.with_streaming_response.edit(
            rule_id="2890e6fa406311ed9b5a23f70f6fb8cf",
            account_id="6f91088a406011ed95aed352566e8d4c",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            advertisement = await response.parse()
            assert_matches_type(Optional[Advertisement], advertisement, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.magic_network_monitoring.rules.advertisements.with_raw_response.edit(
                rule_id="2890e6fa406311ed9b5a23f70f6fb8cf",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `rule_id` but received ''"):
            await async_client.magic_network_monitoring.rules.advertisements.with_raw_response.edit(
                rule_id="",
                account_id="6f91088a406011ed95aed352566e8d4c",
                body={},
            )
