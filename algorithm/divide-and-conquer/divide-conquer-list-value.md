# Problem description
Consider if you have a collection List[A] and you have a binary function (a: A, b: A) => A, and you want to return accumulated result A.
One way we can do it is to use a reduce function which is to accumulate from left to right (i.e. Scala). This works in almost all the scenarios.
However, there is a special case I have learnt recently. What happen if this binary function is associative (a + b) + c == a + (b + c)
In this case, the normal reduce function (acc, ele) => acc iterates one by one is not efficient. Instead, what we need is a mergesort (divide and conquer) algorithm.

```
  def add: (Int, Int) => Int = (a, b) => {
    (1 to 500000).map(_ + 1).map(_ + 1).map(_ + 1) //simulate heavy computation
    a + b
  }

  def time(x: => Unit) = {
    val start = System.currentTimeMillis()
    x
    val end = System.currentTimeMillis()
    println("the total diff: " +  (end - start))
  }

  var list = scala.collection.mutable.MutableList((1 to 100): _*)
  time(list.reduce(add))

  time({
    var step = 1
    val length = list.length
    while(step < length) {
      for (i <- 0 until length - step by step * 2) {
        list.update(i, add(list(i), list(i + step)))
      }
      step = step * 2
    }})

  print(list(0))
```

The second approach is actually faster.