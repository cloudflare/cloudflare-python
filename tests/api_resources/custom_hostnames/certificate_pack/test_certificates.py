# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.custom_hostnames.certificate_pack import (
    CertificateDeleteResponse,
    CertificateUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        certificate = client.custom_hostnames.certificate_pack.certificates.update(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
            custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
        )
        assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.custom_hostnames.certificate_pack.certificates.with_raw_response.update(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
            custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.custom_hostnames.certificate_pack.certificates.with_streaming_response.update(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
            custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_hostnames.certificate_pack.certificates.with_raw_response.update(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
                custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_hostname_id` but received ''"):
            client.custom_hostnames.certificate_pack.certificates.with_raw_response.update(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
                custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            client.custom_hostnames.certificate_pack.certificates.with_raw_response.update(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="",
                custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
                custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.custom_hostnames.certificate_pack.certificates.with_raw_response.update(
                certificate_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
                custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        certificate = client.custom_hostnames.certificate_pack.certificates.delete(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.custom_hostnames.certificate_pack.certificates.with_raw_response.delete(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.custom_hostnames.certificate_pack.certificates.with_streaming_response.delete(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_hostnames.certificate_pack.certificates.with_raw_response.delete(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_hostname_id` but received ''"):
            client.custom_hostnames.certificate_pack.certificates.with_raw_response.delete(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            client.custom_hostnames.certificate_pack.certificates.with_raw_response.delete(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.custom_hostnames.certificate_pack.certificates.with_raw_response.delete(
                certificate_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCertificates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.custom_hostnames.certificate_pack.certificates.update(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
            custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
        )
        assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_hostnames.certificate_pack.certificates.with_raw_response.update(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
            custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_hostnames.certificate_pack.certificates.with_streaming_response.update(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
            custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[CertificateUpdateResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_hostnames.certificate_pack.certificates.with_raw_response.update(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
                custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_hostname_id` but received ''"):
            await async_client.custom_hostnames.certificate_pack.certificates.with_raw_response.update(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
                custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            await async_client.custom_hostnames.certificate_pack.certificates.with_raw_response.update(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="",
                custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
                custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.custom_hostnames.certificate_pack.certificates.with_raw_response.update(
                certificate_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_certificate="-----BEGIN CERTIFICATE-----\nMIIDdjCCAl6gAwIBAgIJAPnMg0Fs+/B0MA0GCSqGSIb3DQEBCwUAMFsx...\n-----END CERTIFICATE-----\n",
                custom_key="-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC/SCB5...\n-----END PRIVATE KEY-----\n",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.custom_hostnames.certificate_pack.certificates.delete(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_hostnames.certificate_pack.certificates.with_raw_response.delete(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_hostnames.certificate_pack.certificates.with_streaming_response.delete(
            certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
            certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_hostnames.certificate_pack.certificates.with_raw_response.delete(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_hostname_id` but received ''"):
            await async_client.custom_hostnames.certificate_pack.certificates.with_raw_response.delete(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_pack_id` but received ''"):
            await async_client.custom_hostnames.certificate_pack.certificates.with_raw_response.delete(
                certificate_id="023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.custom_hostnames.certificate_pack.certificates.with_raw_response.delete(
                certificate_id="",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                custom_hostname_id="023e105f4ecef8ad9ca31a8372d0c353",
                certificate_pack_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
