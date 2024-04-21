#!/usr/bin/env python3
# settings.py - settings for alien_invasion.py


class Settings:
    """Main settings class for alien_invasion.py"""

    def __init__(self, screen_dimensions_tuple, background_color_tuple):
        """Initialize the game settings"""
        # Screen settings
        self.screen_width, self.screen_height = screen_dimensions_tuple
        self.bg_color = background_color_tuple

        # Ship settings
        self.ship_speed = 1.5
