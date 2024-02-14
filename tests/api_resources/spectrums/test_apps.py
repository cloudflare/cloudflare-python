# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from typing import Optional, Any, cast

from cloudflare.types.spectrums import (
    AppUpdateResponse,
    AppDeleteResponse,
    AppGetResponse,
    AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse,
    AppSpectrumApplicationsListSpectrumApplicationsResponse,
)

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.spectrums import app_update_params
from cloudflare.types.spectrums import (
    app_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_params,
)
from cloudflare.types.spectrums import app_spectrum_applications_list_spectrum_applications_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApps:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        app = client.spectrums.apps.update(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        app = client.spectrums.apps.update(
            "ea95132c15732412d22c1476fa83f27a",
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
            tls="full",
            traffic_type="direct",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.spectrums.apps.with_raw_response.update(
            "ea95132c15732412d22c1476fa83f27a",
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

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.spectrums.apps.with_streaming_response.update(
            "ea95132c15732412d22c1476fa83f27a",
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

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrums.apps.with_raw_response.update(
                "ea95132c15732412d22c1476fa83f27a",
                zone="",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.spectrums.apps.with_raw_response.update(
                "",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        app = client.spectrums.apps.delete(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.spectrums.apps.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.spectrums.apps.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrums.apps.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.spectrums.apps.with_raw_response.delete(
                "",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        app = client.spectrums.apps.get(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppGetResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.spectrums.apps.with_raw_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppGetResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.spectrums.apps.with_streaming_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(Optional[AppGetResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrums.apps.with_raw_response.get(
                "ea95132c15732412d22c1476fa83f27a",
                zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            client.spectrums.apps.with_raw_response.get(
                "",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
        self, client: Cloudflare
    ) -> None:
        app = client.spectrums.apps.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )
        assert_matches_type(
            Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse],
            app,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_with_all_params(
        self, client: Cloudflare
    ) -> None:
        app = client.spectrums.apps.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
            tls="full",
            traffic_type="direct",
        )
        assert_matches_type(
            Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse],
            app,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
        self, client: Cloudflare
    ) -> None:
        response = client.spectrums.apps.with_raw_response.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(
            Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse],
            app,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
        self, client: Cloudflare
    ) -> None:
        with client.spectrums.apps.with_streaming_response.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(
                Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse],
                app,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrums.apps.with_raw_response.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
                "",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_spectrum_applications_list_spectrum_applications(self, client: Cloudflare) -> None:
        app = client.spectrums.apps.spectrum_applications_list_spectrum_applications(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_spectrum_applications_list_spectrum_applications_with_all_params(self, client: Cloudflare) -> None:
        app = client.spectrums.apps.spectrum_applications_list_spectrum_applications(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            order="protocol",
            page=1,
            per_page=1,
        )
        assert_matches_type(Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_spectrum_applications_list_spectrum_applications(self, client: Cloudflare) -> None:
        response = client.spectrums.apps.with_raw_response.spectrum_applications_list_spectrum_applications(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = response.parse()
        assert_matches_type(Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_spectrum_applications_list_spectrum_applications(self, client: Cloudflare) -> None:
        with client.spectrums.apps.with_streaming_response.spectrum_applications_list_spectrum_applications(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = response.parse()
            assert_matches_type(
                Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse], app, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_spectrum_applications_list_spectrum_applications(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            client.spectrums.apps.with_raw_response.spectrum_applications_list_spectrum_applications(
                "",
            )


class TestAsyncApps:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrums.apps.update(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrums.apps.update(
            "ea95132c15732412d22c1476fa83f27a",
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
            tls="full",
            traffic_type="direct",
        )
        assert_matches_type(Optional[AppUpdateResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrums.apps.with_raw_response.update(
            "ea95132c15732412d22c1476fa83f27a",
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

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrums.apps.with_streaming_response.update(
            "ea95132c15732412d22c1476fa83f27a",
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

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrums.apps.with_raw_response.update(
                "ea95132c15732412d22c1476fa83f27a",
                zone="",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.spectrums.apps.with_raw_response.update(
                "",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrums.apps.delete(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrums.apps.with_raw_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrums.apps.with_streaming_response.delete(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppDeleteResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrums.apps.with_raw_response.delete(
                "ea95132c15732412d22c1476fa83f27a",
                zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.spectrums.apps.with_raw_response.delete(
                "",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrums.apps.get(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppGetResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.spectrums.apps.with_raw_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppGetResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.spectrums.apps.with_streaming_response.get(
            "ea95132c15732412d22c1476fa83f27a",
            zone="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(Optional[AppGetResponse], app, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrums.apps.with_raw_response.get(
                "ea95132c15732412d22c1476fa83f27a",
                zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `app_id` but received ''"):
            await async_client.spectrums.apps.with_raw_response.get(
                "",
                zone="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
        self, async_client: AsyncCloudflare
    ) -> None:
        app = await async_client.spectrums.apps.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )
        assert_matches_type(
            Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse],
            app,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        app = await async_client.spectrums.apps.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
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
            tls="full",
            traffic_type="direct",
        )
        assert_matches_type(
            Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse],
            app,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.spectrums.apps.with_raw_response.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(
            Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse],
            app,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.spectrums.apps.with_streaming_response.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
            "023e105f4ecef8ad9ca31a8372d0c353",
            dns={},
            origin_dns={},
            origin_port=22,
            protocol="tcp/22",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(
                Optional[AppSpectrumApplicationsCreateSpectrumApplicationUsingANameForTheOriginResponse],
                app,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrums.apps.with_raw_response.spectrum_applications_create_spectrum_application_using_a_name_for_the_origin(
                "",
                dns={},
                origin_dns={},
                origin_port=22,
                protocol="tcp/22",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_spectrum_applications_list_spectrum_applications(self, async_client: AsyncCloudflare) -> None:
        app = await async_client.spectrums.apps.spectrum_applications_list_spectrum_applications(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_spectrum_applications_list_spectrum_applications_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        app = await async_client.spectrums.apps.spectrum_applications_list_spectrum_applications(
            "023e105f4ecef8ad9ca31a8372d0c353",
            direction="desc",
            order="protocol",
            page=1,
            per_page=1,
        )
        assert_matches_type(Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_spectrum_applications_list_spectrum_applications(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.spectrums.apps.with_raw_response.spectrum_applications_list_spectrum_applications(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        app = await response.parse()
        assert_matches_type(Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse], app, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_spectrum_applications_list_spectrum_applications(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.spectrums.apps.with_streaming_response.spectrum_applications_list_spectrum_applications(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            app = await response.parse()
            assert_matches_type(
                Optional[AppSpectrumApplicationsListSpectrumApplicationsResponse], app, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_spectrum_applications_list_spectrum_applications(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone` but received ''"):
            await async_client.spectrums.apps.with_raw_response.spectrum_applications_list_spectrum_applications(
                "",
            )
