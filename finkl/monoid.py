"""
Copyright (c) 2021 Christopher Harrison

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General
Public License for more details.

You should have received a copy of the GNU General Public License along
with this program. If not, see https://www.gnu.org/licenses/
"""

from __future__ import annotations

from abc import ABCMeta
from numbers import Number
from typing import Generic, TypeVar

from finkl.abc import Eq, Monoid
from finkl.monad import Maybe, Nothing


__all__ = ["Sum", "Product", "Any", "All", "First", "Last"]


a = TypeVar("a")
m = TypeVar("m")
maybe = TypeVar("maybe", bound=Maybe)


class _BaseMonoid(Generic[m], Eq, Monoid[m], metaclass=ABCMeta):
    """ We use inheritance to avoid too much boilerplate """
    _m:m

    def __init__(self, value:m) -> None:
        self._m = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self.get)})"

    def __eq__(self, rhs:_BaseMonoid[m]) -> bool:
        return self.get == rhs.get

    @property
    def get(self) -> m:
        return self._m


class Sum(_BaseMonoid[Number]):
    """ Numeric sum monoid """
    @staticmethod
    def mempty():
        return Sum(0)

    def mappend(self, rhs:Sum) -> Sum:
        return Sum(self.get + rhs.get)


class Product(_BaseMonoid[Number]):
    """ Numeric product monoid """
    @staticmethod
    def mempty():
        return Product(1)

    def mappend(self, rhs:Product) -> Product:
        return Product(self.get * rhs.get)


class Any(_BaseMonoid[bool]):
    """ Any monoid """
    @staticmethod
    def mempty():
        return Any(False)

    def mappend(self, rhs:Any) -> Any:
        return Any(self.get or rhs.get)


class All(_BaseMonoid[bool]):
    """ All monoid """
    @staticmethod
    def mempty():
        return All(True)

    def mappend(self, rhs:All) -> All:
        return All(self.get and rhs.get)


class First(Generic[maybe], _BaseMonoid[maybe]):
    """ First monoid """
    @staticmethod
    def mempty():
        return First(Nothing)

    def mappend(self, rhs:First[maybe]) -> First[maybe]:
        return First(self.get if self.get != Nothing else rhs.get)


class Last(Generic[maybe], _BaseMonoid[maybe]):
    """ Last monoid """
    @staticmethod
    def mempty():
        return Last(Nothing)

    def mappend(self, rhs:Last[maybe]) -> Last[maybe]:
        return Last(rhs.get if rhs.get != Nothing else self.get)
