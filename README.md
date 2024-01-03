# cmput404.github.io

## Installation

You want ghp-import and pelican, both of which you can apt-get if you want.

0. `git clone https://github.com/uofa-cmput404/uofa-cmput404.github.io.git && cd uofa-cmput404.github.io`
0. `virtualenv venv --python=python3`
0. `source venv/bin/activate`
0. `pip install -r requirements.txt`

## Running

0. `cd uofa-cmput404.github.io`
0. `source venv/bin/activate`
0. `make devserver`
    * local development with reloading at [localhost:8000](http://localhost:8000)
0. `make publish`
    * production html generated at `output`

To deploy to github pages, manually push the contents of `output` to the master branch.
Alternatively, you can use `make github`.

Licensed under Apache v2 [LICENSE](./LICENSE).
Static site generated using [Pelican](https://github.com/getpelican/pelican).
