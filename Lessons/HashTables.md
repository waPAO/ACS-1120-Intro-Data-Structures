# Hash Tables

## Table of Contents <!-- omit in toc -->

1. [Activities](#activities)
1. [Objectives](#objectives)
1. [Resources](#resources)
1. [Challenges](#challenges)
1. [Stretch Challenges](#stretch-challenges)

## Activities

- Complete [linked list time complexity worksheet]

  - Watch [video of linked list time complexity worksheet review]

- Lecture and discussion following [hash table slides]

  - Watch [video of hash table lecture]

- Act out how hash table data structure and algorithms work

## Objectives

After completing this class session and the associated tutorial challenges, students will be able to ...

- Describe what a hash function does to enable mapping arbitrary keys to integers
- Describe and diagram how a hash table uses arrays and linked lists to store key-value entries
- Explain what a hash collision is, why it happens, and at least one resolution technique
- Compare advantages and disadvantages of using hash tables versus arrays or linked lists
- Implement essential hash table class instance methods

## Resources

- Review Make School's [hash table slides]
- Watch Make School's [hash table video lecture]
- Watch HackerRank's [hash table video]
- Watch Harvard's [old hash table video] and [new hash table video]
- Play with VisuAlgo's [interactive hash table visualization][visualgo hash table]
- Read Wikipedia's [hash table article]

## Challenges

These challenges are the baseline required to complete the project and course. Be sure to complete these before next class session and before starting on the stretch challenges below.

- [Page 9: Hash Table]

  - Implement `HashTable` class using [hash table starter code] with these instance methods:

    - `length()` - return the number of entries (key-value pairs) in the hash table by traversing its buckets
    - `items()` - return a list of all entries (key-value pairs) in the hash table
    - `keys()` - return a list of all keys in the hash table
    - `values()` - return a list of all values in the hash table
    - `contains(key)` - return a boolean indicating whether `key` is in the hash table
    - `get(key)` - return the value associated with `key` in the hash table, or raise `KeyError` if not found
    - `set(key, value)` - insert `key` (or update, if already present) with associated `value` in the hash table
    - `delete(key)` - delete `key` and associated value from the hash table, or raise `KeyError` if not found

  - Run `python hashtable.py` to test `HashTable` class instance methods on a small example
  - Run `pytest hashtable_test.py` to run the [hash table unit tests] and fix any failures

## Stretch Challenges

These challenges are more difficult and help you push your skills and understanding to the next level.

- [Page 9: Hash Table]

  - Add several magic methods to allow subscripting syntax like the [Python `dict` type]
  - Want to make the `HashTable` class more convenient to use? Add methods so that it can be used as an [iterable container], such as in a `for` loop
  - Consider an alternative approach to calculate the `length` of the hash table that doesn't require bucket traversal and implement it, then benchmark its running time against the first approach on small and large hash tables
  - Implement an alternative hash table [collision resolution] strategy instead of [separate chaining] (like [linear probing]) and consider what advantages and disadvantages this approach has over chaining with linked lists
  - Write additional test cases to expand the [hash table unit tests] to ensure your collision resolution strategy is robust

[collision resolution]: https://en.wikipedia.org/wiki/Hash_table#Collision_resolution
[hash table article]: https://en.wikipedia.org/wiki/Hash_table
[hash table slides]: https://github.com/tech-at-du/CS-1.2-Intro-Data-Structures/blob/master/Slides/HashTables.pdf
[hash table starter code]: https://github.com/tech-at-du/CS-1.2-Intro-Data-Structures/blob/master/Code/hashtable.py
[hash table unit tests]: https://github.com/tech-at-du/CS-1.2-Intro-Data-Structures/blob/master/Code/hashtable_test.py
[hash table video]: https://www.youtube.com/watch?v=shs0KM3wKv8
[hash table video lecture]: https://www.youtube.com/watch?v=nLWXJ6IDKmQ
[iterable container]: https://docs.python.org/3/library/stdtypes.html#typeiter
[linear probing]: https://en.wikipedia.org/wiki/Linear_probing
[linked list time complexity worksheet]: https://make.sc/linked-list-time-complexity-worksheet
[new hash table video]: https://www.youtube.com/watch?v=tjtFkT97Xmc
[old hash table video]: https://www.youtube.com/watch?v=h2d9b_nEzoA
[page 9: hash table]: https://bit.ly/tutorial-tweet-generator
[python `dict` type]: https://docs.python.org/3/library/stdtypes.html#dict
[separate chaining]: https://en.wikipedia.org/wiki/Hash_table#Separate_chaining
[video of hash table lecture]: https://www.youtube.com/watch?v=drQ_FfCVxFU
[video of linked list time complexity worksheet review]: https://www.youtube.com/watch?v=ZGtkVO6XlmQ
[visualgo hash table]: https://visualgo.net/hashtable
