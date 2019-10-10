import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")



fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111)
labels = dict([(n, n.split('(user)')[0]) for n in h.nodes_iter()])

nx.draw(h, pos=nx.spring_layout(h),
        arrows=False, ax=ax, node_size=50,
        edge_color='#aaaaaa',
        alpha=0.8, labels=labels, font_size=8)