"""
Imaginary light platform that implements lights.

"""
import asyncio
import random

from homeassistant.components.light import (
    ATTR_BRIGHTNESS, SUPPORT_BRIGHTNESS, Light)

def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    """Set up the lightbringer platform."""
    add_devices_callback([
        LightBringer("Lightbringer", False, True)
    ])


class LightBringer(Light):
    """Representation of a lightbringer light."""

    def __init__(self, name, state, available=False, brightness=180):
        """Initialize the light."""
        self._name = name
        self._state = state
        self._brightness = brightness

    @property
    def should_poll(self) -> bool:
        """No polling needed for a demo light."""
        return False

    @property
    def name(self) -> str:
        """Return the name of the light if any."""
        return self._name

    @property
    def available(self) -> bool:
        """Return availability."""
        # This demo light is always available, but well-behaving components
        # should implement this to inform Home Assistant accordingly.
        return True

    @property
    def brightness(self) -> int:
        """Return the brightness of this light between 0..255."""
        return self._brightness

    @property
    def is_on(self) -> bool:
        """Return true if light is on."""
        return self._state

    @property
    def supported_features(self) -> int:
        """Flag supported features."""
        return SUPPORT_BRIGHTNESS

    def turn_on(self, **kwargs) -> None:
        """Turn the light on."""
        self._state = True

        if ATTR_BRIGHTNESS in kwargs:
            self._brightness = kwargs[ATTR_BRIGHTNESS]

        # As we have disabled polling, we need to inform
        # Home Assistant about updates in our state ourselves.
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs) -> None:
        """Turn the light off."""
        self._state = False

        # As we have disabled polling, we need to inform
        # Home Assistant about updates in our state ourselves.
        self.schedule_update_ha_state()

    @asyncio.coroutine
    def async_restore_state(self, is_on, **kwargs):
        """Restore the demo state."""
        self._state = is_on

        self._brightness = 180