# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["RegistryCreateParams", "Auth", "AuthPrivateCredential"]


class RegistryCreateParams(TypedDict, total=False):
    account_id: Required[str]

    auth: Required[Auth]
    """Credentials for authenticating to a private external image registry.

    Store the private credential in
    [Secrets Store](https://developers.cloudflare.com/secrets-store/) before calling
    the API. Refer to
    [Image management](https://developers.cloudflare.com/containers/platform-details/image-management/)
    for the credential required by each supported registry provider.
    """

    domain: Required[str]
    """Hostname of the private registry, without a scheme or image path.

    Supported hostnames are `docker.io`, AWS ECR hostnames, and Google Artifact
    Registry `*-docker.pkg.dev` hostnames.
    """

    kind: Required[Literal["ECR", "DockerHub", "GAR"]]
    """Registry provider.

    This must match `domain`: `DockerHub` for `docker.io`, `ECR` for AWS ECR, or
    `GAR` for Google Artifact Registry.
    """

    is_public: Literal[False]
    """Omit this field or set it to `false`.

    Public Docker Hub images do not require registry configuration and cannot be
    added with this endpoint.
    """


class AuthPrivateCredential(TypedDict, total=False):
    """A reference to the private registry credential in Secrets Store.

    The referenced
    secret must have the `containers` scope. Raw secret values are not accepted.
    """

    secret_name: Required[str]
    """Name of the secret within the store."""

    store_id: Required[str]
    """Identifier of the Secrets Store containing the secret."""


class Auth(TypedDict, total=False):
    """Credentials for authenticating to a private external image registry.

    Store the
    private credential in [Secrets Store](https://developers.cloudflare.com/secrets-store/)
    before calling the API. Refer to [Image management](https://developers.cloudflare.com/containers/platform-details/image-management/)
    for the credential required by each supported registry provider.
    """

    private_credential: Required[AuthPrivateCredential]
    """A reference to the private registry credential in Secrets Store.

    The referenced secret must have the `containers` scope. Raw secret values are
    not accepted.
    """

    public_credential: Required[str]
    """
    The non-secret part of the registry credential: an AWS access key ID for ECR, a
    username for Docker Hub, or a service account email for Google Artifact
    Registry.
    """
