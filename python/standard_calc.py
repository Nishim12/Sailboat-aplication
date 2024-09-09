def bound_to_180(angle):
    """Bounds the provided angle between [-180, 180) degrees.

    e.g.)
        bound_to_180(135) = 135.0
        bound_to_180(200) = -160.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The bounded angle in degrees.
    """
    bounded_angle = ((angle + 180) % 360)  # Ensure angle is between [0, 360)
    bounded_angle -= 180  # Limits the bound to [-180, 180)
    return bounded_angle


def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:
        bool: True when `middle_angle` is between `first_angle` and `second_angle` in a circular manner,
              False otherwise.
    """
    first_angle_within_360 = first_angle % 360
    second_angle_within_360 = second_angle % 360
    middle_angle_within_360 = middle_angle % 360

    # Bound angles to be within [-180, 180)
    bound_first_angle = bound_to_180(first_angle)
    bound_middle_angle = bound_to_180(middle_angle)
    bound_second_angle = bound_to_180(second_angle)

    # Case 1: Both angles have the same sign or the difference is less than 180 degrees
    #         than the bound_middle_angle should be bound between the bound_first_angle and
    #         bound_second_angle.
    if (bound_first_angle >= 0 and bound_second_angle >= 0) or \
       (bound_first_angle < 0 and bound_second_angle < 0) or \
       abs(bound_first_angle - bound_second_angle) < 180:
        return bound_first_angle <= bound_middle_angle <= bound_second_angle or \
               bound_second_angle <= bound_middle_angle <= bound_first_angle

    # Case 2: The difference between bound_first_angle and bound_second_angle is greater than 180 degrees
    #         than the middle_angle_within_360 should be bound between the first_angle_within_360
    #         and second_angle_within_360.
    elif abs(bound_first_angle - bound_second_angle) > 180:
        return first_angle_within_360 <= middle_angle_within_360 <= second_angle_within_360 or \
               second_angle_within_360 <= middle_angle_within_360 <= first_angle_within_360

    # Case 3: if the difference between bound_first_angle and bound_second_angle is 180 then the middle angle
    #         will always be bound between the first_angle and second_angle.
    else:
        return True
