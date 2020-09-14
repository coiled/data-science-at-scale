import time
import sys
import argparse
import os
from glob import glob
import tarfile
import urllib.request

import pandas as pd

import sources

DATASETS = ["flights", "all"]
here = os.path.dirname(__file__)
data_dir = os.path.abspath(os.path.join(here, 'data'))


def parse_args(args=None):
    parser = argparse.ArgumentParser(description='Downloads, generates and prepares data for the Dask tutorial.')
    parser.add_argument('--no-ssl-verify', dest='no_ssl_verify', action='store_true',
                        default=False, help='Disables SSL verification.')
    parser.add_argument("--small", action="store_true", default=None,
                        help="Whether to use smaller example datasets. Checks DASK_TUTORIAL_SMALL environment variable if not specified.")
    parser.add_argument("-d", "--dataset", choices=DATASETS, help="Datasets to generate.", default="all")

    return parser.parse_args(args)



if not os.path.exists(data_dir):
    raise OSError('data/ directory not found, aborting data preparation. ' \
                  'Restore it with "git checkout data" from the base ' \
                  'directory.')


def flights(small=None):
    start = time.time()
    flights_raw = os.path.join(data_dir, 'nycflights.tar.gz')
    flightdir = os.path.join(data_dir, 'nycflights')
    jsondir = os.path.join(data_dir, 'flightjson')
    if small is None:
        small = bool(os.environ.get("DASK_TUTORIAL_SMALL", False))

    if small:
        N = 500
    else:
        N = 10_000

    if not os.path.exists(flights_raw):
        print("- Downloading NYC Flights dataset... ", end='', flush=True)
        url = sources.flights_url
        urllib.request.urlretrieve(url, flights_raw)
        print("done", flush=True)

    if not os.path.exists(flightdir):
        print("- Extracting flight data... ", end='', flush=True)
        tar_path = os.path.join(data_dir, 'nycflights.tar.gz')
        with tarfile.open(tar_path, mode='r:gz') as flights:
            flights.extractall('data/')

        if small:
            for path in glob(os.path.join(data_dir, "nycflights", "*.csv")):
                with open(path, 'r') as f:
                    lines = f.readlines()[:1000]

                with open(path, 'w') as f:
                    f.writelines(lines)

        print("done", flush=True)

    if not os.path.exists(jsondir):
        print("- Creating json data... ", end='', flush=True)
        os.mkdir(jsondir)
        for path in glob(os.path.join(data_dir, 'nycflights', '*.csv')):
            prefix = os.path.splitext(os.path.basename(path))[0]
            df = pd.read_csv(path, nrows=N)
            df.to_json(os.path.join(data_dir, 'flightjson', prefix + '.json'),
                       orient='records', lines=True)
        print("done", flush=True)
    else:
        return

    end = time.time()
    print("** Created flights dataset! in {:0.2f}s**".format(end - start))


def main(args=None):
    args = parse_args(args)

    if (args.no_ssl_verify):
        print("- Disabling SSL Verification... ", end='', flush=True)
        import ssl
        ssl._create_default_https_context = ssl._create_unverified_context
        print("done", flush=True)

    if args.dataset == "flights" or args.dataset == "all":
        flights(args.small)


if __name__ == '__main__':
    sys.exit(main())
