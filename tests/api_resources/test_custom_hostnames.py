# File generated from our OpenAPI spec by Stainless.

from __future__ import annotations

import os
from typing import Any, Optional, cast

import pytest

from cloudflare import Cloudflare, AsyncCloudflare
from tests.utils import assert_matches_type
from cloudflare.types import (
    CustomHostnameGetResponse,
    CustomHostnameDeleteResponse,
    CustomHostnameUpdateResponse,
    CustomHostnameCustomHostnameForAZoneListCustomHostnamesResponse,
    CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomHostnames:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update(self, client: Cloudflare) -> None:
        custom_hostname = client.custom_hostnames.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomHostnameUpdateResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_update_with_all_params(self, client: Cloudflare) -> None:
        custom_hostname = client.custom_hostnames.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_metadata={"key": "value"},
            custom_origin_server="origin2.example.com",
            custom_origin_sni="sni.example.com",
            ssl={
                "bundle_method": "ubiquitous",
                "certificate_authority": "google",
                "custom_certificate": "-----BEGIN CERTIFICATE-----\nMIIFJDCCBAygAwIBAgIQD0ifmj/Yi5NP/2gdUySbfzANBgkqhkiG9w0BAQsFADBN\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMScwJQYDVQQDEx5E...SzSHfXp5lnu/3V08I72q1QNzOCgY1XeL4GKVcj4or6cT6tX6oJH7ePPmfrBfqI/O\nOeH8gMJ+FuwtXYEPa4hBf38M5eU5xWG7\n-----END CERTIFICATE-----\n",
                "custom_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmG\ndtcGbg/1CGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKn\nabIRuGvBKwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpid\ntnKX/a+50GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+py\nFxIXjbEIdZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pE\newooaeO2izNTERcG9HzAacbVRn2Y2SWIyT/18QIDAQABAoIBACbhTYXBZYKmYPCb\nHBR1IBlCQA2nLGf0qRuJNJZg5iEzXows/6tc8YymZkQE7nolapWsQ+upk2y5Xdp/\naxiuprIs9JzkYK8Ox0r+dlwCG1kSW+UAbX0bQ/qUqlsTvU6muVuMP8vZYHxJ3wmb\n+ufRBKztPTQ/rYWaYQcgC0RWI20HTFBMxlTAyNxYNWzX7RKFkGVVyB9RsAtmcc8g\n+j4OdosbfNoJPS0HeIfNpAznDfHKdxDk2Yc1tV6RHBrC1ynyLE9+TaflIAdo2MVv\nKLMLq51GqYKtgJFIlBRPQqKoyXdz3fGvXrTkf/WY9QNq0J1Vk5ERePZ54mN8iZB7\n9lwy/AkCgYEA6FXzosxswaJ2wQLeoYc7ceaweX/SwTvxHgXzRyJIIT0eJWgx13Wo\n/WA3Iziimsjf6qE+SI/8laxPp2A86VMaIt3Z3mJN/CqSVGw8LK2AQst+OwdPyDMu\niacE8lj/IFGC8mwNUAb9CzGU3JpU4PxxGFjS/eMtGeRXCWkK4NE+G08CgYEA1Kp9\nN2JrVlqUz+gAX+LPmE9OEMAS9WQSQsfCHGogIFDGGcNf7+uwBM7GAaSJIP01zcoe\nVAgWdzXCv3FLhsaZoJ6RyLOLay5phbu1iaTr4UNYm5WtYTzMzqh8l1+MFFDl9xDB\nvULuCIIrglM5MeS/qnSg1uMoH2oVPj9TVst/ir8CgYEAxrI7Ws9Zc4Bt70N1As+U\nlySjaEVZCMkqvHJ6TCuVZFfQoE0r0whdLdRLU2PsLFP+q7qaeZQqgBaNSKeVcDYR\n9B+nY/jOmQoPewPVsp/vQTCnE/R81spu0mp0YI6cIheT1Z9zAy322svcc43JaWB7\nmEbeqyLOP4Z4qSOcmghZBSECgYACvR9Xs0DGn+wCsW4vze/2ei77MD4OQvepPIFX\ndFZtlBy5ADcgE9z0cuVB6CiL8DbdK5kwY9pGNr8HUCI03iHkW6Zs+0L0YmihfEVe\nPG19PSzK9CaDdhD9KFZSbLyVFmWfxOt50H7YRTTiPMgjyFpfi5j2q348yVT0tEQS\nfhRqaQKBgAcWPokmJ7EbYQGeMbS7HC8eWO/RyamlnSffdCdSc7ue3zdVJxpAkQ8W\nqu80pEIF6raIQfAf8MXiiZ7auFOSnHQTXUbhCpvDLKi0Mwq3G8Pl07l+2s6dQG6T\nlv6XTQaMyf6n1yjzL+fzDrH3qXMxHMO/b13EePXpDMpY7HQpoLDi\n-----END RSA PRIVATE KEY-----\n",
                "method": "http",
                "settings": {
                    "ciphers": ["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
                    "early_hints": "on",
                    "http2": "on",
                    "min_tls_version": "1.2",
                    "tls_1_3": "on",
                },
                "type": "dv",
                "wildcard": False,
            },
        )
        assert_matches_type(CustomHostnameUpdateResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_update(self, client: Cloudflare) -> None:
        response = client.custom_hostnames.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_hostname = response.parse()
        assert_matches_type(CustomHostnameUpdateResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_update(self, client: Cloudflare) -> None:
        with client.custom_hostnames.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_hostname = response.parse()
            assert_matches_type(CustomHostnameUpdateResponse, custom_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_update(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_hostnames.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_hostname_id` but received ''"):
            client.custom_hostnames.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_delete(self, client: Cloudflare) -> None:
        custom_hostname = client.custom_hostnames.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomHostnameDeleteResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_delete(self, client: Cloudflare) -> None:
        response = client.custom_hostnames.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_hostname = response.parse()
        assert_matches_type(CustomHostnameDeleteResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_delete(self, client: Cloudflare) -> None:
        with client.custom_hostnames.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_hostname = response.parse()
            assert_matches_type(CustomHostnameDeleteResponse, custom_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_delete(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_hostnames.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_hostname_id` but received ''"):
            client.custom_hostnames.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_custom_hostname_for_a_zone_create_custom_hostname(self, client: Cloudflare) -> None:
        custom_hostname = client.custom_hostnames.custom_hostname_for_a_zone_create_custom_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            hostname="app.example.com",
            ssl={},
        )
        assert_matches_type(
            CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse, custom_hostname, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_custom_hostname_for_a_zone_create_custom_hostname_with_all_params(self, client: Cloudflare) -> None:
        custom_hostname = client.custom_hostnames.custom_hostname_for_a_zone_create_custom_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            hostname="app.example.com",
            ssl={
                "bundle_method": "ubiquitous",
                "certificate_authority": "google",
                "custom_certificate": "-----BEGIN CERTIFICATE-----\nMIIFJDCCBAygAwIBAgIQD0ifmj/Yi5NP/2gdUySbfzANBgkqhkiG9w0BAQsFADBN\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMScwJQYDVQQDEx5E...SzSHfXp5lnu/3V08I72q1QNzOCgY1XeL4GKVcj4or6cT6tX6oJH7ePPmfrBfqI/O\nOeH8gMJ+FuwtXYEPa4hBf38M5eU5xWG7\n-----END CERTIFICATE-----\n",
                "custom_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmG\ndtcGbg/1CGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKn\nabIRuGvBKwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpid\ntnKX/a+50GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+py\nFxIXjbEIdZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pE\newooaeO2izNTERcG9HzAacbVRn2Y2SWIyT/18QIDAQABAoIBACbhTYXBZYKmYPCb\nHBR1IBlCQA2nLGf0qRuJNJZg5iEzXows/6tc8YymZkQE7nolapWsQ+upk2y5Xdp/\naxiuprIs9JzkYK8Ox0r+dlwCG1kSW+UAbX0bQ/qUqlsTvU6muVuMP8vZYHxJ3wmb\n+ufRBKztPTQ/rYWaYQcgC0RWI20HTFBMxlTAyNxYNWzX7RKFkGVVyB9RsAtmcc8g\n+j4OdosbfNoJPS0HeIfNpAznDfHKdxDk2Yc1tV6RHBrC1ynyLE9+TaflIAdo2MVv\nKLMLq51GqYKtgJFIlBRPQqKoyXdz3fGvXrTkf/WY9QNq0J1Vk5ERePZ54mN8iZB7\n9lwy/AkCgYEA6FXzosxswaJ2wQLeoYc7ceaweX/SwTvxHgXzRyJIIT0eJWgx13Wo\n/WA3Iziimsjf6qE+SI/8laxPp2A86VMaIt3Z3mJN/CqSVGw8LK2AQst+OwdPyDMu\niacE8lj/IFGC8mwNUAb9CzGU3JpU4PxxGFjS/eMtGeRXCWkK4NE+G08CgYEA1Kp9\nN2JrVlqUz+gAX+LPmE9OEMAS9WQSQsfCHGogIFDGGcNf7+uwBM7GAaSJIP01zcoe\nVAgWdzXCv3FLhsaZoJ6RyLOLay5phbu1iaTr4UNYm5WtYTzMzqh8l1+MFFDl9xDB\nvULuCIIrglM5MeS/qnSg1uMoH2oVPj9TVst/ir8CgYEAxrI7Ws9Zc4Bt70N1As+U\nlySjaEVZCMkqvHJ6TCuVZFfQoE0r0whdLdRLU2PsLFP+q7qaeZQqgBaNSKeVcDYR\n9B+nY/jOmQoPewPVsp/vQTCnE/R81spu0mp0YI6cIheT1Z9zAy322svcc43JaWB7\nmEbeqyLOP4Z4qSOcmghZBSECgYACvR9Xs0DGn+wCsW4vze/2ei77MD4OQvepPIFX\ndFZtlBy5ADcgE9z0cuVB6CiL8DbdK5kwY9pGNr8HUCI03iHkW6Zs+0L0YmihfEVe\nPG19PSzK9CaDdhD9KFZSbLyVFmWfxOt50H7YRTTiPMgjyFpfi5j2q348yVT0tEQS\nfhRqaQKBgAcWPokmJ7EbYQGeMbS7HC8eWO/RyamlnSffdCdSc7ue3zdVJxpAkQ8W\nqu80pEIF6raIQfAf8MXiiZ7auFOSnHQTXUbhCpvDLKi0Mwq3G8Pl07l+2s6dQG6T\nlv6XTQaMyf6n1yjzL+fzDrH3qXMxHMO/b13EePXpDMpY7HQpoLDi\n-----END RSA PRIVATE KEY-----\n",
                "method": "http",
                "settings": {
                    "ciphers": ["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
                    "early_hints": "on",
                    "http2": "on",
                    "min_tls_version": "1.2",
                    "tls_1_3": "on",
                },
                "type": "dv",
                "wildcard": False,
            },
            custom_metadata={"key": "value"},
        )
        assert_matches_type(
            CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse, custom_hostname, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_custom_hostname_for_a_zone_create_custom_hostname(self, client: Cloudflare) -> None:
        response = client.custom_hostnames.with_raw_response.custom_hostname_for_a_zone_create_custom_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            hostname="app.example.com",
            ssl={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_hostname = response.parse()
        assert_matches_type(
            CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse, custom_hostname, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_custom_hostname_for_a_zone_create_custom_hostname(self, client: Cloudflare) -> None:
        with client.custom_hostnames.with_streaming_response.custom_hostname_for_a_zone_create_custom_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            hostname="app.example.com",
            ssl={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_hostname = response.parse()
            assert_matches_type(
                CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse, custom_hostname, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_custom_hostname_for_a_zone_create_custom_hostname(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_hostnames.with_raw_response.custom_hostname_for_a_zone_create_custom_hostname(
                "",
                hostname="app.example.com",
                ssl={},
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_custom_hostname_for_a_zone_list_custom_hostnames(self, client: Cloudflare) -> None:
        custom_hostname = client.custom_hostnames.custom_hostname_for_a_zone_list_custom_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[CustomHostnameCustomHostnameForAZoneListCustomHostnamesResponse],
            custom_hostname,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_method_custom_hostname_for_a_zone_list_custom_hostnames_with_all_params(self, client: Cloudflare) -> None:
        custom_hostname = client.custom_hostnames.custom_hostname_for_a_zone_list_custom_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
            id="0d89c70d-ad9f-4843-b99f-6cc0252067e9",
            direction="desc",
            hostname="app.example.com",
            order="ssl",
            page=1,
            per_page=5,
            ssl=0,
        )
        assert_matches_type(
            Optional[CustomHostnameCustomHostnameForAZoneListCustomHostnamesResponse],
            custom_hostname,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_custom_hostname_for_a_zone_list_custom_hostnames(self, client: Cloudflare) -> None:
        response = client.custom_hostnames.with_raw_response.custom_hostname_for_a_zone_list_custom_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_hostname = response.parse()
        assert_matches_type(
            Optional[CustomHostnameCustomHostnameForAZoneListCustomHostnamesResponse],
            custom_hostname,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_custom_hostname_for_a_zone_list_custom_hostnames(self, client: Cloudflare) -> None:
        with client.custom_hostnames.with_streaming_response.custom_hostname_for_a_zone_list_custom_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_hostname = response.parse()
            assert_matches_type(
                Optional[CustomHostnameCustomHostnameForAZoneListCustomHostnamesResponse],
                custom_hostname,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_custom_hostname_for_a_zone_list_custom_hostnames(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_hostnames.with_raw_response.custom_hostname_for_a_zone_list_custom_hostnames(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_get(self, client: Cloudflare) -> None:
        custom_hostname = client.custom_hostnames.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomHostnameGetResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_get(self, client: Cloudflare) -> None:
        response = client.custom_hostnames.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_hostname = response.parse()
        assert_matches_type(CustomHostnameGetResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_get(self, client: Cloudflare) -> None:
        with client.custom_hostnames.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_hostname = response.parse()
            assert_matches_type(CustomHostnameGetResponse, custom_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_get(self, client: Cloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            client.custom_hostnames.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_hostname_id` but received ''"):
            client.custom_hostnames.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )


class TestAsyncCustomHostnames:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update(self, async_client: AsyncCloudflare) -> None:
        custom_hostname = await async_client.custom_hostnames.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomHostnameUpdateResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncCloudflare) -> None:
        custom_hostname = await async_client.custom_hostnames.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            custom_metadata={"key": "value"},
            custom_origin_server="origin2.example.com",
            custom_origin_sni="sni.example.com",
            ssl={
                "bundle_method": "ubiquitous",
                "certificate_authority": "google",
                "custom_certificate": "-----BEGIN CERTIFICATE-----\nMIIFJDCCBAygAwIBAgIQD0ifmj/Yi5NP/2gdUySbfzANBgkqhkiG9w0BAQsFADBN\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMScwJQYDVQQDEx5E...SzSHfXp5lnu/3V08I72q1QNzOCgY1XeL4GKVcj4or6cT6tX6oJH7ePPmfrBfqI/O\nOeH8gMJ+FuwtXYEPa4hBf38M5eU5xWG7\n-----END CERTIFICATE-----\n",
                "custom_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmG\ndtcGbg/1CGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKn\nabIRuGvBKwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpid\ntnKX/a+50GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+py\nFxIXjbEIdZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pE\newooaeO2izNTERcG9HzAacbVRn2Y2SWIyT/18QIDAQABAoIBACbhTYXBZYKmYPCb\nHBR1IBlCQA2nLGf0qRuJNJZg5iEzXows/6tc8YymZkQE7nolapWsQ+upk2y5Xdp/\naxiuprIs9JzkYK8Ox0r+dlwCG1kSW+UAbX0bQ/qUqlsTvU6muVuMP8vZYHxJ3wmb\n+ufRBKztPTQ/rYWaYQcgC0RWI20HTFBMxlTAyNxYNWzX7RKFkGVVyB9RsAtmcc8g\n+j4OdosbfNoJPS0HeIfNpAznDfHKdxDk2Yc1tV6RHBrC1ynyLE9+TaflIAdo2MVv\nKLMLq51GqYKtgJFIlBRPQqKoyXdz3fGvXrTkf/WY9QNq0J1Vk5ERePZ54mN8iZB7\n9lwy/AkCgYEA6FXzosxswaJ2wQLeoYc7ceaweX/SwTvxHgXzRyJIIT0eJWgx13Wo\n/WA3Iziimsjf6qE+SI/8laxPp2A86VMaIt3Z3mJN/CqSVGw8LK2AQst+OwdPyDMu\niacE8lj/IFGC8mwNUAb9CzGU3JpU4PxxGFjS/eMtGeRXCWkK4NE+G08CgYEA1Kp9\nN2JrVlqUz+gAX+LPmE9OEMAS9WQSQsfCHGogIFDGGcNf7+uwBM7GAaSJIP01zcoe\nVAgWdzXCv3FLhsaZoJ6RyLOLay5phbu1iaTr4UNYm5WtYTzMzqh8l1+MFFDl9xDB\nvULuCIIrglM5MeS/qnSg1uMoH2oVPj9TVst/ir8CgYEAxrI7Ws9Zc4Bt70N1As+U\nlySjaEVZCMkqvHJ6TCuVZFfQoE0r0whdLdRLU2PsLFP+q7qaeZQqgBaNSKeVcDYR\n9B+nY/jOmQoPewPVsp/vQTCnE/R81spu0mp0YI6cIheT1Z9zAy322svcc43JaWB7\nmEbeqyLOP4Z4qSOcmghZBSECgYACvR9Xs0DGn+wCsW4vze/2ei77MD4OQvepPIFX\ndFZtlBy5ADcgE9z0cuVB6CiL8DbdK5kwY9pGNr8HUCI03iHkW6Zs+0L0YmihfEVe\nPG19PSzK9CaDdhD9KFZSbLyVFmWfxOt50H7YRTTiPMgjyFpfi5j2q348yVT0tEQS\nfhRqaQKBgAcWPokmJ7EbYQGeMbS7HC8eWO/RyamlnSffdCdSc7ue3zdVJxpAkQ8W\nqu80pEIF6raIQfAf8MXiiZ7auFOSnHQTXUbhCpvDLKi0Mwq3G8Pl07l+2s6dQG6T\nlv6XTQaMyf6n1yjzL+fzDrH3qXMxHMO/b13EePXpDMpY7HQpoLDi\n-----END RSA PRIVATE KEY-----\n",
                "method": "http",
                "settings": {
                    "ciphers": ["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
                    "early_hints": "on",
                    "http2": "on",
                    "min_tls_version": "1.2",
                    "tls_1_3": "on",
                },
                "type": "dv",
                "wildcard": False,
            },
        )
        assert_matches_type(CustomHostnameUpdateResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_hostnames.with_raw_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_hostname = await response.parse()
        assert_matches_type(CustomHostnameUpdateResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_hostnames.with_streaming_response.update(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_hostname = await response.parse()
            assert_matches_type(CustomHostnameUpdateResponse, custom_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_update(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_hostnames.with_raw_response.update(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_hostname_id` but received ''"):
            await async_client.custom_hostnames.with_raw_response.update(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_delete(self, async_client: AsyncCloudflare) -> None:
        custom_hostname = await async_client.custom_hostnames.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomHostnameDeleteResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_hostnames.with_raw_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_hostname = await response.parse()
        assert_matches_type(CustomHostnameDeleteResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_hostnames.with_streaming_response.delete(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_hostname = await response.parse()
            assert_matches_type(CustomHostnameDeleteResponse, custom_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_hostnames.with_raw_response.delete(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_hostname_id` but received ''"):
            await async_client.custom_hostnames.with_raw_response.delete(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_custom_hostname_for_a_zone_create_custom_hostname(
        self, async_client: AsyncCloudflare
    ) -> None:
        custom_hostname = await async_client.custom_hostnames.custom_hostname_for_a_zone_create_custom_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            hostname="app.example.com",
            ssl={},
        )
        assert_matches_type(
            CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse, custom_hostname, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_custom_hostname_for_a_zone_create_custom_hostname_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        custom_hostname = await async_client.custom_hostnames.custom_hostname_for_a_zone_create_custom_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            hostname="app.example.com",
            ssl={
                "bundle_method": "ubiquitous",
                "certificate_authority": "google",
                "custom_certificate": "-----BEGIN CERTIFICATE-----\nMIIFJDCCBAygAwIBAgIQD0ifmj/Yi5NP/2gdUySbfzANBgkqhkiG9w0BAQsFADBN\nMQswCQYDVQQGEwJVUzEVMBMGA1UEChMMRGlnaUNlcnQgSW5jMScwJQYDVQQDEx5E...SzSHfXp5lnu/3V08I72q1QNzOCgY1XeL4GKVcj4or6cT6tX6oJH7ePPmfrBfqI/O\nOeH8gMJ+FuwtXYEPa4hBf38M5eU5xWG7\n-----END CERTIFICATE-----\n",
                "custom_key": "-----BEGIN RSA PRIVATE KEY-----\nMIIEowIBAAKCAQEAwQHoetcl9+5ikGzV6cMzWtWPJHqXT3wpbEkRU9Yz7lgvddmG\ndtcGbg/1CGZu0jJGkMoppoUo4c3dts3iwqRYmBikUP77wwY2QGmDZw2FvkJCJlKn\nabIRuGvBKwzESIXgKk2016aTP6/dAjEHyo6SeoK8lkIySUvK0fyOVlsiEsCmOpid\ntnKX/a+50GjB79CJH4ER2lLVZnhePFR/zUOyPxZQQ4naHf7yu/b5jhO0f8fwt+py\nFxIXjbEIdZliWRkRMtzrHOJIhrmJ2A1J7iOrirbbwillwjjNVUWPf3IJ3M12S9pE\newooaeO2izNTERcG9HzAacbVRn2Y2SWIyT/18QIDAQABAoIBACbhTYXBZYKmYPCb\nHBR1IBlCQA2nLGf0qRuJNJZg5iEzXows/6tc8YymZkQE7nolapWsQ+upk2y5Xdp/\naxiuprIs9JzkYK8Ox0r+dlwCG1kSW+UAbX0bQ/qUqlsTvU6muVuMP8vZYHxJ3wmb\n+ufRBKztPTQ/rYWaYQcgC0RWI20HTFBMxlTAyNxYNWzX7RKFkGVVyB9RsAtmcc8g\n+j4OdosbfNoJPS0HeIfNpAznDfHKdxDk2Yc1tV6RHBrC1ynyLE9+TaflIAdo2MVv\nKLMLq51GqYKtgJFIlBRPQqKoyXdz3fGvXrTkf/WY9QNq0J1Vk5ERePZ54mN8iZB7\n9lwy/AkCgYEA6FXzosxswaJ2wQLeoYc7ceaweX/SwTvxHgXzRyJIIT0eJWgx13Wo\n/WA3Iziimsjf6qE+SI/8laxPp2A86VMaIt3Z3mJN/CqSVGw8LK2AQst+OwdPyDMu\niacE8lj/IFGC8mwNUAb9CzGU3JpU4PxxGFjS/eMtGeRXCWkK4NE+G08CgYEA1Kp9\nN2JrVlqUz+gAX+LPmE9OEMAS9WQSQsfCHGogIFDGGcNf7+uwBM7GAaSJIP01zcoe\nVAgWdzXCv3FLhsaZoJ6RyLOLay5phbu1iaTr4UNYm5WtYTzMzqh8l1+MFFDl9xDB\nvULuCIIrglM5MeS/qnSg1uMoH2oVPj9TVst/ir8CgYEAxrI7Ws9Zc4Bt70N1As+U\nlySjaEVZCMkqvHJ6TCuVZFfQoE0r0whdLdRLU2PsLFP+q7qaeZQqgBaNSKeVcDYR\n9B+nY/jOmQoPewPVsp/vQTCnE/R81spu0mp0YI6cIheT1Z9zAy322svcc43JaWB7\nmEbeqyLOP4Z4qSOcmghZBSECgYACvR9Xs0DGn+wCsW4vze/2ei77MD4OQvepPIFX\ndFZtlBy5ADcgE9z0cuVB6CiL8DbdK5kwY9pGNr8HUCI03iHkW6Zs+0L0YmihfEVe\nPG19PSzK9CaDdhD9KFZSbLyVFmWfxOt50H7YRTTiPMgjyFpfi5j2q348yVT0tEQS\nfhRqaQKBgAcWPokmJ7EbYQGeMbS7HC8eWO/RyamlnSffdCdSc7ue3zdVJxpAkQ8W\nqu80pEIF6raIQfAf8MXiiZ7auFOSnHQTXUbhCpvDLKi0Mwq3G8Pl07l+2s6dQG6T\nlv6XTQaMyf6n1yjzL+fzDrH3qXMxHMO/b13EePXpDMpY7HQpoLDi\n-----END RSA PRIVATE KEY-----\n",
                "method": "http",
                "settings": {
                    "ciphers": ["ECDHE-RSA-AES128-GCM-SHA256", "AES128-SHA"],
                    "early_hints": "on",
                    "http2": "on",
                    "min_tls_version": "1.2",
                    "tls_1_3": "on",
                },
                "type": "dv",
                "wildcard": False,
            },
            custom_metadata={"key": "value"},
        )
        assert_matches_type(
            CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse, custom_hostname, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_custom_hostname_for_a_zone_create_custom_hostname(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.custom_hostnames.with_raw_response.custom_hostname_for_a_zone_create_custom_hostname(
                "023e105f4ecef8ad9ca31a8372d0c353",
                hostname="app.example.com",
                ssl={},
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_hostname = await response.parse()
        assert_matches_type(
            CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse, custom_hostname, path=["response"]
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_custom_hostname_for_a_zone_create_custom_hostname(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.custom_hostnames.with_streaming_response.custom_hostname_for_a_zone_create_custom_hostname(
            "023e105f4ecef8ad9ca31a8372d0c353",
            hostname="app.example.com",
            ssl={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_hostname = await response.parse()
            assert_matches_type(
                CustomHostnameCustomHostnameForAZoneCreateCustomHostnameResponse, custom_hostname, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_custom_hostname_for_a_zone_create_custom_hostname(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_hostnames.with_raw_response.custom_hostname_for_a_zone_create_custom_hostname(
                "",
                hostname="app.example.com",
                ssl={},
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_custom_hostname_for_a_zone_list_custom_hostnames(self, async_client: AsyncCloudflare) -> None:
        custom_hostname = await async_client.custom_hostnames.custom_hostname_for_a_zone_list_custom_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(
            Optional[CustomHostnameCustomHostnameForAZoneListCustomHostnamesResponse],
            custom_hostname,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_method_custom_hostname_for_a_zone_list_custom_hostnames_with_all_params(
        self, async_client: AsyncCloudflare
    ) -> None:
        custom_hostname = await async_client.custom_hostnames.custom_hostname_for_a_zone_list_custom_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
            id="0d89c70d-ad9f-4843-b99f-6cc0252067e9",
            direction="desc",
            hostname="app.example.com",
            order="ssl",
            page=1,
            per_page=5,
            ssl=0,
        )
        assert_matches_type(
            Optional[CustomHostnameCustomHostnameForAZoneListCustomHostnamesResponse],
            custom_hostname,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_custom_hostname_for_a_zone_list_custom_hostnames(
        self, async_client: AsyncCloudflare
    ) -> None:
        response = (
            await async_client.custom_hostnames.with_raw_response.custom_hostname_for_a_zone_list_custom_hostnames(
                "023e105f4ecef8ad9ca31a8372d0c353",
            )
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_hostname = await response.parse()
        assert_matches_type(
            Optional[CustomHostnameCustomHostnameForAZoneListCustomHostnamesResponse],
            custom_hostname,
            path=["response"],
        )

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_custom_hostname_for_a_zone_list_custom_hostnames(
        self, async_client: AsyncCloudflare
    ) -> None:
        async with async_client.custom_hostnames.with_streaming_response.custom_hostname_for_a_zone_list_custom_hostnames(
            "023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_hostname = await response.parse()
            assert_matches_type(
                Optional[CustomHostnameCustomHostnameForAZoneListCustomHostnamesResponse],
                custom_hostname,
                path=["response"],
            )

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_custom_hostname_for_a_zone_list_custom_hostnames(
        self, async_client: AsyncCloudflare
    ) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_hostnames.with_raw_response.custom_hostname_for_a_zone_list_custom_hostnames(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_get(self, async_client: AsyncCloudflare) -> None:
        custom_hostname = await async_client.custom_hostnames.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )
        assert_matches_type(CustomHostnameGetResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncCloudflare) -> None:
        response = await async_client.custom_hostnames.with_raw_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_hostname = await response.parse()
        assert_matches_type(CustomHostnameGetResponse, custom_hostname, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncCloudflare) -> None:
        async with async_client.custom_hostnames.with_streaming_response.get(
            "023e105f4ecef8ad9ca31a8372d0c353",
            zone_id="023e105f4ecef8ad9ca31a8372d0c353",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_hostname = await response.parse()
            assert_matches_type(CustomHostnameGetResponse, custom_hostname, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_get(self, async_client: AsyncCloudflare) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `zone_id` but received ''"):
            await async_client.custom_hostnames.with_raw_response.get(
                "023e105f4ecef8ad9ca31a8372d0c353",
                zone_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `custom_hostname_id` but received ''"):
            await async_client.custom_hostnames.with_raw_response.get(
                "",
                zone_id="023e105f4ecef8ad9ca31a8372d0c353",
            )
