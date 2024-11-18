# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.firewall.waf import (
    Override,
    OverrideDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOverrides:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        override = client.firewall.waf.overrides.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            urls=["shop.example.com/*"],
        )
        assert_matches_type(Override, override, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.firewall.waf.overrides.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            urls=["shop.example.com/*"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(Override, override, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.firewall.waf.overrides.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            urls=["shop.example.com/*"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(Override, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.waf.overrides.with_raw_response.create(
                zone_id="",
                urls=["shop.example.com/*"],
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        override = client.firewall.waf.overrides.update(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="023e105f4ecef8ad9ca31a8372d0c353",
            rewrite_action={},
            rules={"100015": "challenge"},
            urls=["shop.example.com/*"],
        )
        assert_matches_type(Override, override, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        override = client.firewall.waf.overrides.update(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="023e105f4ecef8ad9ca31a8372d0c353",
            rewrite_action={
                "block": "challenge",
                "challenge": "challenge",
                "default": "challenge",
                "disable": "challenge",
                "simulate": "challenge",
            },
            rules={"100015": "challenge"},
            urls=["shop.example.com/*"],
        )
        assert_matches_type(Override, override, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.firewall.waf.overrides.with_raw_response.update(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="023e105f4ecef8ad9ca31a8372d0c353",
            rewrite_action={},
            rules={"100015": "challenge"},
            urls=["shop.example.com/*"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(Override, override, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.firewall.waf.overrides.with_streaming_response.update(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="023e105f4ecef8ad9ca31a8372d0c353",
            rewrite_action={},
            rules={"100015": "challenge"},
            urls=["shop.example.com/*"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(Override, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.waf.overrides.with_raw_response.update(
                overrides_id="de677e5818985db1285d0e80225f06e5",
                zone_id="",
                id="023e105f4ecef8ad9ca31a8372d0c353",
                rewrite_action={},
                rules={"100015": "challenge"},
                urls=["shop.example.com/*"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `overrides_id` but received ''"):
            client.firewall.waf.overrides.with_raw_response.update(
                overrides_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="023e105f4ecef8ad9ca31a8372d0c353",
                rewrite_action={},
                rules={"100015": "challenge"},
                urls=["shop.example.com/*"],
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        override = client.firewall.waf.overrides.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[Override], override, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        override = client.firewall.waf.overrides.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(SyncV4PagePaginationArray[Override], override, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.firewall.waf.overrides.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Override], override, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.firewall.waf.overrides.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Override], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.waf.overrides.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        override = client.firewall.waf.overrides.delete(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.firewall.waf.overrides.with_raw_response.delete(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.firewall.waf.overrides.with_streaming_response.delete(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.waf.overrides.with_raw_response.delete(
                overrides_id="de677e5818985db1285d0e80225f06e5",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `overrides_id` but received ''"):
            client.firewall.waf.overrides.with_raw_response.delete(
                overrides_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        override = client.firewall.waf.overrides.get(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Override, override, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.firewall.waf.overrides.with_raw_response.get(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = response.parse()
        assert_matches_type(Override, override, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.firewall.waf.overrides.with_streaming_response.get(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = response.parse()
            assert_matches_type(Override, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.firewall.waf.overrides.with_raw_response.get(
                overrides_id="de677e5818985db1285d0e80225f06e5",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `overrides_id` but received ''"):
            client.firewall.waf.overrides.with_raw_response.get(
                overrides_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncOverrides:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewall.waf.overrides.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            urls=["shop.example.com/*"],
        )
        assert_matches_type(Override, override, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.waf.overrides.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            urls=["shop.example.com/*"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(Override, override, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.waf.overrides.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            urls=["shop.example.com/*"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(Override, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.waf.overrides.with_raw_response.create(
                zone_id="",
                urls=["shop.example.com/*"],
            )

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewall.waf.overrides.update(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="023e105f4ecef8ad9ca31a8372d0c353",
            rewrite_action={},
            rules={"100015": "challenge"},
            urls=["shop.example.com/*"],
        )
        assert_matches_type(Override, override, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewall.waf.overrides.update(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="023e105f4ecef8ad9ca31a8372d0c353",
            rewrite_action={
                "block": "challenge",
                "challenge": "challenge",
                "default": "challenge",
                "disable": "challenge",
                "simulate": "challenge",
            },
            rules={"100015": "challenge"},
            urls=["shop.example.com/*"],
        )
        assert_matches_type(Override, override, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.waf.overrides.with_raw_response.update(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="023e105f4ecef8ad9ca31a8372d0c353",
            rewrite_action={},
            rules={"100015": "challenge"},
            urls=["shop.example.com/*"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(Override, override, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.waf.overrides.with_streaming_response.update(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="023e105f4ecef8ad9ca31a8372d0c353",
            rewrite_action={},
            rules={"100015": "challenge"},
            urls=["shop.example.com/*"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(Override, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate broken test")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.waf.overrides.with_raw_response.update(
                overrides_id="de677e5818985db1285d0e80225f06e5",
                zone_id="",
                id="023e105f4ecef8ad9ca31a8372d0c353",
                rewrite_action={},
                rules={"100015": "challenge"},
                urls=["shop.example.com/*"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `overrides_id` but received ''"):
            await async_client.firewall.waf.overrides.with_raw_response.update(
                overrides_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                id="023e105f4ecef8ad9ca31a8372d0c353",
                rewrite_action={},
                rules={"100015": "challenge"},
                urls=["shop.example.com/*"],
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewall.waf.overrides.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Override], override, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewall.waf.overrides.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            page=1,
            per_page=5,
        )
        assert_matches_type(AsyncV4PagePaginationArray[Override], override, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.waf.overrides.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Override], override, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.waf.overrides.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Override], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.waf.overrides.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewall.waf.overrides.delete(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.waf.overrides.with_raw_response.delete(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.waf.overrides.with_streaming_response.delete(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(Optional[OverrideDeleteResponse], override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.waf.overrides.with_raw_response.delete(
                overrides_id="de677e5818985db1285d0e80225f06e5",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `overrides_id` but received ''"):
            await async_client.firewall.waf.overrides.with_raw_response.delete(
                overrides_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        override = await async_client.firewall.waf.overrides.get(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Override, override, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.firewall.waf.overrides.with_raw_response.get(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        override = await response.parse()
        assert_matches_type(Override, override, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.firewall.waf.overrides.with_streaming_response.get(
            overrides_id="de677e5818985db1285d0e80225f06e5",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            override = await response.parse()
            assert_matches_type(Override, override, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.firewall.waf.overrides.with_raw_response.get(
                overrides_id="de677e5818985db1285d0e80225f06e5",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `overrides_id` but received ''"):
            await async_client.firewall.waf.overrides.with_raw_response.get(
                overrides_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
