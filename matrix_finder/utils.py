import re

from exceptions import HTTPRequestException
from httpx import AsyncClient, TimeoutException, UnsupportedProtocol


async def get_http_response(url: str) -> str:
    async with AsyncClient() as http_client:
        try:
            response = await http_client.get(url)
        except TimeoutException:
            raise HTTPRequestException(f'Не удалось получить ответ от {url}')
        except UnsupportedProtocol:
            raise HTTPRequestException(f'Некорректно указан адрес {url}')

    if response.is_error:
        raise HTTPRequestException(f'При обращении к {url} произошла ошибка {response.content}')

    return response.content.decode()


async def get_matrix_from_response(content: str) -> list[list[int]]:
    return [list(map(int, re.findall(r'\d+', line))) for line in content.splitlines()[1::2]]


async def traverse_matrix(matrix: list[list[int]]) -> list[int]:
    result = []

    while matrix:
        for line in matrix:
            result.append(line.pop(0))

        matrix = list(map(list, zip(*reversed(matrix))))

    return result
