# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.radar.http import SummaryBotClassResponse, SummaryDeviceTypeResponse, SummaryHTTPProtocolResponse, SummaryHTTPVersionResponse, SummaryIPVersionResponse, SummaryOSResponse, SummaryPostQuantumResponse, SummaryTLSVersionResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.http import summary_bot_class_params
from cloudflare.types.radar.http import summary_device_type_params
from cloudflare.types.radar.http import summary_http_protocol_params
from cloudflare.types.radar.http import summary_http_version_params
from cloudflare.types.radar.http import summary_ip_version_params
from cloudflare.types.radar.http import summary_os_params
from cloudflare.types.radar.http import summary_post_quantum_params
from cloudflare.types.radar.http import summary_tls_version_params
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

class TestSummary:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_bot_class(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.bot_class()
        assert_matches_type(SummaryBotClassResponse, summary, path=['response'])

    @parametrize
    def test_method_bot_class_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.bot_class(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
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
        assert_matches_type(SummaryBotClassResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_bot_class(self, client: Cloudflare) -> None:

        response = client.radar.http.summary.with_raw_response.bot_class()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryBotClassResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_bot_class(self, client: Cloudflare) -> None:
        with client.radar.http.summary.with_streaming_response.bot_class() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryBotClassResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_device_type(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.device_type()
        assert_matches_type(SummaryDeviceTypeResponse, summary, path=['response'])

    @parametrize
    def test_method_device_type_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.device_type(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryDeviceTypeResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_device_type(self, client: Cloudflare) -> None:

        response = client.radar.http.summary.with_raw_response.device_type()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryDeviceTypeResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_device_type(self, client: Cloudflare) -> None:
        with client.radar.http.summary.with_streaming_response.device_type() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryDeviceTypeResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_http_protocol(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.http_protocol()
        assert_matches_type(SummaryHTTPProtocolResponse, summary, path=['response'])

    @parametrize
    def test_method_http_protocol_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.http_protocol(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryHTTPProtocolResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_http_protocol(self, client: Cloudflare) -> None:

        response = client.radar.http.summary.with_raw_response.http_protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryHTTPProtocolResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_http_protocol(self, client: Cloudflare) -> None:
        with client.radar.http.summary.with_streaming_response.http_protocol() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryHTTPProtocolResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_http_version(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.http_version()
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=['response'])

    @parametrize
    def test_method_http_version_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.http_version(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_http_version(self, client: Cloudflare) -> None:

        response = client.radar.http.summary.with_raw_response.http_version()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_http_version(self, client: Cloudflare) -> None:
        with client.radar.http.summary.with_streaming_response.http_version() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryHTTPVersionResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_ip_version(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.ip_version()
        assert_matches_type(SummaryIPVersionResponse, summary, path=['response'])

    @parametrize
    def test_method_ip_version_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.ip_version(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryIPVersionResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_ip_version(self, client: Cloudflare) -> None:

        response = client.radar.http.summary.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryIPVersionResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_ip_version(self, client: Cloudflare) -> None:
        with client.radar.http.summary.with_streaming_response.ip_version() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryIPVersionResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_os(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.os()
        assert_matches_type(SummaryOSResponse, summary, path=['response'])

    @parametrize
    def test_method_os_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.os(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryOSResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_os(self, client: Cloudflare) -> None:

        response = client.radar.http.summary.with_raw_response.os()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryOSResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_os(self, client: Cloudflare) -> None:
        with client.radar.http.summary.with_streaming_response.os() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryOSResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_post_quantum(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.post_quantum()
        assert_matches_type(SummaryPostQuantumResponse, summary, path=['response'])

    @parametrize
    def test_method_post_quantum_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.post_quantum(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
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
        assert_matches_type(SummaryPostQuantumResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_post_quantum(self, client: Cloudflare) -> None:

        response = client.radar.http.summary.with_raw_response.post_quantum()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryPostQuantumResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_post_quantum(self, client: Cloudflare) -> None:
        with client.radar.http.summary.with_streaming_response.post_quantum() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryPostQuantumResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tls_version(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.tls_version()
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    def test_method_tls_version_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.http.summary.tls_version(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
        )
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_tls_version(self, client: Cloudflare) -> None:

        response = client.radar.http.summary.with_raw_response.tls_version()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_tls_version(self, client: Cloudflare) -> None:
        with client.radar.http.summary.with_streaming_response.tls_version() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_bot_class(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.bot_class()
        assert_matches_type(SummaryBotClassResponse, summary, path=['response'])

    @parametrize
    async def test_method_bot_class_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.bot_class(
            asn=["string", "string", "string"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
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
        assert_matches_type(SummaryBotClassResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_bot_class(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.http.summary.with_raw_response.bot_class()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryBotClassResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_bot_class(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.summary.with_streaming_response.bot_class() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryBotClassResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_device_type(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.device_type()
        assert_matches_type(SummaryDeviceTypeResponse, summary, path=['response'])

    @parametrize
    async def test_method_device_type_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.device_type(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryDeviceTypeResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_device_type(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.http.summary.with_raw_response.device_type()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryDeviceTypeResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_device_type(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.summary.with_streaming_response.device_type() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryDeviceTypeResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_http_protocol(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.http_protocol()
        assert_matches_type(SummaryHTTPProtocolResponse, summary, path=['response'])

    @parametrize
    async def test_method_http_protocol_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.http_protocol(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryHTTPProtocolResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_http_protocol(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.http.summary.with_raw_response.http_protocol()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryHTTPProtocolResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_http_protocol(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.summary.with_streaming_response.http_protocol() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryHTTPProtocolResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_http_version(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.http_version()
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=['response'])

    @parametrize
    async def test_method_http_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.http_version(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_http_version(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.http.summary.with_raw_response.http_version()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryHTTPVersionResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_http_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.summary.with_streaming_response.http_version() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryHTTPVersionResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_ip_version(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.ip_version()
        assert_matches_type(SummaryIPVersionResponse, summary, path=['response'])

    @parametrize
    async def test_method_ip_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.ip_version(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryIPVersionResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_ip_version(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.http.summary.with_raw_response.ip_version()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryIPVersionResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_ip_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.summary.with_streaming_response.ip_version() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryIPVersionResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_os(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.os()
        assert_matches_type(SummaryOSResponse, summary, path=['response'])

    @parametrize
    async def test_method_os_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.os(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryOSResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_os(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.http.summary.with_raw_response.os()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryOSResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_os(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.summary.with_streaming_response.os() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryOSResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_post_quantum(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.post_quantum()
        assert_matches_type(SummaryPostQuantumResponse, summary, path=['response'])

    @parametrize
    async def test_method_post_quantum_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.post_quantum(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
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
        assert_matches_type(SummaryPostQuantumResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_post_quantum(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.http.summary.with_raw_response.post_quantum()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryPostQuantumResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_post_quantum(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.summary.with_streaming_response.post_quantum() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryPostQuantumResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tls_version(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.tls_version()
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    async def test_method_tls_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.http.summary.tls_version(
            asn=["string", "string", "string"],
            bot_class=["LIKELY_AUTOMATED", "LIKELY_HUMAN"],
            continent=["string", "string", "string"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            device_type=["DESKTOP", "MOBILE", "OTHER"],
            format="JSON",
            http_protocol=["HTTP", "HTTPS"],
            http_version=["HTTPv1", "HTTPv2", "HTTPv3"],
            ip_version=["IPv4", "IPv6"],
            location=["string", "string", "string"],
            name=["string", "string", "string"],
            os=["WINDOWS", "MACOSX", "IOS"],
        )
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_tls_version(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.http.summary.with_raw_response.tls_version()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_tls_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.http.summary.with_streaming_response.tls_version() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True