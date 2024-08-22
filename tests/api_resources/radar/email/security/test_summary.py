# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from cloudflare.types.radar.email.security import SummaryARCResponse, SummaryDKIMResponse, SummaryDMARCResponse, SummaryMaliciousResponse, SummarySpamResponse, SummarySPFResponse, SummarySpoofResponse, SummaryThreatCategoryResponse, SummaryTLSVersionResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.radar.email.security import summary_arc_params
from cloudflare.types.radar.email.security import summary_dkim_params
from cloudflare.types.radar.email.security import summary_dmarc_params
from cloudflare.types.radar.email.security import summary_malicious_params
from cloudflare.types.radar.email.security import summary_spam_params
from cloudflare.types.radar.email.security import summary_spf_params
from cloudflare.types.radar.email.security import summary_spoof_params
from cloudflare.types.radar.email.security import summary_threat_category_params
from cloudflare.types.radar.email.security import summary_tls_version_params
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
    def test_method_arc(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.arc()
        assert_matches_type(SummaryARCResponse, summary, path=['response'])

    @parametrize
    def test_method_arc_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.arc(
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryARCResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_arc(self, client: Cloudflare) -> None:

        response = client.radar.email.security.summary.with_raw_response.arc()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryARCResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_arc(self, client: Cloudflare) -> None:
        with client.radar.email.security.summary.with_streaming_response.arc() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryARCResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dkim(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.dkim()
        assert_matches_type(SummaryDKIMResponse, summary, path=['response'])

    @parametrize
    def test_method_dkim_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.dkim(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryDKIMResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_dkim(self, client: Cloudflare) -> None:

        response = client.radar.email.security.summary.with_raw_response.dkim()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryDKIMResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_dkim(self, client: Cloudflare) -> None:
        with client.radar.email.security.summary.with_streaming_response.dkim() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryDKIMResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dmarc(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.dmarc()
        assert_matches_type(SummaryDMARCResponse, summary, path=['response'])

    @parametrize
    def test_method_dmarc_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.dmarc(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryDMARCResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_dmarc(self, client: Cloudflare) -> None:

        response = client.radar.email.security.summary.with_raw_response.dmarc()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryDMARCResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_dmarc(self, client: Cloudflare) -> None:
        with client.radar.email.security.summary.with_streaming_response.dmarc() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryDMARCResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_malicious(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.malicious()
        assert_matches_type(SummaryMaliciousResponse, summary, path=['response'])

    @parametrize
    def test_method_malicious_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.malicious(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryMaliciousResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_malicious(self, client: Cloudflare) -> None:

        response = client.radar.email.security.summary.with_raw_response.malicious()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryMaliciousResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_malicious(self, client: Cloudflare) -> None:
        with client.radar.email.security.summary.with_streaming_response.malicious() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryMaliciousResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_spam(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.spam()
        assert_matches_type(SummarySpamResponse, summary, path=['response'])

    @parametrize
    def test_method_spam_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.spam(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummarySpamResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_spam(self, client: Cloudflare) -> None:

        response = client.radar.email.security.summary.with_raw_response.spam()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummarySpamResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_spam(self, client: Cloudflare) -> None:
        with client.radar.email.security.summary.with_streaming_response.spam() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummarySpamResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_spf(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.spf()
        assert_matches_type(SummarySPFResponse, summary, path=['response'])

    @parametrize
    def test_method_spf_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.spf(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummarySPFResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_spf(self, client: Cloudflare) -> None:

        response = client.radar.email.security.summary.with_raw_response.spf()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummarySPFResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_spf(self, client: Cloudflare) -> None:
        with client.radar.email.security.summary.with_streaming_response.spf() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummarySPFResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_spoof(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.spoof()
        assert_matches_type(SummarySpoofResponse, summary, path=['response'])

    @parametrize
    def test_method_spoof_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.spoof(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummarySpoofResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_spoof(self, client: Cloudflare) -> None:

        response = client.radar.email.security.summary.with_raw_response.spoof()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummarySpoofResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_spoof(self, client: Cloudflare) -> None:
        with client.radar.email.security.summary.with_streaming_response.spoof() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummarySpoofResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_threat_category(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.threat_category()
        assert_matches_type(SummaryThreatCategoryResponse, summary, path=['response'])

    @parametrize
    def test_method_threat_category_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.threat_category(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryThreatCategoryResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_threat_category(self, client: Cloudflare) -> None:

        response = client.radar.email.security.summary.with_raw_response.threat_category()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryThreatCategoryResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_threat_category(self, client: Cloudflare) -> None:
        with client.radar.email.security.summary.with_streaming_response.threat_category() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryThreatCategoryResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_tls_version(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.tls_version()
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    def test_method_tls_version_with_all_params(self, client: Cloudflare) -> None:
        summary = client.radar.email.security.summary.tls_version(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
        )
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    def test_raw_response_tls_version(self, client: Cloudflare) -> None:

        response = client.radar.email.security.summary.with_raw_response.tls_version()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = response.parse()
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    def test_streaming_response_tls_version(self, client: Cloudflare) -> None:
        with client.radar.email.security.summary.with_streaming_response.tls_version() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = response.parse()
            assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True
class TestAsyncSummary:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_arc(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.arc()
        assert_matches_type(SummaryARCResponse, summary, path=['response'])

    @parametrize
    async def test_method_arc_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.arc(
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryARCResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_arc(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.email.security.summary.with_raw_response.arc()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryARCResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_arc(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.summary.with_streaming_response.arc() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryARCResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dkim(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.dkim()
        assert_matches_type(SummaryDKIMResponse, summary, path=['response'])

    @parametrize
    async def test_method_dkim_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.dkim(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryDKIMResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_dkim(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.email.security.summary.with_raw_response.dkim()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryDKIMResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_dkim(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.summary.with_streaming_response.dkim() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryDKIMResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dmarc(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.dmarc()
        assert_matches_type(SummaryDMARCResponse, summary, path=['response'])

    @parametrize
    async def test_method_dmarc_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.dmarc(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryDMARCResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_dmarc(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.email.security.summary.with_raw_response.dmarc()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryDMARCResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_dmarc(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.summary.with_streaming_response.dmarc() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryDMARCResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_malicious(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.malicious()
        assert_matches_type(SummaryMaliciousResponse, summary, path=['response'])

    @parametrize
    async def test_method_malicious_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.malicious(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryMaliciousResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_malicious(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.email.security.summary.with_raw_response.malicious()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryMaliciousResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_malicious(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.summary.with_streaming_response.malicious() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryMaliciousResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_spam(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.spam()
        assert_matches_type(SummarySpamResponse, summary, path=['response'])

    @parametrize
    async def test_method_spam_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.spam(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummarySpamResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_spam(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.email.security.summary.with_raw_response.spam()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummarySpamResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_spam(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.summary.with_streaming_response.spam() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummarySpamResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_spf(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.spf()
        assert_matches_type(SummarySPFResponse, summary, path=['response'])

    @parametrize
    async def test_method_spf_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.spf(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummarySPFResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_spf(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.email.security.summary.with_raw_response.spf()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummarySPFResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_spf(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.summary.with_streaming_response.spf() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummarySPFResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_spoof(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.spoof()
        assert_matches_type(SummarySpoofResponse, summary, path=['response'])

    @parametrize
    async def test_method_spoof_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.spoof(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummarySpoofResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_spoof(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.email.security.summary.with_raw_response.spoof()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummarySpoofResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_spoof(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.summary.with_streaming_response.spoof() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummarySpoofResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_threat_category(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.threat_category()
        assert_matches_type(SummaryThreatCategoryResponse, summary, path=['response'])

    @parametrize
    async def test_method_threat_category_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.threat_category(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
            tls_version=["TLSv1_0", "TLSv1_1", "TLSv1_2"],
        )
        assert_matches_type(SummaryThreatCategoryResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_threat_category(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.email.security.summary.with_raw_response.threat_category()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryThreatCategoryResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_threat_category(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.summary.with_streaming_response.threat_category() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryThreatCategoryResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_tls_version(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.tls_version()
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    async def test_method_tls_version_with_all_params(self, async_client: AsyncCloudflare) -> None:
        summary = await async_client.radar.email.security.summary.tls_version(
            arc=["PASS", "NONE", "FAIL"],
            date_end=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            date_range=["7d", "7d", "7d"],
            date_start=[parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z"), parse_datetime("2019-12-27T18:11:19.117Z")],
            dkim=["PASS", "NONE", "FAIL"],
            dmarc=["PASS", "NONE", "FAIL"],
            format="JSON",
            name=["string", "string", "string"],
            spf=["PASS", "NONE", "FAIL"],
        )
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    async def test_raw_response_tls_version(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.radar.email.security.summary.with_raw_response.tls_version()

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        summary = await response.parse()
        assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

    @parametrize
    async def test_streaming_response_tls_version(self, async_client: AsyncCloudflare) -> None:
        async with async_client.radar.email.security.summary.with_streaming_response.tls_version() as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            summary = await response.parse()
            assert_matches_type(SummaryTLSVersionResponse, summary, path=['response'])

        assert cast(Any, response.is_closed) is True