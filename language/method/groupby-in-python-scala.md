groupby is different in python and Scala

#Scala groupby

Scala `groupBy` is implemnted in TraversableLike trait. It returns a Map.
The internal implementation is to traverse all elements based on function [T => B], if different T returns the same B, groupby will add up T together as map value.

```
List(1,2,3,1,2,3,1,2,3).groupBy(identity) => Map(2 -> List(2, 2, 2), 1 -> List(1, 1, 1), 3 -> List(3, 3, 3))
```

#Python groupby

Python `groupby` is defined in itertools package. It returns a list of Tuple2.
Why is that, because same element with different order may end up with different Tuple value.

```
[k for k, g in groupby("AAAABBBBCCCDAAABBB")]
```

Also, the value is an iterator, so it won't consume that much memory.

```
list(g) for k, g in groupby("AAAABBBBCCCDAAABBB")]
```