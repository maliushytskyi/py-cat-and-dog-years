from app.main import get_human_age


def test_should_return_zero_when_both_ages_are_zero() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_return_zero_when_ages_less_than_15() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_return_one_when_ages_equal_15() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_return_one_when_ages_at_upper_bound_of_second_stage() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_return_two_when_ages_enter_third_stage() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_return_two_when_cat_and_dog_still_in_same_third_step() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_diverge_when_cat_and_dog_step_sizes_differ() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_return_correct_values_for_large_age() -> None:
    assert get_human_age(100, 100) == [21, 17]


def test_should_discard_remainder_for_cat_between_steps() -> None:
    assert get_human_age(31, 0) == [3, 0]


def test_should_discard_remainder_for_dog_between_steps() -> None:
    assert get_human_age(0, 32) == [0, 3]
