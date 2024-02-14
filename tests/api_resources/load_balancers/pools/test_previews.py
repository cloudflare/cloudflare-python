# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.load_balancers.pools import (
    PreviewAccountLoadBalancerPoolsPreviewPoolResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreviews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_load_balancer_pools_preview_pool(self, client: Cloudflare) -> None:
        preview = client.load_balancers.pools.previews.account_load_balancer_pools_preview_pool(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )
        assert_matches_type(PreviewAccountLoadBalancerPoolsPreviewPoolResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_account_load_balancer_pools_preview_pool_with_all_params(self, client: Cloudflare) -> None:
        preview = client.load_balancers.pools.previews.account_load_balancer_pools_preview_pool(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
            allow_insecure=True,
            consecutive_down=0,
            consecutive_up=0,
            description="Login page monitor",
            expected_body="alive",
            follow_redirects=True,
            header={
                "Host": ["example.com"],
                "X-App-ID": ["abc123"],
            },
            interval=0,
            method="GET",
            path="/health",
            port=0,
            probe_zone="example.com",
            retries=0,
            api_timeout=0,
            type="https",
        )
        assert_matches_type(PreviewAccountLoadBalancerPoolsPreviewPoolResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_account_load_balancer_pools_preview_pool(self, client: Cloudflare) -> None:
        response = client.load_balancers.pools.previews.with_raw_response.account_load_balancer_pools_preview_pool(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = response.parse()
        assert_matches_type(PreviewAccountLoadBalancerPoolsPreviewPoolResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_account_load_balancer_pools_preview_pool(self, client: Cloudflare) -> None:
        with client.load_balancers.pools.previews.with_streaming_response.account_load_balancer_pools_preview_pool(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = response.parse()
            assert_matches_type(PreviewAccountLoadBalancerPoolsPreviewPoolResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_account_load_balancer_pools_preview_pool(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.load_balancers.pools.previews.with_raw_response.account_load_balancer_pools_preview_pool(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="",
                expected_codes="2xx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.load_balancers.pools.previews.with_raw_response.account_load_balancer_pools_preview_pool(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                expected_codes="2xx",
            )


class TestAsyncPreviews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_load_balancer_pools_preview_pool(self, async_client: AsyncCloudflare) -> None:
        preview = await async_client.load_balancers.pools.previews.account_load_balancer_pools_preview_pool(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        )
        assert_matches_type(PreviewAccountLoadBalancerPoolsPreviewPoolResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_account_load_balancer_pools_preview_pool_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        preview = await async_client.load_balancers.pools.previews.account_load_balancer_pools_preview_pool(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
            allow_insecure=True,
            consecutive_down=0,
            consecutive_up=0,
            description="Login page monitor",
            expected_body="alive",
            follow_redirects=True,
            header={
                "Host": ["example.com"],
                "X-App-ID": ["abc123"],
            },
            interval=0,
            method="GET",
            path="/health",
            port=0,
            probe_zone="example.com",
            retries=0,
            api_timeout=0,
            type="https",
        )
        assert_matches_type(PreviewAccountLoadBalancerPoolsPreviewPoolResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_account_load_balancer_pools_preview_pool(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.load_balancers.pools.previews.with_raw_response.account_load_balancer_pools_preview_pool(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                expected_codes="2xx",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preview = await response.parse()
        assert_matches_type(PreviewAccountLoadBalancerPoolsPreviewPoolResponse, preview, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_account_load_balancer_pools_preview_pool(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.load_balancers.pools.previews.with_streaming_response.account_load_balancer_pools_preview_pool(
            "17b5962d775c646f3f9725cbc7a53df4",
            account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            expected_codes="2xx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preview = await response.parse()
            assert_matches_type(PreviewAccountLoadBalancerPoolsPreviewPoolResponse, preview, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_account_load_balancer_pools_preview_pool(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.load_balancers.pools.previews.with_raw_response.account_load_balancer_pools_preview_pool(
                "17b5962d775c646f3f9725cbc7a53df4",
                account_identifier="",
                expected_codes="2xx",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.load_balancers.pools.previews.with_raw_response.account_load_balancer_pools_preview_pool(
                "",
                account_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                expected_codes="2xx",
            )
