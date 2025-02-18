# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.gateway import ProxyEndpoint

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProxyEndpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        proxy_endpoint = client.zero_trust.gateway.proxy_endpoints.create(
            account_id="699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32"],
            name="Devops team",
        )
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.proxy_endpoints.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32"],
            name="Devops team",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.proxy_endpoints.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32"],
            name="Devops team",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.proxy_endpoints.with_raw_response.create(
                account_id="",
                ips=["192.0.2.1/32"],
                name="Devops team",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        proxy_endpoint = client.zero_trust.gateway.proxy_endpoints.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.proxy_endpoints.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.proxy_endpoints.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.proxy_endpoints.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        proxy_endpoint = client.zero_trust.gateway.proxy_endpoints.delete(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(object, proxy_endpoint, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.proxy_endpoints.with_raw_response.delete(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(object, proxy_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.proxy_endpoints.with_streaming_response.delete(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(object, proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.proxy_endpoints.with_raw_response.delete(
                proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_endpoint_id` but received ''"):
            client.zero_trust.gateway.proxy_endpoints.with_raw_response.delete(
                proxy_endpoint_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        proxy_endpoint = client.zero_trust.gateway.proxy_endpoints.edit(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    def test_method_edit_with_all_params(self, client: Cloudflare) -> None:
        proxy_endpoint = client.zero_trust.gateway.proxy_endpoints.edit(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32"],
            name="Devops team",
        )
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.proxy_endpoints.with_raw_response.edit(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.proxy_endpoints.with_streaming_response.edit(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.proxy_endpoints.with_raw_response.edit(
                proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_endpoint_id` but received ''"):
            client.zero_trust.gateway.proxy_endpoints.with_raw_response.edit(
                proxy_endpoint_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        proxy_endpoint = client.zero_trust.gateway.proxy_endpoints.get(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.proxy_endpoints.with_raw_response.get(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(SyncSinglePage[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.proxy_endpoints.with_streaming_response.get(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(SyncSinglePage[ProxyEndpoint], proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.proxy_endpoints.with_raw_response.get(
                proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_endpoint_id` but received ''"):
            client.zero_trust.gateway.proxy_endpoints.with_raw_response.get(
                proxy_endpoint_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncProxyEndpoints:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.zero_trust.gateway.proxy_endpoints.create(
            account_id="699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32"],
            name="Devops team",
        )
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32"],
            name="Devops team",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.proxy_endpoints.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32"],
            name="Devops team",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.create(
                account_id="",
                ips=["192.0.2.1/32"],
                name="Devops team",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.zero_trust.gateway.proxy_endpoints.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.proxy_endpoints.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.zero_trust.gateway.proxy_endpoints.delete(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(object, proxy_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.delete(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(object, proxy_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.proxy_endpoints.with_streaming_response.delete(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(object, proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.delete(
                proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_endpoint_id` but received ''"):
            await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.delete(
                proxy_endpoint_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.zero_trust.gateway.proxy_endpoints.edit(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    async def test_method_edit_with_all_params(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.zero_trust.gateway.proxy_endpoints.edit(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32"],
            name="Devops team",
        )
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.edit(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.proxy_endpoints.with_streaming_response.edit(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(Optional[ProxyEndpoint], proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.edit(
                proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_endpoint_id` but received ''"):
            await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.edit(
                proxy_endpoint_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.zero_trust.gateway.proxy_endpoints.get(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.get(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(AsyncSinglePage[ProxyEndpoint], proxy_endpoint, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.proxy_endpoints.with_streaming_response.get(
            proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(AsyncSinglePage[ProxyEndpoint], proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.get(
                proxy_endpoint_id="ed35569b41ce4d1facfe683550f54086",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `proxy_endpoint_id` but received ''"):
            await async_client.zero_trust.gateway.proxy_endpoints.with_raw_response.get(
                proxy_endpoint_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
