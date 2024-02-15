# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.access import (
    CertificateGetResponse,
    CertificateDeleteResponse,
    CertificateUpdateResponse,
    CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse,
    CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        certificate = client.access.certificates.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
        )
        assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        certificate = client.access.certificates.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
            name="Allow devs",
        )
        assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.access.certificates.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.access.certificates.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.certificates.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.certificates.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.certificates.with_raw_response.update(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        certificate = client.access.certificates.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.access.certificates.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.access.certificates.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.certificates.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.certificates.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.certificates.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_m_tls_authentication_add_an_m_tls_certificate(self, client: Cloudflare) -> None:
        certificate = client.access.certificates.access_m_tls_authentication_add_an_m_tls_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
        )
        assert_matches_type(
            CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse, certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_m_tls_authentication_add_an_m_tls_certificate_with_all_params(
        self, client: Cloudflare
    ) -> None:
        certificate = client.access.certificates.access_m_tls_authentication_add_an_m_tls_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
            associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
        )
        assert_matches_type(
            CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse, certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_m_tls_authentication_add_an_m_tls_certificate(self, client: Cloudflare) -> None:
        response = client.access.certificates.with_raw_response.access_m_tls_authentication_add_an_m_tls_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(
            CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse, certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_m_tls_authentication_add_an_m_tls_certificate(self, client: Cloudflare) -> None:
        with client.access.certificates.with_streaming_response.access_m_tls_authentication_add_an_m_tls_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(
                CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse, certificate, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_m_tls_authentication_add_an_m_tls_certificate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.certificates.with_raw_response.access_m_tls_authentication_add_an_m_tls_certificate(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.certificates.with_raw_response.access_m_tls_authentication_add_an_m_tls_certificate(
                "",
                account_or_zone="string",
                certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_access_m_tls_authentication_list_m_tls_certificates(self, client: Cloudflare) -> None:
        certificate = client.access.certificates.access_m_tls_authentication_list_m_tls_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(
            Optional[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse], certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_access_m_tls_authentication_list_m_tls_certificates(self, client: Cloudflare) -> None:
        response = client.access.certificates.with_raw_response.access_m_tls_authentication_list_m_tls_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(
            Optional[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse], certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_access_m_tls_authentication_list_m_tls_certificates(self, client: Cloudflare) -> None:
        with client.access.certificates.with_streaming_response.access_m_tls_authentication_list_m_tls_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(
                Optional[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse],
                certificate,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_access_m_tls_authentication_list_m_tls_certificates(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.certificates.with_raw_response.access_m_tls_authentication_list_m_tls_certificates(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.certificates.with_raw_response.access_m_tls_authentication_list_m_tls_certificates(
                "",
                account_or_zone="string",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        certificate = client.access.certificates.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificateGetResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.access.certificates.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(CertificateGetResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.access.certificates.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(CertificateGetResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            client.access.certificates.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            client.access.certificates.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            client.access.certificates.with_raw_response.get(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCertificates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.access.certificates.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
        )
        assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.access.certificates.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
            name="Allow devs",
        )
        assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.certificates.with_raw_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.certificates.with_streaming_response.update(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(CertificateUpdateResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.certificates.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.certificates.with_raw_response.update(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
                associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.certificates.with_raw_response.update(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
                associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.access.certificates.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.certificates.with_raw_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.certificates.with_streaming_response.delete(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(CertificateDeleteResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.certificates.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.certificates.with_raw_response.delete(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.certificates.with_raw_response.delete(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_m_tls_authentication_add_an_m_tls_certificate(
        self, async_client: AsyncCloudflare
    ) -> None:
        certificate = await async_client.access.certificates.access_m_tls_authentication_add_an_m_tls_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
        )
        assert_matches_type(
            CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse, certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_m_tls_authentication_add_an_m_tls_certificate_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        certificate = await async_client.access.certificates.access_m_tls_authentication_add_an_m_tls_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
            associated_hostnames=["admin.example.com", "admin.example.com", "admin.example.com"],
        )
        assert_matches_type(
            CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse, certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_m_tls_authentication_add_an_m_tls_certificate(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.access.certificates.with_raw_response.access_m_tls_authentication_add_an_m_tls_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(
            CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse, certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_m_tls_authentication_add_an_m_tls_certificate(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.certificates.with_streaming_response.access_m_tls_authentication_add_an_m_tls_certificate(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
            certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
            name="Allow devs",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(
                CertificateAccessMTLSAuthenticationAddAnMTLSCertificateResponse, certificate, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_m_tls_authentication_add_an_m_tls_certificate(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.certificates.with_raw_response.access_m_tls_authentication_add_an_m_tls_certificate(
                "023e105f4ecef8ad9ca31a8372d0c353",
                account_or_zone="",
                certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
                name="Allow devs",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.certificates.with_raw_response.access_m_tls_authentication_add_an_m_tls_certificate(
                "",
                account_or_zone="string",
                certificate="-----BEGIN CERTIFICATE-----\nMIIGAjCCA+qgAwIBAgIJAI7kymlF7CWT...N4RI7KKB7nikiuUf8vhULKy5IX10\nDrUtmu/B\n-----END CERTIFICATE-----",
                name="Allow devs",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_access_m_tls_authentication_list_m_tls_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        certificate = await async_client.access.certificates.access_m_tls_authentication_list_m_tls_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )
        assert_matches_type(
            Optional[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse], certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_access_m_tls_authentication_list_m_tls_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.access.certificates.with_raw_response.access_m_tls_authentication_list_m_tls_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(
            Optional[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse], certificate, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_access_m_tls_authentication_list_m_tls_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.access.certificates.with_streaming_response.access_m_tls_authentication_list_m_tls_certificates(
            "023e105f4ecef8ad9ca31a8372d0c353",
            account_or_zone="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(
                Optional[CertificateAccessMTLSAuthenticationListMTLSCertificatesResponse],
                certificate,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_access_m_tls_authentication_list_m_tls_certificates(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await (
                async_client.access.certificates.with_raw_response.access_m_tls_authentication_list_m_tls_certificates(
                    "023e105f4ecef8ad9ca31a8372d0c353",
                    account_or_zone="",
                )
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await (
                async_client.access.certificates.with_raw_response.access_m_tls_authentication_list_m_tls_certificates(
                    "",
                    account_or_zone="string",
                )
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.access.certificates.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CertificateGetResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.access.certificates.with_raw_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(CertificateGetResponse, certificate, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.access.certificates.with_streaming_response.get(
            "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_or_zone="string",
            account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(CertificateGetResponse, certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone` but received ''"):
            await async_client.access.certificates.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_or_zone_id` but received ''"):
            await async_client.access.certificates.with_raw_response.get(
                "f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_or_zone="string",
                account_or_zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `uuid` but received ''"):
            await async_client.access.certificates.with_raw_response.get(
                "",
                account_or_zone="string",
                account_or_zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
