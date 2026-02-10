import pytest


@pytest.fixture
def left_hand(request):
    return request.getfixturevalue(request.param)


@pytest.fixture
def right_hand(request):
    return request.getfixturevalue(request.param)


@pytest.fixture
def pt(request):
    return request.getfixturevalue(request.param)
