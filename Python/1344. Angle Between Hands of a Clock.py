class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour_angle = 30 * hour + 0.5 * minutes
        minute_angle = 6 * minutes
      
        # Calculate the absolute difference between the two hands
        angle_difference = abs(hour_angle - minute_angle)
      
        # Return the smaller angle between the two possible angles
        # (the direct angle or the reflex angle)
        return min(angle_difference, 360 - angle_difference)
