from standard_calc import bound_to_180, is_angle_between

""" Tests for bound_to_180() """


def test_bound_basic1():
    assert bound_to_180(0) == 0
    # Testing the zero angle.
    # This is a basic edge case where the angle is exactly 0, which should remain unchanged.

    assert bound_to_180(135) == 135.0
    # Testing a positive angle within the [-180, 180) range.
    # The angle 135 is already within the desired range, so the function should return it unchanged.

    assert bound_to_180(200) == -160.0
    # Testing a positive angle slightly exceeding the upper boundary of 180 degrees.
    # The function should wrap this angle back into the [-180, 180) range by subtracting 360, resulting in -160.

    assert bound_to_180(370) == 10.0
    # Testing a positive angle that exceeds 360 degrees.
    # The angle 370 is equivalent to 10 degrees after subtracting one full rotation (360 degrees).
    # This tests how the function handles angles larger than one full rotation.

    assert bound_to_180(180) == -180.0
    # Testing the edge case where the angle is exactly 180 degrees.
    # According to the function's logic, angles should be in the range [-180, 180),
    # so 180 should be wrapped around to -180.

    assert bound_to_180(-150) == -150.0
    # Testing a negative angle within the [-180, 0) range.
    # The angle -150 is already within the valid range, so it should be returned unchanged.

    assert bound_to_180(-200) == 160.0
    # Testing a negative angle slightly exceeding the lower boundary of -180 degrees.
    # The function should wrap this angle into the [-180, 180) range by adding 360, resulting in 160.

    assert bound_to_180(-370) == -10.0
    # Testing a negative angle that exceeds -360 degrees.
    # The angle -370 is equivalent to -10 degrees after adding one full rotation (360 degrees).
    # This tests how the function handles negative angles larger than one full negative rotation.


""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    # Testing a case where the middle angle (1) is between the first angle (0) and the second angle (2).
    # The function should return True.


def test_between_edge_case():
    assert not is_angle_between(45, 90, 270)
    # Testing a case where the middle angle (90) is not between the first angle (45) and the second angle (270).
    # The function should return False.
    