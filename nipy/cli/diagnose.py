# emacs: -*- mode: python; py-indent-offset: 4; indent-tabs-mode: nil -*-
# vi: set ft=python sts=4 ts=4 sw=4 et:
DESCRIP = 'Calculate and write results for diagnostic screen'
EPILOG = \
'''nipy_diagnose will generate a series of diagnostic images for a 4D
fMRI image volume.  The following images will be generated.  <ext> is
the input filename extension (e.g. '.nii'):

    * components_<label>.png : plots of PCA basis vectors
    * max_<label><ext> : max image
    * mean_<label><ext> : mean image
    * min_<label><ext> : min image
    * pca_<label><ext> : 4D image of PCA component images
    * pcnt_var_<label>.png : percent variance scree plot for PCA
      components
    * std_<label><ext> : standard deviation image
    * tsdiff_<label>.png : time series diagnostic plot

The filenames for the outputs are of the form
<out-path>/<some_prefix><label><file-ext> where <out-path> is the path
specified by the --out-path option, or the path of the input filename;
<some_prefix> are the standard prefixes above, <label> is given by
--out-label, or by the filename of the input image (with path and
extension removed), and <file-ext> is '.png' for graphics, or the
extension of the input filename for volume images.  For example,
specifying only the input filename ``/some/path/fname.img`` will
generate filenames of the form ``/some/path/components_fname.png,
/some/path/max_fname.img`` etc.
'''

from argparse import ArgumentParser, RawDescriptionHelpFormatter
import nipy.algorithms.diagnostics.commands as nadc


def main():
    import matplotlib
    matplotlib.use('Agg')

    parser = ArgumentParser(description=DESCRIP,
                            epilog=EPILOG,
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('filename', type=str,
                        help='4D image filename')
    parser.add_argument('--out-path', type=str,
                        help='path for output image files')
    parser.add_argument('--out-fname-label', type=str,
                        help='mid part of output image filenames')
    parser.add_argument('--ncomponents', type=int, default=10,
                        help='number of PCA components to write')
    parser.add_argument('--time-axis', type=str, default=-1,
                        help='Image axis for time')
    parser.add_argument('--slice-axis', type=str, default=None,
                        help='Image axis for slice')
    # parse the command line
    args = parser.parse_args()
    nadc.diagnose(args)
