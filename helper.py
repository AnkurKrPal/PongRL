import matplotlib.pyplot as plt
from IPython import display

plt.ion()

def plot(hits, mean_hits):
    display.clear_output(wait=True)
    display.display(plt.gcf())
    plt.clf()
    plt.title('Training... Successful Hits per Game')
    plt.xlabel('Number of Games')
    plt.ylabel('Successful Hits')
    plt.plot(hits)
    plt.plot(mean_hits)
    plt.ylim(ymin=0)
    plt.text(len(hits)-1, hits[-1], str(hits[-1]))
    plt.text(len(mean_hits)-1, mean_hits[-1], str(mean_hits[-1]))
    plt.show(block=False)
    plt.pause(.1)