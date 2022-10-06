# __init__.py
# 
# Ampli - A strong typed wrapper for your Analytics
# 
# This file is generated by Amplitude.
# To update run 'ampli pull book-launch-website'
# 
# Required dependencies: amplitude-analytics
# Tracking Plan Version: 1
# Build: 1.0.0
# Runtime: python-ampli
# 
# [View Tracking Plan](https://data.amplitude.com/codedbychavez/ab-testing-python/events/main/latest)
# 
# [Full Setup Instructions](https://data.amplitude.com/codedbychavez/ab-testing-python/implementation/main/latest/getting-started/book-launch-website)
# 
# pylint: skip-file
# flake8: noqa
# 
# WARNING: We do our best to remove lint warning from this file but if you would like to disable linting completely you will need to take some extra steps. See more details here: https://stackoverflow.com/questions/18444840/how-to-disable-a-pep8-error-in-a-specific-file/48772387


from amplitude import Amplitude, BaseEvent, EventOptions, Revenue, IdentifyEvent, \
    GroupIdentifyEvent, RevenueEvent, Plan, Config, PluginType, EventPlugin, DestinationPlugin
from .ampli import Ampli, LoadOptions, LoadClientOptions, Environment, ampli, \
    BookPurchase
