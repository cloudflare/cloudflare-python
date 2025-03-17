# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.origin_ca_certificates import (
    OriginCACertificate,
    OriginCACertificateDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOriginCACertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        origin_ca_certificate = client.origin_ca_certificates.create()
        assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        origin_ca_certificate = client.origin_ca_certificates.create(
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICxzCCAa8CAQAwSDELMAkGA1UEBhMCVVMxFjAUBgNVBAgTDVNhbiBGcmFuY2lz\nY28xCzAJBgNVBAcTAkNBMRQwEgYDVQQDEwtleGFtcGxlLm5ldDCCASIwDQYJKoZI\nhvcNAQEBBQADggEPADCCAQoCggEBALxejtu4b+jPdFeFi6OUsye8TYJQBm3WfCvL\nHu5EvijMO/4Z2TImwASbwUF7Ir8OLgH+mGlQZeqyNvGoSOMEaZVXcYfpR1hlVak8\n4GGVr+04IGfOCqaBokaBFIwzclGZbzKmLGwIQioNxGfqFm6RGYGA3be2Je2iseBc\nN8GV1wYmvYE0RR+yWweJCTJ157exyRzu7sVxaEW9F87zBQLyOnwXc64rflXslRqi\ng7F7w5IaQYOl8yvmk/jEPCAha7fkiUfEpj4N12+oPRiMvleJF98chxjD4MH39c5I\nuOslULhrWunfh7GB1jwWNA9y44H0snrf+xvoy2TcHmxvma9Eln8CAwEAAaA6MDgG\nCSqGSIb3DQEJDjErMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5uZXSCD3d3dy5leGFt\ncGxlLm5ldDANBgkqhkiG9w0BAQsFAAOCAQEAcBaX6dOnI8ncARrI9ZSF2AJX+8mx\npTHY2+Y2C0VvrVDGMtbBRH8R9yMbqWtlxeeNGf//LeMkSKSFa4kbpdx226lfui8/\nauRDBTJGx2R1ccUxmLZXx4my0W5iIMxunu+kez+BDlu7bTT2io0uXMRHue4i6quH\nyc5ibxvbJMjR7dqbcanVE10/34oprzXQsJ/VmSuZNXtjbtSKDlmcpw6To/eeAJ+J\nhXykcUihvHyG4A1m2R6qpANBjnA0pHexfwM/SgfzvpbvUg0T1ubmer8BgTwCKIWs\ndcWYTthM51JIqRBfNqy4QcBnX+GY05yltEEswQI55wdiS3CjTTA67sdbcQ==\n-----END CERTIFICATE REQUEST-----",
            hostnames=["example.com", "*.example.com"],
            request_type="origin-rsa",
            requested_validity=7,
        )
        assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.origin_ca_certificates.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_ca_certificate = response.parse()
        assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.origin_ca_certificates.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_ca_certificate = response.parse()
            assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        origin_ca_certificate = client.origin_ca_certificates.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncSinglePage[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.origin_ca_certificates.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_ca_certificate = response.parse()
        assert_matches_type(SyncSinglePage[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.origin_ca_certificates.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_ca_certificate = response.parse()
            assert_matches_type(SyncSinglePage[OriginCACertificate], origin_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        origin_ca_certificate = client.origin_ca_certificates.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCACertificateDeleteResponse], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.origin_ca_certificates.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_ca_certificate = response.parse()
        assert_matches_type(Optional[OriginCACertificateDeleteResponse], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.origin_ca_certificates.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_ca_certificate = response.parse()
            assert_matches_type(Optional[OriginCACertificateDeleteResponse], origin_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.origin_ca_certificates.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        origin_ca_certificate = client.origin_ca_certificates.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.origin_ca_certificates.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_ca_certificate = response.parse()
        assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.origin_ca_certificates.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_ca_certificate = response.parse()
            assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.origin_ca_certificates.with_raw_response.get(
                "",
            )


class TestAsyncOriginCACertificates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        origin_ca_certificate = await async_client.origin_ca_certificates.create()
        assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        origin_ca_certificate = await async_client.origin_ca_certificates.create(
            csr="-----BEGIN CERTIFICATE REQUEST-----\nMIICxzCCAa8CAQAwSDELMAkGA1UEBhMCVVMxFjAUBgNVBAgTDVNhbiBGcmFuY2lz\nY28xCzAJBgNVBAcTAkNBMRQwEgYDVQQDEwtleGFtcGxlLm5ldDCCASIwDQYJKoZI\nhvcNAQEBBQADggEPADCCAQoCggEBALxejtu4b+jPdFeFi6OUsye8TYJQBm3WfCvL\nHu5EvijMO/4Z2TImwASbwUF7Ir8OLgH+mGlQZeqyNvGoSOMEaZVXcYfpR1hlVak8\n4GGVr+04IGfOCqaBokaBFIwzclGZbzKmLGwIQioNxGfqFm6RGYGA3be2Je2iseBc\nN8GV1wYmvYE0RR+yWweJCTJ157exyRzu7sVxaEW9F87zBQLyOnwXc64rflXslRqi\ng7F7w5IaQYOl8yvmk/jEPCAha7fkiUfEpj4N12+oPRiMvleJF98chxjD4MH39c5I\nuOslULhrWunfh7GB1jwWNA9y44H0snrf+xvoy2TcHmxvma9Eln8CAwEAAaA6MDgG\nCSqGSIb3DQEJDjErMCkwJwYDVR0RBCAwHoILZXhhbXBsZS5uZXSCD3d3dy5leGFt\ncGxlLm5ldDANBgkqhkiG9w0BAQsFAAOCAQEAcBaX6dOnI8ncARrI9ZSF2AJX+8mx\npTHY2+Y2C0VvrVDGMtbBRH8R9yMbqWtlxeeNGf//LeMkSKSFa4kbpdx226lfui8/\nauRDBTJGx2R1ccUxmLZXx4my0W5iIMxunu+kez+BDlu7bTT2io0uXMRHue4i6quH\nyc5ibxvbJMjR7dqbcanVE10/34oprzXQsJ/VmSuZNXtjbtSKDlmcpw6To/eeAJ+J\nhXykcUihvHyG4A1m2R6qpANBjnA0pHexfwM/SgfzvpbvUg0T1ubmer8BgTwCKIWs\ndcWYTthM51JIqRBfNqy4QcBnX+GY05yltEEswQI55wdiS3CjTTA67sdbcQ==\n-----END CERTIFICATE REQUEST-----",
            hostnames=["example.com", "*.example.com"],
            request_type="origin-rsa",
            requested_validity=7,
        )
        assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.origin_ca_certificates.with_raw_response.create()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_ca_certificate = await response.parse()
        assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.origin_ca_certificates.with_streaming_response.create() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_ca_certificate = await response.parse()
            assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        origin_ca_certificate = await async_client.origin_ca_certificates.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(AsyncSinglePage[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.origin_ca_certificates.with_raw_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_ca_certificate = await response.parse()
        assert_matches_type(AsyncSinglePage[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.origin_ca_certificates.with_streaming_response.list(
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_ca_certificate = await response.parse()
            assert_matches_type(AsyncSinglePage[OriginCACertificate], origin_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        origin_ca_certificate = await async_client.origin_ca_certificates.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCACertificateDeleteResponse], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.origin_ca_certificates.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_ca_certificate = await response.parse()
        assert_matches_type(Optional[OriginCACertificateDeleteResponse], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.origin_ca_certificates.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_ca_certificate = await response.parse()
            assert_matches_type(Optional[OriginCACertificateDeleteResponse], origin_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.origin_ca_certificates.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        origin_ca_certificate = await async_client.origin_ca_certificates.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.origin_ca_certificates.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin_ca_certificate = await response.parse()
        assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.origin_ca_certificates.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin_ca_certificate = await response.parse()
            assert_matches_type(Optional[OriginCACertificate], origin_ca_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="TODO: investigate auth errors on test suite")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.origin_ca_certificates.with_raw_response.get(
                "",
            )
