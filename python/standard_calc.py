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
    bounded_angle = ((angle + 180) % 360) #Ensure angle is in between [0,360)
    bounded_angle -= 180 #Limits the bound to [-180,180)
    return bounded_angle

def get_reflex_angle(angle):
    """Returns the reflex angle of the provided angle.

    e.g.)
        get_reflex_angle(30) = 210.0
        get_reflex_angle(200) = 20.0

    Args:
        angle (float): The input angle in degrees.

    Returns:
        float: The reflex angle in degrees.
    """
    if angle < 0:
        angle = angle+360
    else:
        angle = angle+180
    return angle

def is_angle_between(first_angle, middle_angle, second_angle):
    """Determines whether an angle is between two other angles.

    e.g.)
        is_angle_between(0, 45, 90) = True
        is_angle_between(45, 90, 270) = False

    Args:
        first_angle (float): The first bounding angle in degrees.
        middle_angle (float): The angle in question in degrees.
        second_angle (float): The second bounding angle in degrees.

    Returns:True
        bool:  when `middle_angle` is not in the reflex angle of `first_angle` and `second_angle`, false otherwise.
    """
    first_angle = bound_to_180(first_angle)
    second_angle = bound_to_180(second_angle)
    first_angle = get_reflex_angle(first_angle)
    second_angle = get_reflex_angle(second_angle)
    return (first_angle < middle_angle < second_angle) or (second_angle < middle_angle < first_angle)