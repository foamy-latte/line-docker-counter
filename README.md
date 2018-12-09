[![Build Status](https://travis-ci.com/foamy-latte/line-docker-counter.svg?branch=master)](https://travis-ci.com/foamy-latte/line-docker-counter)
[![Coverage Status](https://coveralls.io/repos/github/foamy-latte/line-docker-counter/badge.svg?branch=)](https://coveralls.io/github/foamy-latte/line-docker-counter?branch=)
[![Inline docs](http://inch-ci.org/github/foamy-latte/line-docker-counter.svg?branch=master)](http://inch-ci.org/github/foamy-latte/line-docker-counter)

## About

### Documentation reference

[Github pages](https://foamy-latte.github.io/line-docker-counter/docs/build/html/)

### Prerequisites

- Clean installation of Ubuntu host
- Internet connection

### Installation

From within the line-docker-counter directory:
```bash
chmod +x install.sh
sudo install.sh
```

### Coverage/tests

```bash
sudo ./test_no_coverage.sh
```

### Use

```bash
curl -s http://localhost/counter/?to=1000
```

## Infrastructure

![Infra](https://s3.ap-northeast-2.amazonaws.com/file.cpuabuse.com/public/boop/imageset/programming/site/2018-10-26/0784eec8a2ad9027923d8ec9af34d970.PNG)

### Database

`db/db_creation.sql` is added for reference purposes only, otherwise the database is to be used "as is".

### Notes

- Using third party image to run nginx proxy server
- Even though the counters are not physically deleted from the database upon app server shutdown, the functionality is fully preserved
- Tests are submitted to [coveralls](https://coveralls.io/github/foamy-latte/line-docker-counter) from the docker container inside of the travis container. The choice to use the docker inside travis is due to design, as we might want to have some test that require cross container testing. The warnings/errors coming up from within the travis builds are expected and not to be treated as errors, as the tests are run from within the docker and not the travis itself. The coverage shows lower than it actually is(close to 100%) due to testing functions directly, and not through testing Flask, I assume.