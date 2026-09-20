"""Synthetic alpha module with an independent integer contribution."""


def contribution():
    return 1


def scaled(multiplier):
    return contribution() * multiplier
