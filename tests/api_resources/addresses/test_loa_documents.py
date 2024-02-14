# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

from cloudflare.types.addresses import LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse

from typing import Any, cast

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.addresses import loa_document_ip_address_management_prefixes_upload_loa_document_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLoaDocuments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_ip_address_management_prefixes_upload_loa_document(self, client: Cloudflare) -> None:
        loa_document = client.addresses.loa_documents.ip_address_management_prefixes_upload_loa_document(
            "023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        )
        assert_matches_type(
            LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse, loa_document, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_ip_address_management_prefixes_upload_loa_document(self, client: Cloudflare) -> None:
        response = client.addresses.loa_documents.with_raw_response.ip_address_management_prefixes_upload_loa_document(
            "023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_document = response.parse()
        assert_matches_type(
            LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse, loa_document, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_ip_address_management_prefixes_upload_loa_document(self, client: Cloudflare) -> None:
        with client.addresses.loa_documents.with_streaming_response.ip_address_management_prefixes_upload_loa_document(
            "023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_document = response.parse()
            assert_matches_type(
                LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse, loa_document, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_ip_address_management_prefixes_upload_loa_document(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            client.addresses.loa_documents.with_raw_response.ip_address_management_prefixes_upload_loa_document(
                "",
                loa_document="@document.pdf",
            )


class TestAsyncLoaDocuments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_ip_address_management_prefixes_upload_loa_document(
        self, async_client: AsyncCloudflare
    ) -> None:
        loa_document = await async_client.addresses.loa_documents.ip_address_management_prefixes_upload_loa_document(
            "023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        )
        assert_matches_type(
            LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse, loa_document, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_ip_address_management_prefixes_upload_loa_document(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.addresses.loa_documents.with_raw_response.ip_address_management_prefixes_upload_loa_document(
            "023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        loa_document = await response.parse()
        assert_matches_type(
            LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse, loa_document, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_ip_address_management_prefixes_upload_loa_document(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.addresses.loa_documents.with_streaming_response.ip_address_management_prefixes_upload_loa_document(
            "023e105f4ecef8ad9ca31a8372d0c353",
            loa_document="@document.pdf",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            loa_document = await response.parse()
            assert_matches_type(
                LoaDocumentIPAddressManagementPrefixesUploadLoaDocumentResponse, loa_document, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_ip_address_management_prefixes_upload_loa_document(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_identifier` but received ''"):
            await async_client.addresses.loa_documents.with_raw_response.ip_address_management_prefixes_upload_loa_document(
                "",
                loa_document="@document.pdf",
            )
