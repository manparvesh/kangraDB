<div align="center">
  <h1>kangraDB</h1>

  <a href="https://travis-ci.org/manparvesh/kangraDB/builds" target="_blank"><img src="https://img.shields.io/travis-ci/manparvesh/kangraDB.svg?style=for-the-badge" alt="Build Status"></a> 
  <a href="https://manparvesh.mit-license.org/" target="_blank"><img src="https://img.shields.io/badge/license-MIT-blue.svg?longCache=true&style=for-the-badge" alt="License"></a> 
  <a href="https://codecov.io/gh/manparvesh/kangraDB" target="_blank"><img src="https://img.shields.io/codecov/c/github/manparvesh/kangraDB/master.svg?style=for-the-badge" alt="Coverage"></a>
  <p>A simple key/value database implementation in Python, based on <a href="http://aosabook.org/en/500L/dbdb-dog-bed-database.html">the Dog Bed Database implementation</a> from the book "500 Lines or less"</p>
</div>

## Features
- Saves data on disk using serialization

## Installation
- Clone this repository
- `[Optional]` create a `virtualenv with Python 3.6
- `pip install .`
- `kangra` to see options and information
- `kangra query` to make a query to a particular database.

## How to use
Example queries:
```
$ kangra query mp set firstkey "First value"
$ kangra query mp get firstkey
First value
$ kangra query mp delete firstkey
$ kangra query mp get firstkey
Key not found
```

## TODO
- More tests
- REST API
- specify storage file location
- consistent data reading
- use better data structure to update data, like B-Trees, B+ trees, etc
- Storing richer data by using `json` or `msgpack`
- database compaction

## LICENSE

```
MIT License

Copyright (c) 2018 Man Parvesh Singh Randhawa

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```