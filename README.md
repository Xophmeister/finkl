# finkl

Learning Haskell by reimplementing its algebraic structures and classic
primitives in Python. Perhaps even usefully so!

## Abstract Base Classes

Where it makes sense -- and even where it doesn't -- Haskell's algebraic
typeclasses are implemented as Python abstract base classes (i.e., class
interfaces). Type annotations are used throughout, but bear in mind that
Python does not enforce these nor does its type system lend itself to
Haskell's parametric polymorphism.

### `finkl.data`

Convenience imports at the package root:

* [`Eq`](#eq)
* [`Functor`](#functor)
* [`Applicative`](#applicative)
* [`Monad`](#monad)

### `finkl.data.eq`

#### `Eq`

...

### `finkl.data.functor`

#### `Functor`

...

#### `Applicative`

...

### `finkl.data.monad`

#### `Monad`

...

## Implementations

### `finkl.utils`

#### `identity`

Identity function; equivalent to Haskell's:

```haskell
id :: a -> a
```

#### `compose`

Function composition; equivalent to Haskell's:

```haskell
(.) :: (b -> c) -> (a -> b) -> (a -> c)
```

### `finkl.maybe`

#### `Maybe`, `Just` and `Nothing`

Python doesn't have sum types, so `Just` and `Nothing` are just wrappers
that instantiate an appropriate `Maybe` object. You probably don't need
to use `Maybe` directly; you'd only need it for explicit type checking,
or when using `pure`/`retn`.

Implements:
* `Eq`
* `Applicative`
* `Monad`

**Note** The `Maybe` type is genericised over two type variables, as it
is an `Applicative`, which expects a function. This doesn't make a lot
of sense, but is required to satisfy Python's `Generic` interface.

Example:

```python
not Just(123) == Nothing
Just(123).fmap(lambda x: x + 1)
Just(lambda x: x + 1).applied_over(Just(123))
Just(123).bind(lambda x: Just(x + 1))
```
