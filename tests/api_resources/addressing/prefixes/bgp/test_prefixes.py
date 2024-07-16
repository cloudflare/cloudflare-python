# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.addressing.prefixes.bgp import BGPPrefix

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPrefixes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        prefix = client.addressing.prefixes.bgp.prefixes.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[BGPPrefix], prefix, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bgp.prefixes.with_raw_response.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(SyncSinglePage[BGPPrefix], prefix, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bgp.prefixes.with_streaming_response.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(SyncSinglePage[BGPPrefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp.prefixes.with_raw_response.list(
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp.prefixes.with_raw_response.list(
                prefix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        prefix = client.addressing.prefixes.bgp.prefixes.edit(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        prefix = client.addressing.prefixes.bgp.prefixes.edit(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            on_demand={"advertised": True},
        )
        assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bgp.prefixes.with_raw_response.edit(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bgp.prefixes.with_streaming_response.edit(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp.prefixes.with_raw_response.edit(
                bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp.prefixes.with_raw_response.edit(
                bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            client.addressing.prefixes.bgp.prefixes.with_raw_response.edit(
                bgp_prefix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        prefix = client.addressing.prefixes.bgp.prefixes.get(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bgp.prefixes.with_raw_response.get(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = response.parse()
        assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bgp.prefixes.with_streaming_response.get(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = response.parse()
            assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp.prefixes.with_raw_response.get(
                bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp.prefixes.with_raw_response.get(
                bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            client.addressing.prefixes.bgp.prefixes.with_raw_response.get(
                bgp_prefix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncPrefixes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addressing.prefixes.bgp.prefixes.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[BGPPrefix], prefix, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(AsyncSinglePage[BGPPrefix], prefix, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bgp.prefixes.with_streaming_response.list(
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(AsyncSinglePage[BGPPrefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.list(
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.list(
                prefix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addressing.prefixes.bgp.prefixes.edit(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addressing.prefixes.bgp.prefixes.edit(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            on_demand={"advertised": True},
        )
        assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.edit(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bgp.prefixes.with_streaming_response.edit(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.edit(
                bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.edit(
                bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.edit(
                bgp_prefix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        prefix = await async_client.addressing.prefixes.bgp.prefixes.get(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.get(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        prefix = await response.parse()
        assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bgp.prefixes.with_streaming_response.get(
            bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            prefix = await response.parse()
            assert_matches_type(Optional[BGPPrefix], prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.get(
                bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.get(
                bgp_prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp.prefixes.with_raw_response.get(
                bgp_prefix_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
                prefix_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
