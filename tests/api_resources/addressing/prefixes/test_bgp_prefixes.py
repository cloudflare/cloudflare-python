# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.addressing.prefixes import BGPPrefix

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBGPPrefixes:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        bgp_prefix = client.addressing.prefixes.bgp_prefixes.create(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        bgp_prefix = client.addressing.prefixes.bgp_prefixes.create(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            cidr="192.0.2.0/24",
        )
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bgp_prefixes.with_raw_response.create(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = response.parse()
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bgp_prefixes.with_streaming_response.create(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = response.parse()
            assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.create(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.create(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        bgp_prefix = client.addressing.prefixes.bgp_prefixes.list(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(SyncSinglePage[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = response.parse()
        assert_matches_type(SyncSinglePage[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bgp_prefixes.with_streaming_response.list(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = response.parse()
            assert_matches_type(SyncSinglePage[BGPPrefix], bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        bgp_prefix = client.addressing.prefixes.bgp_prefixes.edit(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        )
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        bgp_prefix = client.addressing.prefixes.bgp_prefixes.edit(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            on_demand={"advertised": True},
        )
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bgp_prefixes.with_raw_response.edit(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = response.parse()
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bgp_prefixes.with_streaming_response.edit(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = response.parse()
            assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.edit(
                bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
                account_id="",
                prefix_id="2af39739cc4e3b5910c918468bb89828",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.edit(
                bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.edit(
                bgp_prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                prefix_id="2af39739cc4e3b5910c918468bb89828",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        bgp_prefix = client.addressing.prefixes.bgp_prefixes.get(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        )
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = response.parse()
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.addressing.prefixes.bgp_prefixes.with_streaming_response.get(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = response.parse()
            assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
                account_id="",
                prefix_id="2af39739cc4e3b5910c918468bb89828",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                bgp_prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                prefix_id="2af39739cc4e3b5910c918468bb89828",
            )


class TestAsyncBGPPrefixes:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        bgp_prefix = await async_client.addressing.prefixes.bgp_prefixes.create(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bgp_prefix = await async_client.addressing.prefixes.bgp_prefixes.create(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            cidr="192.0.2.0/24",
        )
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.create(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = await response.parse()
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bgp_prefixes.with_streaming_response.create(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = await response.parse()
            assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.create(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.create(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        bgp_prefix = await async_client.addressing.prefixes.bgp_prefixes.list(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )
        assert_matches_type(AsyncSinglePage[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = await response.parse()
        assert_matches_type(AsyncSinglePage[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bgp_prefixes.with_streaming_response.list(
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            account_id="258def64c72dae45f3e4c8516e2111f2",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = await response.parse()
            assert_matches_type(AsyncSinglePage[BGPPrefix], bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
                prefix_id="2af39739cc4e3b5910c918468bb89828",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.list(
                prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        bgp_prefix = await async_client.addressing.prefixes.bgp_prefixes.edit(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        )
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        bgp_prefix = await async_client.addressing.prefixes.bgp_prefixes.edit(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
            on_demand={"advertised": True},
        )
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.edit(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = await response.parse()
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bgp_prefixes.with_streaming_response.edit(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = await response.parse()
            assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.edit(
                bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
                account_id="",
                prefix_id="2af39739cc4e3b5910c918468bb89828",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.edit(
                bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.edit(
                bgp_prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                prefix_id="2af39739cc4e3b5910c918468bb89828",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        bgp_prefix = await async_client.addressing.prefixes.bgp_prefixes.get(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        )
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bgp_prefix = await response.parse()
        assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.addressing.prefixes.bgp_prefixes.with_streaming_response.get(
            bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
            account_id="258def64c72dae45f3e4c8516e2111f2",
            prefix_id="2af39739cc4e3b5910c918468bb89828",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bgp_prefix = await response.parse()
            assert_matches_type(Optional[BGPPrefix], bgp_prefix, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
                account_id="",
                prefix_id="2af39739cc4e3b5910c918468bb89828",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                bgp_prefix_id="7009ba364c7a5760798ceb430e603b74",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                prefix_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `bgp_prefix_id` but received ''"):
            await async_client.addressing.prefixes.bgp_prefixes.with_raw_response.get(
                bgp_prefix_id="",
                account_id="258def64c72dae45f3e4c8516e2111f2",
                prefix_id="2af39739cc4e3b5910c918468bb89828",
            )
