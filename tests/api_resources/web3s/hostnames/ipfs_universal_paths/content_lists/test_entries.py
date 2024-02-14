# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.web3s.hostnames.ipfs_universal_paths.content_lists import (
    EntryGetResponse,
    EntryDeleteResponse,
    EntryUpdateResponse,
    EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse,
    EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestEntries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        entry = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        )
        assert_matches_type(EntryUpdateResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        entry = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
            description="this is my content list entry",
        )
        assert_matches_type(EntryUpdateResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(EntryUpdateResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(EntryUpdateResponse, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `content_list_entry_identifier` but received ''"
        ):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        entry = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[EntryDeleteResponse], entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(Optional[EntryDeleteResponse], entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(Optional[EntryDeleteResponse], entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `content_list_entry_identifier` but received ''"
        ):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        entry = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(EntryGetResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(EntryGetResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(EntryGetResponse, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `content_list_entry_identifier` but received ''"
        ):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
        self, client: Cloudflare
    ) -> None:
        entry = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        )
        assert_matches_type(
            EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse, entry, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry_with_all_params(
        self, client: Cloudflare
    ) -> None:
        entry = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
            description="this is my content list entry",
        )
        assert_matches_type(
            EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse, entry, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
        self, client: Cloudflare
    ) -> None:
        response = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(
            EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse, entry, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
        self, client: Cloudflare
    ) -> None:
        with client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_streaming_response.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(
                EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse, entry, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
        self, client: Cloudflare
    ) -> None:
        entry = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse], entry, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
        self, client: Cloudflare
    ) -> None:
        response = client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = response.parse()
        assert_matches_type(
            Optional[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse], entry, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
        self, client: Cloudflare
    ) -> None:
        with client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_streaming_response.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = response.parse()
            assert_matches_type(
                Optional[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse],
                entry,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
        self, client: Cloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncEntries:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        entry = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        )
        assert_matches_type(EntryUpdateResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        entry = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
            description="this is my content list entry",
        )
        assert_matches_type(EntryUpdateResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(EntryUpdateResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(EntryUpdateResponse, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `content_list_entry_identifier` but received ''"
        ):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.update(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        entry = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(Optional[EntryDeleteResponse], entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = (
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(Optional[EntryDeleteResponse], entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(Optional[EntryDeleteResponse], entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `content_list_entry_identifier` but received ''"
        ):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.delete(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        entry = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(EntryGetResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(EntryGetResponse, entry, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(EntryGetResponse, entry, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="",
            )

        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `content_list_entry_identifier` but received ''"
        ):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.get(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
        self, async_client: AsyncCloudflare
    ) -> None:
        entry = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        )
        assert_matches_type(
            EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse, entry, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        entry = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
            description="this is my content list entry",
        )
        assert_matches_type(
            EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse, entry, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(
            EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse, entry, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_streaming_response.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
            type="cid",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(
                EntryWeb3HostnameCreateIpfsUniversalPathGatewayContentListEntryResponse, entry, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_create_ipfs_universal_path_gateway_content_list_entry(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
                content="QmPZ9gcCEpqKTo6aq61g2nXGUhM4iCL3ewB6LDXZCtioEB",
                type="cid",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
        self, async_client: AsyncCloudflare
    ) -> None:
        entry = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse], entry, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        entry = await response.parse()
        assert_matches_type(
            Optional[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse], entry, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_streaming_response.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            entry = await response.parse()
            assert_matches_type(
                Optional[EntryWeb3HostnameListIpfsUniversalPathGatewayContentListEntriesResponse],
                entry,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_identifier="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `identifier` but received ''"):
            await async_client.web3s.hostnames.ipfs_universal_paths.content_lists.entries.with_raw_response.web3_hostname_list_ipfs_universal_path_gateway_content_list_entries(
                "",
                zone_identifier="023e105f4ecef8ad9ca31a8372d0c353",
            )
