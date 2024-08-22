# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from cloudflare import Cloudflare, AsyncCloudflare

from typing import Optional, Any, cast

from cloudflare.types.secondary_dns import IncomingCreateResponse, IncomingUpdateResponse, IncomingDeleteResponse, IncomingGetResponse

import os
import pytest
import httpx
from typing_extensions import get_args
from typing import Optional
from respx import MockRouter
from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types.secondary_dns import incoming_create_params
from cloudflare.types.secondary_dns import incoming_update_params

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")

class TestIncoming:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    def test_method_create(self, client: Cloudflare) -> None:
        incoming = client.secondary_dns.incoming.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(Optional[IncomingCreateResponse], incoming, path=['response'])

    @parametrize
    def test_raw_response_create(self, client: Cloudflare) -> None:

        response = client.secondary_dns.incoming.with_raw_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        incoming = response.parse()
        assert_matches_type(Optional[IncomingCreateResponse], incoming, path=['response'])

    @parametrize
    def test_streaming_response_create(self, client: Cloudflare) -> None:
        with client.secondary_dns.incoming.with_streaming_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            incoming = response.parse()
            assert_matches_type(Optional[IncomingCreateResponse], incoming, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_create(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.secondary_dns.incoming.with_raw_response.create(
              zone_id="",
              auto_refresh_seconds=86400,
              name="www.example.com.",
              peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
          )

    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        incoming = client.secondary_dns.incoming.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(Optional[IncomingUpdateResponse], incoming, path=['response'])

    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:

        response = client.secondary_dns.incoming.with_raw_response.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        incoming = response.parse()
        assert_matches_type(Optional[IncomingUpdateResponse], incoming, path=['response'])

    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.secondary_dns.incoming.with_streaming_response.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            incoming = response.parse()
            assert_matches_type(Optional[IncomingUpdateResponse], incoming, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.secondary_dns.incoming.with_raw_response.update(
              zone_id="",
              auto_refresh_seconds=86400,
              name="www.example.com.",
              peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
          )

    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        incoming = client.secondary_dns.incoming.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(Optional[IncomingDeleteResponse], incoming, path=['response'])

    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:

        response = client.secondary_dns.incoming.with_raw_response.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        incoming = response.parse()
        assert_matches_type(Optional[IncomingDeleteResponse], incoming, path=['response'])

    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.secondary_dns.incoming.with_streaming_response.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            incoming = response.parse()
            assert_matches_type(Optional[IncomingDeleteResponse], incoming, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.secondary_dns.incoming.with_raw_response.delete(
              zone_id="",
          )

    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        incoming = client.secondary_dns.incoming.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(Optional[IncomingGetResponse], incoming, path=['response'])

    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:

        response = client.secondary_dns.incoming.with_raw_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        incoming = response.parse()
        assert_matches_type(Optional[IncomingGetResponse], incoming, path=['response'])

    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.secondary_dns.incoming.with_streaming_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            incoming = response.parse()
            assert_matches_type(Optional[IncomingGetResponse], incoming, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          client.secondary_dns.incoming.with_raw_response.get(
              zone_id="",
          )
class TestAsyncIncoming:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=['loose', 'strict'])


    @parametrize
    async def test_method_create(self, async_client: AsyncCloudflare) -> None:
        incoming = await async_client.secondary_dns.incoming.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(Optional[IncomingCreateResponse], incoming, path=['response'])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.secondary_dns.incoming.with_raw_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        incoming = await response.parse()
        assert_matches_type(Optional[IncomingCreateResponse], incoming, path=['response'])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.incoming.with_streaming_response.create(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            incoming = await response.parse()
            assert_matches_type(Optional[IncomingCreateResponse], incoming, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_create(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.secondary_dns.incoming.with_raw_response.create(
              zone_id="",
              auto_refresh_seconds=86400,
              name="www.example.com.",
              peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
          )

    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        incoming = await async_client.secondary_dns.incoming.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )
        assert_matches_type(Optional[IncomingUpdateResponse], incoming, path=['response'])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.secondary_dns.incoming.with_raw_response.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        incoming = await response.parse()
        assert_matches_type(Optional[IncomingUpdateResponse], incoming, path=['response'])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.incoming.with_streaming_response.update(
            zone_id="269d8f4853475ca241c4e730be286b20",
            auto_refresh_seconds=86400,
            name="www.example.com.",
            peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            incoming = await response.parse()
            assert_matches_type(Optional[IncomingUpdateResponse], incoming, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.secondary_dns.incoming.with_raw_response.update(
              zone_id="",
              auto_refresh_seconds=86400,
              name="www.example.com.",
              peers=["23ff594956f20c2a721606e94745a8aa", "00920f38ce07c2e2f4df50b1f61d4194"],
          )

    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        incoming = await async_client.secondary_dns.incoming.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(Optional[IncomingDeleteResponse], incoming, path=['response'])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.secondary_dns.incoming.with_raw_response.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        incoming = await response.parse()
        assert_matches_type(Optional[IncomingDeleteResponse], incoming, path=['response'])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.incoming.with_streaming_response.delete(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            incoming = await response.parse()
            assert_matches_type(Optional[IncomingDeleteResponse], incoming, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.secondary_dns.incoming.with_raw_response.delete(
              zone_id="",
          )

    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        incoming = await async_client.secondary_dns.incoming.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )
        assert_matches_type(Optional[IncomingGetResponse], incoming, path=['response'])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:

        response = await async_client.secondary_dns.incoming.with_raw_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get('X-Stainless-Lang') == 'python'
        incoming = await response.parse()
        assert_matches_type(Optional[IncomingGetResponse], incoming, path=['response'])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.secondary_dns.incoming.with_streaming_response.get(
            zone_id="269d8f4853475ca241c4e730be286b20",
        ) as response :
            assert not response.is_closed
            assert response.http_request.headers.get('X-Stainless-Lang') == 'python'

            incoming = await response.parse()
            assert_matches_type(Optional[IncomingGetResponse], incoming, path=['response'])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
          await async_client.secondary_dns.incoming.with_raw_response.get(
              zone_id="",
          )