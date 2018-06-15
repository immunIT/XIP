# XIP

## Description

XIP generates a list of IP addresses by applying a set of transformations used to bypass security measures e.g. blacklist filtering, WAF, etc.

[![asciicast](https://asciinema.org/a/bQ51BOhJcFMM9glz9Sky7FExm.png)](https://asciinema.org/a/bQ51BOhJcFMM9glz9Sky7FExm)

## Usage

```bash
python3 xip.py --help
```

## Docker alternative

### Official image

You can pull the official Drupwn image from the dockerhub registry using the following command:

```
docker pull immunit/XIP
```

### Build

To build the container, just use this command:

```bash
docker build -t xip .
```

Docker will download the Alpine image and then execute the installation steps.

> Be patient, the process can be quite long the first time.

### Run

Once the build process is over, get and enjoy your new tool.

```bash
docker run --rm -it xip --help
```

## Logging

The output generated is stored in the **/tmp/** folder.
When using docker, run your container using the following option

```bash
-v YOUR_PATH_FOLDER:/tmp/
```

## Disclaimer of Warranty

XIP is provided under this License on an "as is" basis, without warranty of any kind, either expressed, implied, or statutory, including, without limitation, warranties that the XIP is free of defects, merchantable, fit for a particular purpose or non-infringing.

## Acknowledgement

Credits of that tool amount to Nicolas Grégoire following the [Hackfest conference](https://youtu.be/TrBUrVDlc20?t=22m57s
)(French ONLY) which took place in 2015
