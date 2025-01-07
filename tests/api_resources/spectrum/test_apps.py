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
    AppListResponse,
    AppCreateResponse,
    AppDeleteResponse,
    AppUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_create_overload_1(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
            argo_smart_routing=True,
            edge_ips={
                "connectivity": "all",
                "type": "dynamic",
            },
            origin_direct=["tcp://127.0.0.1:8080"],
            origin_dns={
                "name": "origin.example.com",
                "ttl": 600,
                "type": "",
            },
            origin_port=22,
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_create_overload_1(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_create_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.spectrum.apps.with_raw_response.create(
                zone_id="",
                dns={},
                ip_firewall=True,
                protocol="tcp/22",
                proxy_protocol="off",
                tls="off",
                traffic_type="direct",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_create_overload_2(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            protocol="tcp/22",
            origin_direct=["tcp://127.0.0.1:8080"],
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_create_overload_2(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_create_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.spectrum.apps.with_raw_response.create(
                zone_id="",
                dns={},
                protocol="tcp/22",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_update_overload_1(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
            argo_smart_routing=True,
            edge_ips={
                "connectivity": "all",
                "type": "dynamic",
            },
            origin_direct=["tcp://127.0.0.1:8080"],
            origin_dns={
                "name": "origin.example.com",
                "ttl": 600,
                "type": "",
            },
            origin_port=22,
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_update_overload_1(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_update_overload_1(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.spectrum.apps.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                dns={},
                ip_firewall=True,
                protocol="tcp/22",
                proxy_protocol="off",
                tls="off",
                traffic_type="direct",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.spectrum.apps.with_raw_response.update(
                app_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                dns={},
                ip_firewall=True,
                protocol="tcp/22",
                proxy_protocol="off",
                tls="off",
                traffic_type="direct",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_update_overload_2(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            protocol="tcp/22",
            origin_direct=["tcp://127.0.0.1:8080"],
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_update_overload_2(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_update_overload_2(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.spectrum.apps.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                dns={},
                protocol="tcp/22",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.spectrum.apps.with_raw_response.update(
                app_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                dns={},
                protocol="tcp/22",
            )

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[Optional[AppListResponse]], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="protocol",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[Optional[AppListResponse]], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[Optional[AppListResponse]], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(SyncV4PagePaginationArray[Optional[AppListResponse]], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.spectrum.apps.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.spectrum.apps.with_raw_response.delete(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.spectrum.apps.with_raw_response.delete(
                app_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        app = client.spectrum.apps.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppGetResponse], app, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.spectrum.apps.with_raw_response.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppGetResponse], app, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.spectrum.apps.with_streaming_response.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppGetResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.spectrum.apps.with_raw_response.get(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.spectrum.apps.with_raw_response.get(
                app_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncApps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
            argo_smart_routing=True,
            edge_ips={
                "connectivity": "all",
                "type": "dynamic",
            },
            origin_direct=["tcp://127.0.0.1:8080"],
            origin_dns={
                "name": "origin.example.com",
                "ttl": 600,
                "type": "",
            },
            origin_port=22,
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_create_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.create(
                zone_id="",
                dns={},
                ip_firewall=True,
                protocol="tcp/22",
                proxy_protocol="off",
                tls="off",
                traffic_type="direct",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            protocol="tcp/22",
            origin_direct=["tcp://127.0.0.1:8080"],
        )
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.create(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppCreateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_create_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.create(
                zone_id="",
                dns={},
                protocol="tcp/22",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
            argo_smart_routing=True,
            edge_ips={
                "connectivity": "all",
                "type": "dynamic",
            },
            origin_direct=["tcp://127.0.0.1:8080"],
            origin_dns={
                "name": "origin.example.com",
                "ttl": 600,
                "type": "",
            },
            origin_port=22,
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            ip_firewall=True,
            protocol="tcp/22",
            proxy_protocol="off",
            tls="off",
            traffic_type="direct",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                dns={},
                ip_firewall=True,
                protocol="tcp/22",
                proxy_protocol="off",
                tls="off",
                traffic_type="direct",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.update(
                app_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                dns={},
                ip_firewall=True,
                protocol="tcp/22",
                proxy_protocol="off",
                tls="off",
                traffic_type="direct",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={
                "name": "ssh.example.com",
                "type": "CNAME",
            },
            protocol="tcp/22",
            origin_direct=["tcp://127.0.0.1:8080"],
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.update(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            protocol="tcp/22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.update(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                dns={},
                protocol="tcp/22",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.update(
                app_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                dns={},
                protocol="tcp/22",
            )

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncV4PagePaginationArray[Optional[AppListResponse]], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            direction="asc",
            order="protocol",
            page=1,
            per_page=1,
        )
        assert_matches_type(AsyncV4PagePaginationArray[Optional[AppListResponse]], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(AsyncV4PagePaginationArray[Optional[AppListResponse]], app, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(AsyncV4PagePaginationArray[Optional[AppListResponse]], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate HTTP 422 errors on test suite")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.list(
                zone_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.delete(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.delete(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.delete(
                app_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrum.apps.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppGetResponse], app, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrum.apps.with_raw_response.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppGetResponse], app, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrum.apps.with_streaming_response.get(
            app_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppGetResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.get(
                app_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.spectrum.apps.with_raw_response.get(
                app_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
