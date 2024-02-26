# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.secondary_dns import (
    ACLGetResponse,
    ACLListResponse,
    ACLCreateResponse,
    ACLDeleteResponse,
    ACLUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestACLs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        acl = client.secondary_dns.acls.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            body={},
        )
        assert_matches_type(ACLCreateResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:
        response = client.secondary_dns.acls.with_raw_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACLCreateResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.secondary_dns.acls.with_streaming_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACLCreateResponse, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        acl = client.secondary_dns.acls.update(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )
        assert_matches_type(ACLUpdateResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.secondary_dns.acls.with_raw_response.update(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACLUpdateResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.secondary_dns.acls.with_streaming_response.update(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACLUpdateResponse, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list(self, client: Cloudflare) -> None:
        acl = client.secondary_dns.acls.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[ACLListResponse], acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list(self, client: Cloudflare) -> None:
        response = client.secondary_dns.acls.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(Optional[ACLListResponse], acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list(self, client: Cloudflare) -> None:
        with client.secondary_dns.acls.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(Optional[ACLListResponse], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        acl = client.secondary_dns.acls.delete(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(ACLDeleteResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.secondary_dns.acls.with_raw_response.delete(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACLDeleteResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.secondary_dns.acls.with_streaming_response.delete(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACLDeleteResponse, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        acl = client.secondary_dns.acls.get(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(ACLGetResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.secondary_dns.acls.with_raw_response.get(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = response.parse()
        assert_matches_type(ACLGetResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.secondary_dns.acls.with_streaming_response.get(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = response.parse()
            assert_matches_type(ACLGetResponse, acl, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncACLs:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.secondary_dns.acls.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            body={},
        )
        assert_matches_type(ACLCreateResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.acls.with_raw_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            body={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACLCreateResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.acls.with_streaming_response.create(
            account_id="01a7362d577a6c3019a474fd6f485823",
            body={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACLCreateResponse, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.secondary_dns.acls.update(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )
        assert_matches_type(ACLUpdateResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.acls.with_raw_response.update(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACLUpdateResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.acls.with_streaming_response.update(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
            ip_range="192.0.2.53/28",
            name="my-acl-1",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACLUpdateResponse, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.secondary_dns.acls.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(Optional[ACLListResponse], acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.acls.with_raw_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(Optional[ACLListResponse], acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.acls.with_streaming_response.list(
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(Optional[ACLListResponse], acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.secondary_dns.acls.delete(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(ACLDeleteResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.acls.with_raw_response.delete(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACLDeleteResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.acls.with_streaming_response.delete(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACLDeleteResponse, acl, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        acl = await async_client.secondary_dns.acls.get(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )
        assert_matches_type(ACLGetResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.secondary_dns.acls.with_raw_response.get(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        acl = await response.parse()
        assert_matches_type(ACLGetResponse, acl, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.acls.with_streaming_response.get(
            "23ff594956f20c2a721606e94745a8aa",
            account_id="01a7362d577a6c3019a474fd6f485823",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            acl = await response.parse()
            assert_matches_type(ACLGetResponse, acl, path=["response"])

        assert cast(Any, response.is_closed) is True
