import os
from pathlib import Path
import click
from pypdf import PdfWriter


@click.command()
@click.option('--input-dir', default='.', help='input dir')
@click.option('--out', default='merged-pdf', help='output pdf file name')
def pdf_merge(input_dir, out):
    click.echo(click.style(f'input dir: {input_dir}', fg='green'))
    out_filename = f'{out}.pdf'

    files = sorted(Path(input_dir).iterdir(), key=os.path.getmtime)
    pdf_files = list(filter(lambda f: f.name.endswith('.pdf'), files))

    if not pdf_files:
        click.echo(click.style("err: pdf files not found!", fg='red'))
        return

    merger = PdfWriter()

    with click.progressbar(pdf_files) as bar:
        for file in bar:
            merger.append(file, outline_item=file.name)

    click.echo("write...")
    merger.write(out_filename)
    merger.close()


if __name__ == '__main__':
    pdf_merge()
