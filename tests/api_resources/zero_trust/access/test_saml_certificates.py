# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import httpx
import pytest
from respx import MockRouter

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from cloudflare.pagination import SyncV4PagePaginationArray, AsyncV4PagePaginationArray
from cloudflare.types.zero_trust.access import (
    SAMLCertificateGetResponse,
    SAMLCertificateListResponse,
    SAMLCertificateRotateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSAMLCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        saml_certificate = client.zero_trust.access.saml_certificates.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(SyncV4PagePaginationArray[SAMLCertificateListResponse], saml_certificate, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Cloudflare) -> None:
        saml_certificate = client.zero_trust.access.saml_certificates.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="a5bb4b3f-c2d1-4e6a-8f9b-1d3e4f5a6b7c,f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            page=1,
            per_page=1,
        )
        assert_matches_type(SyncV4PagePaginationArray[SAMLCertificateListResponse], saml_certificate, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.saml_certificates.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saml_certificate = response.parse()
        assert_matches_type(SyncV4PagePaginationArray[SAMLCertificateListResponse], saml_certificate, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.access.saml_certificates.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saml_certificate = response.parse()
            assert_matches_type(
                SyncV4PagePaginationArray[SAMLCertificateListResponse], saml_certificate, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.saml_certificates.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        saml_certificate = client.zero_trust.access.saml_certificates.get(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SAMLCertificateGetResponse], saml_certificate, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.saml_certificates.with_raw_response.get(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saml_certificate = response.parse()
        assert_matches_type(Optional[SAMLCertificateGetResponse], saml_certificate, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.access.saml_certificates.with_streaming_response.get(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saml_certificate = response.parse()
            assert_matches_type(Optional[SAMLCertificateGetResponse], saml_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.saml_certificates.with_raw_response.get(
                saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `saml_cert_set_id` but received ''"):
            client.zero_trust.access.saml_certificates.with_raw_response.get(
                saml_cert_set_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_get_pem(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/access/saml_certificates/f174e90a-fafe-4643-bbbc-4a0ed4fc8415/pem"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        saml_certificate = client.zero_trust.access.saml_certificates.get_pem(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert saml_certificate.is_closed
        assert saml_certificate.json() == {"foo": "bar"}
        assert cast(Any, saml_certificate.is_closed) is True
        assert isinstance(saml_certificate, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_get_pem(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/access/saml_certificates/f174e90a-fafe-4643-bbbc-4a0ed4fc8415/pem"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        saml_certificate = client.zero_trust.access.saml_certificates.with_raw_response.get_pem(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert saml_certificate.is_closed is True
        assert saml_certificate.http_request.headers.get("X-Stainless-Lang") == "python"
        assert saml_certificate.json() == {"foo": "bar"}
        assert isinstance(saml_certificate, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_get_pem(self, client: Cloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/access/saml_certificates/f174e90a-fafe-4643-bbbc-4a0ed4fc8415/pem"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.zero_trust.access.saml_certificates.with_streaming_response.get_pem(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as saml_certificate:
            assert not saml_certificate.is_closed
            assert saml_certificate.http_request.headers.get("X-Stainless-Lang") == "python"

            assert saml_certificate.json() == {"foo": "bar"}
            assert cast(Any, saml_certificate.is_closed) is True
            assert isinstance(saml_certificate, StreamedBinaryAPIResponse)

        assert cast(Any, saml_certificate.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_get_pem(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.saml_certificates.with_raw_response.get_pem(
                saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `saml_cert_set_id` but received ''"):
            client.zero_trust.access.saml_certificates.with_raw_response.get_pem(
                saml_cert_set_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    def test_method_rotate(self, client: Cloudflare) -> None:
        saml_certificate = client.zero_trust.access.saml_certificates.rotate(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SAMLCertificateRotateResponse], saml_certificate, path=["response"])

    @parametrize
    def test_raw_response_rotate(self, client: Cloudflare) -> None:
        response = client.zero_trust.access.saml_certificates.with_raw_response.rotate(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saml_certificate = response.parse()
        assert_matches_type(Optional[SAMLCertificateRotateResponse], saml_certificate, path=["response"])

    @parametrize
    def test_streaming_response_rotate(self, client: Cloudflare) -> None:
        with client.zero_trust.access.saml_certificates.with_streaming_response.rotate(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saml_certificate = response.parse()
            assert_matches_type(Optional[SAMLCertificateRotateResponse], saml_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_rotate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.access.saml_certificates.with_raw_response.rotate(
                saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `saml_cert_set_id` but received ''"):
            client.zero_trust.access.saml_certificates.with_raw_response.rotate(
                saml_cert_set_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncSAMLCertificates:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        saml_certificate = await async_client.zero_trust.access.saml_certificates.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[SAMLCertificateListResponse], saml_certificate, path=["response"]
        )

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCloudflare) -> None:
        saml_certificate = await async_client.zero_trust.access.saml_certificates.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
            id="a5bb4b3f-c2d1-4e6a-8f9b-1d3e4f5a6b7c,f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            page=1,
            per_page=1,
        )
        assert_matches_type(
            AsyncV4PagePaginationArray[SAMLCertificateListResponse], saml_certificate, path=["response"]
        )

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.saml_certificates.with_raw_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saml_certificate = await response.parse()
        assert_matches_type(
            AsyncV4PagePaginationArray[SAMLCertificateListResponse], saml_certificate, path=["response"]
        )

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.saml_certificates.with_streaming_response.list(
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saml_certificate = await response.parse()
            assert_matches_type(
                AsyncV4PagePaginationArray[SAMLCertificateListResponse], saml_certificate, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.saml_certificates.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        saml_certificate = await async_client.zero_trust.access.saml_certificates.get(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SAMLCertificateGetResponse], saml_certificate, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.saml_certificates.with_raw_response.get(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saml_certificate = await response.parse()
        assert_matches_type(Optional[SAMLCertificateGetResponse], saml_certificate, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.saml_certificates.with_streaming_response.get(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saml_certificate = await response.parse()
            assert_matches_type(Optional[SAMLCertificateGetResponse], saml_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.saml_certificates.with_raw_response.get(
                saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `saml_cert_set_id` but received ''"):
            await async_client.zero_trust.access.saml_certificates.with_raw_response.get(
                saml_cert_set_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_get_pem(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/access/saml_certificates/f174e90a-fafe-4643-bbbc-4a0ed4fc8415/pem"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        saml_certificate = await async_client.zero_trust.access.saml_certificates.get_pem(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert saml_certificate.is_closed
        assert await saml_certificate.json() == {"foo": "bar"}
        assert cast(Any, saml_certificate.is_closed) is True
        assert isinstance(saml_certificate, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_get_pem(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/access/saml_certificates/f174e90a-fafe-4643-bbbc-4a0ed4fc8415/pem"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        saml_certificate = await async_client.zero_trust.access.saml_certificates.with_raw_response.get_pem(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert saml_certificate.is_closed is True
        assert saml_certificate.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await saml_certificate.json() == {"foo": "bar"}
        assert isinstance(saml_certificate, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_get_pem(self, async_client: AsyncCloudflare, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/accounts/023e105f4ecef8ad9ca31a8372d0c353/access/saml_certificates/f174e90a-fafe-4643-bbbc-4a0ed4fc8415/pem"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.zero_trust.access.saml_certificates.with_streaming_response.get_pem(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as saml_certificate:
            assert not saml_certificate.is_closed
            assert saml_certificate.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await saml_certificate.json() == {"foo": "bar"}
            assert cast(Any, saml_certificate.is_closed) is True
            assert isinstance(saml_certificate, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, saml_certificate.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_get_pem(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.saml_certificates.with_raw_response.get_pem(
                saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `saml_cert_set_id` but received ''"):
            await async_client.zero_trust.access.saml_certificates.with_raw_response.get_pem(
                saml_cert_set_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @parametrize
    async def test_method_rotate(self, async_client: AsyncCloudflare) -> None:
        saml_certificate = await async_client.zero_trust.access.saml_certificates.rotate(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[SAMLCertificateRotateResponse], saml_certificate, path=["response"])

    @parametrize
    async def test_raw_response_rotate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.access.saml_certificates.with_raw_response.rotate(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saml_certificate = await response.parse()
        assert_matches_type(Optional[SAMLCertificateRotateResponse], saml_certificate, path=["response"])

    @parametrize
    async def test_streaming_response_rotate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.access.saml_certificates.with_streaming_response.rotate(
            saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saml_certificate = await response.parse()
            assert_matches_type(Optional[SAMLCertificateRotateResponse], saml_certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_rotate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.access.saml_certificates.with_raw_response.rotate(
                saml_cert_set_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `saml_cert_set_id` but received ''"):
            await async_client.zero_trust.access.saml_certificates.with_raw_response.rotate(
                saml_cert_set_id="",
                account_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
