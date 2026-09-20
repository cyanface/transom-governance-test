"""Synthetic gamma module with an independent integer contribution."""


def contribution():
    return 3


def scaled(multiplier):
    return contribution() * multiplier
