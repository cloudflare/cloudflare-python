# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.radar import (
    HTTPBotClassesResponse,
    HTTPBrowserFamiliesResponse,
    HTTPBrowsersResponse,
    HTTPDeviceTypesResponse,
    HTTPHTTPProtocolsResponse,
    HTTPHTTPVersionsResponse,
    HTTPIPVersionsResponse,
    HTTPOssResponse,
)

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar import http_bot_classes_params
from cloudflare.types.radar import http_browser_families_params
from cloudflare.types.radar import http_browsers_params
from cloudflare.types.radar import http_device_types_params
from cloudflare.types.radar import http_http_protocols_params
from cloudflare.types.radar import http_http_versions_params
from cloudflare.types.radar import http_ip_versions_params
from cloudflare.types.radar import http_oss_params
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime
from cloudflare._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestHTTP:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_bot_classes(self, client: Cloudflare) -> None:
        http = client.radar.http.bot_classes()
        assert_matches_type(HTTPBotClassesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_bot_classes_with_all_params(self, client: Cloudflare) -> None:
        http = client.radar.http.bot_classes(
            agg_interval="1h",
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPBotClassesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_bot_classes(self, client: Cloudflare) -> None:
        response = client.radar.http.with_raw_response.bot_classes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(HTTPBotClassesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_bot_classes(self, client: Cloudflare) -> None:
        with client.radar.http.with_streaming_response.bot_classes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(HTTPBotClassesResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_browser_families(self, client: Cloudflare) -> None:
        http = client.radar.http.browser_families()
        assert_matches_type(HTTPBrowserFamiliesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_browser_families_with_all_params(self, client: Cloudflare) -> None:
        http = client.radar.http.browser_families(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPBrowserFamiliesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_browser_families(self, client: Cloudflare) -> None:
        response = client.radar.http.with_raw_response.browser_families()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(HTTPBrowserFamiliesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_browser_families(self, client: Cloudflare) -> None:
        with client.radar.http.with_streaming_response.browser_families() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(HTTPBrowserFamiliesResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_browsers(self, client: Cloudflare) -> None:
        http = client.radar.http.browsers()
        assert_matches_type(HTTPBrowsersResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_browsers_with_all_params(self, client: Cloudflare) -> None:
        http = client.radar.http.browsers(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit_per_group=4,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPBrowsersResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_browsers(self, client: Cloudflare) -> None:
        response = client.radar.http.with_raw_response.browsers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(HTTPBrowsersResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_browsers(self, client: Cloudflare) -> None:
        with client.radar.http.with_streaming_response.browsers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(HTTPBrowsersResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_device_types(self, client: Cloudflare) -> None:
        http = client.radar.http.device_types()
        assert_matches_type(HTTPDeviceTypesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_device_types_with_all_params(self, client: Cloudflare) -> None:
        http = client.radar.http.device_types(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPDeviceTypesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_device_types(self, client: Cloudflare) -> None:
        response = client.radar.http.with_raw_response.device_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(HTTPDeviceTypesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_device_types(self, client: Cloudflare) -> None:
        with client.radar.http.with_streaming_response.device_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(HTTPDeviceTypesResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_http_protocols(self, client: Cloudflare) -> None:
        http = client.radar.http.http_protocols()
        assert_matches_type(HTTPHTTPProtocolsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_http_protocols_with_all_params(self, client: Cloudflare) -> None:
        http = client.radar.http.http_protocols(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPHTTPProtocolsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_http_protocols(self, client: Cloudflare) -> None:
        response = client.radar.http.with_raw_response.http_protocols()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(HTTPHTTPProtocolsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_http_protocols(self, client: Cloudflare) -> None:
        with client.radar.http.with_streaming_response.http_protocols() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(HTTPHTTPProtocolsResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_http_versions(self, client: Cloudflare) -> None:
        http = client.radar.http.http_versions()
        assert_matches_type(HTTPHTTPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_http_versions_with_all_params(self, client: Cloudflare) -> None:
        http = client.radar.http.http_versions(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPHTTPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_http_versions(self, client: Cloudflare) -> None:
        response = client.radar.http.with_raw_response.http_versions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(HTTPHTTPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_http_versions(self, client: Cloudflare) -> None:
        with client.radar.http.with_streaming_response.http_versions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(HTTPHTTPVersionsResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_versions(self, client: Cloudflare) -> None:
        http = client.radar.http.ip_versions()
        assert_matches_type(HTTPIPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_versions_with_all_params(self, client: Cloudflare) -> None:
        http = client.radar.http.ip_versions(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPIPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip_versions(self, client: Cloudflare) -> None:
        response = client.radar.http.with_raw_response.ip_versions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(HTTPIPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip_versions(self, client: Cloudflare) -> None:
        with client.radar.http.with_streaming_response.ip_versions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(HTTPIPVersionsResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_oss(self, client: Cloudflare) -> None:
        http = client.radar.http.oss()
        assert_matches_type(HTTPOssResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_oss_with_all_params(self, client: Cloudflare) -> None:
        http = client.radar.http.oss(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPOssResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_oss(self, client: Cloudflare) -> None:
        response = client.radar.http.with_raw_response.oss()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = response.parse()
        assert_matches_type(HTTPOssResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_oss(self, client: Cloudflare) -> None:
        with client.radar.http.with_streaming_response.oss() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = response.parse()
            assert_matches_type(HTTPOssResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncHTTP:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_bot_classes(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.bot_classes()
        assert_matches_type(HTTPBotClassesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_bot_classes_with_all_params(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.bot_classes(
            agg_interval="1h",
            asn=["string", "string", "string"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPBotClassesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_bot_classes(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.with_raw_response.bot_classes()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(HTTPBotClassesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_bot_classes(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.with_streaming_response.bot_classes() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(HTTPBotClassesResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_browser_families(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.browser_families()
        assert_matches_type(HTTPBrowserFamiliesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_browser_families_with_all_params(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.browser_families(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPBrowserFamiliesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_browser_families(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.with_raw_response.browser_families()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(HTTPBrowserFamiliesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_browser_families(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.with_streaming_response.browser_families() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(HTTPBrowserFamiliesResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_browsers(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.browsers()
        assert_matches_type(HTTPBrowsersResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_browsers_with_all_params(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.browsers(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            limit_per_group=4,
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPBrowsersResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_browsers(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.with_raw_response.browsers()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(HTTPBrowsersResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_browsers(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.with_streaming_response.browsers() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(HTTPBrowsersResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_types(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.device_types()
        assert_matches_type(HTTPDeviceTypesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_device_types_with_all_params(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.device_types(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPDeviceTypesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_device_types(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.with_raw_response.device_types()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(HTTPDeviceTypesResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_device_types(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.with_streaming_response.device_types() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(HTTPDeviceTypesResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_http_protocols(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.http_protocols()
        assert_matches_type(HTTPHTTPProtocolsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_http_protocols_with_all_params(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.http_protocols(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPHTTPProtocolsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_http_protocols(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.with_raw_response.http_protocols()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(HTTPHTTPProtocolsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_http_protocols(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.with_streaming_response.http_protocols() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(HTTPHTTPProtocolsResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_http_versions(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.http_versions()
        assert_matches_type(HTTPHTTPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_http_versions_with_all_params(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.http_versions(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPHTTPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_http_versions(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.with_raw_response.http_versions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(HTTPHTTPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_http_versions(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.with_streaming_response.http_versions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(HTTPHTTPVersionsResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_versions(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.ip_versions()
        assert_matches_type(HTTPIPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_versions_with_all_params(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.ip_versions(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPIPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip_versions(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.with_raw_response.ip_versions()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(HTTPIPVersionsResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip_versions(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.with_streaming_response.ip_versions() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(HTTPIPVersionsResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_oss(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.oss()
        assert_matches_type(HTTPOssResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_oss_with_all_params(self, async_client: AsyncCloudflare) -> None:
        http = await async_client.radar.http.oss(
            agg_interval="1h",
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            date_end=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            date_range=["1d", "2d", "7d"],
            date_start=[
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
                parse_datetime("2019-12-27T18:11:19.117Z"),
            ],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(HTTPOssResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_oss(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.radar.http.with_raw_response.oss()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        http = await response.parse()
        assert_matches_type(HTTPOssResponse, http, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_oss(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.with_streaming_response.oss() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            http = await response.parse()
            assert_matches_type(HTTPOssResponse, http, path=["response"])

        assert cast(Any, response.is_closed) is True
