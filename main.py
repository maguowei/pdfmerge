import os
from pathlib import Path
import click
from PyPDF2 import PdfMerger


@click.command()
@click.option('--input-dir', default='.', help='input dir')
@click.option('--out', default='merged-pdf', help='output pdf file name')
def pdf_merge(input_dir, out):
    click.echo(input_dir)
    out_filename = f'{out}.pdf'

    files = sorted(Path(input_dir).iterdir(), key=os.path.getmtime)

    merger = PdfMerger()

    with click.progressbar(files) as bar:
        for file in bar:
            merger.append(file, outline_item=file.name)

    click.echo("write...")
    merger.write(out_filename)
    merger.close()


if __name__ == '__main__':
    pdf_merge()
