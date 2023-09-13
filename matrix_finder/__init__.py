import asyncio

from utils import get_http_response, get_matrix_from_response, traverse_matrix


async def get_matrix(url: str) -> list[int]:
    response = await get_http_response(url)
    matrix = await get_matrix_from_response(response)
    traversal_matrix = await traverse_matrix(matrix)

    return traversal_matrix


if __name__ == '__main__':
    asyncio.run(get_matrix('https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'))
