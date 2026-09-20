"""Synthetic beta module with an independent integer contribution."""


def contribution():
    return 2


def scaled(multiplier):
    return contribution() * multiplier
