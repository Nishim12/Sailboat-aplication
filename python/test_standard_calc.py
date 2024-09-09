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
    # This checks the basic functionality where the middle angle lies directly between the two bounding angles.

    assert not is_angle_between(45, 90, 270)
    # Testing a case where the middle angle (90) is not between the first angle (45) and the second angle (270).
    # The function should correctly handle the circular nature of angles and return False.

    assert is_angle_between(45, 0, 270)
    # Testing a case where the middle angle (0) is between the first angle (45) and the second angle (270).
    # This tests the handling of angles wrapping around the zero mark.

    assert is_angle_between(210, 180, 135)
    # Testing a case where the middle angle (210) is between the first angle (180) and the second angle (135).
    # This checks if the function can handle angles requiring normalization from negative to positive ranges.

    assert is_angle_between(-570, 160, -150)
    # Testing a case with large negative angles and checking if the function normalizes them correctly.

    assert is_angle_between(90, 89, 270)
    # Testing a case where the middle angle (89) is between the first angle (90) and the second angle (270).
    # This checks handling of angles close to the boundary in a circular context.
