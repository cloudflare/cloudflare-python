# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.addressing.prefixes import BGPPrefixUpdateResponse, BGPPrefixListResponse, BGPPrefixGetResponse

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.addressing.prefixes import bgp_prefix_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBGPPrefixes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        bgp_prefix = client.addressing.prefixes.bgp_prefixes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BGPPrefixUpdateResponse, bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        bgp_prefix = client.addressing.prefixes.bgp_prefixes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            on_demand={"advertised": True},
        )
        assert_matches_type(BGPPrefixUpdateResponse, bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bgp_prefixes.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = response.parse()
        assert_matches_type(BGPPrefixUpdateResponse, bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bgp_prefixes.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = response.parse()
            assert_matches_type(BGPPrefixUpdateResponse, bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        bgp_prefix = client.addressing.prefixes.bgp_prefixes.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[BGPPrefixListResponse], bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = response.parse()
        assert_matches_type(Optional[BGPPrefixListResponse], bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bgp_prefixes.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = response.parse()
            assert_matches_type(Optional[BGPPrefixListResponse], bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bgp_prefix = client.addressing.prefixes.bgp_prefixes.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BGPPrefixGetResponse, bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = response.parse()
        assert_matches_type(BGPPrefixGetResponse, bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bgp_prefixes.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = response.parse()
            assert_matches_type(BGPPrefixGetResponse, bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncBGPPrefixes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        bgp_prefix = await async_client.addressing.prefixes.bgp_prefixes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BGPPrefixUpdateResponse, bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bgp_prefix = await async_client.addressing.prefixes.bgp_prefixes.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            on_demand={"advertised": True},
        )
        assert_matches_type(BGPPrefixUpdateResponse, bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = await response.parse()
        assert_matches_type(BGPPrefixUpdateResponse, bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bgp_prefixes.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = await response.parse()
            assert_matches_type(BGPPrefixUpdateResponse, bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.update(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        bgp_prefix = await async_client.addressing.prefixes.bgp_prefixes.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[BGPPrefixListResponse], bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = await response.parse()
        assert_matches_type(Optional[BGPPrefixListResponse], bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bgp_prefixes.with_streaming_response.list(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = await response.parse()
            assert_matches_type(Optional[BGPPrefixListResponse], bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bgp_prefix = await async_client.addressing.prefixes.bgp_prefixes.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(BGPPrefixGetResponse, bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = await response.parse()
        assert_matches_type(BGPPrefixGetResponse, bgp_prefix, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bgp_prefixes.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = await response.parse()
            assert_matches_type(BGPPrefixGetResponse, bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                "",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
