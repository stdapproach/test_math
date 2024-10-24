from matplotlib import pyplot as plt


def show_result(solution, x_axis, y_axis, title_solution, ref_solution):
    t = solution['t']
    y1 = solution['sol']
    ref = solution['ref']
    abs_err = solution['abs_err']
    example = solution['example']
    sol_ref = example.sol_ref
    book_ref = sol_ref.book_ref
    #
    fig, ax1 = plt.subplots()
    ax1.set_title(book_ref)
    #
    dimensions = y1.shape
    _, columns = dimensions
    if columns > 1:
        y1 = y1[:, 0]
    #
    ax1.plot(t,y1,'g-',linewidth=2,label=f'{title_solution}')
    ax1.plot(t,ref,'b--',linewidth=2,label=f'{ref_solution}')
    plt.xlabel(x_axis)
    ax1.set_ylabel(y_axis)
    ax1.legend()
    #
    ax2 = ax1.twinx()  # instantiate a second Axes that shares the same x-axis
    color = 'tab:red'
    ax2.set_ylabel('abs_error', color=color)  # we already handled the x-label with ax1
    #
    ax2.plot(t, abs_err, color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    #
    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.show()
