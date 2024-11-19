# Unity Audio Beheader
Chops off the header from mp3 files extracted from [UABEA](https://github.com/nesrak1/UABEA).

~~Mainly for one particular game which I bought the deluxe upgrade for expecting mp3 files, and it was a bloody Unity app!~~

*Edit*: On further inspection it turns out I just had to launch the app for it to extract the files by itself...Oops.

## Instructions

### Extract Assets

Open StreamingAsset file, go into "Info", select all the files and press "Export Raw" from UABEA.  


### Setup App

Install [UV](https://docs.astral.sh/uv/) and run:
```bash
uv sync
```

...or don't install UV and run:
```bash
pip install -r uv.lock
```

### Run App

Run the help command to learn how to use this app:

```bash
python ./main.py -h
```

Enjoy!
