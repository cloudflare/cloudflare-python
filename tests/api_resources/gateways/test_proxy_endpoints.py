# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.gateways import (
    ProxyEndpointUpdateResponse,
    ProxyEndpointListResponse,
    ProxyEndpointDeleteResponse,
    ProxyEndpointGetResponse,
    ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse,
    ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse,
)

from typing import Any, cast, Optional

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.gateways import proxy_endpoint_update_params
from cloudflare.types.gateways import proxy_endpoint_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProxyEndpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        proxy_endpoint = client.gateways.proxy_endpoints.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ProxyEndpointUpdateResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        proxy_endpoint = client.gateways.proxy_endpoints.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32", "192.0.2.1/32", "192.0.2.1/32"],
            name="Devops team",
            subdomain="oli3n9zkz5.proxy.cloudflare-gateway.com",
        )
        assert_matches_type(ProxyEndpointUpdateResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.gateways.proxy_endpoints.with_raw_response.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(ProxyEndpointUpdateResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.gateways.proxy_endpoints.with_streaming_response.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(ProxyEndpointUpdateResponse, proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        proxy_endpoint = client.gateways.proxy_endpoints.list(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ProxyEndpointListResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.gateways.proxy_endpoints.with_raw_response.list(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(ProxyEndpointListResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.gateways.proxy_endpoints.with_streaming_response.list(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(ProxyEndpointListResponse, proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        proxy_endpoint = client.gateways.proxy_endpoints.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ProxyEndpointDeleteResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.gateways.proxy_endpoints.with_raw_response.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(ProxyEndpointDeleteResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.gateways.proxy_endpoints.with_streaming_response.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(ProxyEndpointDeleteResponse, proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        proxy_endpoint = client.gateways.proxy_endpoints.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ProxyEndpointGetResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.gateways.proxy_endpoints.with_raw_response.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(ProxyEndpointGetResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.gateways.proxy_endpoints.with_streaming_response.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(ProxyEndpointGetResponse, proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(self, client: Cloudflare) -> None:
        proxy_endpoint = client.gateways.proxy_endpoints.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
            "699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32", "192.0.2.1/32", "192.0.2.1/32"],
            name="Devops team",
        )
        assert_matches_type(
            ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse, proxy_endpoint, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint_with_all_params(
        self, client: Cloudflare
    ) -> None:
        proxy_endpoint = client.gateways.proxy_endpoints.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
            "699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32", "192.0.2.1/32", "192.0.2.1/32"],
            name="Devops team",
            subdomain="oli3n9zkz5.proxy.cloudflare-gateway.com",
        )
        assert_matches_type(
            ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse, proxy_endpoint, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(self, client: Cloudflare) -> None:
        response = (
            client.gateways.proxy_endpoints.with_raw_response.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
                "699d98642c564d2e855e9661899b7252",
                ips=["192.0.2.1/32", "192.0.2.1/32", "192.0.2.1/32"],
                name="Devops team",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(
            ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse, proxy_endpoint, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.proxy_endpoints.with_streaming_response.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
            "699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32", "192.0.2.1/32", "192.0.2.1/32"],
            name="Devops team",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(
                ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse,
                proxy_endpoint,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(self, client: Cloudflare) -> None:
        proxy_endpoint = client.gateways.proxy_endpoints.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
            "699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(
            Optional[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse],
            proxy_endpoint,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(self, client: Cloudflare) -> None:
        response = (
            client.gateways.proxy_endpoints.with_raw_response.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
                "699d98642c564d2e855e9661899b7252",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = response.parse()
        assert_matches_type(
            Optional[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse],
            proxy_endpoint,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
        self, client: Cloudflare
    ) -> None:
        with client.gateways.proxy_endpoints.with_streaming_response.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = response.parse()
            assert_matches_type(
                Optional[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse],
                proxy_endpoint,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True


class TestAsyncProxyEndpoints:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.gateways.proxy_endpoints.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ProxyEndpointUpdateResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.gateways.proxy_endpoints.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32", "192.0.2.1/32", "192.0.2.1/32"],
            name="Devops team",
            subdomain="oli3n9zkz5.proxy.cloudflare-gateway.com",
        )
        assert_matches_type(ProxyEndpointUpdateResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.proxy_endpoints.with_raw_response.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(ProxyEndpointUpdateResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.proxy_endpoints.with_streaming_response.update(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(ProxyEndpointUpdateResponse, proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.gateways.proxy_endpoints.list(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ProxyEndpointListResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.proxy_endpoints.with_raw_response.list(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(ProxyEndpointListResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.proxy_endpoints.with_streaming_response.list(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(ProxyEndpointListResponse, proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.gateways.proxy_endpoints.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ProxyEndpointDeleteResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.proxy_endpoints.with_raw_response.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(ProxyEndpointDeleteResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.proxy_endpoints.with_streaming_response.delete(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(ProxyEndpointDeleteResponse, proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        proxy_endpoint = await async_client.gateways.proxy_endpoints.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(ProxyEndpointGetResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.gateways.proxy_endpoints.with_raw_response.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(ProxyEndpointGetResponse, proxy_endpoint, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.gateways.proxy_endpoints.with_streaming_response.get(
            "ed35569b41ce4d1facfe683550f54086",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(ProxyEndpointGetResponse, proxy_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
        self, async_client: AsyncCloudflare
    ) -> None:
        proxy_endpoint = (
            await async_client.gateways.proxy_endpoints.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
                "699d98642c564d2e855e9661899b7252",
                ips=["192.0.2.1/32", "192.0.2.1/32", "192.0.2.1/32"],
                name="Devops team",
            )
        )
        assert_matches_type(
            ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse, proxy_endpoint, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        proxy_endpoint = (
            await async_client.gateways.proxy_endpoints.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
                "699d98642c564d2e855e9661899b7252",
                ips=["192.0.2.1/32", "192.0.2.1/32", "192.0.2.1/32"],
                name="Devops team",
                subdomain="oli3n9zkz5.proxy.cloudflare-gateway.com",
            )
        )
        assert_matches_type(
            ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse, proxy_endpoint, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.proxy_endpoints.with_raw_response.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
            "699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32", "192.0.2.1/32", "192.0.2.1/32"],
            name="Devops team",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(
            ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse, proxy_endpoint, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.proxy_endpoints.with_streaming_response.zero_trust_gateway_proxy_endpoints_create_proxy_endpoint(
            "699d98642c564d2e855e9661899b7252",
            ips=["192.0.2.1/32", "192.0.2.1/32", "192.0.2.1/32"],
            name="Devops team",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(
                ProxyEndpointZeroTrustGatewayProxyEndpointsCreateProxyEndpointResponse,
                proxy_endpoint,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
        self, async_client: AsyncCloudflare
    ) -> None:
        proxy_endpoint = (
            await async_client.gateways.proxy_endpoints.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
                "699d98642c564d2e855e9661899b7252",
            )
        )
        assert_matches_type(
            Optional[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse],
            proxy_endpoint,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.gateways.proxy_endpoints.with_raw_response.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
            "699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        proxy_endpoint = await response.parse()
        assert_matches_type(
            Optional[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse],
            proxy_endpoint,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.gateways.proxy_endpoints.with_streaming_response.zero_trust_gateway_proxy_endpoints_list_proxy_endpoints(
            "699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            proxy_endpoint = await response.parse()
            assert_matches_type(
                Optional[ProxyEndpointZeroTrustGatewayProxyEndpointsListProxyEndpointsResponse],
                proxy_endpoint,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True
