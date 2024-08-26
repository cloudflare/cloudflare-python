# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.zero_trust.networks import Route

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNetworks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        network = client.zero_trust.networks.routes.networks.create(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        network = client.zero_trust.networks.routes.networks.create(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            comment="Example comment for this route.",
            virtual_network_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.routes.networks.with_raw_response.create(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.routes.networks.with_streaming_response.create(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(Route, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.routes.networks.with_raw_response.create(
                ip_network_encoded="172.16.0.0%2F16",
                account_id="",
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_network_encoded` but received ''"):
            client.zero_trust.networks.routes.networks.with_raw_response.create(
                ip_network_encoded="",
                account_id="699d98642c564d2e855e9661899b7252",
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        network = client.zero_trust.networks.routes.networks.delete(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    def test_method_delete_with_all_params(self, client: Cloudflare) -> None:
        network = client.zero_trust.networks.routes.networks.delete(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
            tun_type="cfd_tunnel",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            virtual_network_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.routes.networks.with_raw_response.delete(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.routes.networks.with_streaming_response.delete(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(Route, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.routes.networks.with_raw_response.delete(
                ip_network_encoded="172.16.0.0%2F16",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_network_encoded` but received ''"):
            client.zero_trust.networks.routes.networks.with_raw_response.delete(
                ip_network_encoded="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_edit(self, client: Cloudflare) -> None:
        network = client.zero_trust.networks.routes.networks.edit(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    def test_raw_response_edit(self, client: Cloudflare) -> None:
        response = client.zero_trust.networks.routes.networks.with_raw_response.edit(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = response.parse()
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    def test_streaming_response_edit(self, client: Cloudflare) -> None:
        with client.zero_trust.networks.routes.networks.with_streaming_response.edit(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = response.parse()
            assert_matches_type(Route, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_edit(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.networks.routes.networks.with_raw_response.edit(
                ip_network_encoded="172.16.0.0%2F16",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_network_encoded` but received ''"):
            client.zero_trust.networks.routes.networks.with_raw_response.edit(
                ip_network_encoded="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncNetworks:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        network = await async_client.zero_trust.networks.routes.networks.create(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        network = await async_client.zero_trust.networks.routes.networks.create(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            comment="Example comment for this route.",
            virtual_network_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.routes.networks.with_raw_response.create(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.routes.networks.with_streaming_response.create(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(Route, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.routes.networks.with_raw_response.create(
                ip_network_encoded="172.16.0.0%2F16",
                account_id="",
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_network_encoded` but received ''"):
            await async_client.zero_trust.networks.routes.networks.with_raw_response.create(
                ip_network_encoded="",
                account_id="699d98642c564d2e855e9661899b7252",
                tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        network = await async_client.zero_trust.networks.routes.networks.delete(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    async def test_method_delete_with_all_params(self, async_client: AsyncCloudflare) -> None:
        network = await async_client.zero_trust.networks.routes.networks.delete(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
            tun_type="cfd_tunnel",
            tunnel_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
            virtual_network_id="f70ff985-a4ef-4643-bbbc-4a0ed4fc8415",
        )
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.routes.networks.with_raw_response.delete(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.routes.networks.with_streaming_response.delete(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(Route, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.routes.networks.with_raw_response.delete(
                ip_network_encoded="172.16.0.0%2F16",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_network_encoded` but received ''"):
            await async_client.zero_trust.networks.routes.networks.with_raw_response.delete(
                ip_network_encoded="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_edit(self, async_client: AsyncCloudflare) -> None:
        network = await async_client.zero_trust.networks.routes.networks.edit(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    async def test_raw_response_edit(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.networks.routes.networks.with_raw_response.edit(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        network = await response.parse()
        assert_matches_type(Route, network, path=["response"])

    @parametrize
    async def test_streaming_response_edit(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.networks.routes.networks.with_streaming_response.edit(
            ip_network_encoded="172.16.0.0%2F16",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            network = await response.parse()
            assert_matches_type(Route, network, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_edit(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.networks.routes.networks.with_raw_response.edit(
                ip_network_encoded="172.16.0.0%2F16",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `ip_network_encoded` but received ''"):
            await async_client.zero_trust.networks.routes.networks.with_raw_response.edit(
                ip_network_encoded="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
