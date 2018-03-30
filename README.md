Images to PDF Converter
==============

This Python script reads all images in the current project directory and converts them into a single .pdf document.
Supported image formats are JPEG, PNG and GIF.
The default page size is A4 and all input images are expected to be of A4 size. Page orientation is determined from size of the original image. Page orientation is portrait if height is greater than width and Landscape if width is greater than height.


## References

Major libraries used in this project are [FPDF](https://pypi.python.org/pypi/fpdf) and [PyPDF2](https://pypi.python.org/pypi/PyPDF2).
