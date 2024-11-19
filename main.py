import argparse
import os
from io import BytesIO

import mutagen
import glob

from mutagen.mp3 import MP3

def main(args):

    os.makedirs(args.out_dir, exist_ok=True)
    in_dir = args.in_dir
    if not in_dir.endswith('/'):
        in_dir += '/'

    files = glob.glob(f'{in_dir}*.*')

    for file in files:
        print(f'Reading {file}')
        with open(file, 'rb') as fh:
            fh.seek(20)
            magic = fh.read(4)

            if magic != b'\xdfz\xfe\xf8':
                print("WARNING: Magic number is not 0xDF 0x7A 0xFE 0xF8! Skipping.")
                continue

            fh.seek(60)
            raw = fh.read()

        file = MP3(BytesIO(raw))
        tags = file.tags

        # Setup for a metaphorical game soundtrack scenario...
        album = tags.getall('TALB')[0]
        artist = tags.getall('TPE1')[0]
        title = tags.getall('TIT2')[0]
        position = tags.getall('TRCK')[0]
        disc = tags.getall('TPOS')[0]
        date = tags.getall('TDRC')[0]

        track_number = f'{position}.'
        if disc:
            track_number = f'{disc}.{position}'

        # Ensure none of the artist, album, or titles have non-breaking spaces in them
        artist = artist.text[0].replace('\xa0', '').replace(' /', ',')
        album = album.text[0].replace('\xa0', '').replace(' /', ',')
        title = title.text[0].replace('\xa0', '').replace(' /', ',')

        new_filename = f'{track_number} {artist} - {title}.mp3'
        new_out_path = os.path.join(args.out_dir, f'{album} ({date})')

        os.makedirs(new_out_path, exist_ok=True)

        with open(os.path.join(new_out_path, new_filename), 'wb') as fh:
            fh.write(raw)

    print("Done!")

parser = argparse.ArgumentParser(
                    prog='Unity Audio Beheader',
                    description='Chops off the header of extracted mp3 files',
                    epilog='bottom text')

parser.add_argument('in_dir')
parser.add_argument('-o', '--out_dir', default='./out')

main(parser.parse_args())