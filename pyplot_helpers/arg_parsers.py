from argparse import ArgumentParser
from path import path


def subplot_params_args_parser(*args, **kwargs):
    '''
    Return an `argparse.ArgumentParser` object, which is configured for
    arguments relevant to `matplotlib.pyplot` sub-plots.
    '''
    import matplotlib

    parser = ArgumentParser(*args, **kwargs)
    parser.add_argument('--plot-linewidth', type=float,
                        default=matplotlib.rcParams.get('lines.linewidth', 1.))
    parser.add_argument('--plot-legend', action='store_true', default=False)
    parser.add_argument('-f', '--figures-per-row', type=int, default=1,
                        help='default=%(default)s')
    parser.add_argument('--plot-width', type=int)
    parser.add_argument('--plot-attr', action='append', default=[])

    return parser


def figure_params_args_parser(*args, **kwargs):
    '''
    Return an `argparse.ArgumentParser` object, which is configured for
    arguments relevant to `matplotlib.pyplot` sub-plots.
    '''
    kwargs_ = kwargs.copy()
    kwargs_.update(dict(parents=[subplot_params_args_parser()], add_help=False))
    parser = ArgumentParser(*args, **kwargs_)
    parser.add_argument('--figure-width-inches', type=float)
    parser.add_argument('--figure-height-inches', type=float)
    parser.add_argument('--figure-font-size', type=int)
    parser.add_argument('--figure-attr', action='append', default=[])
    parser.add_argument('--dpi', type=int)

    return parser


def pdf_pages_params_args_parser(*args, **kwargs):
    '''
    Return an `argparse.ArgumentParser` object, which is configured for
    arguments relevant to `matplotlib.pyplot` sub-plots.
    '''
    kwargs_ = kwargs.copy()
    kwargs_.update(dict(parents=[figure_params_args_parser()], add_help=False))
    parser = ArgumentParser(*args, **kwargs_)
    parser.add_argument('--figures-per-page', type=int)
    parser.add_argument('-o', '--pdf-path', type=path)

    return parser
