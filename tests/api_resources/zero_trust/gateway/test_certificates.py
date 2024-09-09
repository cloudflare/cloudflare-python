# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.pagination import SyncSinglePage, AsyncSinglePage
from cloudflare.types.zero_trust.gateway import (
    CertificateGetResponse,
    CertificateListResponse,
    CertificateCreateResponse,
    CertificateDeleteResponse,
    CertificateActivateResponse,
    CertificateDeactivateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCertificates:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.gateway.certificates.create(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[CertificateCreateResponse], certificate, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.gateway.certificates.create(
            account_id="699d98642c564d2e855e9661899b7252",
            validity_period_days=1826,
        )
        assert_matches_type(Optional[CertificateCreateResponse], certificate, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.certificates.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[CertificateCreateResponse], certificate, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.certificates.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[CertificateCreateResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.certificates.with_raw_response.create(
                account_id="",
            )

    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.gateway.certificates.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(SyncSinglePage[CertificateListResponse], certificate, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.certificates.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(SyncSinglePage[CertificateListResponse], certificate, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.certificates.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(SyncSinglePage[CertificateListResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.certificates.with_raw_response.list(
                account_id="",
            )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.gateway.certificates.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.certificates.with_raw_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.certificates.with_streaming_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.certificates.with_raw_response.delete(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.zero_trust.gateway.certificates.with_raw_response.delete(
                certificate_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    def test_method_activate(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.gateway.certificates.activate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(Optional[CertificateActivateResponse], certificate, path=["response"])

    @parametrize
    def test_raw_response_activate(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.certificates.with_raw_response.activate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[CertificateActivateResponse], certificate, path=["response"])

    @parametrize
    def test_streaming_response_activate(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.certificates.with_streaming_response.activate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[CertificateActivateResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_activate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.certificates.with_raw_response.activate(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.zero_trust.gateway.certificates.with_raw_response.activate(
                certificate_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @parametrize
    def test_method_deactivate(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.gateway.certificates.deactivate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(Optional[CertificateDeactivateResponse], certificate, path=["response"])

    @parametrize
    def test_raw_response_deactivate(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.certificates.with_raw_response.deactivate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[CertificateDeactivateResponse], certificate, path=["response"])

    @parametrize
    def test_streaming_response_deactivate(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.certificates.with_streaming_response.deactivate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[CertificateDeactivateResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_deactivate(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.certificates.with_raw_response.deactivate(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.zero_trust.gateway.certificates.with_raw_response.deactivate(
                certificate_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        certificate = client.zero_trust.gateway.certificates.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.zero_trust.gateway.certificates.with_raw_response.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = response.parse()
        assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.zero_trust.gateway.certificates.with_streaming_response.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = response.parse()
            assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.zero_trust.gateway.certificates.with_raw_response.get(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            client.zero_trust.gateway.certificates.with_raw_response.get(
                certificate_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )


class TestAsyncCertificates:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.gateway.certificates.create(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[CertificateCreateResponse], certificate, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.gateway.certificates.create(
            account_id="699d98642c564d2e855e9661899b7252",
            validity_period_days=1826,
        )
        assert_matches_type(Optional[CertificateCreateResponse], certificate, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.certificates.with_raw_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[CertificateCreateResponse], certificate, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.certificates.with_streaming_response.create(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[CertificateCreateResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.certificates.with_raw_response.create(
                account_id="",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.gateway.certificates.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(AsyncSinglePage[CertificateListResponse], certificate, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.certificates.with_raw_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(AsyncSinglePage[CertificateListResponse], certificate, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.certificates.with_streaming_response.list(
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(AsyncSinglePage[CertificateListResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.certificates.with_raw_response.list(
                account_id="",
            )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.gateway.certificates.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.certificates.with_raw_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.certificates.with_streaming_response.delete(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[CertificateDeleteResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.certificates.with_raw_response.delete(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.zero_trust.gateway.certificates.with_raw_response.delete(
                certificate_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )

    @parametrize
    async def test_method_activate(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.gateway.certificates.activate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(Optional[CertificateActivateResponse], certificate, path=["response"])

    @parametrize
    async def test_raw_response_activate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.certificates.with_raw_response.activate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[CertificateActivateResponse], certificate, path=["response"])

    @parametrize
    async def test_streaming_response_activate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.certificates.with_streaming_response.activate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[CertificateActivateResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_activate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.certificates.with_raw_response.activate(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.zero_trust.gateway.certificates.with_raw_response.activate(
                certificate_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @parametrize
    async def test_method_deactivate(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.gateway.certificates.deactivate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )
        assert_matches_type(Optional[CertificateDeactivateResponse], certificate, path=["response"])

    @parametrize
    async def test_raw_response_deactivate(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.certificates.with_raw_response.deactivate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[CertificateDeactivateResponse], certificate, path=["response"])

    @parametrize
    async def test_streaming_response_deactivate(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.certificates.with_streaming_response.deactivate(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[CertificateDeactivateResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_deactivate(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.certificates.with_raw_response.deactivate(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
                body={},
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.zero_trust.gateway.certificates.with_raw_response.deactivate(
                certificate_id="",
                account_id="699d98642c564d2e855e9661899b7252",
                body={},
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        certificate = await async_client.zero_trust.gateway.certificates.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )
        assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.zero_trust.gateway.certificates.with_raw_response.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        certificate = await response.parse()
        assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.zero_trust.gateway.certificates.with_streaming_response.get(
            certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
            account_id="699d98642c564d2e855e9661899b7252",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            certificate = await response.parse()
            assert_matches_type(Optional[CertificateGetResponse], certificate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.zero_trust.gateway.certificates.with_raw_response.get(
                certificate_id="f174e90a-fafe-4643-bbbc-4a0ed4fc8415",
                account_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `certificate_id` but received ''"):
            await async_client.zero_trust.gateway.certificates.with_raw_response.get(
                certificate_id="",
                account_id="699d98642c564d2e855e9661899b7252",
            )
