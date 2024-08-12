# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.spectrum import (
    AppGetResponse,
    AppCreateResponse,
    AppDeleteResponse,
    AppUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.create(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.create(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            origin_dns={
                "name": "origin.example.com",
                "ttl": 600,
                "type": "",
            },
            origin_port=22,
            protocol="tcp/22",
            argo_smart_routing=True,
            edge_ips={
                "connectivity": "all",
                "type": "dynamic",
            },
            ip_firewall=True,
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.create(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.create(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrum.apps.with_raw_response.create(
                zone="",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.update(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.update(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            origin_dns={
                "name": "origin.example.com",
                "ttl": 600,
                "type": "",
            },
            origin_port=22,
            protocol="tcp/22",
            argo_smart_routing=True,
            edge_ips={
                "connectivity": "all",
                "type": "dynamic",
            },
            ip_firewall=True,
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.update(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.update(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrum.apps.with_raw_response.update(
                app_id="ea95132c15732412d22c1476fa83f27a",
                zone="",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.spectrum.apps.with_raw_response.update(
                app_id="",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.list(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[object], app, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.list(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="protocol",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[object], app, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.list(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[object], app, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.list(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[object], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrum.apps.with_raw_response.list(
                zone="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.delete(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.delete(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.delete(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrum.apps.with_raw_response.delete(
                app_id="ea95132c15732412d22c1476fa83f27a",
                zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.spectrum.apps.with_raw_response.delete(
                app_id="",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.get(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppGetResponse, app, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.get(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(AppGetResponse, app, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.get(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(AppGetResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrum.apps.with_raw_response.get(
                app_id="ea95132c15732412d22c1476fa83f27a",
                zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.spectrum.apps.with_raw_response.get(
                app_id="",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncApps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.create(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.create(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            origin_dns={
                "name": "origin.example.com",
                "ttl": 600,
                "type": "",
            },
            origin_port=22,
            protocol="tcp/22",
            argo_smart_routing=True,
            edge_ips={
                "connectivity": "all",
                "type": "dynamic",
            },
            ip_firewall=True,
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.create(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.create(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrum.apps.with_raw_response.create(
                zone="",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.update(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.update(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            origin_dns={
                "name": "origin.example.com",
                "ttl": 600,
                "type": "",
            },
            origin_port=22,
            protocol="tcp/22",
            argo_smart_routing=True,
            edge_ips={
                "connectivity": "all",
                "type": "dynamic",
            },
            ip_firewall=True,
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.update(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.update(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrum.apps.with_raw_response.update(
                app_id="ea95132c15732412d22c1476fa83f27a",
                zone="",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.update(
                app_id="",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.list(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[object], app, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.list(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="protocol",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[object], app, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.list(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[object], app, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.list(
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[object], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrum.apps.with_raw_response.list(
                zone="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.delete(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.delete(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.delete(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrum.apps.with_raw_response.delete(
                app_id="ea95132c15732412d22c1476fa83f27a",
                zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.delete(
                app_id="",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.get(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AppGetResponse, app, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.get(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AppGetResponse, app, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.get(
            app_id="ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AppGetResponse, app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrum.apps.with_raw_response.get(
                app_id="ea95132c15732412d22c1476fa83f27a",
                zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.get(
                app_id="",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
            )
