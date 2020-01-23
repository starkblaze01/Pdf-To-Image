#!/usr/bin/env python

from pdf2image import convert_from_path
import sys
import getopt


def main():
    argv = sys.argv[1:]
    pdf_path = ''
    output_folder = None
    fmt = 'jpeg'
    dpi = 200
    grayscale = False
    try:
        opts, args = getopt.getopt(
            argv, "hi:o:f:d:g:", ["pdf_path=", "output_folder=", "fmt=", "dpi=", "grayscale="])
    except getopt.GetoptError:
        print('Usage: pdftoimg -i <pdf_path> -o <output_folder_path> -f <format> -d <dpi> -g <True/False>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(
                'Usage: pdftoimg -i <pdf_path> -o <output_folder_path> -f <format> -d <dpi> -g <True/False>')
            sys.exit()
        elif opt in ("-i", "--pdf_path"):
            pdf_path = arg.strip()
        elif opt in ("-o", "--output_folder"):
            output_folder = arg.strip()
        elif opt in ("-f", "--fmt"):
            fmt = arg.strip()
        elif opt in ("-d", "dpi"):
            dpi = int(arg.strip())
        elif opt in ("-g", "grayscale"):
            grayscale = arg.lower().strip()
            if grayscale == 'true':
                grayscale = True
            else:
                grayscale = False

    images_from_path = convert_from_path(
        pdf_path=pdf_path, output_folder=output_folder, fmt=fmt, dpi=dpi, grayscale=grayscale)
