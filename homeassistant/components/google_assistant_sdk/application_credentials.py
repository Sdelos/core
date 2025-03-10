"""application_credentials platform for Google Assistant SDK."""
import oauth2client

from homeassistant.components.application_credentials import AuthorizationServer
from homeassistant.core import HomeAssistant


async def async_get_authorization_server(hass: HomeAssistant) -> AuthorizationServer:
    """Return authorization server."""
    return AuthorizationServer(
        oauth2client.GOOGLE_AUTH_URI,
        oauth2client.GOOGLE_TOKEN_URI,
    )


async def async_get_description_placeholders(hass: HomeAssistant) -> dict[str, str]:
    """Return description placeholders for the credentials dialog."""
    return {
        "oauth_consent_url": "https://console.cloud.google.com/apis/credentials/consent",
        "more_info_url": "https://www.home-assistant.io/integrations/google_assistant_sdk/",
        "oauth_creds_url": "https://console.cloud.google.com/apis/credentials",
    }
