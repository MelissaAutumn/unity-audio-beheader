# Unity Audio Beheader
Chops off the header from mp3 files extracted from [UABEA](https://github.com/nesrak1/UABEA).

Mainly for one particular game which I bought the deluxe upgrade for expecting mp3 files, and it was a bloody Unity app!

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

Replace the arguments below and run the help command to learn how to use this app:

```bash
python ./main.py -h
```

Enjoy!
