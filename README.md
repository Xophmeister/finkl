# finkl

Learning Haskell by reimplementing its algebraic structures and classic
primitives in Python. Perhaps even usefully so!

## Install

    pip install finkl

## Abstract Base Classes

Where it makes sense -- and even where it doesn't -- Haskell's algebraic
typeclasses are implemented as Python abstract base classes (i.e., class
interfaces). Type annotations are used throughout, but bear in mind that
Python does not enforce these nor does its type system lend itself to
Haskell's parametric polymorphism.

### `finkl.data`

Convenience imports at the package root:

* `Eq`
* `Functor`
* `Applicative`
* `Monad`

### `finkl.data.eq`

#### `Eq`

Abstract base class for equality checking.

##### `__eq__`

Implementation required: Python dunder method to implement equality
checking. Equivalent to Haskell's:

```haskell
(==) :: Eq a => a -> a -> bool
```

##### `__neq__`

Default implementation is the logical inverse of `__eq__`. Equivalent to
Haskell's:

```haskell
(/=) :: Eq a => a -> a -> bool
```

### `finkl.data.functor`

#### `Functor[a]`

Abstract base class for functors over type `a`.

##### `fmap`

Implementation required: Functor mapping, which applies the given
function to itself and returns a functor. Equivalent to Haskell's:

```haskell
fmap :: Functor f => f a -> (a -> b) -> f b
```

#### `Applicative[a, b]`

Abstract base class for applicative functors; that is, functors of
functions from type `a` to `b`.

##### `pure`

Static implementation required: Return the functor from the given value.
Equivalent to Haskell's:

```haskell
pure :: Functor f => a -> f a
```

##### `applied_over`

Implementation required: Return the functor created by appling the
applicative functor over the specified input functor. Equivalent to
Haskell's:

```haskell
(<*>) :: Functor f => f (a -> b) -> f a -> f b
```

**Note** Python's matrix multiplication operator (`@`) is overloaded to
mimic Haskell's `(<*>)`.

### `finkl.data.monad`

#### `Monad[a]`

Abstract base class for monads over type `a`.

##### `retn`

Static implementation required: Return the monad from the given value.
Equivalent to Haskell's:

```haskell
return :: Monad m => a -> m a
```

##### `bind`

Implementation required: Monadic bind. Equivalent to Haskell's:

```haskell
(>>=) :: Monad m => m a -> (a -> m b) -> m b
```

**Note** Python's greater or equal than operator (`>=`) is overloaded to
mimic Haskell's `(>>=)`. Using `bind` may be clearer due to the operator
precedence of `>=`, which may necessitate excessive parentheses.

##### `then`

Default implementation does a monadic bind that supplants the monad with
the new, given monad. Equivalent to Haskell's:

```haskell
(>>) :: Monad m => m a -> m b -> m b
```

**Note** Python's right shift operator (`>>`) is overloaded to mimic
Haskell's `(>>)`. Using `then` may be clearer due to the operator
precedence of `>>`, which may necessitate excessive parentheses.

##### `fail`

Implementation required: Return a monad from a given input string.
Equivalent to Haskell's:

```haskell
fail :: Monad m => String => m a
```

**Note** This function is used in Haskell's `do` notation, an analogue
of which is not currently implemented. As such, the implementation for
this method can be stubbed.

## Implementations

### `finkl.util`

#### `identity`

Identity function. Equivalent to Haskell's:

```haskell
id :: a -> a
```

#### `compose`

Function composition. Equivalent to Haskell's:

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
