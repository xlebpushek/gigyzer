from typing import Union
from uuid import uuid4

from aiohttp import ClientError, ClientSession
from urllib3 import disable_warnings

from gigyzer.configs import GIGACHAT_APP_API_AUTH, GIGACHAT_APP_API_SCOPE

# TODO: Remove this line in production and fix error
# ERROR: InsecureRequestWarning: Unverified HTTPS request is being made to host "ngw.devices.sberbank.ru". Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
disable_warnings()


class Gigachat:
    @staticmethod
    async def oauth() -> Union[str, None]:
        url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"
        data = {"scope": GIGACHAT_APP_API_SCOPE}
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "application/json",
            "RqUID": str(uuid4()),
            "Authorization": f"Basic {GIGACHAT_APP_API_AUTH}"
        }
        async with ClientSession() as session:
            try:
                async with session.post(url, data=data, headers=headers, ssl=False) as response:
                    response.raise_for_status()
                    return (await response.json()).get("access_token")
            except ClientError as e:
                print(f"Error: {e}")
                return None

    @staticmethod
    async def completion(user_content: str, system_content: str | None = None) -> Union[str, None]:
        access_token = await Gigachat.oauth()
        messages = [
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content}
        ] if system_content else [{"role": "user", "content": user_content}]
        url = "https://gigachat.devices.sberbank.ru/api/v1/chat/completions"
        data = {
            "model": "GigaChat",
            "messages": messages,
            "temperature": 1,
            "top_p": 0.1,
            "n": 1,
            "stream": False,
            "max_tokens": 512,
            "repetition_penalty": 1,
            "update_interval": 0
        }
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Authorization": f"Bearer {access_token}",
        }
        async with ClientSession() as session:
            try:
                async with session.post(url, json=data, headers=headers, ssl=False) as response:
                    response.raise_for_status()
                    return (await response.json()).get("choices")[0].get("message").get("content")
            except ClientError as e:
                print(f"Error: {e}")
                return None


__all__ = ["Gigachat"]
