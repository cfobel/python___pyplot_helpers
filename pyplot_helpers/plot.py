from itertools import combinations

import numpy as np
from pandas_helpers.stats import significance_comparison


def p_value_from_labels(p_values_frame, a_label, b_label):
    # Given two labels, look-up p-value from table
    row = p_values_frame[(p_values_frame['A'] == a_label)
                          & (p_values_frame['B'] == b_label)]
    if not row:
        row = p_values_frame[(p_values_frame['A'] == b_label)
                              & (p_values_frame['B'] == a_label)]
    if not row:
        raise KeyError, ('No p-value row matching labels: %s and %s'
                         % (a_label, b_label))
    return row


def significance_boxplot(plot_context, data_vectors_by_label, colors=None):
    '''
    Plot a box-plot based on the vectors provided.  Annotate the box-plot with arrows
    indicating the _$p$-value_ result from a statistical comparison of the
    corresponding pair of value vectors.

    The significance _$p$-values_ are computed using a
    [Wilcoxon signed-rank test][1] and are labelled on the plot using either a
    _red_ or _green_ arrow, pointing to the relevant means in the box plot.

    A _green_ arrow indicates that the $p$-value is less than 0.05, such that the
    null-hypothesis may be rejected, indicating that the means are not
    statistically likely by sampling from the same distribution.  If the
    $p$-value is greater than 0.05, the arrow is _red_.

    [1]: http://en.wikipedia.org/wiki/Wilcoxon_signed-rank_test
    '''
    labels = np.array(data_vectors_by_label.keys())
    data_vectors = np.array(data_vectors_by_label.values())
    if colors is None:
        colors = ['red', 'green']
    compare_results = significance_comparison(data_vectors_by_label)

    plot_context.boxplot(data_vectors_by_label.values())

    yticks = plot_context.get_yticks()
    ytick_extent = yticks[1] - yticks[0]

    # Generate all unique combinations of vector pairs.
    pairs = np.array(list(combinations(range(len(labels)), 2)))

    # Annotate the statistical comparison between each pair of vectors with:
    #   * The $p$-value from the Wilcoxon signed-rank test.
    #   * An arrow: _red_ if $p$-value >= 0.05, _green_ if $p$-value < 0.05.
    for pair in pairs:
        vectors = data_vectors[pair]
        p_value_row = p_value_from_labels(compare_results, *labels[pair])
        p_value = p_value_row['p-value']
        means = np.array([v.mean() for v in vectors])
        plot_context.annotate('', xy=((pair[0] + 1) + .15, means[0]),
                              xytext=((pair[1] + 1) - .15, means[1]),
                              arrowprops={'arrowstyle': '<->', 'color':
                                          colors[int(p_value < 0.05)],
                                          'alpha': 0.7, 'linewidth': 3})
        x_center = (pair[1] + pair[0] + 2) / 2.
        if (pair[1] - pair[0]) % 2:
            y_factor = 1
        else:
            y_factor = -1
        plot_context.annotate('p-value: %.2g' % p_value,
                              xy=(x_center, means.mean()),
                              ha='center', fontsize=16,
                              xytext=(x_center, y_factor * 0.65 * ytick_extent
                                      + means.mean()),
                              bbox=dict(boxstyle='round', fc='white',
                                        alpha=0.9))
    return compare_results
