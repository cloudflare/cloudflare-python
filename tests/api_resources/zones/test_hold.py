# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.zones import HoldEnforceResponse, HoldGetResponse, HoldRemoveResponse

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zones import hold_enforce_params
from cloudflare.types.zones import hold_remove_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHold:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_enforce(self, client: Cloudflare) -> None:
        hold = client.zones.hold.enforce(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HoldEnforceResponse, hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_enforce_with_all_params(self, client: Cloudflare) -> None:
        hold = client.zones.hold.enforce(
            "023e105f4ecef8ad9ca31a8372d0c353",
            include_subdomains=True,
        )
        assert_matches_type(HoldEnforceResponse, hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_enforce(self, client: Cloudflare) -> None:
        response = client.zones.hold.with_raw_response.enforce(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(HoldEnforceResponse, hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_enforce(self, client: Cloudflare) -> None:
        with client.zones.hold.with_streaming_response.enforce(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(HoldEnforceResponse, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_enforce(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.hold.with_raw_response.enforce(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        hold = client.zones.hold.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HoldGetResponse, hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zones.hold.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(HoldGetResponse, hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zones.hold.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(HoldGetResponse, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.hold.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_remove(self, client: Cloudflare) -> None:
        hold = client.zones.hold.remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HoldRemoveResponse], hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_remove_with_all_params(self, client: Cloudflare) -> None:
        hold = client.zones.hold.remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
            hold_after="string",
        )
        assert_matches_type(Optional[HoldRemoveResponse], hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_remove(self, client: Cloudflare) -> None:
        response = client.zones.hold.with_raw_response.remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = response.parse()
        assert_matches_type(Optional[HoldRemoveResponse], hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_remove(self, client: Cloudflare) -> None:
        with client.zones.hold.with_streaming_response.remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = response.parse()
            assert_matches_type(Optional[HoldRemoveResponse], hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_remove(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.zones.hold.with_raw_response.remove(
                "",
            )


class TestAsyncHold:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_enforce(self, async_client: AsyncCloudflare) -> None:
        hold = await async_client.zones.hold.enforce(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HoldEnforceResponse, hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_enforce_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hold = await async_client.zones.hold.enforce(
            "023e105f4ecef8ad9ca31a8372d0c353",
            include_subdomains=True,
        )
        assert_matches_type(HoldEnforceResponse, hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_enforce(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.hold.with_raw_response.enforce(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = await response.parse()
        assert_matches_type(HoldEnforceResponse, hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_enforce(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.hold.with_streaming_response.enforce(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(HoldEnforceResponse, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_enforce(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.hold.with_raw_response.enforce(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        hold = await async_client.zones.hold.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(HoldGetResponse, hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.hold.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = await response.parse()
        assert_matches_type(HoldGetResponse, hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.hold.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(HoldGetResponse, hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.hold.with_raw_response.get(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_remove(self, async_client: AsyncCloudflare) -> None:
        hold = await async_client.zones.hold.remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[HoldRemoveResponse], hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_remove_with_all_params(self, async_client: AsyncCloudflare) -> None:
        hold = await async_client.zones.hold.remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
            hold_after="string",
        )
        assert_matches_type(Optional[HoldRemoveResponse], hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_remove(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zones.hold.with_raw_response.remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        hold = await response.parse()
        assert_matches_type(Optional[HoldRemoveResponse], hold, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_remove(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zones.hold.with_streaming_response.remove(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            hold = await response.parse()
            assert_matches_type(Optional[HoldRemoveResponse], hold, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_remove(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.zones.hold.with_raw_response.remove(
                "",
            )
