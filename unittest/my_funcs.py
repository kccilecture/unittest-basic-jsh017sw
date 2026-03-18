def is_even(number: int) -> bool:
    """주어진 값이 짝수이면 True, 홀수이면 False를 반환"""
    return number % 2 == 0


def get_average(numbers: list[int]) -> float:
    """정수 리스트의 평균값을 반환"""
    return sum(numbers) / len(numbers)


def get_max(numbers: list[int]) -> int:
    """정수 리스트의 최댓값을 반환"""
    return max(numbers)


def get_min(numbers: list[int]) -> int:
    """정수 리스트의 최솟값을 반환"""
    return min(numbers)